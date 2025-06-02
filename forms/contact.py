import streamlit as st
import re
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZiMDYzNzA0MzA1MjY4NTUzNzUxM2Ei_pc"

def is_valid_email(email):
    #Validate email adress submitted by user
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit✅")

    if submit_button:
        if not WEBHOOK_URL:
            st.error(
                "Email service not set up. Please try again later."
            )
            st.stop()
        
        if not name or not email or not message:
            st.error("Please provide the missing information.")
            st.stop()
    
        data = {"email": email, "name": name, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Message sent successfully. Thank you for your feedback.", icon="✅")
        else:
            st.error("There was an issue with sending your message.", icon="🥲")
