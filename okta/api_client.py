from pydash.strings import camel_case


class APIClient():
    """
    A base class for the Okta API Clients.
    """

    def __init__(self):
        pass

    def form_response_body(self, body: dict):
        """
        Method to verify the response body from the Okta API before
        passing it into the constructor.

        Args:
            body (dict): Okta API response body
        """
        result = {}
        for key, val in body.items():
            if val is None:
                continue
            if not isinstance(val, dict):
                result[camel_case(key)] = val
            else:
                result[camel_case(key)] = self.form_response_body(val)
        return result
