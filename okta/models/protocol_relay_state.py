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
from okta.models import protocol_relay_state_format\
    as protocol_relay_state_format


class ProtocolRelayState(
    OktaObject
):
    """
    A class for ProtocolRelayState objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "format" in config:
                if isinstance(config["format"],
                              protocol_relay_state_format.ProtocolRelayStateFormat):
                    self.format = config["format"]
                elif config["format"] is not None:
                    self.format = protocol_relay_state_format.ProtocolRelayStateFormat(
                        config["format"].upper()
                    )
                else:
                    self.format = None
            else:
                self.format = None
        else:
            self.format = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "format": self.format
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
