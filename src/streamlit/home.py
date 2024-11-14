import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration()

authenticator, auth_config = utils.import_authentication_config()
authenticator.login()

page_formatting.make_sidebar(authenticator)

if st.session_state["authentication_status"]:
    # Markdown
    st.markdown(
        f"""
        ## Hello, {st.session_state["name"]}!
        ## Welcome to Context Chatbot!

        This web application is a powerful tool that uses advanced artificial intelligence techniques to analyze and extract information from documents.

        With the power of AI, you can:

        - **Instant Analysis**: Gain quick insights into your documents.
        - **Process Optimization**: Simplify and streamline data analysis, saving time and resources.
        - **Strategic Decisions**: Base your business decisions on accurate information about trends and performance.

        Explore the features in the sidebar menu and discover how this tool can transform your approach to document analysis!
        """
    )

elif st.session_state["authentication_status"] is False:
    st.error('Incorrect username and/or password')
elif st.session_state["authentication_status"] is None:
    st.warning('Please log in to access the system.')
