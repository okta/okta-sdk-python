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
from okta.models.protocol_endpoint\
    import ProtocolEndpoint


class ProtocolEndpoints(
    OktaObject
):
    """
    A class for ProtocolEndpoints objects.
    """

    def __init__(self, config=None):
        if config:
            if "acs" in config:
                if isinstance(config["acs"],
                              ProtocolEndpoint):
                    self.acs = config["acs"]
                else:
                    self.acs = ProtocolEndpoint(
                        config["acs"]
                    )
            else:
                self.acs = None
            if "authorization" in config:
                if isinstance(config["authorization"],
                              ProtocolEndpoint):
                    self.authorization = config["authorization"]
                else:
                    self.authorization = ProtocolEndpoint(
                        config["authorization"]
                    )
            else:
                self.authorization = None
            if "jwks" in config:
                if isinstance(config["jwks"],
                              ProtocolEndpoint):
                    self.jwks = config["jwks"]
                else:
                    self.jwks = ProtocolEndpoint(
                        config["jwks"]
                    )
            else:
                self.jwks = None
            if "metadata" in config:
                if isinstance(config["metadata"],
                              ProtocolEndpoint):
                    self.metadata = config["metadata"]
                else:
                    self.metadata = ProtocolEndpoint(
                        config["metadata"]
                    )
            else:
                self.metadata = None
            if "slo" in config:
                if isinstance(config["slo"],
                              ProtocolEndpoint):
                    self.slo = config["slo"]
                else:
                    self.slo = ProtocolEndpoint(
                        config["slo"]
                    )
            else:
                self.slo = None
            if "sso" in config:
                if isinstance(config["sso"],
                              ProtocolEndpoint):
                    self.sso = config["sso"]
                else:
                    self.sso = ProtocolEndpoint(
                        config["sso"]
                    )
            else:
                self.sso = None
            if "token" in config:
                if isinstance(config["token"],
                              ProtocolEndpoint):
                    self.token = config["token"]
                else:
                    self.token = ProtocolEndpoint(
                        config["token"]
                    )
            else:
                self.token = None
            if "userInfo" in config:
                if isinstance(config["userInfo"],
                              ProtocolEndpoint):
                    self.user_info = config["userInfo"]
                else:
                    self.user_info = ProtocolEndpoint(
                        config["userInfo"]
                    )
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
