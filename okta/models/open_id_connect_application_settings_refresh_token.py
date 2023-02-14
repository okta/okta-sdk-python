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
from okta.models import open_id_connect_refresh_token_rotation_type\
    as open_id_connect_refresh_token_rotation_type


class OpenIdConnectApplicationSettingsRefreshToken(
    OktaObject
):
    """
    A class for OpenIdConnectApplicationSettingsRefreshToken objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.leeway = config["leeway"]\
                if "leeway" in config else None
            if "rotationType" in config:
                if isinstance(config["rotationType"],
                              open_id_connect_refresh_token_rotation_type.OpenIdConnectRefreshTokenRotationType):
                    self.rotation_type = config["rotationType"]
                elif config["rotationType"] is not None:
                    self.rotation_type = open_id_connect_refresh_token_rotation_type.OpenIdConnectRefreshTokenRotationType(
                        config["rotationType"].upper()
                    )
                else:
                    self.rotation_type = None
            else:
                self.rotation_type = None
        else:
            self.leeway = None
            self.rotation_type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "leeway": self.leeway,
            "rotation_type": self.rotation_type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
