import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

load_dotenv()

def get_llm(provider: str):
    """
    provider: gemini | openai | groq
    """

    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            temperature=0.7,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )

    if provider == "openai":
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    if provider == "groq":
        return ChatGroq(
            model="qwen/qwen3-32b",
            temperature=0.7,
            api_key=os.getenv("GROQ_API_KEY"),
        )

    raise ValueError("Unsupported LLM provider")
