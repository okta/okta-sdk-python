# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

from okta.cache.cache import Cache


class NoOpCache(Cache):
    """
    This is a disabled Cache Class where no operations occur
    in the cache.
    Implementing the okta.cache.cache.Cache abstract class.
    """

    def __init__(self):
        super()

    def get(self, key):
        """
        Nothing is returned.

        Arguments:
            key {str} -- Key to look for

        Returns:
            None -- No op cache doesn't contain any data to return
        """
        return None

    def contains(self, key):
        """
        False is returned

        Arguments:
            key {str} -- Key to look for

        Returns:
            False -- No data to return so key can never be in cache
        """
        return False

    def add(self, key, value):
        """
        This is a void method

        Arguments:
            key {str} -- Key in pair
            value {str} -- Val in pair
        """
        pass

    def delete(self, key):
        """This is a void method. No need to delete anything not contained.

        Arguments:
            key {str} -- Key to delete
        """
        pass

    def clear(self):
        """
        This is a void method. No need to clear when nothing's stored.
        """
        pass
