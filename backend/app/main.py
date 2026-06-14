from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.database import init_db
from app.rag_engine import stream_ai_response

app = FastAPI(title="Claude-Style Portfolio Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()

class ChatPayload(BaseModel):
    message: str
    history: list

# Removed the Clerk dependency to open the endpoint
@app.post("/api/chat")
async def chat_endpoint(payload: ChatPayload):
    return StreamingResponse(
        stream_ai_response(payload.message, payload.history), 
        media_type="text/event-stream"
    )