
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found. Check your .env file.")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Start JAWAAD conversation
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
      system_instruction=(
    "You are JAWAAD, a personal voice assistant. "
    "You are running on the user's laptop. "
    "Always answer the user's questions directly. "
    "Never say that you can only communicate through text. "
    "Never tell the user to enable a screen reader. "
    "Keep answers short and natural because your responses "
    "will be spoken aloud using text-to-speech. "
    "Address the user as aslam sir."
)
    )
)


def ask_jawaad(question):
    try:
        response = chat.send_message(question)

        if response.text:
            return response.text

        return "Sorry sir, I could not generate a response."

    except Exception as error:
        print("GEMINI ERROR:", error)
        return "Sorry sir, I could not connect to my intelligence system."
    
def ask_jawaad(message):
    response = chat.send_message(message)
    return response.text

