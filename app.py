import streamlit as st
from services.generator import generate_linkedin_post

st.set_page_config(page_title="AI LinkedIn Generator", page_icon=":robot_face:")

st.title("AI-Powered LinkedIn Post Generator")

provider = st.selectbox(
    "Select AI Model",
    [
        "groq",
        "gemini",
        "openai",
    ],
    format_func=lambda x: {
        "groq": "Groq (LLaMA – Fast)",
        "gemini": "Gemini (Free)",
        "openai": "OpenAI (GPT)",
    }[x]
)

topic = st.text_input("Topic")
language = st.selectbox("Language", ["English", "Bengali", "Spanish"])

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating..."):
            category, post = generate_linkedin_post(topic, language, provider)

        st.write(post)
