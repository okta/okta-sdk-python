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
from okta.models import identity_provider_policy\
    as identity_provider_policy
from okta.models import protocol\
    as protocol


class IdentityProvider(
    OktaObject
):
    """
    A class for IdentityProvider objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.issuer_mode = config["issuerMode"]\
                if "issuerMode" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "policy" in config:
                if isinstance(config["policy"],
                              identity_provider_policy.IdentityProviderPolicy):
                    self.policy = config["policy"]
                elif config["policy"] is not None:
                    self.policy = identity_provider_policy.IdentityProviderPolicy(
                        config["policy"]
                    )
                else:
                    self.policy = None
            else:
                self.policy = None
            if "protocol" in config:
                if isinstance(config["protocol"],
                              protocol.Protocol):
                    self.protocol = config["protocol"]
                elif config["protocol"] is not None:
                    self.protocol = protocol.Protocol(
                        config["protocol"]
                    )
                else:
                    self.protocol = None
            else:
                self.protocol = None
            self.status = config["status"]\
                if "status" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.links = None
            self.created = None
            self.id = None
            self.issuer_mode = None
            self.last_updated = None
            self.name = None
            self.policy = None
            self.protocol = None
            self.status = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "created": self.created,
            "id": self.id,
            "issuerMode": self.issuer_mode,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "policy": self.policy,
            "protocol": self.protocol,
            "status": self.status,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
