def calculate_usage_price(used_tokens: int):
    """Calculate price for used tokens.

    Parameters:
    used_tokens (int): Used amount of tokens.

    Returns:
    float: Price for used tokens.
    """

    # See https://openai.com/pricing/
    TOKEN_PRICE = 0.002 / 1000

    price = used_tokens * TOKEN_PRICE

    # Round to 4 decimal places
    return round(price, 4)
