import openai
from config import OPENAI_API_KEY
import logging

logger = logging.getLogger(__name__)

openai.api_key = OPENAI_API_KEY


def translate(text: str, target_language: str):
    """Translate text to target language.
    It uses OpenAI's API. More info: https://platform.openai.com/docs/api-reference/chat/create

    Parameters:
    text (str): Text to translate.
    target_language (str): Target language defined by user.

    Returns:
    str: Translated text.
    """

    MODEL = "gpt-3.5-turbo"
    MESSAGES = [
        {
            "role": "system",
            "content": "You are a helpful assistant that detects input language and translates it to specified language.",
        },
        {
            "role": "user",
            "content": f'Translate the following text to {target_language}: "{text}". Give response without quotes.',
        },
    ]

    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=MESSAGES,
            max_tokens=1000,
        )

        translated_text: str = response["choices"][0]["message"]["content"]

        # Log usage
        used_tokens: int = response["usage"]["total_tokens"]
        logger.info(f"Translation success. Used tokens: {used_tokens}.")

        return translated_text.strip()
    except Exception as e:
        logger.error(f"Caught translate exception: {e}.")

        # Return error message
        return "Oops, something went wrong."
