import requests


class Http(object):
    """
    Okta's HTTP client.
    """
    def __init__(self, headers):
        self.headers = headers

    def get(self, uri, data=None):
        """
        Okta HTTP client for making GET requests.
        """
        headers = self.headers
        if data:
            headers['Content-Type'] = 'application/json'
            headers['Accept'] = 'application/json'
        return requests.get(uri, headers=headers, data=data)

    def post(self, uri, data=None):
        """
        Okta HTTP client for making POST requests.
        """
        headers = self.headers
        if data:
            headers['Content-Type'] = 'application/json'
            headers['Accept'] = 'application/json'
        return requests.post(uri, headers=headers, data=data)

    def put(self, uri, data=None):
        """
        Okta HTTP client for making PUT requests.
        """
        headers = self.headers
        if data:
            headers['Content-Type'] = 'application/json'
            headers['Accept'] = 'application/json'
        return requests.put(uri, headers=headers, data=data)

    def delete(self, uri):
        """
        Okta HTTP client for making DELETE requests.
        """
        return requests.delete(uri, headers=self.headers)
