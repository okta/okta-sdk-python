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
from okta.models.application_credentials_signing\
    import ApplicationCredentialsSigning
from okta.models.application_credentials_username_template\
    import ApplicationCredentialsUsernameTemplate


class ApplicationCredentials(
    OktaObject
):
    """
    A class for ApplicationCredentials objects.
    """

    def __init__(self, config=None):
        if config:
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
            if "userNameTemplate" in config:
                if isinstance(config["userNameTemplate"],
                              ApplicationCredentialsUsernameTemplate):
                    self.user_name_template = config["userNameTemplate"]
                else:
                    self.user_name_template = ApplicationCredentialsUsernameTemplate(
                        config["userNameTemplate"]
                    )
            else:
                self.user_name_template = None
        else:
            self.signing = None
            self.user_name_template = None
