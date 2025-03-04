import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file (if used)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBKsIf_wDcZ0_PEgclEtL6VIqGZT1Km6xM")

def get_genai_model():
    import google.generativeai as genai
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel("gemini-1.5-pro-latest")
