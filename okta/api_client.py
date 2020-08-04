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
        # Camel case keys to match Lodash camel case
        for original_key in body.keys():
            body[camel_case(original_key)] = body.pop(original_key)

        return body
