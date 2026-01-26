import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime, timedelta
import random

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="ShopImpact | Gamified Companion",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. SESSION STATE SETUP ---
if 'users' not in st.session_state:
    st.session_state['users'] = {"admin": "admin"} 

if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None

# Initialize User Data
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {
        'purchases': [],
        'xp': 0,
        'level': 1,
        'badges': [],
        'streak': 0,               
        'last_log_date': None,     
        'last_category': None, # <--- NEW: Tracks last choice for sidebar
        'goal': 100.0
    }
else:
    # Migration Fix for existing sessions
    required_keys = {'streak': 0, 'last_log_date': None, 'last_category': None, 'goal': 100.0}
    for key, val in required_keys.items():
        if key not in st.session_state['user_data']:
            st.session_state['user_data'][key] = val

# --- 3. CONSTANTS & DATA ---
IMPACT_MULTIPLIERS = {
    "Local Produce 🥦": 0.1, "Second-Hand/Vintage 🧥": 0.05,
    "Eco-Certified Brand 🌿": 0.2, "Standard Groceries 🍞": 0.4,
    "New Electronics 📱": 0.8, "Fast Fashion 👗": 0.9,
    "Imported Goods ✈️": 1.2
}

# NEW: Alternatives Logic for Sidebar
ALTERNATIVES = {
    "Fast Fashion 👗": ["Thrift stores (Depop, Vinted)", "Organic cotton brands", "Repair old clothes"],
    "New Electronics 📱": ["Refurbished tech (Back Market)", "Repair cafes", "Keep using current device"],
    "Standard Groceries 🍞": ["Local farmer's markets", "Bulk food stores (zero waste)", "Seasonal produce"],
    "Imported Goods ✈️": ["Local artisans", "Domestic alternatives", "DIY solutions"],
    "Plastic Goods": ["Bamboo alternatives", "Glass/Metal containers", "Beeswax wraps"]
}

# NEW: Random Eco Tips
ECO_TIPS = [
    "Did you know? Buying second-hand reduces carbon impact by over 80%!",
    "Eating local food reduces 'food miles' and supports your community.",
    "Extending the life of clothes by just 9 months reduces carbon footprint by 30%.",
    "Refurbished electronics save e-waste from landfills and use less energy.",
    "Bamboo grows 10x faster than trees and absorbs more CO2!"
]

MOTIVATION_QUOTES = [
    "🌍 Small steps today create a greener tomorrow.",
    "♻️ You don’t need to be perfect to make a difference.",
    "🌱 Every sustainable choice counts.",
    "💚 Progress, not perfection, builds a better planet.",
    "🐢 Slow and mindful choices win the sustainability race.",
    "🌎 The future depends on what you buy today.",
    "✨ Conscious shopping is a form of self-respect for Earth.",
    "🌿 Sustainability starts with awareness.",
    "🛍️ Buy less, choose better, make it last.",
    "🌞 Your choices today shape tomorrow’s world.",
    "🍃 Even small reductions create big impact over time."
]

XP_PER_LOG = 10
XP_BONUS_LOW_IMPACT = 20
LEVEL_THRESHOLDS = {1: 0, 2: 100, 3: 250, 4: 500, 5: 1000}

# --- 4. CSS STYLING (Dark Forest Theme) ---
col_bg = "#121212"        
col_card = "#1E1E1E"      
col_text = "#FFFFFF"      
col_accent = "#66BB6A"    
col_input_bg = "#2C2C2C"  
col_border = "#333333"    

st.markdown(f"""
    <style>
    .stApp {{ background-color: {col_bg}; color: {col_text}; }}
    h1, h2, h3, h4, p, label, li, span, div {{ color: {col_text} !important; }}
    div[data-testid="stMetricValue"] {{ color: {col_accent} !important; font-weight: 800; }}
    div[data-testid="stMetricLabel"] {{ color: {col_text} !important; opacity: 0.7; }}
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {{
        background-color: {col_card};
        border: 1px solid {col_border};
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        padding: 20px;
    }}
    input, .stTextInput input, .stNumberInput input, .stDateInput input, .stSelectbox div[data-baseweb="select"] {{
        background-color: {col_input_bg} !important;
        color: white !important;
        border: 1px solid {col_border} !important;
    }}
    ul[data-testid="stSelectboxVirtualDropdown"] li {{ background-color: {col_card} !important; color: white !important; }}
    .stButton > button {{ background-color: {col_accent}; color: white !important; border-radius: 8px; font-weight: bold; border: none; }}
    section[data-testid="stSidebar"] {{ background-color: {col_card}; border-right: 1px solid {col_border}; }}
    
    /* Badges */
    .locked-badge {{ filter: grayscale(100%) blur(2px); opacity: 0.5; border: 1px dashed #555; padding: 10px; border-radius: 8px; text-align: center; }}
    .unlocked-badge {{ border: 1px solid {col_accent}; box-shadow: 0 0 10px {col_accent}; padding: 10px; border-radius: 8px; text-align: center; background-color: rgba(102, 187, 106, 0.1); }}
    </style>
""", unsafe_allow_html=True)

# --- 5. LOGIC & VISUALIZATION FUNCTIONS ---

def calculate_level(xp):
    for lvl in sorted(LEVEL_THRESHOLDS.keys(), reverse=True):
        if xp >= LEVEL_THRESHOLDS[lvl]: return lvl
    return 1

def update_streak(current_date):
    last_date = st.session_state['user_data']['last_log_date']
    if last_date is None:
        st.session_state['user_data']['streak'] = 1
    else:
        delta = (current_date - last_date).days
        if delta == 1:
            st.session_state['user_data']['streak'] += 1
        elif delta > 1:
            st.session_state['user_data']['streak'] = 1
    st.session_state['user_data']['last_log_date'] = current_date

def check_badges(purchases):
    unlocked = []

    if not purchases:
        return unlocked

    df = pd.DataFrame(purchases)

    total_impact = df['impact'].sum()
    avg_impact = df['impact'].mean()

    # % of low-impact purchases
    low_impact_count = df[df['impact'] <= 5.0].shape[0]
    low_impact_ratio = low_impact_count / len(df)

    # 🌱 Eco Saver – overall low footprint
    if total_impact <= 50:
        unlocked.append("🌱 Eco Saver")

    # ♻️ Conscious Consumer – majority low-impact choices
    if low_impact_ratio >= 0.6:
        unlocked.append("♻️ Conscious Consumer")

    # 🛡️ Eco Warrior – consistently efficient purchases
    if avg_impact <= 4.0 and len(df) >= 3:
        unlocked.append("🛡️ Eco Warrior")

    # 🔥 Sustainability Streaker – streak without high-impact items
    streak = st.session_state['user_data']['streak']
    if streak >= 5:
        unlocked.append("🔥 Sustainability Streaker")

    # 🏆 Green Champion – improvement over time
    if len(df) >= 6:
        first_half = df.iloc[:len(df)//2]['impact'].mean()
        second_half = df.iloc[len(df)//2:]['impact'].mean()
        if second_half < first_half:
            unlocked.append("🏆 Green Champion")

    return unlocked


def draw_turtle_avatar(level):
    fig, ax = plt.subplots(figsize=(3, 3))
    rect = patches.Rectangle((0,0), 100, 100, color='#1E1E1E')
    ax.add_patch(rect)
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

    body_c = '#66BB6A'; shell_c = '#2E7D32'
    ax.add_patch(patches.Ellipse((50, 50), 50, 60, color=shell_c))
    ax.add_patch(patches.Circle((50, 85), 12, color=body_c))
    for pos in [(25, 65), (75, 65), (25, 35), (75, 35)]: ax.add_patch(patches.Circle(pos, 8, color=body_c))
    ax.add_patch(patches.Circle((46, 88), 2, color='white')); ax.add_patch(patches.Circle((54, 88), 2, color='white'))
    ax.add_patch(patches.Circle((46, 88), 0.5, color='black')); ax.add_patch(patches.Circle((54, 88), 0.5, color='black'))
    
    if level >= 2: ax.text(50, 48, f"LVL {level}", ha='center', color='#FFD700', fontweight='bold', fontsize=12)
    if level >= 3: ax.add_patch(patches.Polygon([[40, 95], [60, 95], [50, 110]], color='#FF5722')) 
    return fig

def draw_progress_chart(purchases):
    if not purchases: return None
    df = pd.DataFrame(purchases)
    df['date'] = pd.to_datetime(df['date'])
    today = datetime.today().date()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    daily_impact = {day: 0.0 for day in last_7_days}
    
    for _, row in df.iterrows():
        row_date = row['date'].date()
        if row_date in daily_impact: daily_impact[row_date] += row['impact']
        
    days = [d.strftime('%a') for d in last_7_days]
    values = list(daily_impact.values())
    
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_alpha(0); ax.patch.set_alpha(0)
    bars = ax.bar(days, values, color="#66BB6A")
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False); ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color("white"); ax.tick_params(colors="white")
    
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{bar.get_height():.1f}", ha='center', va='bottom', color="white", fontsize=9)
    return fig

# --- 6. PAGE LOGIC ---

def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.title("🌿 ShopImpact")
        st.write("Login to access your sustainable shopping companion.")
        with st.container(border=True):
            tab1, tab2 = st.tabs(["Login", "Sign Up"])
            with tab1:
                u = st.text_input("Username", key="l_u")
                p = st.text_input("Password", type="password", key="l_p")
                if st.button("🚀 Log In", use_container_width=True):
                    if u in st.session_state['users'] and st.session_state['users'][u] == p:
                        st.session_state['current_user'] = u; st.rerun()
                    else: st.error("Invalid credentials.")
            with tab2:
                nu = st.text_input("New Username", key="n_u")
                np = st.text_input("New Password", type="password", key="n_p")
                if st.button("✨ Create Account", use_container_width=True):
                    if nu and np: st.session_state['users'][nu] = np; st.success("Account created! Go to Login.")

def main_app():
    # --- PERSISTENT SIDEBAR ---
    with st.sidebar:
        st.subheader(f"👋 Hello, {st.session_state['current_user']}")
        lvl = st.session_state['user_data']['level']
        xp = st.session_state['user_data']['xp']
        next_xp = LEVEL_THRESHOLDS.get(lvl+1, 1000)
        
        st.caption(f"**Level {lvl} Status**")
        st.progress(min(xp/next_xp, 1.0))
        st.write(f"Points: {xp} / {next_xp} XP")
        
        st.divider()
        nav = st.radio("Menu", ["📊 Dashboard", "📝 History Log", "🏆 Leaderboard", "⚙️ Settings"])
        
        # --- NEW: ECO FEEDBACK PANEL (Persistent) ---
        st.divider()
        st.subheader("🌿 Eco Feedback Panel")
        
        # 1. Greener Alternatives (Persists based on last category)
        last_cat = st.session_state['user_data']['last_category']
        if last_cat and last_cat in ALTERNATIVES:
            st.caption(f"Alternatives for: **{last_cat}**")
            for alt in ALTERNATIVES[last_cat]:
                st.write(f"• {alt}")
        else:
            st.info("Log an item to see alternatives here.")
            
        # 2. Random Eco Tip (Always visible)
        st.caption("💡 **Daily Tip:**")
        st.info(random.choice(ECO_TIPS))
        
        st.divider()
        st.caption("✨ **Motivation:**")
        st.success(random.choice(MOTIVATION_QUOTES))
        st.divider()
        if st.button("Logout"):
            st.session_state['current_user'] = None; st.rerun()

    # --- DASHBOARD ---
    if nav == "📊 Dashboard":
        st.title("📊 Eco-Dashboard")
        total_co2 = sum(p['impact'] for p in st.session_state['user_data']['purchases'])
        streak_count = st.session_state['user_data']['streak']
        
        m1, m2, m3, m4 = st.columns(4)
        with m1: st.container(border=True).metric("Current Level", f"{lvl}")
        with m2: st.container(border=True).metric("Items Logged", len(st.session_state['user_data']['purchases']))
        with m3: st.container(border=True).metric("Total Impact", f"{total_co2:.1f} kg")
        with m4: st.container(border=True).metric("Streak", f"🔥 {streak_count} Days")
        
        c1, c2 = st.columns([1.5, 1])
        with c1:
            st.subheader("🛒 Log Purchase")
            with st.container(border=True):
                with st.form("entry_form", border=False):
                    col_a, col_b = st.columns(2)
                    with col_a:
                        cat = st.selectbox("Category", list(IMPACT_MULTIPLIERS.keys()))
                        price = st.number_input("Price ($)", 0.0, step=1.0)
                    with col_b:
                        brand = st.text_input("Brand")
                        date_val = st.date_input("Date", datetime.today())
                    
                    if st.form_submit_button("Add Entry"):
                        mult = IMPACT_MULTIPLIERS[cat]
                        imp = round(price * mult, 2)
                        st.session_state['user_data']['purchases'].append({
                            "category": cat, "brand": brand, "price": price, 
                            "impact": imp, "date": date_val 
                        })
                        
                        # UPDATE PERSISTENT STATE
                        st.session_state['user_data']['last_category'] = cat # <--- Key Fix
                        update_streak(date_val)
                        
                        bonus = XP_BONUS_LOW_IMPACT if mult <= 0.2 else 0
                        st.session_state['user_data']['xp'] += (XP_PER_LOG + bonus)
                        st.session_state['user_data']['level'] = calculate_level(st.session_state['user_data']['xp'])
                        st.rerun()

            st.subheader("📅 Weekly Progress")
            if st.session_state['user_data']['purchases']:
                with st.container(border=True):
                    fig = draw_progress_chart(st.session_state['user_data']['purchases'])
                    st.pyplot(fig, use_container_width=True)
                    st.caption("Weekly progress calculated from purchase dates logged by the user.")
            else: st.info("Start logging to see your daily progress chart here.")

        with c2:
            st.subheader("🐢 Your Avatar")
            with st.container(border=True):
                fig_turtle = draw_turtle_avatar(lvl)
                st.pyplot(fig_turtle, use_container_width=True)
                st.caption("Turtle animation is symbolic due to headless Streamlit deployment.")
            
            st.subheader("🏅 Badges")
            badges = check_badges(st.session_state['user_data']['purchases'])
            all_b = ["🌱 Eco Saver","♻️ Conscious Consumer","🛡️ Eco Warrior","🔥 Sustainability Streaker","🏆 Green Champion"]
            with st.container(border=True):
                bc1, bc2 = st.columns(2)
                for i, b in enumerate(all_b):
                    col = bc1 if i % 2 == 0 else bc2
                    if b in badges: col.markdown(f"<div class='unlocked-badge'>{b}</div>", unsafe_allow_html=True)
                    else: col.markdown(f"<div class='locked-badge'>🔒 {b}</div>", unsafe_allow_html=True)

    # --- HISTORY TAB ---
    elif nav == "📝 History Log":
        st.title("📝 History")
        if st.session_state['user_data']['purchases']:
            df = pd.DataFrame(st.session_state['user_data']['purchases'])
            df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
            st.data_editor(df, use_container_width=True, num_rows="dynamic")
            if st.button("Clear History"):
                st.session_state['user_data']['purchases'] = []
                st.session_state['user_data']['streak'] = 0
                st.session_state['user_data']['last_log_date'] = None
                st.session_state['user_data']['last_category'] = None
                st.rerun()
        else: st.info("No records found.")

    # --- LEADERBOARD TAB ---
    elif nav == "🏆 Leaderboard":
        st.title("🏆 Leaderboard")
        data = [{"Rank": "🥇", "User": "EcoQueen", "XP": 4500}, {"Rank": "🥈", "User": "GreenGary", "XP": 3200}, {"Rank": "🥉", "User": st.session_state['current_user'], "XP": xp}]
        st.table(data)

    # --- SETTINGS TAB ---
    elif nav == "⚙️ Settings":
        st.title("⚙️ Settings")
        with st.container(border=True):
            st.subheader("Data Export")
            if st.session_state['user_data']['purchases']:
                df = pd.DataFrame(st.session_state['user_data']['purchases'])
                st.download_button("📥 Download CSV", df.to_csv().encode('utf-8'), "data.csv")
            else: st.warning("No data.")

# --- 7. RUN ---
if __name__ == "__main__":
    if st.session_state['current_user']: main_app()
    else: login_page()
