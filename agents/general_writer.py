from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm.gemini import get_gemini_llm

llm = get_gemini_llm()

prompt = PromptTemplate(
    input_variables=["topic", "language"],
    template="""
Write a professional LinkedIn post in {language} about this general topic:

Topic: {topic}

Rules:
- 2–4 short paragraphs
- Professional and engaging tone
- End with a thoughtful question or call-to-action
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def write_general_post(topic: str, language: str) -> str:
    return chain.run(topic=topic, language=language)
