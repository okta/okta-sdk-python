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
from okta.models import password_credential\
    as password_credential


class ChangePasswordRequest(
    OktaObject
):
    """
    A class for ChangePasswordRequest objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "newPassword" in config:
                if isinstance(config["newPassword"],
                              password_credential.PasswordCredential):
                    self.new_password = config["newPassword"]
                elif config["newPassword"] is not None:
                    self.new_password = password_credential.PasswordCredential(
                        config["newPassword"]
                    )
                else:
                    self.new_password = None
            else:
                self.new_password = None
            if "oldPassword" in config:
                if isinstance(config["oldPassword"],
                              password_credential.PasswordCredential):
                    self.old_password = config["oldPassword"]
                elif config["oldPassword"] is not None:
                    self.old_password = password_credential.PasswordCredential(
                        config["oldPassword"]
                    )
                else:
                    self.old_password = None
            else:
                self.old_password = None
        else:
            self.new_password = None
            self.old_password = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "newPassword": self.new_password,
            "oldPassword": self.old_password
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
