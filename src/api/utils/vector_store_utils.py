import src.api.integrations.qdrant as qdrant
import src.api.prompts.hotmart_prompts as hotmart_prompts
import src.api.text_extraction.html_extraction as html_extraction


def build_vector_store_index_from_url(collection_name: str, html_url: str):
    # Extract the documents from the uploaded files
    print("Extracting documents from files")
    documents = html_extraction.extract_documents_from_url(html_url)

    # Build the vector store index
    print("Building vector store index")
    qdrant.build_vector_store_index(documents, collection_name)

    return documents


def get_query_engine_from_vector_store(collection_name: str, similarity_top_k: int = 4):
    # Get the vector store index
    index = qdrant.get_vector_store_index(collection_name)

    # Query the vector store index
    query_engine = index.as_query_engine(
        similarity_top_k=similarity_top_k)

    # Update the query engine with the custom prompt
    query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": hotmart_prompts.PT_CHAT_TEXT_QA_PROMPT})

    return query_engine
