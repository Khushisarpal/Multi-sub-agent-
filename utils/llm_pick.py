
from pathlib import Path
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

# Project root: the parent directory of utils/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_FILE, override=True)


def pick_llm(Level: str):
    """
    Returns a Gemini chat model based on the requested level.
    """

    models = {
        "low": "gemini-3.5-flash-lite",
        "medium": "gemini-3.6-flash",
        "high": "gemini-3.1-pro-preview",
    }

    level = Level.strip().lower()

    
    if level not in models:
        raise ValueError(f"Unsupported level: {Level}")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from .env")

    return ChatGoogleGenerativeAI(
        model=models[level],
        google_api_key=api_key,
        temperature=0,
        thinking_level= level,
    )
    


