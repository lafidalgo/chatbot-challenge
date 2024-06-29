import streamlit as st

from navigation import make_sidebar

import utils
import chatbot_funcs

utils.init_page_configuration(add_logo=False)

authenticator, auth_config = utils.import_authentication_config()
authenticator.login()

make_sidebar(authenticator)

INITIAL_ASSISTANT_TEXT = "Olá! Como posso te ajudar hoje?"

ASSISTANT_AVATAR = "src/streamlit/assets/favicon-hotmart.png"
USER_AVATAR = "src/streamlit/assets/user-icon.png"

st.markdown("# ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", "avatar": ASSISTANT_AVATAR, "content": INITIAL_ASSISTANT_TEXT}]

# Initialize the check for the OpenAI API key
if "check_openai_key" not in st.session_state:
    st.session_state.check_openai_key = utils.check_openai_key_api()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message["avatar"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Envie sua pergunta aqui..."):
    # Display user message in chat message container
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append(
        {"role": "user", "avatar": USER_AVATAR, "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
        if st.session_state.check_openai_key:
            response = st.write(utils.send_question_to_openai_api(prompt))
            # response = st.write_stream(
            #    utils.send_question_to_openai_api(prompt, stream=True))
        else:
            response = st.write_stream(chatbot_funcs.response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "avatar": ASSISTANT_AVATAR, "content": response})
