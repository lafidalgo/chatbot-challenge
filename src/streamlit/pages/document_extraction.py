import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration(add_logo=False)

authenticator, auth_config = utils.import_authentication_config()

page_formatting.make_sidebar(authenticator)

st.markdown(
    """
        # Extração de Documentos

        Nesta seção, você pode cadastrar um novo documento de referência da Hotmart.

        Para isso, você tem duas opções, escolha apenas uma delas:
        - **Cadastro por URL**: Insira a URL do documento desejado. Ex: https://hotmart.com/pt-br/blog/como-funciona-hotmart
        - **Cadastro por arquivo**: Faça o upload do arquivo.

        Em seguida, insira o nome do documento e clique no botão "Cadastrar documento".
        """
)

# Get document URL
document_url = st.text_input("URL do documento")
# Get uploaded file
uploaded_file = st.file_uploader("Arquivo do documento")
# Get collection name
collection_name = st.text_input("Nome do documento")

# Register document
if st.button("Cadastrar documento"):
    if collection_name == "":
        st.error("Por favor, insira o nome do documento.")
        st.stop()
    if document_url == "" and not uploaded_file:
        st.error("Por favor, insira a URL ou o arquivo.")
        st.stop()
    if document_url and uploaded_file:
        st.error("Por favor, insira apenas a URL ou o arquivo.")
        st.stop()

    with st.spinner('Cadastrando documento...'):
        if document_url:
            # Send URL to file extraction API
            response = utils.send_url_to_document_extraction_api(
                document_url, collection_name)
        else:
            # Send file to file extraction API
            response = utils.send_file_to_document_extraction_api(
                uploaded_file, collection_name)
    st.success("Documento cadastrado com sucesso!")
