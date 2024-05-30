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
from okta.models import identity_provider_credentials_client\
    as identity_provider_credentials_client
from okta.models import identity_provider_credentials_signing\
    as identity_provider_credentials_signing
from okta.models import identity_provider_credentials_trust\
    as identity_provider_credentials_trust


class IdentityProviderCredentials(
    OktaObject
):
    """
    A class for IdentityProviderCredentials objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "client" in config:
                if isinstance(config["client"],
                              identity_provider_credentials_client.IdentityProviderCredentialsClient):
                    self.client = config["client"]
                elif config["client"] is not None:
                    self.client = identity_provider_credentials_client.IdentityProviderCredentialsClient(
                        config["client"]
                    )
                else:
                    self.client = None
            else:
                self.client = None
            if "signing" in config:
                if isinstance(config["signing"],
                              identity_provider_credentials_signing.IdentityProviderCredentialsSigning):
                    self.signing = config["signing"]
                elif config["signing"] is not None:
                    self.signing = identity_provider_credentials_signing.IdentityProviderCredentialsSigning(
                        config["signing"]
                    )
                else:
                    self.signing = None
            else:
                self.signing = None
            if "trust" in config:
                if isinstance(config["trust"],
                              identity_provider_credentials_trust.IdentityProviderCredentialsTrust):
                    self.trust = config["trust"]
                elif config["trust"] is not None:
                    self.trust = identity_provider_credentials_trust.IdentityProviderCredentialsTrust(
                        config["trust"]
                    )
                else:
                    self.trust = None
            else:
                self.trust = None
        else:
            self.client = None
            self.signing = None
            self.trust = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "client": self.client,
            "signing": self.signing,
            "trust": self.trust
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
