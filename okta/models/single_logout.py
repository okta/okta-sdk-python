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


class SingleLogout(
    OktaObject
):
    """
    A class for SingleLogout objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.enabled = config["enabled"]\
                if "enabled" in config else None
            self.issuer = config["issuer"]\
                if "issuer" in config else None
            self.logout_url = config["logoutUrl"]\
                if "logoutUrl" in config else None
        else:
            self.enabled = None
            self.issuer = None
            self.logout_url = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "enabled": self.enabled,
            "issuer": self.issuer,
            "logoutUrl": self.logout_url
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
