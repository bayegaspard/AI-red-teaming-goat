from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.lessons import prompt_injection
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to OWASP AI Goat 🧠🐐"}

@app.post("/lesson/1/prompt-injection")
async def lesson_1_prompt_injection(request: Request):
    try:
        body = await request.json()
        user_input = body.get("input")
        if not user_input:
            return {"error": "Missing 'input' field in request body"}
        return {"response": prompt_injection.vulnerable_llm_response(user_input)}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON in request body"}
    except Exception as e:
        return {"error": f"Server error: {str(e)}"} 