import streamlit as st
from utils import predict_cost, calculate_gap, risk_score, recommendation

st.title("Medical Financial Preparedness")

age = st.number_input("Age", 18, 80)
income = st.number_input("Monthly Income (₹)")
savings = st.number_input("Current Savings (₹)")
insurance = st.number_input("Insurance Coverage (₹)")
dependents = st.number_input("Dependents", 0, 6)

if st.button("Analyze"):
    cost = predict_cost(age, dependents)
    gap = calculate_gap(cost, savings, insurance)
    risk = risk_score(gap, income)
    advice = recommendation(gap)

    st.metric("Estimated Medical Cost", f"₹{cost}")
    st.metric("Funding Gap", f"₹{gap}")
    st.metric("Risk Level", risk)
    st.success(advice)