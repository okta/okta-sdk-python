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
from okta.models import application_credentials_signing\
    as application_credentials_signing
from okta.models import application_credentials_username_template\
    as application_credentials_username_template


class ApplicationCredentials(
    OktaObject
):
    """
    A class for ApplicationCredentials objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "signing" in config:
                if isinstance(config["signing"],
                              application_credentials_signing.ApplicationCredentialsSigning):
                    self.signing = config["signing"]
                elif config["signing"] is not None:
                    self.signing = application_credentials_signing.ApplicationCredentialsSigning(
                        config["signing"]
                    )
                else:
                    self.signing = None
            else:
                self.signing = None
            if "userNameTemplate" in config:
                if isinstance(config["userNameTemplate"],
                              application_credentials_username_template.ApplicationCredentialsUsernameTemplate):
                    self.user_name_template = config["userNameTemplate"]
                elif config["userNameTemplate"] is not None:
                    self.user_name_template = application_credentials_username_template.ApplicationCredentialsUsernameTemplate(
                        config["userNameTemplate"]
                    )
                else:
                    self.user_name_template = None
            else:
                self.user_name_template = None
        else:
            self.signing = None
            self.user_name_template = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "signing": self.signing,
            "userNameTemplate": self.user_name_template
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
