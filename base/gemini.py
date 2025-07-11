import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_suggestions(prompt):
    try:
        response = model.generate_content(
            f"Suggest 3 short and friendly follow-up replies for this chat message:\n\n\"{prompt}\"\n\nList them."
        )
        lines = response.text.strip().split('\n')
        # Extract list items (handles markdown or numbered replies)
        suggestions = [line.lstrip("-1234567890. ").strip() for line in lines if line.strip()]
        return suggestions[:3] if suggestions else ["No suggestions."]
    except Exception as e:
        print("Gemini API error:", e)
        return []
