"""
Class of utility functions.
"""

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
