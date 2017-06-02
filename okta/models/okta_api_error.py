class OktaApiError(Exception):
    """
    Custom Okta Error for interactions with the Okta API.
    """
    def __init__(self, error):
        if error is None:
            error = {}

        Exception.__init__(self, error.get('errorSummary'))

        self.error_causes = error.get('errorCauses')
        self.error_code = error.get('errorCode')
        self.error_id = error.get('errorId')
        self.error_link = error.get('errorLink')
        self.error_summary = error.get('errorSummary')
