import json
import os
import urllib.request


def summarize(prompt: str):
    provider = os.getenv("AI_PROVIDER", "local")

    if provider == "ollama":
        return provider, summarize_with_ollama(prompt)

    return "local", summarize_locally(prompt)


def summarize_locally(prompt: str):
    lines = [line.strip() for line in prompt.splitlines() if line.strip()]
    text = " ".join(lines)
    return text[:120] + ("..." if len(text) > 120 else "")


def summarize_with_ollama(prompt: str):
    model = os.getenv("OLLAMA_MODEL", "llama3.2")
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
