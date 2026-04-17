from app.services.gemini_service import generate_text
from app.utils.prompts import email_prompt, improve_text_prompt

def generate_email(topic: str):
    prompt = email_prompt(topic)
    return generate_text(prompt)

def improve_text(text: str):
    prompt = improve_text_prompt(text)
    return generate_text(prompt)