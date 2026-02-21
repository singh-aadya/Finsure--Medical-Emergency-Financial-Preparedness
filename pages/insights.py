import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Insights")

data = pd.DataFrame({
    "Category": ["Savings", "Insurance", "Expected Cost"],
    "Amount": [200000, 500000, 650000]
})

fig = px.bar(data, x="Category", y="Amount")
st.plotly_chart(fig)