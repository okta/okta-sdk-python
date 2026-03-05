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
from typing import Any
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


def flatten_dict(
    d: dict[str, Any],
    parent_key: str = '',
    delimiter: str = '::',
    _depth: int = 0,
    max_depth: int = 100
) -> dict[str, Any]:
    """
    Flatten a nested dictionary into a single-level dictionary.

    Args:
        d: The dictionary to flatten
        parent_key: The base key to prepend to all keys (used in recursion)
        delimiter: The delimiter to use when joining keys (default '::' to avoid collision with snake_case)
        _depth: Internal recursion depth counter (do not set manually)
        max_depth: Maximum allowed nesting depth (default 100)

    Returns:
        A flattened dictionary with delimited keys

    Raises:
        TypeError: If d is not a dictionary
        ValueError: If nesting depth exceeds max_depth

    Examples:
        >>> flatten_dict({'a': {'b': 1, 'c': 2}})
        {'a::b': 1, 'a::c': 2}

        >>> flatten_dict({'x': {'y': {'z': 3}}})
        {'x::y::z': 3}

        >>> flatten_dict({'user_name': {'first_name': 'John'}})
        {'user_name::first_name': 'John'}
    """
    if not isinstance(d, dict):
        raise TypeError(f"flatten_dict expects dict, got {type(d).__name__}")

    if _depth > max_depth:
        raise ValueError(
            f"Dictionary nesting depth exceeds maximum allowed depth of {max_depth}. "
            f"This may indicate a circular reference or malformed configuration."
        )

    result = {}
    for key, value in d.items():
        new_key = f"{parent_key}{delimiter}{key}" if parent_key else key
        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key, delimiter, _depth + 1, max_depth))
        else:
            result[new_key] = value
    return result


def unflatten_dict(d: dict[str, Any], delimiter: str = '::') -> dict[str, Any]:
    """
    Unflatten a dictionary with delimited keys into a nested structure.

    Args:
        d: The flattened dictionary
        delimiter: The delimiter used in the keys

    Returns:
        A nested dictionary

    Raises:
        TypeError: If d is not a dictionary
        ValueError: If there are conflicting keys (key is both a leaf value and a nested dict)

    Examples:
        >>> unflatten_dict({'a::b': 1, 'a::c': 2})
        {'a': {'b': 1, 'c': 2}}

        >>> unflatten_dict({'x::y::z': 3})
        {'x': {'y': {'z': 3}}}

        >>> unflatten_dict({'a_b': 1, 'a_c': 2}, delimiter='_')
        {'a': {'b': 1, 'c': 2}}
    """
    if not isinstance(d, dict):
        raise TypeError(f"unflatten_dict expects dict, got {type(d).__name__}")

    result: dict[str, Any] = {}
    for key, value in d.items():
        parts = key.split(delimiter)
        current = result
        for i, part in enumerate(parts[:-1]):
            if part not in current:
                current[part] = {}
            elif not isinstance(current[part], dict):
                # Conflict: trying to traverse into a leaf value
                conflicting_key = delimiter.join(parts[:i + 1])
                raise ValueError(
                    f"Key conflict in unflatten_dict: '{conflicting_key}' is both "
                    f"a leaf value and a nested dictionary"
                )
            current = current[part]

        # Check final key conflict
        if parts[-1] in current and isinstance(current[parts[-1]], dict):
            raise ValueError(
                f"Key conflict in unflatten_dict: '{key}' would overwrite "
                f"existing nested dictionary"
            )

        current[parts[-1]] = value
    return result


def deep_merge(
    base: dict[str, Any],
    updates: dict[str, Any],
    _depth: int = 0,
    max_depth: int = 100
) -> dict[str, Any]:
    """
    Deep merge two dictionaries, with updates overriding base values.

    Args:
        base: The base dictionary
        updates: Dictionary with values to merge/override
        _depth: Internal recursion depth counter (do not set manually)
        max_depth: Maximum allowed nesting depth (default 100)

    Returns:
        A new dictionary with merged values

    Raises:
        TypeError: If base or updates is not a dictionary
        ValueError: If nesting depth exceeds max_depth

    Examples:
        >>> deep_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}

        >>> deep_merge({'a': {'b': 1}}, {'a': {'c': 2}})
        {'a': {'b': 1, 'c': 2}}
    """
    if not isinstance(base, dict):
        raise TypeError(f"deep_merge base expects dict, got {type(base).__name__}")
    if not isinstance(updates, dict):
        raise TypeError(f"deep_merge updates expects dict, got {type(updates).__name__}")

    if _depth > max_depth:
        raise ValueError(
            f"Dictionary nesting depth exceeds maximum allowed depth of {max_depth}. "
            f"This may indicate a circular reference or malformed configuration."
        )

    result = base.copy()
    for key, value in updates.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value, _depth + 1, max_depth)
        else:
            result[key] = value
    return result


def remove_empty_values(
    d: dict[str, Any],
    _depth: int = 0,
    max_depth: int = 100
) -> dict[str, Any]:
    """
    Recursively remove empty string values from a nested dictionary.

    Args:
        d: The dictionary to clean
        _depth: Internal recursion depth counter (do not set manually)
        max_depth: Maximum allowed nesting depth (default 100)

    Returns:
        A new dictionary with empty strings removed

    Raises:
        TypeError: If d is not a dictionary
        ValueError: If nesting depth exceeds max_depth

    Examples:
        >>> remove_empty_values({'a': '', 'b': 'value'})
        {'b': 'value'}

        >>> remove_empty_values({'a': {'b': '', 'c': 1}})
        {'a': {'c': 1}}

    Note:
        Only removes empty strings (""), not other falsy values like None, 0, False, []
    """
    if not isinstance(d, dict):
        raise TypeError(f"remove_empty_values expects dict, got {type(d).__name__}")

    if _depth > max_depth:
        raise ValueError(
            f"Dictionary nesting depth exceeds maximum allowed depth of {max_depth}. "
            f"This may indicate a circular reference or malformed configuration."
        )

    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            nested = remove_empty_values(value, _depth + 1, max_depth)
            if nested:  # Only add if nested dict is not empty after cleaning
                result[key] = nested
        elif value != "":
            result[key] = value
    return result
