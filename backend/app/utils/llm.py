import requests

def call_llm(prompt: str) -> str:
    # This assumes you're using Ollama locally with Vicuna or Mistral
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json().get("response", "[Error generating response]") 