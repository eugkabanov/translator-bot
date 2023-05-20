import openai
from config import OPENAI_API_KEY
import logging

from .calculate_usage_price import calculate_usage_price

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
            "content": "You are a bilingual assistant, skilled in detecting the nuances and idioms of both the source and target languages. Your task is to translate the input text to the specified language in a way that preserves its meaning while sounding natural and idiomatic in the target language. If necessary, feel free to rephrase the text to achieve this.",
        },
        {
            "role": "user",
            "content": f'Translate the following text to {target_language}, taking into account any cultural idioms or phrases that might make the translation more natural: "{text}".',
        },
    ]

    logger = logging.getLogger(__name__)

    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=MESSAGES,
            max_tokens=1000,
        )

        # Log usage
        used_tokens: int = response["usage"]["total_tokens"]
        used_price = calculate_usage_price(used_tokens)
        logger.info(
            f"Translation success. Used tokens: {used_tokens}. Usage price: {used_price}"
        )

        translated_text: str = response["choices"][0]["message"]["content"]
        # Remove quotes from translated text
        formatted_translated_text = translated_text[1:-1]

        return formatted_translated_text
    except Exception as e:
        logger.error(f"Caught translate exception: {e}.")

        # Return error message
        return "Oops, something went wrong."
