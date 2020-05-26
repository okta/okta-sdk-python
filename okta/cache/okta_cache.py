from okta.cache.cache import Cache
from threading import Timer


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
        # allow 0.01 for methods to work for more consistent results
        # https://stackoverflow.com/a/39582288
        self._time_to_live = ttl - 0.01
        self._time_to_idle = tti - 0.01

    def get(self, key):
        """
        Retrieves value from cache using key

        Arguments:
            key {str} -- Desired key

        Returns:
            str -- Corresponding value to given key
            None -- Unable to find value for this key
        """
        # Check if key is in cache
        if self.contains(key):
            # Create unique key and search for entry
            entry_key = self.create_key(key)
            entry = self._store[entry_key]

            # Cancel and restart TTI timer
            entry['tti'].cancel()
            new_idle_timer = self._create_delete_timer(entry_key, idle=True)
            entry['tti'] = new_idle_timer
            new_idle_timer.start()

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
        return self.create_key(key) in self._store

    def add(self, key, value):
        """
        Adds a key-value pair to the cache.

        Arguments:
            key {str} -- Key in pair
            value {str} -- Value in pair
        """
        # Generate unique identifier
        entry_key = self.create_key(key)

        # Create timers for TTI and TTL
        idle_timer = self._create_delete_timer(entry_key, idle=True)
        life_timer = self._create_delete_timer(entry_key, idle=False)

        # Add new entry to cache with timers
        self._store[entry_key] = {
            'value': value,
            'tti': idle_timer,
            'ttl': life_timer
        }

        # Start timers!
        idle_timer.start()
        life_timer.start()

    def delete(self, key):
        """
        Delete a key-value pair from the cache.

        Arguments:
            key {str} -- Desired key
        """
        # Make sure key is in cache
        if self.contains(key):
            # Get unique key for key given and cancel timers in entry
            entry_key = self.create_key(key)
            self._store[entry_key]['tti'].cancel()
            self._store[entry_key]['ttl'].cancel()

            # Delete entry
            del self._store[entry_key]

    def clear(self):
        """
        Clear the cache.
        """
        self._store.clear()

    def _create_delete_timer(self, key, idle=False):
        """
        Helper function to create Timers for key-value pairs

        Arguments:
            key {str} -- Key identifying entry

        Keyword Arguments:
            idle {bool} -- If timer is for TTI (default) or TTL
            (default: {False})

        Returns:
            threading.Timer -- Timer object with contains the callback to
            delete the key-value pair if finished
        """
        if idle is True:
            return Timer(self._time_to_idle, self.delete, [key], {})
        else:
            return Timer(self._time_to_live, self.delete, [key], {})
