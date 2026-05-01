from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context, question):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": """You are an AI teacher.

STRICT RULES:
- Answer ONLY from given content
- Do NOT combine everything in one paragraph
- Each section MUST be on a new line
- Keep answers clear and structured

OUTPUT FORMAT (STRICT):

What:
<2-3 lines>

Why:
<clear reason>

How:
<step-by-step explanation>

Simple Explanation:
<easy explanation>

Diagram:
<vertical flow using ↓ arrows>
"""
                },
                {
                    "role": "user",
                    "content": f"""
CONTENT:
{context}

QUESTION:
{question}

IMPORTANT:
- Follow the format EXACTLY
- Do NOT write in paragraph form
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"