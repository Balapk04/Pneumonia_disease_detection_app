import streamlit as st
from login import login_signup
from dashboard import dashboard_page
from predict import predict_page

# Initialize session variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# Sidebar navigation
def sidebar():
    st.sidebar.title("📋 Navigation")
    if st.session_state.logged_in:
        st.sidebar.button("🏠 Dashboard", on_click=lambda: set_page("dashboard"))
        st.sidebar.button("🩻 Predict Disease", on_click=lambda: set_page("predict"))
        st.sidebar.button("🔓 Logout", on_click=logout)
    else:
        st.sidebar.info("Please log in to access the app.")

def set_page(page):
    st.session_state.page = page

def logout():
    st.session_state.logged_in = False
    st.session_state.user = {}
    st.session_state.page = "login"
    st.experimental_rerun()

# Display sidebar
sidebar()

# Page routing
if st.session_state.page == "login":
    login_signup()
elif st.session_state.page == "dashboard":
    dashboard_page()
elif st.session_state.page == "predict":
    predict_page()
