[7:23 PM, 12/26/2025] sunshine✨: import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Achuth Gym", layout="centered")
st.title("🏋️‍♂️ Achuth's Gym Enrollment")

# Data save ayye file peru
data_file = "enrollments.csv"

with st.form("enroll_form"):
    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    plan = st.selectbox("Plan", ["Monthly", "Quarterly", "Yearly"])
    submit = st.form_submit_button("Submit Details")
    
    if submit:
        # Data store cheyadam
        new_data = {"Name": [name], "Phone": [phone], "Plan": [plan]}
        df = pd.DataFrame(new_data)
        if not os.path.isfile(data_file):
            df.to_csv(data_file, index=False)
        else:
            df.to_csv(data_file, mode='a', header=False, index=False)
            
        st.success(f"Welcome to the Gym, {name}!")
        st.balloons()

# Achuth ki names list chupinchadaniki
if st.checkbox("Show Admin Dashboard (For Achuth)"):
    if os.path.isfile(data_file):
        st.write("### All Enrolled Members")
        st.table(pd.read_csv(data_file))
    else:
        st.write("No one has enrolled yet.")
[7:30 PM, 12/26/2025] sunshine✨: import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Achuth Gym", layout="centered")
st.title("🏋️‍♂️ Achuth's Gym Enrollment")

# Data save ayye file
data_file = "enrollments.csv"

with st.form("enroll_form"):
    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    plan = st.selectbox("Plan", ["Monthly", "Quarterly", "Yearly"])
    submit = st.form_submit_button("Submit Details")
    
    if submit:
        # Data store cheyadam
        new_data = {"Name": [name], "Phone": [phone], "Plan": [plan]}
        df = pd.DataFrame(new_data)
        if not os.path.isfile(data_file):
            df.to_csv(data_file, index=False)
        else:
            df.to_csv(data_file, mode='a', header=False, index=False)
            
        st.success(f"Successfully Enrolled: {name}!")
        st.balloons()

# Achuth list chuskovadaniki
st.divider()
if st.checkbox("Show Admin Dashboard"):
    if os.path.isfile(data_file):
        st.write("### Customer List")
        st.dataframe(pd.read_csv(data_file))
    else:
        st.write("No data yet.")
