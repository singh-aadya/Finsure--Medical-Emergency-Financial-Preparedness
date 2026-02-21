import streamlit as st

st.title("Support Schemes")

income = st.number_input("Monthly Income")

if income < 30000:
    st.info("You may be eligible for Ayushman Bharat")
else:
    st.info("Consider private health insurance plans")