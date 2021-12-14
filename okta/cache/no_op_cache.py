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
