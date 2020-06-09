from okta.cache.cache import Cache
import time


class OktaCache(Cache):
    """
    This is a base class implementing a Cache using TTL and TTI.
    Implementing the okta.cache.cache.Cache abstract class.
    """

    def __init__(self, ttl, tti):
        """
        Constructor.

        Arguments:
            ttl {float} -- Time to Live: for cache entries
            tti {float} -- Time to Idle: for cache entries
        """
        super()  # Inherit from parent class
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
        self._clean_cache()
        now = self.get_current_time()
        # Check if key is in cache
        if self.contains(key):
            entry = self._store[key]
            print("GET", entry)
            entry["tti"] = now + self._time_to_idle
            # Return desired value
            return entry["value"]
        # Return None if key isn't in cache
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

    def add(self, key: str, value: str):
        """
        Adds a key-value pair to the cache.

        Arguments:
            key {str} -- Key in pair
            value {str} -- Value in pair
        """
        if type(key) == str and type(value) != list:
            # Create timers for TTI and TTL
            now = self.get_current_time()

            # Add new entry to cache with timers
            self._store[key] = {
                'value': value,
                'tti': now + self._time_to_idle,
                'ttl': now + self._time_to_live
            }
            print("ADD", self._store[key])
        self._clean_cache()

    def delete(self, key):
        """
        Delete a key-value pair from the cache.

        Arguments:
            key {str} -- Desired key
        """
        # Make sure key is in cache
        if self.contains(key):
            # Delete entry
            del self._store[key]

    def clear(self):
        """
        Clear the cache.
        """
        self._store.clear()

    def _clean_cache(self):
        for key in self._store.keys():
            if not self._is_valid_entry(self._store[key]):
                self.delete(key)

    def _is_valid_entry(self, entry):
        now = self.get_current_time()
        timers = [entry["tti"], entry["ttl"]]
        return not any(timer <= now for timer in timers)

    def get_current_time(self):
        return time.time()
