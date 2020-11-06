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
from okta.models import protocol_algorithms\
    as protocol_algorithms
from okta.models import identity_provider_credentials\
    as identity_provider_credentials
from okta.models import protocol_endpoints\
    as protocol_endpoints
from okta.models import protocol_endpoint\
    as protocol_endpoint
from okta.models import protocol_relay_state\
    as protocol_relay_state
from okta.models import protocol_settings\
    as protocol_settings


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
                              protocol_algorithms.ProtocolAlgorithms):
                    self.algorithms = config["algorithms"]
                elif config["algorithms"] is not None:
                    self.algorithms = protocol_algorithms.ProtocolAlgorithms(
                        config["algorithms"]
                    )
                else:
                    self.algorithms = None
            else:
                self.algorithms = None
            if "credentials" in config:
                if isinstance(config["credentials"],
                              identity_provider_credentials.IdentityProviderCredentials):
                    self.credentials = config["credentials"]
                elif config["credentials"] is not None:
                    self.credentials = identity_provider_credentials.IdentityProviderCredentials(
                        config["credentials"]
                    )
                else:
                    self.credentials = None
            else:
                self.credentials = None
            if "endpoints" in config:
                if isinstance(config["endpoints"],
                              protocol_endpoints.ProtocolEndpoints):
                    self.endpoints = config["endpoints"]
                elif config["endpoints"] is not None:
                    self.endpoints = protocol_endpoints.ProtocolEndpoints(
                        config["endpoints"]
                    )
                else:
                    self.endpoints = None
            else:
                self.endpoints = None
            if "issuer" in config:
                if isinstance(config["issuer"],
                              protocol_endpoint.ProtocolEndpoint):
                    self.issuer = config["issuer"]
                elif config["issuer"] is not None:
                    self.issuer = protocol_endpoint.ProtocolEndpoint(
                        config["issuer"]
                    )
                else:
                    self.issuer = None
            else:
                self.issuer = None
            if "relayState" in config:
                if isinstance(config["relayState"],
                              protocol_relay_state.ProtocolRelayState):
                    self.relay_state = config["relayState"]
                elif config["relayState"] is not None:
                    self.relay_state = protocol_relay_state.ProtocolRelayState(
                        config["relayState"]
                    )
                else:
                    self.relay_state = None
            else:
                self.relay_state = None
            self.scopes = OktaCollection.form_list(
                config["scopes"] if "scopes"\
                    in config else [],
                str
            )
            if "settings" in config:
                if isinstance(config["settings"],
                              protocol_settings.ProtocolSettings):
                    self.settings = config["settings"]
                elif config["settings"] is not None:
                    self.settings = protocol_settings.ProtocolSettings(
                        config["settings"]
                    )
                else:
                    self.settings = None
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
            self.scopes = []
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
