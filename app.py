
import streamlit as st
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #1F3C88;
}
.card {
    background: linear-gradient(135deg, #eef2ff, #f0fdf4);
    padding: 20px;
    border-radius: 15px;
}
.metric-container {
    background: #ffffff;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
}
</style>
""", unsafe_allow_html=True)
st.image("logo.png", width=200)

st.set_page_config(page_title="Finsure", layout="wide")

st.title("Finsure")
st.subheader("Medical Emergency Financial Preparedness Platform")

st.write("""
Use the sidebar to navigate through features:
- Assessment
- Insights
- Planner
- Schemes
- Advisor
""")

st.set_page_config(
    page_title="Finsure",
    layout="wide",
    initial_sidebar_state="expanded"
)
