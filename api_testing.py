import os
from dotenv import load_dotenv

load_dotenv()

openrouter_api_key = os.getenv("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")

if not openrouter_api_key:
    raise ValueError("ERROR: OPENROUTER_API_KEY is missing!")

print(f"Loaded API Key: {openrouter_api_key}")  # Debugging: Remove this after testing
