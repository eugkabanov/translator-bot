import openai
import logging
import re

from config import OPENAI_API_KEY
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
            "content": "You are a bilingual assistant, skilled in translating both the literal and idiomatic meanings of phrases from one language to another. After translating the text, consider whether there are any local idioms or phrases in the original language, and what their equivalent idioms or phrases are in the target language. Apply these changes to produce a natural and idiomatic translation in the target language. Always respond in the format: \
            TRANSLATION: '' \
            CAN BE CHANGED TO: '' \
            FINAL RESULT: 'your final translation after considering changes'.",
        },
        {
            "role": "user",
            "content": f'Translate the following text to {target_language}: "{text}".',
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
        """ Example response:
        TRANSLATION: "Hi, I'm Bob."
        CAN BE CHANGED TO: "Hello, my name is Bob."
        FINAL RESULT: "Hello, my name is Bob."
        """

        # Extract only final translated text from response
        # define the pattern to search for, following 'FINAL RESULT:'
        pattern = r'FINAL RESULT: "(.*?)"'

        # find the pattern in the translated text
        match = re.search(pattern, translated_text)

        # extract the matched group (the text inside the quotes)
        if match:
            formatted_translated_text = match.group(1)
        else:
            # fallback to the whole translated text
            formatted_translated_text = translated_text

        return formatted_translated_text
    except Exception as e:
        logger.error(f"Caught translate exception: {e}.")

        # Return error message
        return "Oops, something went wrong."
