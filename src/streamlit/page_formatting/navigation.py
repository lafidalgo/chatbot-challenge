from PIL import Image
import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

import utils


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar(authenticator):
    # Initialize the check for the APIs status
    if "check_document_querying_api_status" not in st.session_state:
        st.session_state.check_document_querying_api_status = utils.check_document_querying_api_status()
    if "check_document_extraction_api_status" not in st.session_state:
        st.session_state.check_document_extraction_api_status = utils.check_document_extraction_api_status()

    with st.sidebar:
        logo = Image.open("src/streamlit/assets/logo-hotmart.png")
        st.image(logo)
        st.write("")
        st.write("")

        if st.session_state["authentication_status"]:
            st.page_link("home.py",
                         label="Home", icon="🏠")
            st.page_link("pages/chatbot.py",
                         label="ChatBot", icon="🤖")
            st.page_link("pages/document_extraction.py",
                         label="Extração de Documentos", icon="📄")
            st.page_link("pages/profile_settings.py",
                         label="Ajustes de Conta", icon="🧑")
            st.write("")
            st.write("")

            # Check the status of the Document Querying API
            if st.session_state.check_document_querying_api_status is True:
                st.success(f"Querying API status: OK", icon="✅")
            else:
                st.warning(
                    f"Querying API status: {st.session_state.check_document_querying_api_status}", icon="🚨")
            # Check the status of the Document Extraction API
            if st.session_state.check_document_extraction_api_status is True:
                st.success(f"Extraction API status: OK", icon="✅")
            else:
                st.warning(
                    f"Extraction API status: {st.session_state.check_document_extraction_api_status}", icon="🚨")
            st.write("")
            st.write("")

            authenticator.logout()
        else:
            st.page_link("home.py",
                         label="Home", icon="🏠")
            st.write("")
            st.write("")

            allowed_pages = ["home"]
            if get_current_page_name() not in allowed_pages:
                # If anyone tries to access a secret page without being logged in,
                # redirect them to the login page
                st.switch_page("home.py")
