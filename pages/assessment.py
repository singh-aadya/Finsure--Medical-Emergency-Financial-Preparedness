import streamlit as st
from utils import predict_cost, calculate_gap, risk_score, recommendation

st.title("Assessment")

age = st.number_input("Age")
income = st.number_input("Income")
savings = st.number_input("Savings")
insurance = st.number_input("Insurance")
dependents = st.number_input("Dependents")

if st.button("Analyze"):
    cost = predict_cost(age, dependents)
    gap = calculate_gap(cost, savings, insurance)
    risk = risk_score(gap, income)

    st.metric("Cost", cost)
    st.metric("Gap", gap)
    st.metric("Risk", risk)