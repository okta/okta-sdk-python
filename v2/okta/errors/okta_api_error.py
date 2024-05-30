from okta.errors.error import Error


class OktaAPIError(Error):
    def __init__(self, url, response_details, response_body):
        self.status = response_details.status
        self.error_code = response_body["errorCode"]
        self.error_summary = response_body.get("errorSummary", "")
        self.error_causes = response_body.get("errorCauses", [])
        error_causes_string = ". ".join(list(map(lambda x:
                                                 x.get("errorSummary", ""),
                                                 self.error_causes)))
        self.error_link = response_body["errorLink"]
        self.error_id = response_body["errorId"]

        self.url = url
        self.headers = response_details.headers
        self.stack = ""

        self.message = (f"Okta HTTP {self.status} {self.error_code} "
                        f"{self.error_summary}\n{error_causes_string}")
