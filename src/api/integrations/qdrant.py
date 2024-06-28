import os

import qdrant_client


def create_vector_store_client():
    # Create a Qdrant client
    url = os.environ.get("QDRANT_CLUSTER_URL")
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
