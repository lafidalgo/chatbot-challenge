from PIL import Image
import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        logo = Image.open("src/streamlit/assets/logo-hotmart.png")
        st.image(logo)
        st.write("")
        st.write("")

        st.page_link("home.py",
                     label="Home", icon="🏠")
        st.page_link("pages/chatbot.py",
                     label="ChatBot", icon="🤖")

        st.write("")
        st.write("")
