import streamlit as st
import json
import os

def login_signup():
    st.title("🩺 Pneumonia Detector")

    if not os.path.exists("users.json") or os.stat("users.json").st_size == 0:
        with open("users.json", "w") as f:
            json.dump({}, f)

    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except json.JSONDecodeError:
        users = {}
        with open("users.json", "w") as f:
            json.dump(users, f)

    choice = st.radio("Select", ["Login", "Sign Up"])

    if choice == "Sign Up":
        st.subheader("Create New Account")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Create Account"):
            if email in users:
                st.error("User already exists.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long.")
            elif not all([name, email, password]):
                st.error("Please fill in all fields.")
            else:
                users[email] = {"name": name, "password": password}
                with open("users.json", "w") as f:
                    json.dump(users, f)
                st.success("Account created! Please login.")
                st.session_state.page = "login"
                 # To reload app and move to login page

    else:
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = users.get(email)
            if user and user["password"] == password:
                st.success(f"Welcome back, {user['name']}!")
                st.session_state.username = user["name"]
                st.session_state.page = "dashboard"
                  # Refresh app to dashboard
            else:
                st.error("Invalid credentials.")
