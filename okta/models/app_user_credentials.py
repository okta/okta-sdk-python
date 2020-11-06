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
from okta.models import app_user_password_credential\
    as app_user_password_credential


class AppUserCredentials(
    OktaObject
):
    """
    A class for AppUserCredentials objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "password" in config:
                if isinstance(config["password"],
                              app_user_password_credential.AppUserPasswordCredential):
                    self.password = config["password"]
                elif config["password"] is not None:
                    self.password = app_user_password_credential.AppUserPasswordCredential(
                        config["password"]
                    )
                else:
                    self.password = None
            else:
                self.password = None
            self.user_name = config["userName"]\
                if "userName" in config else None
        else:
            self.password = None
            self.user_name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "password": self.password,
            "userName": self.user_name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
