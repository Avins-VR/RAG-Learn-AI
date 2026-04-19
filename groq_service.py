from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context, question):
    try:
        context = context[:3000]

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.3,
            messages=[
                {
                    "role": "system",
                    "content": """You are an AI teacher.

RULES:
- Answer ONLY using the given content.
- If content is incomplete, give best possible explanation.
- Avoid very short answers.
- Keep explanation clear and moderate level (not too simple, not complex).

FORMAT:
What:
Why:
How:
Simple Words:
Diagram:
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
- Always include a diagram like:
A → B → C
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error: {str(e)}"