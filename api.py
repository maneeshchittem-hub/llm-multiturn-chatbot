from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Chatbot API is running"}


@app.post("/chat")
def chat(message: str):
    response = get_response(message)

    return {
        "message": message,
        "response": response
    }