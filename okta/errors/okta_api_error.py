# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

from okta.errors.error import Error


class OktaAPIError(Error):
    def __init__(self, url, response_details, response_body):
        self.status = response_details.status
        self.error_code = response_body["errorCode"]
        self.error_summary = response_body.get("errorSummary", "")
        self.error_causes = response_body.get("errorCauses", [])
        error_causes_string = ". ".join(
            list(map(lambda x: x.get("errorSummary", ""), self.error_causes))
        )
        self.error_link = response_body["errorLink"]
        self.error_id = response_body["errorId"]

        self.url = url
        self.headers = response_details.headers
        self.stack = ""

        self.message = (
            f"Okta HTTP {self.status} {self.error_code} "
            f"{self.error_summary}\n{error_causes_string}"
        )
