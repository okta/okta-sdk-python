# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import logging
import time

from okta.cache.cache import Cache
from okta.constants import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class OktaCache(Cache):
    """
    This is a base class implementing a Cache using TTL and TTI.
    Implementing the okta.cache.cache.Cache abstract class.

    THREAD SAFETY WARNING:
    ---------------------
    This cache implementation is NOT thread-safe and should only be used in
    single-threaded or single-coroutine contexts. In concurrent environments
    (e.g., asyncio with multiple coroutines accessing the same cache instance),
    race conditions may occur during cache operations.

    For multi-threaded applications, consider:
    1. Using threading.local() to create per-thread cache instances
    2. Implementing a thread-safe cache wrapper with locks
    3. Using an external cache (Redis, Memcached) for distributed scenarios

    The default SDK usage pattern (one client instance per thread/coroutine)
    is safe. Issues only arise when sharing a single client across multiple
    concurrent execution contexts.
    """

    def __init__(self, ttl, tti):
        """
        Constructor.

        Arguments:
            ttl {float} -- Time to Live: for cache entries
            tti {float} -- Time to Idle: for cache entries
        """
        super().__init__()  # Inherit from parent class
        self._store = {}  # key -> {value, TTI, TTL}
        self._time_to_live = ttl
        self._time_to_idle = tti

    def get(self, key):
        """
        Retrieves value from cache using key

        Arguments:
            key {str} -- Desired key

        Returns:
            str -- Corresponding value to given key
            None -- Unable to find value for this key
        """
        # Get current time
        now = self._get_current_time()
        # Check if key is in cache and valid
        if self.contains(key):
            entry = self._store[key]
            # Reset TTI
            entry["tti"] = now + self._time_to_idle
            # Return desired value and update cache
            self._clean_cache()
            logger.info('Got value from cache for key "%s".', key)
            return entry["value"]

        # Return None if key isn't in cache and update cache
        self._clean_cache()
        return None

    def contains(self, key):
        """
        Returns existence of key in cache, as boolean

        Arguments:
            key {str} -- Desired key

        Returns:
            bool -- Existence of key in cache
        """
        return key in self._store and self._is_valid_entry(self._store[key])

    def add(self, key: str, value):
        """
        Adds a key-value pair to the cache.

        Arguments:
            key {str} -- Key in pair
            value -- Value to cache (e.g., tuple of response and body,
                     or tuple of access_token and token_type)
        """
        if isinstance(key, str) and (
            not isinstance(value, list) or not isinstance(value[1], list)
        ):
            # Get current time
            now = self._get_current_time()

            # Add new entry to cache with timers
            self._store[key] = {
                "value": value,
                "tti": now + self._time_to_idle,
                "ttl": now + self._time_to_live,
            }
            logger.info('Added to cache value for key "%s".', key)
        # Update cache
        self._clean_cache()

    def delete(self, key):
        """
        Delete a key-value pair from the cache.

        Arguments:
            key {str} -- Desired key
        """
        # Make sure key is in cache
        if key in self._store:
            # Delete entry
            del self._store[key]
            logger.info('Removed value from cache for key "%s".', key)

    def clear(self):
        """
        Clear the cache.
        """
        self._store.clear()
        logger.info("Cleared the cache.")

    def _clean_cache(self):
        """
        Updates cache by removing expired entries at time of call
        """
        expired = []
        # Check every entry
        for key in self._store.keys():
            # If not valid, delete
            if not self._is_valid_entry(self._store[key]):
                expired.append(key)
        # Delete keys
        for expired_key in expired:
            self.delete(expired_key)

    def _is_valid_entry(self, entry):
        """
        Determines if a given cache entry is not expired.

        Args:
            entry (dict): An entry from the cache composed of value,
            TTI, and TTL

        Returns:
            bool: Boolean value representing if entry is expired
        """
        # Get Current time
        now = self._get_current_time()
        # Check timers and compare against current time
        timers = [entry["tti"], entry["ttl"]]
        return not any(timer <= now for timer in timers)

    def _get_current_time(self):
        """
        Helper function to get current time

        Returns:
            float: value representing the number of seconds since the epoch
        """
        return time.time()
