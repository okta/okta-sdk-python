from urllib.parse import urlparse


class Cache():
    """
    This is the ABSTRACT class that defines a Cache object for the Okta Client
    """

    def __init__(self):
        pass

    def get(self, key):
        """
        A method which retrieves the desired value from the cache.

        Arguments:
            key {str} -- The key used to find the desired value

        Raises:
            NotImplementedError: If the subclass inheriting this class
            has not implemented this function
        """
        raise NotImplementedError

    def contains(self, key):
        """
        A method which checks if the cache contains the desired value.

        Arguments:
            key {str} -- The key used to check the desired value

        Raises:
            NotImplementedError: If the subclass inheriting this class
            has not implemented this function
        """
        raise NotImplementedError

    def add(self, key, value):
        """
        A method which adds a key-value pair to the cache.

        Arguments:
            key {str} -- The key used to identify the entry.
            value {[type]} -- The value in the pair

        Raises:
            NotImplementedError: If the subclass inheriting this class
            has not implemented this function
        """
        raise NotImplementedError

    def delete(self, key):
        """
        A method which deletes a key-value pair from the cache.

        Arguments:
            key {str} -- The key used to identify the entry

        Raises:
            NotImplementedError: If the subclass inheriting this class
            has not implemented this function
        """
        raise NotImplementedError

    def clear(self):
        """
        A method used to empty the cache.

        Raises:
            NotImplementedError: If the subclass inheriting this class
            has not implemented this function
        """
        raise NotImplementedError

    def create_key(self, request):
        """
        A method used to create a unique key for an entry in the cache.
        Used with URLs that requests fire at.

        Arguments:
            request {str} -- The key to use to produce a unique key

        Returns:
            str -- Unique key based on the input
        """
        # Validate URL and return URL string
        url_object = urlparse(request)
        return url_object.geturl()
