import streamlit as st
import plotly.express as px
import pandas as pd
from utils import predict_cost, calculate_gap, risk_score, recommendation

st.set_page_config(page_title="Finsure", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.image("https://img.icons8.com/color/96/heart-health.png", width=80)
st.sidebar.title("Finsure")

page = st.sidebar.radio("Navigate", ["Assessment", "Insights"])

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.card { background:#f7f9fc; padding:20px; border-radius:14px; }
.big-title { font-size:40px; font-weight:700; text-align:center; }
</style>
""", unsafe_allow_html=True)

# ---------- MAIN PAGE ----------
if page == "Assessment":

    st.markdown('<div class="big-title">Medical Financial Preparedness</div>', unsafe_allow_html=True)

    st.markdown("### Enter your details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", help="Your current age")
        income = st.number_input("Monthly Income ₹", help="Net monthly income")

    with col2:
        savings = st.number_input("Savings ₹", help="Total liquid savings")
        insurance = st.number_input("Insurance ₹", help="Total health coverage")

    dependents = st.slider("Dependents", 0, 6)

    if st.button("Analyze"):
        cost = predict_cost(age, dependents)
        gap = calculate_gap(cost, savings, insurance)
        risk = risk_score(gap, income)
        advice = recommendation(gap)

        st.markdown("## Key Metrics")

        k1, k2, k3 = st.columns(3)
        k1.metric("Estimated Cost", f"₹{cost}")
        k2.metric("Funding Gap", f"₹{gap}")
        k3.metric("Risk Level", risk)

        st.success(advice)

# ---------- INSIGHTS PAGE ----------
if page == "Insights":

    st.title("Financial Insights")

    data = pd.DataFrame({
        "Category": ["Savings", "Insurance", "Expected Cost"],
        "Amount": [200000, 500000, 650000]
    })

    fig = px.bar(data, x="Category", y="Amount", title="Financial Breakdown")
    st.plotly_chart(fig, use_container_width=True)

    option = st.pills("Select View", ["Overview", "Risk"], default="Overview")

    if option == "Overview":
        st.info("Your savings cover a portion of expected costs.")
    else:
        st.warning("Risk increases if savings are low.")
