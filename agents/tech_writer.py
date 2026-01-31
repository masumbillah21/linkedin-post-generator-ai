from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from llm.factory import get_llm
from llm.system_prompt import SYSTEM_MESSAGE
from utils.clean_output import clean_llm_output

prompt = PromptTemplate(
    input_variables=["topic", "language"],
    template="""
Write a professional LinkedIn post in {language} about the following technology topic:

Topic: {topic}

Rules:
- 2–4 short paragraphs
- Professional and engaging tone
- End with a thoughtful question or call-to-action
"""
)

def write_tech_post(topic: str, language: str, provider: str) -> str:
    llm = get_llm(provider)

    human_message = HumanMessage(
        content=prompt.format(topic=topic, language=language)
    )

    response = llm.invoke([SYSTEM_MESSAGE, human_message])

    return clean_llm_output(response.content)
