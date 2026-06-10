from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_bot_response


app = FastAPI(
    title="Ask Kinkini Backend",
    description="Backend API for Kinkini's personal portfolio chatbot",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def home():
    return {
        "message": "Ask Kinkini backend is running successfully."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    bot_reply = get_bot_response(request.message)
    return {
        "response": bot_reply
    }