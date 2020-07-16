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

from okta.models.application_credentials\
    import ApplicationCredentials
from okta.models.password_credential\
    import PasswordCredential
from okta.models.application_credentials_scheme\
    import ApplicationCredentialsScheme
from okta.models.application_credentials_signing\
    import ApplicationCredentialsSigning


class SchemeApplicationCredentials(
    ApplicationCredentials
):
    """
    A class for SchemeApplicationCredentials objects.
    """

    def __init__(self, config=None):
        if config:
            if "password" in config:
                if isinstance(config["password"],
                              PasswordCredential):
                    self.password = config["password"]
                else:
                    self.password = PasswordCredential(
                        config["password"]
                    )
            else:
                self.password = None
            self.reveal_password = config["revealPassword"]\
                if "revealPassword" in config else None
            if "scheme" in config:
                if isinstance(config["scheme"],
                              ApplicationCredentialsScheme):
                    self.scheme = config["scheme"]
                else:
                    self.scheme = ApplicationCredentialsScheme(
                        config["scheme"]
                    )
            else:
                self.scheme = None
            if "signing" in config:
                if isinstance(config["signing"],
                              ApplicationCredentialsSigning):
                    self.signing = config["signing"]
                else:
                    self.signing = ApplicationCredentialsSigning(
                        config["signing"]
                    )
            else:
                self.signing = None
            self.user_name = config["userName"]\
                if "userName" in config else None
        else:
            self.password = None
            self.reveal_password = None
            self.scheme = None
            self.signing = None
            self.user_name = None
