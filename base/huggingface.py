import os
from huggingface_hub import InferenceClient

client = InferenceClient(token=os.environ.get("HF_TOKEN"))

def get_suggestions(prompt, num_suggestions=3):
    try:
        outputs = client.text_generation.generate(
            model="google/flan-t5-base",
            inputs=f"Suggest a reply: {prompt}",
            max_new_tokens=50,
            num_return_sequences=num_suggestions,
            temperature=0.7
        )
        return [out.generated_text for out in outputs]
    except Exception as e:
        print("❌ Hugging Face Inference error:", e)
        return []
