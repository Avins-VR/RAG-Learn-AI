from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context, question):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # safer model
            messages=[
                {"role": "system", "content": "You are a helpful AI teacher."},
                {
                    "role": "user",
                    "content": f"""
Content:
{context}

Question:
{question}

Format:
What:
Why:
How:
Simple Words:
Diagram:
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Real Error: {str(e)}"