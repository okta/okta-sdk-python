import string
import random

"""
File for utility functions used in testing
"""


def random_string_of_length(length):
    """
    Generates a random string of ASCII letters of a fixed length.

    Args:
        length (int): fixed length desired

    Returns:
        string: random string generated
    """
    return "".join(random.choices(string.ascii_letters, k=length))
