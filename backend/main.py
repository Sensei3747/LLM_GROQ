# backend/main.py

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from groq_client import query_groq

app = FastAPI()

# Allow frontend dev environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                   "https://llm-groq-gfvsgu5a0-vivekofficial619-gmailcoms-projects.vercel.app",
                   "https://llm-groq.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "FastAPI Backend is Running", "status": "online"}

@app.head("/")
async def root_head():
    return Response()

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_prompt = body.get("prompt", "")
    if not user_prompt:
        return {"response": "Empty prompt received."}

    try:
        response = await query_groq(user_prompt)
        return {"response": response}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
    
@app.options("/chat")
async def options_chat():
    return Response(status_code=200)
