import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact me")
def show_contact_form():
    contact_form()

#Hero section
st.title("InnoVault by grubk", anchor = "false")
st.write(
        "A project providing (maybe) helpful tools to create the best note-taking experience for students."
    )

st.write("\n")
col1, col2 = st.columns(2, gap="medium")
with col1:
    if st.button("📭Contact Me"):
        show_contact_form()
with col2:
    st.link_button("☕Buy Me A Coffee", "https://buymeacoffee.com/grubk")

st.write("\n")


#Tools description
st.header("Tools included:")
st.markdown(r"""
- Formula Booklet: Displays the formula booklet for certain courses at UBC -- year 1 eng. only for now, CPEN coming soon
- English to LaTeX: Convert written English into LaTex. Useful for writing mathematical expressions quickly
""")


