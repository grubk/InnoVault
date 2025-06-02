import streamlit as st

#Theme/Style

#Page setup
about_page = st.Page(
    page="views/about.py",
    title="Welcome to InnoVault",
    icon=":material/home:",
    default=True
)
codenotes_page = st.Page(
    page="views/codenotes.py",
    title="Code Notes",
    icon=":material/code:",
)
mathnotes_page = st.Page(
    page="views/mathnotes.py",
    title="English to LaTex Converter",
    icon=":material/function:"
)

#Navigation setup
pg = st.navigation(
    {
    "Info": [about_page],
    "Tools": [codenotes_page, mathnotes_page]
    }
    )

#Assets shown on all pages
st.sidebar.text("Made by Kai Grubert")
st.logo("assets/innovaultlogo.png", size="large")


#Run navigation
pg.run()