
import streamlit as st

# --- Sidebar Login ---
st.sidebar.header("🔒 Login to Access Unit Converter")

# --- Username & Password Input ---
username = st.sidebar.text_input("👤 Username")
password = st.sidebar.text_input("🔑 Password", type="password")

# --- Correct Credentials ---
correct_username = "Jawad"
correct_password = "2233"

# --- Authentication ---
if st.sidebar.button("Login"):
    if username == correct_username and password == correct_password:
        st.sidebar.success("✅ Login Successful!")
        st.session_state["logged_in"] = True  
    else:
        st.sidebar.error("❌ Access Denied! Incorrect Username or Password.")
        st.session_state["logged_in"] = False

# --- Check if User is Logged In ---
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    # --- Title ---
    st.title("🌍 Unit Converter App 🌍")
    st.markdown("### Converts✨ length, ⚖️ weight, and ⏳ time instantly")
    st.write("❤️ Welcome! Select a category:")

    # --- Category Selection ---
    category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

    # --- Function to Convert Units ---
    def convert_unit(category, value, unit):
        if category == "Length":
            if unit == "Kilometers to Miles":
                return value * 0.621371
            elif unit == "Miles to Kilometers":
                return value / 0.621371

        elif category == "Weight":
            if unit == "Kilograms to Pounds":
                return value * 2.20462
            elif unit == "Pounds to Kilograms":
                return value / 2.20462

        elif category == "Time":
            if unit == "Seconds to Minutes":
                return value / 60
            elif unit == "Minutes to Seconds":
                return value * 60
            elif unit == "Minutes to Hours":
                return value / 60
            elif unit == "Hours to Minutes":
                return value * 60
            elif unit == "Hours to Days":
                return value / 24
            elif unit == "Days to Hours":
                return value * 24

    # --- Unit Selection ---
    if category == "Length":
        unit = st.selectbox("✏️ Select conversion", ["Miles to Kilometers", "Kilometers to Miles"])
    elif category == "Weight":
        unit = st.selectbox("⚖️ Select conversion", ["Pounds to Kilograms", "Kilograms to Pounds"])
    elif category == "Time":
        unit = st.selectbox("⏰ Select conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

    # --- User Input for Value ---
    value = st.number_input("🔢 Enter your value:", min_value=0.0, format="%.2f")

    # --- Convert Button ---
    if st.button("Convert"):
        result = convert_unit(category, value, unit)
        st.success(f"✅ The result is: {result:.4f}")

else:
    st.warning("🔴 Please login from the sidebar to access the Unit Converter.")