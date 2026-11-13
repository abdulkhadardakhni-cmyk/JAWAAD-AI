
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
        from fastapi.responses import StreamingResponse
import edge_tts
import io

@app.post("/speak")
async def speak(request: ChatRequest):
    voice = "en-US-GuyNeural"
    communicate = edge_tts.Communicate(request.message, voice)

    audio = bytearray()

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio.extend(chunk["data"])

    return StreamingResponse(
        io.BytesIO(audio),
        media_type="audio/mpeg"
    )
