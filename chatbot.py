import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are a helpful AI Conversation Assistant.
Maintain context from the current conversation.
Give clear, accurate, and beginner-friendly answers.
Be polite and professional.
Do not make up information.
"""

conversation_history = []

MAX_MESSAGES = 6


def get_response(user_message):

    conversation_history.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })

    # Context management
    conversation_history[:] = conversation_history[-MAX_MESSAGES:]

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=conversation_history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        if response.text:
            bot_message = response.text

            conversation_history.append({
                "role": "model",
                "parts": [{"text": bot_message}]
            })

            return bot_message

        return "Sorry, I couldn't generate a response."

    except Exception:
        return "Sorry, something went wrong. Please try again."