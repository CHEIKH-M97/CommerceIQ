def format_currency(value: float) -> str:
    """
    Formats a monetary value.

    Example:
        1234567.8 -> 1,234,567.80 TND
    """

    return f"{value:,.2f} TND"
def format_number(value: int) -> str:
    """
    Formats integers with thousand separators.
    """

    return f"{value:,}"