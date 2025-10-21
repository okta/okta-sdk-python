# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import random
import string

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
