from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from pydantic import BaseModel
from typing import Optional

import src.api.shared.integrations.openai as openai


class OpenAICompletionParams(BaseModel):
    user_prompt: str
    system_prompt: Optional[str] = None
    stream_response: Optional[bool] = False


router = APIRouter()


@router.get("/check-openai/")
def check_openai():
    return {"results": openai.check_openai_key(),
            "params": "",
            "error": ""}


@router.post("/openai-completion/")
async def openai_completion(params: OpenAICompletionParams = Depends()):
    stream_response = params.stream_response

    response = openai.get_openai_completions(
        params.user_prompt, params.system_prompt, stream=stream_response)

    if stream_response:
        return StreamingResponse(response, media_type='text/event-stream')
    else:
        return {"results": response,
                "params": params,
                "error": ""}
