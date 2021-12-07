"""
Module contains different helper functions.
Module is independent from any okta modules.
"""

import re


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
    if components[0]:
        components[0] = components[0][0].lower() + components[0][1:]
    # join other components with first capitalized first letter
    return components[0] + ''.join(x.title() for x in components[1:])
