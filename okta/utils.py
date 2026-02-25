# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

"""
Class of utility functions.
"""

from datetime import datetime as dt
from enum import Enum
from typing import Any, Dict
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


# Dictionary utility functions for nested dictionary operations
# These replace the external flatdict dependency


def flatten_dict(d: Dict[str, Any], parent_key: str = '', delimiter: str = '::') -> Dict[str, Any]:
    """
    Flatten a nested dictionary into a single-level dictionary.

    Args:
        d: The dictionary to flatten
        parent_key: The base key to prepend to all keys (used in recursion)
        delimiter: The delimiter to use when joining keys (default '::' to avoid collision with snake_case)

    Returns:
        A flattened dictionary with delimited keys

    Examples:
        >>> flatten_dict({'a': {'b': 1, 'c': 2}})
        {'a::b': 1, 'a::c': 2}

        >>> flatten_dict({'x': {'y': {'z': 3}}})
        {'x::y::z': 3}

        >>> flatten_dict({'user_name': {'first_name': 'John'}})
        {'user_name::first_name': 'John'}
    """
    items = []
    for key, value in d.items():
        new_key = f"{parent_key}{delimiter}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, delimiter).items())
        else:
            items.append((new_key, value))
    return dict(items)


def unflatten_dict(d: Dict[str, Any], delimiter: str = '::') -> Dict[str, Any]:
    """
    Unflatten a dictionary with delimited keys into a nested structure.

    Args:
        d: The flattened dictionary
        delimiter: The delimiter used in the keys

    Returns:
        A nested dictionary

    Examples:
        >>> unflatten_dict({'a_b': 1, 'a_c': 2})
        {'a': {'b': 1, 'c': 2}}

        >>> unflatten_dict({'x_y_z': 3})
        {'x': {'y': {'z': 3}}}
    """
    result: Dict[str, Any] = {}
    for key, value in d.items():
        parts = key.split(delimiter)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def deep_merge(base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deep merge two dictionaries, with updates overriding base values.

    Args:
        base: The base dictionary
        updates: Dictionary with values to merge/override

    Returns:
        A new dictionary with merged values

    Examples:
        >>> deep_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}

        >>> deep_merge({'a': {'b': 1}}, {'a': {'c': 2}})
        {'a': {'b': 1, 'c': 2}}
    """
    result = base.copy()
    for key, value in updates.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def remove_empty_values(d: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively remove empty string values from a nested dictionary.

    Args:
        d: The dictionary to clean

    Returns:
        A new dictionary with empty strings removed

    Examples:
        >>> remove_empty_values({'a': '', 'b': 'value'})
        {'b': 'value'}

        >>> remove_empty_values({'a': {'b': '', 'c': 1}})
        {'a': {'c': 1}}

    Note:
        Only removes empty strings (""), not other falsy values like None, 0, False, []
    """
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            nested = remove_empty_values(value)
            if nested:  # Only add if nested dict is not empty after cleaning
                result[key] = nested
        elif value != "":
            result[key] = value
    return result
