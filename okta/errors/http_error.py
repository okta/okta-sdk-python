from okta.errors.error import Error


class HTTPError(Error):
    def __init__(self, url, response_details, response_body):
        self.status = response_details.status
        self.url = url
        self.response_headers = response_details.headers
        self.stack = ""
        self.message = f"HTTP {self.status} {response_body}"
