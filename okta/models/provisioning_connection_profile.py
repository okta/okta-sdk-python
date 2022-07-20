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
from okta.models import provisioning_connection_auth_scheme\
    as provisioning_connection_auth_scheme


class ProvisioningConnectionProfile(
    OktaObject
):
    """
    A class for ProvisioningConnectionProfile objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "authScheme" in config:
                if isinstance(config["authScheme"],
                              provisioning_connection_auth_scheme.ProvisioningConnectionAuthScheme):
                    self.auth_scheme = config["authScheme"]
                elif config["authScheme"] is not None:
                    self.auth_scheme = provisioning_connection_auth_scheme.ProvisioningConnectionAuthScheme(
                        config["authScheme"].upper()
                    )
                else:
                    self.auth_scheme = None
            else:
                self.auth_scheme = None
            self.token = config["token"]\
                if "token" in config else None
        else:
            self.auth_scheme = None
            self.token = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "authScheme": self.auth_scheme,
            "token": self.token
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
