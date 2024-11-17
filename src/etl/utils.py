from datetime import datetime
import re
from typing import Optional

from dateutil import parser
from kestra import Kestra


def clean_whitespace(text: str) -> str:
    """
    Strips leading and trailing whitespace and normalizes multiple spaces.

    Parameters:
        text (str): Input string.

    Returns:
        str: Cleaned string.

    Example:
        >>> clean_whitespace("  Hello   World  ")
        'Hello World'
    """
    result = re.sub(r"\s+", " ", text.strip())
    output = dict(input=text, output=result)
    Kestra.outputs(output)
    return result


def title_case(text: str) -> str:
    """
    Converts a string to title case.

    Parameters:
        text (str): Input string.

    Returns:
        str: Title-cased string.

    Example:
        >>> title_case("  alice SMITH  ")
        'Alice Smith'
    """
    result = text.strip().title()
    output = dict(input=text, output=result)
    Kestra.outputs(output)
    return result


def standardize_date_format(date_str: str) -> Optional[str]:
    """
    Autodetects the format of a date string and standardizes it to the format YYYY-MM-DD.

    Parameters:
        date_str (str): Input date string.

    Returns:
        Optional[str]: Date string in the standardized format (YYYY-MM-DD), or None if parsing fails.

    Example:
        >>> standardize_date_format("02/15/1988")
        '1988-02-15'
        >>> standardize_date_format("15-02-1988")
        '1988-02-15'
        >>> standardize_date_format("1988.02.15")
        '1988-02-15'
    """
    try:
        parsed_date = parser.parse(date_str)  # Automatically detect the input format
        standardized_date = parsed_date.strftime("%Y-%m-%d")  # Output in standardized format
        Kestra.outputs(dict(input=date_str, output=standardized_date))
        return standardized_date
    except (ValueError, parser.ParserError):  # Handle invalid dates
        return None


def remove_special_characters(text: str, allowed_chars: str = "") -> str:
    """
    Removes special characters from a string, keeping only alphanumeric characters
    and those specified in `allowed_chars`.

    Parameters:
        text (str): Input string.
        allowed_chars (str): String of additional characters to allow.

    Returns:
        str: Cleaned string.

    Example:
        >>> remove_special_characters("Hello@World!123", allowed_chars="@")
        'Hello@World123'
        >>> remove_special_characters("123-456-7890", allowed_chars="-")
        '123-456-7890'
    """
    pattern = f"[^{re.escape(allowed_chars)}a-zA-Z0-9\s]"
    result = re.sub(pattern, "", text)
    output = dict(input=text, output=result)
    Kestra.outputs(output)
    return result


def parse_numeric(text: str) -> Optional[float]:
    """
    Parses a string into a float, handling common numeric formatting issues.

    Parameters:
        text (str): Input string.

    Returns:
        Optional[float]: Parsed float, or None if parsing fails.

    Example:
        >>> parse_numeric("$1,234.56")
        1234.56
        >>> parse_numeric("  7890 ")
        7890.0
    """
    try:
        result = float(text.replace(",", "").replace("$", "").strip())
        output = dict(input=text, output=result)
        Kestra.outputs(output)
        return result
    except ValueError:
        return None
