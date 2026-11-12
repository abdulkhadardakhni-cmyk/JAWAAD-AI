
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from brain import ask_jawaad

app = FastAPI(title="JAWAAD AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "JAWAAD AI backend is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        answer = ask_jawaad(request.message)
        return {"reply": answer}
    except Exception as error:
        return {"error": str(error)}
