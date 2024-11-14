import streamlit as st
from PIL import Image


def init_page_configuration(add_logo: bool = True):
    # Page configuration
    favicon = Image.open("src/streamlit/assets/favicon-chatbot.png")
    st.set_page_config(
        page_title="Context Chatbot",
        page_icon=favicon,
    )

    # Logo
    if add_logo:
        logo = Image.open("src/streamlit/assets/logo-chatbot.png")
        st.image(logo)
