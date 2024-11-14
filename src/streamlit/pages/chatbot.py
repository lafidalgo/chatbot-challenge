import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration(add_logo=False)

authenticator, auth_config = utils.import_authentication_config()
authenticator.login()

page_formatting.make_sidebar(authenticator)

INITIAL_ASSISTANT_TEXT = "Hello! How may I help you?"

ASSISTANT_AVATAR = "src/streamlit/assets/favicon-chatbot.png"
USER_AVATAR = "src/streamlit/assets/user-icon.png"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", "avatar": ASSISTANT_AVATAR, "content": INITIAL_ASSISTANT_TEXT}]

# Initialize llm models infos
if "qdrant_collections" not in st.session_state:
    st.session_state.qdrant_collections = utils.get_all_qdrant_collections()

# Initialize llm models infos
if "llms_infos" not in st.session_state:
    st.session_state.llms_infos = utils.get_available_llms()

st.markdown("# ChatBot")

# Dropdown to select desired qdrant collection
selected_collection = page_formatting.collection_selectbox(
    st.session_state.qdrant_collections)

# Dropdown to select the language model
selected_llm_model_name = page_formatting.llm_model_selectbox(
    st.session_state.llms_infos)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message["avatar"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Send you question here..."):
    # Display user message in chat message container
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append(
        {"role": "user", "avatar": USER_AVATAR, "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=ASSISTANT_AVATAR):
        references = []
        if not st.session_state.llms_infos:
            response = "Sorry, OpenAI or Replicate API keys not found."
        elif not selected_collection:
            response = "Sorry, no collection selected."
        elif not selected_llm_model_name:
            response = "Sorry, no language model selected."
        else:
            response, references = utils.send_question_to_html_querying_api(
                selected_collection, prompt, selected_llm_model_name)

        # Display response
        st.write(response)
        # Display references
        page_formatting.display_response_references(references)

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "avatar": ASSISTANT_AVATAR, "content": response})
