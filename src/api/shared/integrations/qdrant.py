import os
from typing import List

from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core import Settings, Document, StorageContext
from llama_index.core.indices.vector_store.base import VectorStoreIndex

import qdrant_client


def create_vector_store_client():
    # Create a Qdrant client
    url = os.environ.get("QDRANT_CLUSTER_URL",
                         "http://qdrant-hotmart-challenge:6333")
    api_key = os.environ.get("QDRANT_API_KEY", None)

    if not url:
        raise ValueError(
            "Missing environment variables for QDRANT configuration.")

    client = qdrant_client.QdrantClient(
        url=url,
        api_key=api_key,
    )

    return client


def check_collection_exists(collection_name: str):
    client = create_vector_store_client()
    return client.collection_exists(collection_name)


def get_all_collections():
    client = create_vector_store_client()
    all_collections = client.get_collections()
    return all_collections.collections


def get_infos_collection(collection_name):
    client = create_vector_store_client()
    return client.get_collection(collection_name)


def configure_documents_chunks(chunk_size: int = 512, chunk_overlap: int = 0):
    Settings.chunk_size = chunk_size
    Settings.chunk_overlap = chunk_overlap


def build_vector_store_index(documents: List[Document], collection_name: str):
    client = create_vector_store_client()

    # Create a Qdrant vector store
    vector_store = QdrantVectorStore(
        client=client, collection_name=collection_name)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )

    return index


def get_vector_store_index(collection_name: str):
    client = create_vector_store_client()

    vector_store = QdrantVectorStore(
        client=client, collection_name=collection_name)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    return index
