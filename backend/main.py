### owasp-ai-goat/backend/app/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.lessons import prompt_injection

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
    body = await request.json()
    user_input = body.get("input")
    return {"response": prompt_injection.vulnerable_llm_response(user_input)}


### owasp-ai-goat/backend/app/lessons/prompt_injection.py
from app.utils.llm import call_llm

SYSTEM_PROMPT = "You are a helpful assistant. Only answer questions about AI safety."

def vulnerable_llm_response(user_input: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"
    return call_llm(prompt)


### owasp-ai-goat/backend/app/utils/llm.py
import requests

def call_llm(prompt: str) -> str:
    # This assumes you're using Ollama locally with Vicuna or Mistral
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json().get("response", "[Error generating response]")


### owasp-ai-goat/backend/requirements.txt
fastapi
uvicorn
requests


### owasp-ai-goat/frontend/src/pages/Lesson1.jsx
import { useState } from "react";

function Lesson1() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = async () => {
    const res = await fetch("http://localhost:8000/lesson/1/prompt-injection", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input })
    });
    const data = await res.json();
    setOutput(data.response);
  };

  return (
    <div>
      <h2>Lesson 1: Prompt Injection</h2>
      <p>Try to bypass the system prompt and make the LLM say something off-topic.</p>
      <textarea value={input} onChange={(e) => setInput(e.target.value)} rows="4" cols="50" />
      <br />
      <button onClick={handleSubmit}>Submit</button>
      <pre>{output}</pre>
    </div>
  );
}

export default Lesson1;
