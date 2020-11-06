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
from okta.models import application_settings_notifications_vpn_network\
    as application_settings_notifications_vpn_network


class ApplicationSettingsNotificationsVpn(
    OktaObject
):
    """
    A class for ApplicationSettingsNotificationsVpn objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.help_url = config["helpUrl"]\
                if "helpUrl" in config else None
            self.message = config["message"]\
                if "message" in config else None
            if "network" in config:
                if isinstance(config["network"],
                              application_settings_notifications_vpn_network.ApplicationSettingsNotificationsVpnNetwork):
                    self.network = config["network"]
                elif config["network"] is not None:
                    self.network = application_settings_notifications_vpn_network.ApplicationSettingsNotificationsVpnNetwork(
                        config["network"]
                    )
                else:
                    self.network = None
            else:
                self.network = None
        else:
            self.help_url = None
            self.message = None
            self.network = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "helpUrl": self.help_url,
            "message": self.message,
            "network": self.network
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
