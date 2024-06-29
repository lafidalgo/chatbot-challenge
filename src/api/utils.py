from urllib.parse import urlparse

import src.api.text_extraction.html_extraction as html_extraction
import src.api.integrations.qdrant as qdrant


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def build_vector_store_index_from_url(collection_name: str, html_url: str):
    # Extract the documents from the uploaded files
    print("Extracting documents from files")
    documents = html_extraction.extract_documents_from_url(html_url)

    # Build the vector store index
    print("Building vector store index")
    qdrant.build_vector_store_index(documents, collection_name)

    return documents
