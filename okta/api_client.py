from pydash.strings import camel_case


class APIClient():
    """
    A base class for the Okta API Clients.
    """

    def __init__(self):
        pass

    @staticmethod
    def form_response_body(body: dict):
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
            if key == "profile":  # don't change keys in profile dict
                result[key] = APIClient.form_response_body(val)
            elif not isinstance(val, dict):
                result[key] = val
            else:
                result[key] = APIClient.form_response_body(val)
        return result

    @staticmethod
    def form_response_body_without_changing_keys(body: dict):
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
                result[key] = val
            else:
                result[key] = APIClient.form_response_body_without_changing_keys(val)
        return result
