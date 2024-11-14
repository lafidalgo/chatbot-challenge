import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration(add_logo=False)

authenticator, auth_config = utils.import_authentication_config()

page_formatting.make_sidebar(authenticator)

st.markdown("# Profile Settings")

# Reset password
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            utils.update_authentication_config(auth_config)
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

# Update user details
if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            utils.update_authentication_config(auth_config)
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
