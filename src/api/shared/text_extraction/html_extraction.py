from llama_index.readers.web import BeautifulSoupWebReader


def extract_documents_from_url(url: str):
    documents = BeautifulSoupWebReader().load_data([url])

    return documents
