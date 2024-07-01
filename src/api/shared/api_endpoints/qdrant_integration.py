from fastapi import APIRouter, Depends

from pydantic import BaseModel

import src.api.shared.integrations.qdrant as qdrant


class CollectionInfosParams(BaseModel):
    collection_name: str


router = APIRouter()


@router.get("/get-all-collections/")
def all_collections():
    return {"results": {"collections": qdrant.get_all_collections()},
            "params": "",
            "error": ""}


@router.get("/get-infos-collection/")
def infos_collection(params: CollectionInfosParams = Depends()):
    return {"results": qdrant.get_infos_collection(params.collection_name),
            "params": params,
            "error": ""}


@router.get("/collection-exists/")
def collection_exists(params: CollectionInfosParams = Depends()):
    return {"results": qdrant.check_collection_exists(params.collection_name),
            "params": params,
            "error": ""}
