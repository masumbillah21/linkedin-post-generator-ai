from agents.router import classify_topic
from agents.tech_writer import write_tech_post
from agents.general_writer import write_general_post

def generate_linkedin_post(topic: str, language: str):
    category = classify_topic(topic)

    if category == "Tech":
        post = write_tech_post(topic, language)
    else:
        post = write_general_post(topic, language)

    return category, post
