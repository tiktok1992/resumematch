import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key=os.getenv("google_api_key")
if not api_key:
    raise ValueError("oogle_api_key not found")

genai.configure(api_key=api_key)

print("available gemini models")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f" - {model.name}")