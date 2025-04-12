import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use one of these models:
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Best for quality
# or
# model = genai.GenerativeModel("gemini-1.5-flash-latest")  # Best for speed

def summarize_and_flashcards(notes_text):
    prompt = f"""
    Given the following academic notes:\n\n{notes_text}\n\n
    1. Provide a concise summary (max 5-8 bullet points).
    2. Create 5 flashcards (Q&A format).

    Format strictly as:
    Summary:
    - Point 1
    - Point 2
    ...
    Flashcards:
    Q1: Question here
    A1: Answer here
    Q2: ...
    """
    try:
        response = model.generate_content(prompt)
        if response.parts:
            return response.text
        else:
            return "Error: No response generated. Try simplifying your notes."
    except Exception as e:
        return f"API Error: {str(e)}"