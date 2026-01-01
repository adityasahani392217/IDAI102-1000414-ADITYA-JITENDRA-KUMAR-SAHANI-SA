import streamlit as st
from datetime import datetime
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ShopImpact", layout="wide")

st.title("🌍 ShopImpact – Conscious Shopping Dashboard")
st.write(
    "ShopImpact helps you understand the environmental impact of your purchases "
    "and encourages eco-friendly shopping through awareness and rewards."
)

# ---------------- SESSION STATE ----------------
if "purchases" not in st.session_state:
    st.session_state.purchases = []

# ---------------- DATA DEFINITIONS ----------------
IMPACT_MULTIPLIER = {
    "Electronics": 0.6,
    "Clothes": 0.3,
    "Groceries": 0.1,
    "Footwear": 0.4,
    "Second-hand": 0.05
}

ALTERNATIVES = {
    "Electronics": ["Refurbished devices", "Energy-efficient brands"],
    "Clothes": ["Organic cotton", "Second-hand clothing"],
    "Groceries": ["Local produce", "Minimal packaging brands"],
    "Footwear": ["Vegan leather", "Sustainable materials"],
    "Second-hand": ["Reuse stores", "Community swaps"]
}

ECO_TIPS = [
    "Buying second-hand dramatically reduces waste.",
    "Local products reduce transport emissions.",
    "Repairing items is greener than replacing them.",
    "Minimal packaging helps protect the environment."
]

QUOTES = [
    "Small choices make a big difference.",
    "Sustainability starts with awareness.",
    "There is no planet B."
]

# ---------------- FUNCTIONS ----------------
def calculate_impact(product, price):
    return price * IMPACT_MULTIPLIER.get(product, 0.2)

def assign_badge(total_impact):
    if total_impact < 500:
        return "🌱 Eco Saver"
    elif total_impact < 1500:
        return "♻️ Conscious Shopper"
    else:
        return "⚠️ High Impact Month"

# ---------------- INPUT FORM ----------------
st.subheader("🛒 Add a Purchase")

with st.form("purchase_form"):
    product = st.selectbox("Product Type", list(IMPACT_MULTIPLIER.keys()))
    brand = st.text_input("Brand Name")
    price = st.number_input("Price (₹)", min_value=0)
    submitted = st.form_submit_button("Add Purchase")

if submitted:
    impact = calculate_impact(product, price)
    st.session_state.purchases.append({
        "product": product,
        "brand": brand,
        "price": price,
        "impact": impact,
        "month": datetime.now().strftime("%Y-%m")
    })
    st.success("Purchase logged successfully!")

def eco_score(total_impact):
    # Simple, interpretable score
    score = 100 - (total_impact / 20)
    return max(0, min(100, round(score)))

def impact_category(total_impact):
    if total_impact < 500:
        return "🟢 Low Impact"
    elif total_impact < 1500:
        return "🟡 Medium Impact"
    else:
        return "🔴 High Impact"

# Qualitative insights
st.markdown("### 📈 Impact Insights")

col3, col4, col5 = st.columns(3)

col3.metric("🎯 Eco Score", f"{eco_score(total_impact)} / 100")
col4.metric("🧭 Impact Level", impact_category(total_impact))

if prev_month_impact > 0:
    delta = total_impact - prev_month_impact
    trend = "lower" if delta < 0 else "higher"
    col5.info(
        f"This month’s impact is {trend} than last month "
        f"by {abs(round(delta, 2))} units."
    )
else:
    col5.info("No data from last month yet.")

# ---------------- MONTHLY DASHBOARD ----------------
st.subheader("📊 Monthly Dashboard")

current_month = datetime.now().strftime("%Y-%m")
monthly_purchases = [p for p in st.session_state.purchases if p["month"] == current_month]

total_spend = sum(p["price"] for p in monthly_purchases)
total_impact = sum(p["impact"] for p in monthly_purchases)

col1, col2 = st.columns(2)
col1.metric("💰 Total Monthly Spend", f"₹{total_spend}")
col2.metric("🌫️ Estimated CO₂ Impact", f"{total_impact:.2f}")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🏅 Eco Badge")
    badge = assign_badge(total_impact)
    st.write(badge)

    st.header("🌿 Greener Alternatives")
    if submitted:
        for alt in ALTERNATIVES.get(product, []):
            st.write(f"• {alt}")

# ---------------- TURTLE VISUAL SIMULATION ----------------
if total_impact < 500 and monthly_purchases:
    st.subheader("🐢 Turtle Eco Reward")
    st.write(
        "A Turtle graphic is conceptually used to reward eco-friendly behavior. "
        "Due to Streamlit Cloud limitations (no Tkinter support), the Turtle drawing "
        "is represented symbolically."
    )
    st.success("🌿 Turtle draws a green leaf to celebrate your low-impact choices!")

# ---------------- CREATIVE FEATURES ----------------
st.subheader("💡 Eco Tip")
st.info(random.choice(ECO_TIPS))

st.subheader("🌟 Motivation")
st.success(random.choice(QUOTES))

# ---------------- PURCHASE HISTORY ----------------
if st.session_state.purchases:
    st.subheader("📋 Purchase History")
    st.table(st.session_state.purchases)

# ---------------- FOOTER ----------------
st.write("---")
st.caption(
    "Note: Environmental impact values are estimates intended for awareness purposes only."
)
