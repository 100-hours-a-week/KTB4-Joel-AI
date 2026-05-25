import json
import os
import urllib.request
from fastapi import HTTPException

def summarize_with_ollama(prompt: str):
    model = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
    url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    data = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode())

    return result["response"].strip()


def summarize(prompt: str):
    provider = os.getenv("AI_PROVIDER", "ollama")
    print(f"[DEBUG] AI_PROVIDER={provider}")

    if provider == "ollama":
        return provider, summarize_with_ollama(prompt)
    
    raise HTTPException(
        status_code=400, 
        detail=f"지원하지 않는 AI 제공자(Provider)입니다: '{provider}'." 
    )