import streamlit as st

from PIL import Image


def init_page_configuration(add_logo: bool = True):
    # Page configuration
    favicon = Image.open("src/streamlit/assets/favicon-hotmart.png")
    st.set_page_config(
        page_title="Hotmart Challenge",
        page_icon=favicon,
    )

    # Logo
    if add_logo:
        logo = Image.open("src/streamlit/assets/logo-hotmart.png")
        st.image(logo)
