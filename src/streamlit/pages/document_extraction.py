import streamlit as st

import page_formatting

import utils

page_formatting.init_page_configuration(add_logo=False)

authenticator, auth_config = utils.import_authentication_config()

page_formatting.make_sidebar(authenticator)

st.markdown(
    """
        # Document Extraction

        In this section, you can register a new reference document.

        To do this, you have two options. Choose only one:
        - **Register by URL**: Enter the URL of the desired document. Example: https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/
        - **Register by file**: Upload the file.

        Next, enter the document's name and click the "Register Document" button.
        """
)

# Get document URL
document_url = st.text_input("Document URL")
# Get uploaded file
uploaded_file = st.file_uploader("Document File")
# Get collection name
collection_name = st.text_input("Document Name")

# Register document
if st.button("Register Document"):
    if collection_name == "":
        st.error("Please enter the document's name.")
        st.stop()
    if document_url == "" and not uploaded_file:
        st.error("Please provide the URL or the file.")
        st.stop()
    if document_url and uploaded_file:
        st.error("Please provide only the URL or the file.")
        st.stop()

    with st.spinner('Registering document...'):
        if document_url:
            # Send URL to document extraction API
            response = utils.send_url_to_document_extraction_api(
                document_url, collection_name)
        else:
            # Send file to document extraction API
            response = utils.send_file_to_document_extraction_api(
                uploaded_file, collection_name)
    st.success("Document registered successfully!")
