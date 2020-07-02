"""
Class of utility functions.
"""

from enum import Enum


def format_url(base_string):
    """
    Turns multiline strings in generated clients into
    simple one-line string

    Args:
        base_string (str): multiline URL

    Returns:
        str: single line URL
    """
    return ''.join(
        [line.strip() for line in base_string.splitlines()]
    )


def is_enum_value(value: str, enum: Enum):
    """
    Determines if given string is in given enumeration

    Args:
        value (str): string to test
        enum (Enum): enumeration to test on

    Returns:
        bool: True iff the string is in the enumeration
    """
    return value in set(entry.value for entry in enum)
