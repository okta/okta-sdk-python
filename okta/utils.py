# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

"""
Class of utility functions.
"""

from datetime import datetime as dt
from enum import Enum
from urllib.parse import urlsplit, urlunsplit

from okta.constants import DATETIME_FORMAT, EPOCH_DAY, EPOCH_MONTH, EPOCH_YEAR


def format_url(base_string):
    """
    Turns multiline strings in generated clients into
    simple one-line string

    Args:
        base_string (str): multiline URL

    Returns:
        str: single line URL
    """
    return "".join([line.strip() for line in base_string.splitlines()])


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
    dt_obj = dt.strptime(date_time, DATETIME_FORMAT)
    return float((dt_obj - dt(EPOCH_YEAR, EPOCH_MONTH, EPOCH_DAY)).total_seconds())


def convert_absolute_url_into_relative_url(absolute_url):
    """
    Converts absolute url into relative url.

    Args:
        absolute_url (str): URL

    Returns:
        str: URL

    Example:
        >>> convert_absolute_url_into_relative_url('https://test.okta.com/api/v1/users')
        '/api/v1/users'
    """
    url_parts = urlsplit(absolute_url)
    return urlunsplit(("", "", url_parts[2], url_parts[3], url_parts[4]))
