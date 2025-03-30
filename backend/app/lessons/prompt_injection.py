from app.utils.llm import call_llm

SYSTEM_PROMPT = "You are a helpful assistant. Only answer questions about AI safety."

def vulnerable_llm_response(user_input: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"
    return call_llm(prompt) 