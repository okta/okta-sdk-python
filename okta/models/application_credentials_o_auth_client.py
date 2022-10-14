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
from okta.models import o_auth_endpoint_authentication_method\
    as o_auth_endpoint_authentication_method


class ApplicationCredentialsOAuthClient(
    OktaObject
):
    """
    A class for ApplicationCredentialsOAuthClient objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.auto_key_rotation = config["autoKeyRotation"]\
                if "autoKeyRotation" in config else None
            self.client_id = config["clientId"]\
                if "clientId" in config else None
            self.client_secret = config["clientSecret"]\
                if "clientSecret" in config else None
            if "tokenEndpointAuthMethod" in config:
                if isinstance(config["tokenEndpointAuthMethod"],
                              o_auth_endpoint_authentication_method.OAuthEndpointAuthenticationMethod):
                    self.token_endpoint_auth_method = config["tokenEndpointAuthMethod"]
                elif config["tokenEndpointAuthMethod"] is not None:
                    self.token_endpoint_auth_method = o_auth_endpoint_authentication_method.OAuthEndpointAuthenticationMethod(
                        config["tokenEndpointAuthMethod"].upper()
                    )
                else:
                    self.token_endpoint_auth_method = None
            else:
                self.token_endpoint_auth_method = None
        else:
            self.auto_key_rotation = None
            self.client_id = None
            self.client_secret = None
            self.token_endpoint_auth_method = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "autoKeyRotation": self.auto_key_rotation,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "token_endpoint_auth_method": self.token_endpoint_auth_method
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
