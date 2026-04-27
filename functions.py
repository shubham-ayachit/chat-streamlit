import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(messages: list) -> str:
    """
    Send the conversation history to the OpenAI API and return the assistant's reply.

    Args:
        messages: List of message dicts with 'role' and 'content' keys.

    Returns:
        The assistant's response as a string.
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0].message.content
