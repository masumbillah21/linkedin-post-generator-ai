from langchain_core.messages import SystemMessage, HumanMessage
from llm.factory import get_llm

SYSTEM_ROUTER = SystemMessage(
    content=(
        "You are a strict classifier.\n"
        "Reply with ONLY one word: Tech or General.\n"
        "No explanations."
    )
)

def classify_topic(topic: str, provider: str) -> str:
    llm = get_llm(provider)

    response = llm.invoke([
        SYSTEM_ROUTER,
        HumanMessage(content=f"Topic: {topic}")
    ])

    return response.content.strip()
