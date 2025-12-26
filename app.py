import streamlit as st
import pandas as pd

# Page setup for Mobile
st.set_page_config(page_title="Achuth Gym", layout="centered")

st.title("🏋️‍♂️ Achuth's Gym Enrollment")

# Form
with st.form("enroll_form"):
    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    plan = st.selectbox("Plan", ["Monthly", "Quarterly", "Yearly"])
    submit = st.form_submit_button("Submit Details")
    
    if submit:
        st.success(f"Welcome to the Gym, {name}!")
        st.balloons()
