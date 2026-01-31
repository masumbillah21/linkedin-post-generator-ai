# AI LinkedIn Post Generator

An intelligent LinkedIn post generator that uses AI agents to automatically classify topics and generate professional, engaging content.

## Overview

This application uses a multi-agent architecture to generate LinkedIn posts tailored to different content types. It intelligently routes topics to specialized writing agents based on automatic classification.

## Agent Workflow Architecture

The system follows a three-stage workflow:

```text
User Input → Router Agent → Specialized Writer Agent → Generated Post
```

### 1. Router Agent ([agents/router.py](agents/router.py))

The router agent acts as a classifier that determines the nature of the input topic.

**Function**: `classify_topic(topic: str, provider: str) -> str`

**Routing Logic**:

- Takes a topic as input
- Uses a strict classification prompt that returns ONLY "Tech" or "General"
- No explanations or reasoning, just a single-word classification
- Routes the topic to the appropriate specialized writer

**Classification Criteria**:

- **Tech**: Technology-related topics (programming, software, AI, tools, frameworks, etc.)
- **General**: All other professional topics (business, career, leadership, productivity, etc.)

### 2. Specialized Writer Agents

Based on the router's classification, one of two specialized agents generates the post:

#### Tech Writer Agent ([agents/tech_writer.py](agents/tech_writer.py))

**Function**: `write_tech_post(topic: str, language: str, provider: str) -> str`

- Specializes in technology-focused content
- Generates posts with technical context and industry-specific language
- Maintains professional tone suitable for tech professionals

#### General Writer Agent ([agents/general_writer.py](agents/general_writer.py))

**Function**: `write_general_post(topic: str, language: str, provider: str) -> str`

- Handles general professional topics
- Focuses on broader business and career content
- Maintains professional tone suitable for general audiences

### 3. Post Generation Flow

The main orchestration happens in [services/generator.py](services/generator.py):

```python
def generate_linkedin_post(topic: str, language: str, provider: str):
    # Step 1: Classify the topic
    category = classify_topic(topic, provider)

    # Step 2: Route to appropriate writer
    if category == "Tech":
        post = write_tech_post(topic, language, provider)
    else:
        post = write_general_post(topic, language, provider)

    # Step 3: Return classification and generated post
    return category, post
```

## Writing Guidelines

Both agents follow consistent rules ([llm/system_prompt.py](llm/system_prompt.py)):

- 2-4 short paragraphs
- Professional and engaging tone
- End with a thoughtful question or call-to-action
- Include relevant hashtags
- Clean output without reasoning or explanations

## Supported LLM Providers

The application supports multiple AI providers ([llm/factory.py](llm/factory.py)):

| Provider | Model | Speed | Cost |
| -------- | ----- | ----- | ---- |
| **Groq** | qwen/qwen3-32b | Very Fast | Free |
| **Gemini** | gemini-2.5-pro | Fast | Free |
| **OpenAI** | gpt-4o-mini | Fast | Paid |

All models use a temperature of 0.7 for creative yet controlled output.

## Setup

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:

   ```env
   GOOGLE_API_KEY=your_gemini_key
   OPENAI_API_KEY=your_openai_key
   GROQ_API_KEY=your_groq_key
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Select your preferred AI model
2. Enter a topic for your LinkedIn post
3. Choose the output language (English, Bengali, or Spanish)
4. Click "Generate"
5. The system will:
   - Automatically classify your topic
   - Route it to the appropriate writer agent
   - Generate a professional LinkedIn post

## Project Structure

```text
├── agents/
│   ├── router.py           # Topic classification agent
│   ├── tech_writer.py      # Tech-focused post generator
│   └── general_writer.py   # General-purpose post generator
├── llm/
│   ├── factory.py          # LLM provider factory
│   └── system_prompt.py    # Shared system instructions
├── services/
│   └── generator.py        # Main orchestration logic
├── utils/
│   └── clean_output.py     # Output cleaning utilities
├── app.py                  # Streamlit web interface
└── requirements.txt        # Project dependencies
```

## Architecture Benefits

- **Separation of Concerns**: Router logic separated from content generation
- **Specialization**: Each agent focuses on what it does best
- **Flexibility**: Easy to add new agent types or routing rules
- **Provider Agnostic**: Works with multiple LLM providers
- **Multilingual**: Supports multiple output languages
