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
from okta.models.protocol_algorithms\
    import ProtocolAlgorithms
from okta.models.identity_provider_credentials\
    import IdentityProviderCredentials
from okta.models.protocol_endpoints\
    import ProtocolEndpoints
from okta.models.protocol_endpoint\
    import ProtocolEndpoint
from okta.models.protocol_relay_state\
    import ProtocolRelayState
from okta.models.protocol_settings\
    import ProtocolSettings


class Protocol(
    OktaObject
):
    """
    A class for Protocol objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "algorithms" in config:
                if isinstance(config["algorithms"],
                              ProtocolAlgorithms):
                    self.algorithms = config["algorithms"]
                else:
                    self.algorithms = ProtocolAlgorithms(
                        config["algorithms"]
                    )
            else:
                self.algorithms = None
            if "credentials" in config:
                if isinstance(config["credentials"],
                              IdentityProviderCredentials):
                    self.credentials = config["credentials"]
                else:
                    self.credentials = IdentityProviderCredentials(
                        config["credentials"]
                    )
            else:
                self.credentials = None
            if "endpoints" in config:
                if isinstance(config["endpoints"],
                              ProtocolEndpoints):
                    self.endpoints = config["endpoints"]
                else:
                    self.endpoints = ProtocolEndpoints(
                        config["endpoints"]
                    )
            else:
                self.endpoints = None
            if "issuer" in config:
                if isinstance(config["issuer"],
                              ProtocolEndpoint):
                    self.issuer = config["issuer"]
                else:
                    self.issuer = ProtocolEndpoint(
                        config["issuer"]
                    )
            else:
                self.issuer = None
            if "relayState" in config:
                if isinstance(config["relayState"],
                              ProtocolRelayState):
                    self.relay_state = config["relayState"]
                else:
                    self.relay_state = ProtocolRelayState(
                        config["relayState"]
                    )
            else:
                self.relay_state = None
            self.scopes = config["scopes"]\
                if "scopes" in config else None
            if "settings" in config:
                if isinstance(config["settings"],
                              ProtocolSettings):
                    self.settings = config["settings"]
                else:
                    self.settings = ProtocolSettings(
                        config["settings"]
                    )
            else:
                self.settings = None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.algorithms = None
            self.credentials = None
            self.endpoints = None
            self.issuer = None
            self.relay_state = None
            self.scopes = None
            self.settings = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "algorithms": self.algorithms,
            "credentials": self.credentials,
            "endpoints": self.endpoints,
            "issuer": self.issuer,
            "relayState": self.relay_state,
            "scopes": self.scopes,
            "settings": self.settings,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
