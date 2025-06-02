import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact me")
def show_contact_form():
    contact_form()

#Hero section
st.title("InnoVault by grubk", anchor = "false")
st.write(
        "A project built by Kai Grubert providing helpful tools to create the best note-taking experience for students."
    )

st.write("\n")
if st.button("📭Contact Me"):
    show_contact_form()
st.write("\n")

#Tools description
st.header("Tools included:")
st.markdown(r"""
- Code Notes: Supports automatic indentation, interactive interface, and user comments to help remember what certain lines of code do
- English to LaTeX: Convert written English into LaTex. Useful for writing mathematical expressions quickly
- Sync Notes: Type notes on one device, draw notes on a tablet or iPad. See both in real-time on one screen. (Currently work-in-progress)
""")


