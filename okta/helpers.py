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
        >>> to_snake_case('camel2snake')
        'camel_2_snake'
    """
    # Simulate the same behavior as "lodash" library
    string = re.sub("([A-Za-z]+)([0-9]+)", "\g<1>_\g<2>", string)
    string = re.sub("([0-9])([A-Za-z]+)", "\g<1>_\g<2>", string)
    string = re.sub("([A-Z]+)([A-Z][a-z])", "\g<1>_\g<2>", string)
    string = re.sub("([a-z])([A-Z])", "\g<1>_\g<2>", string);
    return string.lower()


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
