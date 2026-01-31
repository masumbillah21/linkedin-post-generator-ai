from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from llm.gemini import get_gemini_llm

llm = get_gemini_llm()

routing_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
Classify the topic below as either:
- Tech
- General

Topic: {topic}

Respond with only one word.
"""
)

routing_chain = LLMChain(llm=llm, prompt=routing_prompt)

def classify_topic(topic: str) -> str:
    return routing_chain.run(topic).strip()
