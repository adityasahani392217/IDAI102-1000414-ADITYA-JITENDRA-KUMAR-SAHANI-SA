import streamlit as st
from datetime import datetime
import random
import turtle
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="ShopImpact", layout="wide")

st.title("🌍 ShopImpact – Conscious Shopping Dashboard")
st.write(
    "ShopImpact helps you understand the hidden environmental impact of your purchases "
    "and gently encourages more eco-friendly shopping habits."
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

def draw_turtle_leaf():
    screen = turtle.Screen()
    screen.setup(width=300, height=300)
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.hideturtle()
    canvas = screen.getcanvas()
    canvas.postscript(file="leaf.ps")
    turtle.bye()
    os.system("convert leaf.ps leaf.png")  # local conversion

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

# ---------------- TURTLE GRAPHIC ----------------
if total_impact < 500 and monthly_purchases:
    st.subheader("🐢 Eco Reward")
    st.write("You made eco-friendly choices this month!")
    st.write("Turtle graphic displayed for positive impact.")

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
    "Note: Environmental impact values shown are estimates intended for awareness purposes only."
)
