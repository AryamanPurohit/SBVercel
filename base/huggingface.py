import os
import requests

HF_API_URL = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-common_gen"
HF_TOKEN = os.environ.get("HF_TOKEN")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_suggestions(prompt, num_suggestions=3):
    payload = {"inputs": f"generate: {prompt}", "parameters": {"num_return_sequences": num_suggestions}}

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()
        return [item["generated_text"] for item in data]
    except Exception as e:
        print("Hugging Face API error:", e)
        return []
