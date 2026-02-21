import streamlit as st

st.title("Emergency Fund Planner")

gap = st.number_input("Funding Gap")

if gap > 0:
    monthly = gap / 12
    st.write(f"Save ₹{monthly:.0f} per month to cover gap in 1 year")