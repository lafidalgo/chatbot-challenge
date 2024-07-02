from fastapi import APIRouter, Depends

from pydantic import BaseModel
from typing import Optional

import src.api.shared.integrations.qdrant as qdrant
import src.api.shared.integrations.openai as openai
import src.api.shared.integrations.replicate as replicate

import src.api.shared.utils as utils


class HTMLQueryingParams(BaseModel):
    collection_name: str
    question: str
    llm_model_name: str
    similarity_top_k: Optional[int] = 4


router = APIRouter()


@router.get("/get-available-llms/")
def available_llms():
    return {"results": utils.get_available_llms(),
            "params": "",
            "error": ""}


@router.post("/html-querying/")
async def html_querying(params: HTMLQueryingParams = Depends()):
    results = {}

    print("Params:", params.model_dump())

    collection_name = params.collection_name

    # Check if the collection doesn't exist
    if not qdrant.check_collection_exists(collection_name):
        return {"results": results, "params": params,
                "error": "Collection doesn't exist yet."}

    llm_model_name = params.llm_model_name

    # Set llm model to be used
    llm_models_infos = utils.get_available_llms()
    if llm_model_name not in llm_models_infos.keys():
        return {"results": results, "params": params,
                "error": "Invalid 'llm_model_name' parameter."}

    selected_llm_model = llm_models_infos[llm_model_name]

    if selected_llm_model["provider"] == "openai":
        openai.configure_llamaindex_openai_llm(selected_llm_model["model_id"])
    elif selected_llm_model["provider"] == "replicate":
        replicate.configure_llamaindex_replicate_llm(
            selected_llm_model["model_id"])

    # Get the query engine from vector store
    query_engine = utils.get_query_engine_from_vector_store(
        collection_name, params.similarity_top_k)

    question = params.question

    print("Query question:", question)
    response = query_engine.query(question)
    print("Query response:", response)

    # Return the results
    results["response"] = response

    return {"results": results, "params": params, "error": ""}
