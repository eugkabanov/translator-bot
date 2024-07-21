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

    MODEL = "gpt-4o-mini"
    MESSAGES = [
        {
            "role": "system",
            "content": "You are a professional translator. \nYou help people get translations from their input language to the specified language. \n\nI'll give you a text to translate labeled as \"Input:\". \n\nNext I'll give you the target language labeled as \"Target:\".\n\nTranslate the input text to the target language. When translating, keep the following guidelines in mind:\n- Understand the full context and meaning of the source text before translating. Capture the key ideas, tone and purpose.\n- Adapt idioms, metaphors, and culturally-specific references to equivalent phrases that will resonate with the target language and culture. Avoid literal translations of these.\n- Restructure sentences as needed to sound natural and fluent in the target language. The grammatical structure and word order may need to change.\n- Prioritize clarity and comprehension for the target audience. Use words and phrasing that will be easily understood.\n- Maintain the original text's style and formality level in the translation.\n\nImportant: Provide ONLY the translated text as your output, without any additional explanations, commentary or other text. The translation should stand on its own.",
        },
        {
            "role": "user",
            "content": f'Input:\n{text}\n\nTarget:\n{target_language}',
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

        return translated_text
    except Exception as e:
        logger.error(f"Caught translate exception: {e}.")

        # Return error message
        return "Oops, something went wrong."
