from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
import os

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Ensure API keys are loaded
if not openrouter_api_key or not groq_api_key:
    raise ValueError("API keys are missing. Check your .env file!")

# Initiate FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server for Essays and Poems"
)

# Define DeepSeek and Groq LLMs with proper error handling
try:
    deepseek_llm = ChatOpenAI(
        model="deepseek/deepseek-r1-zero:free",  # Correct DeepSeek model on OpenRouter
        api_key=openrouter_api_key,
        base_url="https://openrouter.ai/api/v1",  # Required for OpenRouter
        extra_headers={
            "HTTP-Referer": "https://yourwebsite.com",  # Update this with your site
            "X-Title": "YourAppTitle"
        }
    )
except Exception as e:
    raise ValueError(f"DeepSeek initialization error: {e}")

try:
    groq_llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)
except Exception as e:
    raise ValueError(f"Groq initialization error: {e}")

# Define prompts
essay_prompt = ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words.")
poem_prompt = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5 years child with 100 words.")

# Add routes to FastAPI
try:
    add_routes(app, essay_prompt | deepseek_llm, path="/essay")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"DeepSeek API Route Error: {e}")

try:
    add_routes(app, poem_prompt | groq_llm, path="/poem")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Groq API Route Error: {e}")

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
