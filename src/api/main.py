from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def home():
    return RedirectResponse(url="/help/")


@app.get("/help/")
def help():
    return """
    Hotmart Challenge
    
    /help - help endpoint
    """


if __name__ == "__main__":
    import uvicorn
    # Start FastAPI
    uvicorn.run(app, port=8000, host="0.0.0.0")
