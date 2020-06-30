"""
Class of utility functions.
"""


def format_url(self, base_string):
    return ''.join(
        [line.strip() for line in base_string.splitlines()]
    )
