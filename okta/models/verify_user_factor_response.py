# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class VerifyUserFactorResponse(
    OktaObject
):
    """
    A class for VerifyUserFactorResponse objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            if "_links" in config:
                self.links = config["_links"]
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.factor_result = config["factorResult"]\
                if "factorResult" in config else None
            self.factor_result_message = config["factorResultMessage"]\
                if "factorResultMessage" in config else None
        else:
            self.embedded = None
            self.links = None
            self.expires_at = None
            self.factor_result = None
            self.factor_result_message = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "expiresAt": self.expires_at,
            "factorResult": self.factor_result,
            "factorResultMessage": self.factor_result_message
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
