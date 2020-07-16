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
from okta.models.identity_provider_credentials_client\
    import IdentityProviderCredentialsClient
from okta.models.identity_provider_credentials_signing\
    import IdentityProviderCredentialsSigning
from okta.models.identity_provider_credentials_trust\
    import IdentityProviderCredentialsTrust


class IdentityProviderCredentials(
    OktaObject
):
    """
    A class for IdentityProviderCredentials objects.
    """

    def __init__(self, config=None):
        if config:
            if "client" in config:
                if isinstance(config["client"],
                              IdentityProviderCredentialsClient):
                    self.client = config["client"]
                else:
                    self.client = IdentityProviderCredentialsClient(
                        config["client"]
                    )
            else:
                self.client = None
            if "signing" in config:
                if isinstance(config["signing"],
                              IdentityProviderCredentialsSigning):
                    self.signing = config["signing"]
                else:
                    self.signing = IdentityProviderCredentialsSigning(
                        config["signing"]
                    )
            else:
                self.signing = None
            if "trust" in config:
                if isinstance(config["trust"],
                              IdentityProviderCredentialsTrust):
                    self.trust = config["trust"]
                else:
                    self.trust = IdentityProviderCredentialsTrust(
                        config["trust"]
                    )
            else:
                self.trust = None
        else:
            self.client = None
            self.signing = None
            self.trust = None
