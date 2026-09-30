import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)


def run_agent(question):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=question
    )

    return response.text
