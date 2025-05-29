import streamlit as st

import streamlit as st

def dashboard_page():
    st.markdown("<h1 style='font-size: 48px; color: #4CAF50;'>🏥 Welcome to the X-ray Diagnostic Center</h1>", unsafe_allow_html=True)

    user_name = st.session_state.get("user", {}).get("name", "User")
    st.markdown(f"<h2 style='font-size: 32px;'>👋 Hello, {user_name}!</h2>", unsafe_allow_html=True)

    st.markdown("<p style='font-size: 20px;'>Use the sidebar to upload chest X-rays and get an instant diagnosis powered by AI.</p>", unsafe_allow_html=True)

    if st.button("➡️ Go to Prediction Page"):
        st.session_state.page = "predict"


    
