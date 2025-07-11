import os
import requests

HF_API_URL = "https://api-inference.huggingface.co/models/bigscience/T0pp"
HF_TOKEN = os.environ.get("HF_TOKEN")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def get_suggestions(prompt, num_suggestions=3):
    if not HF_TOKEN:
        print("⚠️ Missing HF_TOKEN environment variable.")
        return []

    payload = {
        "inputs": f"generate: {prompt}",
        "parameters": {
            "num_return_sequences": num_suggestions,
            "max_length": 50,
            "temperature": 0.7,
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            return [item.get("generated_text", "") for item in data if "generated_text" in item]

        print("Unexpected response format from Hugging Face API:", data)
        return []

    except requests.exceptions.RequestException as e:
        print("❌ Hugging Face API request failed:", e)
        return []
