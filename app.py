import streamlit as st
from services.generator import generate_linkedin_post

st.set_page_config(
    page_title="AI LinkedIn Post Generator",
    page_icon="💼"
)

st.title("AI-Powered LinkedIn Post Generator")
st.caption("LangChain + Gemini | Modular Agent System")

topic = st.text_input(
    "Enter Topic",
    placeholder="e.g., AI in Healthcare, Remote Work Productivity"
)

language = st.selectbox(
    "Select Language",
    ["English", "Bengali", "Spanish", "French"]
)

if st.button("Generate Post"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating LinkedIn post..."):
            category, post = generate_linkedin_post(topic, language)

        st.success(f" Routed to **{category} Writer Agent**")
        st.markdown("### Generated LinkedIn Post")
        st.write(post)
