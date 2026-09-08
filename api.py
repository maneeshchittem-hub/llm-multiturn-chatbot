from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()

@app.post("/chat")
def chat(message: str):
    response = get_response(message)

    return {
        "message": message,
        "response": response
    }