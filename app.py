import streamlit as st

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

st.sidebar.title("Navigation")
st.sidebar.write("Use pages below")