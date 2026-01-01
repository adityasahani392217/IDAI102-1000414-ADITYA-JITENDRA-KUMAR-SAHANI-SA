import streamlit as st
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="ShopImpact – Conscious Shopping Dashboard",
    layout="wide"
)

st.title("🌍 ShopImpact – Conscious Shopping Dashboard")
st.write(
    "Track your shopping habits, understand their environmental impact, "
    "and get encouraged to make eco-friendly choices."
)

# Initialize session state
if "purchases" not in st.session_state:
    st.session_state.purchases = []

# Impact multipliers (estimated values)
IMPACT_MULTIPLIER = {
    "Electronics": 0.6,
    "Clothes": 0.3,
    "Groceries": 0.1,
    "Footwear": 0.4,
    "Second-hand": 0.05
}

# Eco tips
ECO_TIPS = [
    "Buying second-hand products significantly reduces waste.",
    "Local products reduce carbon emissions from transport.",
    "Repairing items is often more eco-friendly than replacing them.",
    "Minimal packaging helps reduce environmental pollution."
]

# Functions
def calculate_impact(product, price):
    return price * IMPACT_MULTIPLIER.get(product, 0.2)

def assign_badge(total_impact):
    if total_impact < 500:
        return "🌱 Eco Saver"
    elif total_impact < 1500:
        return "♻️ Conscious Shopper"
    else:
        return "⚠️ High Impact Month"

# Input form
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
    st.success("Purchase added successfully!")

# Dashboard calculations
total_spend = sum(p["price"] for p in st.session_state.purchases)
total_impact = sum(p["impact"] for p in st.session_state.purchases)

st.subheader("📊 Monthly Dashboard")

col1, col2 = st.columns(2)
col1.metric("💰 Total Spend (₹)", f"{total_spend}")
col2.metric("🌫️ Estimated CO₂ Impact", f"{total_impact:.2f}")

# Sidebar content
with st.sidebar:
    st.header("🏅 Your Eco Badge")
    st.write(assign_badge(total_impact))

    st.header("🌿 Greener Alternatives")
    st.write(
        "• Choose second-hand or refurbished products\n"
        "• Prefer local and sustainable brands\n"
        "• Avoid excessive packaging"
    )

# Eco tip section
st.subheader("💡 Eco Tip")
st.info(random.choice(ECO_TIPS))

# Purchase history
if st.session_state.purchases:
    st.subheader("📋 Purchase History")
    st.table(st.session_state.purchases)

# Footer
st.write("---")
st.caption(
    "Note: Environmental impact values shown are estimates intended for awareness purposes only."
)
