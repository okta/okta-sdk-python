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

from okta.models.application_credentials\
    import ApplicationCredentials
import okta.models.password_credential\
    as password_credential
import okta.models.application_credentials_scheme\
    as application_credentials_scheme
import okta.models.application_credentials_signing\
    as application_credentials_signing


class SchemeApplicationCredentials(
    ApplicationCredentials
):
    """
    A class for SchemeApplicationCredentials objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "password" in config:
                if isinstance(config["password"],
                              password_credential.PasswordCredential):
                    self.password = config["password"]
                else:
                    self.password = password_credential.PasswordCredential(
                        config["password"]
                    )
            else:
                self.password = None
            self.reveal_password = config["revealPassword"]\
                if "revealPassword" in config else None
            if "scheme" in config:
                if isinstance(config["scheme"],
                              application_credentials_scheme.ApplicationCredentialsScheme):
                    self.scheme = config["scheme"]
                else:
                    self.scheme = application_credentials_scheme.ApplicationCredentialsScheme(
                        config["scheme"].upper()
                    )
            else:
                self.scheme = None
            if "signing" in config:
                if isinstance(config["signing"],
                              application_credentials_signing.ApplicationCredentialsSigning):
                    self.signing = config["signing"]
                else:
                    self.signing = application_credentials_signing.ApplicationCredentialsSigning(
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

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "password": self.password,
            "revealPassword": self.reveal_password,
            "scheme": self.scheme,
            "signing": self.signing,
            "userName": self.user_name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
