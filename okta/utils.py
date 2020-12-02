"""
Class of utility functions.
"""

import re

from enum import Enum
from datetime import datetime as dt
from okta.constants import DATETIME_FORMAT, EPOCH_DAY, EPOCH_MONTH,\
    EPOCH_YEAR


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


def convert_date_time_to_seconds(date_time):
    """
    Takes in a date time string and returns the number of seconds
    since the epoch (Unix timestamp).

    Args:
        date_time (str): Date time string in the datetime format

    Returns:
        float: Number of seconds since the epoch
    """
    dt_obj = dt.strptime(date_time,
                         DATETIME_FORMAT)
    return float((dt_obj
                  - dt(EPOCH_YEAR, EPOCH_MONTH, EPOCH_DAY))
                 .total_seconds())


def to_snake_case(string):
    """
    Converts string to snake case.

    Args:
        string (str): input string in any case

    Returns:
        str: string converted to snake case

    Example:
        >>> to_snake_case('lowerCamelCaseString')
        'lower_camel_case_string'
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()


def to_lower_camel_case(string):
    """
    Converts string to lower camel case.

    Args:
        string (str): input string in any case

    Returns:
        str: string converted to lower camel case

    Example:
        >>> to_lower_camel_case('snake_case_string')
        'snakeCaseString'
    """
    components = string.split('_')
    # lower first letter in the first component
    components[0] = components[0][0].lower() + components[0][1:]
    # join other components with first capitalized first letter
    return components[0] + ''.join(x.title() for x in components[1:])
