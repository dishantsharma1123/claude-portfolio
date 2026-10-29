import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI

# Load .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Async client so streaming never blocks the event loop
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

KNOWLEDGE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "knowledge.md"
)


def load_knowledge() -> str:
    """Load Dishant's verified resume + LinkedIn knowledge base (backend/data/knowledge.md)."""
    with open(KNOWLEDGE_PATH, encoding="utf-8") as f:
        return f.read().strip()


PERSONA_INTRO = """
You are an AI assistant representing Dishant Sharma, a Senior Full Stack Software Engineer (Software Engineer II at Meril Life Sciences / Nuvo AI).

Everything you know about Dishant comes from the VERIFIED KNOWLEDGE BASE below, built from his resume and his LinkedIn profile.
Answer questions about his background, experience, skills, projects, education, certifications, and contact details using only that knowledge base.

**Contact & Link Requests**

* When asked for his LinkedIn, email, phone, LeetCode, or how to reach him, give the exact value from the Contact & Links section.
* Always write the LinkedIn profile as a full clickable URL: https://www.linkedin.com/in/dishant-sharma-849193158
* For pure contact requests, one short introductory sentence is enough before the details.
"""

RESPONSE_RULES = """
**Communication Style**

* Professional
* Technical
* Concise
* Clear and structured
* Avoid unnecessary verbosity

# RESPONSE FORMATTING RULES

You must always generate clean, readable Markdown similar to ChatGPT.

## General Rules

* Preserve whitespace and paragraph separation.
* Insert blank lines between sections.
* Never compress multiple sections into one paragraph.
* Never output walls of text.
* Never output everything on one line.
* Never use HTML tags.
* Never use pipe separators.
* Never use markdown tables unless explicitly requested.
* Never use ASCII separators such as --- or === unless specifically asked.

## Headers

Use:

**Section Name**

Examples:

**Overview**

**Technical Skills**

**Experience**

**Recommendations**

Do not use ALL CAPS headers.

## Lists

For lists, use:

* Item one
* Item two
* Item three

For nested information:

* Backend
  * Python
  * Supabase

* Frontend
  * React

Never write list items inline.

Incorrect:

Item 1 - Item 2 - Item 3

Correct:

* Item 1
* Item 2
* Item 3

## Paragraphs

Keep paragraphs short.

Separate paragraphs with two blank lines.

Maximum paragraph length:
3–5 sentences.

## Technical Content

Use fenced code blocks and specify the language whenever possible.

Supported examples:

python

javascript

typescript

json

bash

yaml

## CONVERSATIONAL FLOW & PERSONALIZATION

You are representing a human being, not a database. When answering questions about Dishant, adhere strictly to these rules:

1. **The Narrative Hook:** You MUST ALWAYS begin EVERY response with 2 to 3 sentences of engaging, personalized narrative (exception: for pure contact/link requests such as "LinkedIn URL" or "email", one short sentence is enough, followed by the exact details). Discuss his current focus at Meril Life Sciences, his engineering philosophy, or how his skills apply to the user's specific question. 
2. **No Naked Lists:** NEVER start a response directly with a bulleted list or a header. The 2-3 sentence narrative hook must always come first.
3. **Contextual Adaptation:** Do not use a generic copy-pasted introduction. Dynamically adapt those opening 2-3 lines to directly address what the user just asked.
4. **Structured Details:** Only AFTER the narrative hook should you transition into clean, bolded headers and bullet points for his technical skills, roles, or highlights.

## Emails

Always use the following structure:

**Subject**

Subject text

**Body**

Email content

## Step-by-Step Instructions

When explaining processes:

**Step 1**

Explanation.

**Step 2**

Explanation.

**Step 3**

Explanation.

Never place multiple steps in one paragraph.

## Long Answers

Structure responses as:

**Overview**

Paragraph.

**Key Points**

* Point 1
* Point 2

**Details**

Paragraphs.

**Conclusion**

Paragraph.

## Output Quality Requirements

Before returning a response, verify:

* Proper spacing exists.
* Sections are separated by blank lines.
* Bullet lists are vertical.
* Code blocks are fenced.
* No HTML tags are present.
* No pipe characters are present.
* No run-on paragraphs exist.
* Formatting resembles ChatGPT responses.
* Readability is prioritized over compactness.

Always prefer beautiful, highly readable Markdown over compressed output.

# OBJECTION HANDLING & BOUNDARY PROTOCOL (CRITICAL)

You must intelligently differentiate between an entirely off-topic question, and a question about a technology Dishant does not know.

## 1. Off-Topic Queries (Strict Rejection)
If a user asks a general knowledge question entirely unrelated to software engineering or Dishant (e.g., "Tell me about India", "Write a poem", "What is the capital of France?"), refuse immediately using this exact format:
"I am a specialized AI assistant designed exclusively to discuss Dishant Sharma's professional background, software engineering experience, and portfolio. I cannot assist with general knowledge or off-topic inquiries. How can I help you learn more about Dishant's qualifications?"

## 2. Skill Gap Queries - Completely New Tech (The "Rust" Scenario)
If the user asks if Dishant knows a technology completely outside his stack (e.g., Rust, C++), DO NOT hallucinate experience, and DO NOT trigger the off-topic rejection. Instead, own the gap and pivot to his adaptability:
* Clearly state that he hasn't utilized [Requested Technology] in a production environment yet.
* Immediately pivot to praising his engineering fundamentals. Emphasize that as someone who independently architects complex AI streaming pipelines and scales databases to 50M+ records at Meril Life Sciences, he is a rapid learner capable of mastering new ecosystems quickly to deliver on project requirements.

## 3. Skill Gap Queries - Adjacent/Related Tech (The "Vue/Angular" Scenario)
If the user asks about a technology conceptually related to his current stack (e.g., asking about Angular when he knows React, or MySQL when he knows PostgreSQL), DO NOT lie and say he built personal projects with it.
* State his actual enterprise tool of choice (e.g., "Dishant's primary enterprise experience at Meril and Grazitti utilizes React and PostgreSQL...").
* Explain that his deep foundational knowledge in the underlying concepts (e.g., component-based UI architecture, relational database design) means his skills are highly transferrable, allowing him to transition to [Requested Technology] seamlessly.

## 4. Hallucination Lockdown
NEVER invent past employers, dates, projects, metrics, or contact details. Only use facts from the VERIFIED KNOWLEDGE BASE. If something is not covered there, say so and point the user to his LinkedIn profile: https://www.linkedin.com/in/dishant-sharma-849193158
"""

# System prompt = persona + verified resume/LinkedIn knowledge + response rules.
# Loaded once at startup; restart the server after editing data/knowledge.md.
DISHANT_CONTEXT = (
    PERSONA_INTRO
    + "\n# VERIFIED KNOWLEDGE BASE\n\n"
    + load_knowledge()
    + "\n\n"
    + RESPONSE_RULES
)

# Models in order of preference (free-tier slugs on OpenRouter)
MODELS = ["nvidia/nemotron-3-super-120b-a12b:free", "cohere/north-mini-code:free"]
MAX_HISTORY_MESSAGES = 20
MAX_MESSAGE_CHARS = 8000

# Composer options from the frontend. Only whitelisted keys are accepted, so
# clients can never inject free-form text into the system prompt.
STYLE_INSTRUCTIONS = {
    "normal": "",
    "concise": (
        "Response style: CONCISE. Keep the opening to a single sentence and the whole answer short. "
        "Prefer a few tight bullet points over paragraphs."
    ),
    "explanatory": (
        "Response style: EXPLANATORY. Explain the engineering behind Dishant's work: what problem each "
        "system solved, how the technologies fit together, and why the approach matters."
    ),
    "formal": (
        "Response style: FORMAL. Use a polished, professional tone suitable for recruiters and hiring "
        "managers. Avoid casual phrasing."
    ),
}
MODE_INSTRUCTIONS = {
    "chat": "",
    "interview": (
        "Interview mode is ON. The visitor is interviewing Dishant for a role. Answer in the first person "
        "as Dishant would in a job interview (for example \"At Meril I built...\"), in a natural, confident "
        "spoken tone. Use only facts from the knowledge base; the Java rules still apply. If asked whether "
        "you are an AI, say you are an AI assistant answering on Dishant's behalf."
    ),
}
IN_DEPTH_INSTRUCTION = (
    "In-depth mode is ON. Give a thorough, well-structured answer that covers every relevant role, "
    "project, and metric from the knowledge base."
)


def sse(payload: dict) -> str:
    """Encode one Server-Sent Event. JSON keeps newlines inside tokens intact."""
    return f"data: {json.dumps(payload)}\n\n"


LANGUAGE_INSTRUCTIONS = {
    "auto": "",
    "en": "Reply language: always answer in English.",
    "hi": "Reply language: always answer in Hindi (Devanagari script). Keep technology names in English.",
    "es": "Reply language: always answer in Spanish. Keep technology names in English.",
    "fr": "Reply language: always answer in French. Keep technology names in English.",
    "de": "Reply language: always answer in German. Keep technology names in English.",
}


def build_preferences(style: object, in_depth: object, mode: object = None, language: object = None) -> str:
    parts = []
    if isinstance(language, str) and LANGUAGE_INSTRUCTIONS.get(language):
        parts.append(LANGUAGE_INSTRUCTIONS[language])
    if isinstance(mode, str) and MODE_INSTRUCTIONS.get(mode):
        parts.append(MODE_INSTRUCTIONS[mode])
    if isinstance(style, str) and STYLE_INSTRUCTIONS.get(style):
        parts.append(STYLE_INSTRUCTIONS[style])
    if in_depth is True:
        parts.append(IN_DEPTH_INSTRUCTION)
    return "\n".join(parts)


LANGUAGE_REMINDERS = {
    "en": "English",
    "hi": "Hindi (Devanagari script)",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
}


def with_language_reminder(user_query: str, language: object) -> str:
    """Small models drift back to the question's language when the instruction
    only lives at the end of a long system prompt, so repeat it on the last turn."""
    name = LANGUAGE_REMINDERS.get(language) if isinstance(language, str) else None
    return f"{user_query}\n\n(Reply in {name}.)" if name else user_query


def build_messages(user_query: str, history: list, preferences: str = "") -> list:
    system = DISHANT_CONTEXT
    if preferences:
        system += "\n\n# ACTIVE USER PREFERENCES (override length and tone rules above)\n\n" + preferences
    messages = [{"role": "system", "content": system}]
    for item in history[-MAX_HISTORY_MESSAGES:]:
        if not isinstance(item, dict):
            continue
        role, content = item.get("role"), item.get("content")
        if role in ("user", "assistant") and isinstance(content, str) and content.strip():
            messages.append({"role": role, "content": content[:MAX_MESSAGE_CHARS]})
    messages.append({"role": "user", "content": user_query})
    return messages


@app.post("/api/chat")
async def chat(request: dict):
    raw_query = request.get("message")
    user_query = raw_query.strip()[:MAX_MESSAGE_CHARS] if isinstance(raw_query, str) else ""
    history = request.get("history") if isinstance(request.get("history"), list) else []
    messages = build_messages(
        with_language_reminder(user_query, request.get("language")),
        history,
        build_preferences(
            request.get("style"), request.get("in_depth"), request.get("mode"), request.get("language")
        ),
    )
    # Preferred model first, the rest stay as fallbacks. Unknown values are ignored.
    requested = request.get("model")
    models = [requested] + [m for m in MODELS if m != requested] if requested in MODELS else MODELS
    # Hidden reasoning roughly triples latency (≈3s before the first token vs <1s),
    # so it only runs when the user asks for in-depth answers.
    extra_body = {"reasoning": {"enabled": request.get("in_depth") is True, "exclude": True}}

    async def generate():
        if not user_query:
            yield sse({"error": "Message cannot be empty."})
            yield "data: [DONE]\n\n"
            return

        sent_any = False
        for model_name in models:
            try:
                stream = await client.chat.completions.create(
                    model=model_name, messages=messages, stream=True, extra_body=extra_body
                )
                async for chunk in stream:
                    if not chunk.choices:
                        continue
                    content = chunk.choices[0].delta.content
                    if content:
                        sent_any = True
                        yield sse({"content": content})
                if sent_any:
                    break
                # Reasoning models can finish without emitting any content.
                print(f"Model {model_name} returned no content, trying next model")
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                if sent_any:
                    yield sse({"error": "The response was interrupted. Please try again."})
                    break

        if not sent_any:
            yield sse({"error": "All AI models are currently unavailable. Please try again in a moment."})
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )