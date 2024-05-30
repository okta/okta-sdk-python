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
from okta.models import protocol_endpoint\
    as protocol_endpoint


class ProtocolEndpoints(
    OktaObject
):
    """
    A class for ProtocolEndpoints objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "acs" in config:
                if isinstance(config["acs"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.acs = config["acs"]
                elif config["acs"] is not None:
                    self.acs = protocol_endpoint.ProtocolEndpoint(
                        config["acs"]
                    )
                else:
                    self.acs = None
            else:
                self.acs = None
            if "authorization" in config:
                if isinstance(config["authorization"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.authorization = config["authorization"]
                elif config["authorization"] is not None:
                    self.authorization = protocol_endpoint.ProtocolEndpoint(
                        config["authorization"]
                    )
                else:
                    self.authorization = None
            else:
                self.authorization = None
            if "jwks" in config:
                if isinstance(config["jwks"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.jwks = config["jwks"]
                elif config["jwks"] is not None:
                    self.jwks = protocol_endpoint.ProtocolEndpoint(
                        config["jwks"]
                    )
                else:
                    self.jwks = None
            else:
                self.jwks = None
            if "metadata" in config:
                if isinstance(config["metadata"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.metadata = config["metadata"]
                elif config["metadata"] is not None:
                    self.metadata = protocol_endpoint.ProtocolEndpoint(
                        config["metadata"]
                    )
                else:
                    self.metadata = None
            else:
                self.metadata = None
            if "slo" in config:
                if isinstance(config["slo"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.slo = config["slo"]
                elif config["slo"] is not None:
                    self.slo = protocol_endpoint.ProtocolEndpoint(
                        config["slo"]
                    )
                else:
                    self.slo = None
            else:
                self.slo = None
            if "sso" in config:
                if isinstance(config["sso"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.sso = config["sso"]
                elif config["sso"] is not None:
                    self.sso = protocol_endpoint.ProtocolEndpoint(
                        config["sso"]
                    )
                else:
                    self.sso = None
            else:
                self.sso = None
            if "token" in config:
                if isinstance(config["token"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.token = config["token"]
                elif config["token"] is not None:
                    self.token = protocol_endpoint.ProtocolEndpoint(
                        config["token"]
                    )
                else:
                    self.token = None
            else:
                self.token = None
            if "userInfo" in config:
                if isinstance(config["userInfo"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.user_info = config["userInfo"]
                elif config["userInfo"] is not None:
                    self.user_info = protocol_endpoint.ProtocolEndpoint(
                        config["userInfo"]
                    )
                else:
                    self.user_info = None
            else:
                self.user_info = None
        else:
            self.acs = None
            self.authorization = None
            self.jwks = None
            self.metadata = None
            self.slo = None
            self.sso = None
            self.token = None
            self.user_info = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "acs": self.acs,
            "authorization": self.authorization,
            "jwks": self.jwks,
            "metadata": self.metadata,
            "slo": self.slo,
            "sso": self.sso,
            "token": self.token,
            "userInfo": self.user_info
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
