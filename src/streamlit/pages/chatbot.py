import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration(add_logo=False)

authenticator, auth_config = utils.import_authentication_config()
authenticator.login()

page_formatting.make_sidebar(authenticator)

INITIAL_ASSISTANT_TEXT = "Olá! Como posso te ajudar hoje?"

ASSISTANT_AVATAR = "src/streamlit/assets/favicon-hotmart.png"
USER_AVATAR = "src/streamlit/assets/user-icon.png"

HTML_COLLECTION_NAME = "teste"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", "avatar": ASSISTANT_AVATAR, "content": INITIAL_ASSISTANT_TEXT}]

# Initialize llm models infos
if "llms_infos" not in st.session_state:
    st.session_state.llms_infos = utils.get_available_llms()

st.markdown("# ChatBot")

# Dropdown to select the language model
selected_llm_model_name = page_formatting.llm_model_selectbox(
    st.session_state.llms_infos)

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
        if st.session_state.llms_infos:
            response, references = utils.send_question_to_html_querying_api(
                HTML_COLLECTION_NAME, prompt, selected_llm_model_name)
        else:
            response = "Sorry, OpenAI or Replicate API keys not found."
            references = []

        # Display response
        st.write(response)
        # Display references
        page_formatting.display_response_references(references)

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "avatar": ASSISTANT_AVATAR, "content": response})
