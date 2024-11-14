from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/")
def home():
    return RedirectResponse(url="/help/")


@router.get("/help/")
def help():
    return """
    Chatbot Challenge
    
    /help - help endpoint
    """


@router.get("/api-status/")
def api_status():
    return True
