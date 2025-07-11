import os
import requests

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def get_suggestions(prompt, num_suggestions=3):
    if not GEMINI_API_KEY:
        return []

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": f"Suggest {num_suggestions} helpful replies to: '{prompt}'"}]}]
    }

    try:
        response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [candidate["content"]["parts"][0]["text"] for candidate in data.get("candidates", [])][:num_suggestions]
    except Exception as e:
        print("Gemini API error:", e)
        return []
