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
from okta.okta_collection import OktaCollection


class SocialAuthToken(
    OktaObject
):
    """
    A class for SocialAuthToken objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.scopes = OktaCollection.form_list(
                config["scopes"] if "scopes"\
                    in config else [],
                str
            )
            self.token = config["token"]\
                if "token" in config else None
            self.token_auth_scheme = config["tokenAuthScheme"]\
                if "tokenAuthScheme" in config else None
            self.token_type = config["tokenType"]\
                if "tokenType" in config else None
        else:
            self.expires_at = None
            self.id = None
            self.scopes = []
            self.token = None
            self.token_auth_scheme = None
            self.token_type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expiresAt": self.expires_at,
            "id": self.id,
            "scopes": self.scopes,
            "token": self.token,
            "tokenAuthScheme": self.token_auth_scheme,
            "tokenType": self.token_type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
