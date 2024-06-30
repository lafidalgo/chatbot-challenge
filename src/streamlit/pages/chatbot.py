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

HTML_COLLECTION_NAME = "teste"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", "avatar": ASSISTANT_AVATAR, "content": INITIAL_ASSISTANT_TEXT}]

# Initialize the check for the OpenAI API key
if "check_openai_key" not in st.session_state:
    st.session_state.check_openai_key = utils.check_openai_key_api()


st.markdown("# ChatBot")

# Dropdown to select the language model
dropdown_label = "Selecione o modelo de linguagem desejado:"
llms_infos = utils.get_available_llms()
selected_llm_model_name = st.selectbox(dropdown_label, llms_infos.keys())

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
            response, references = utils.send_question_to_html_querying_api(
                HTML_COLLECTION_NAME, prompt, selected_llm_model_name)
            # response = utils.send_question_to_openai_api(prompt)
            # response = st.write_stream(
            #    utils.send_question_to_openai_api(prompt, stream=True))
            st.write(response)
        else:
            response = chatbot_funcs.response_generator()
            st.write_stream(response)

        # Display references
        chatbot_funcs.display_response_references(references)

    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "avatar": ASSISTANT_AVATAR, "content": response})
