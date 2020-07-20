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
from okta.models.application_settings_notifications_vpn_network\
    import ApplicationSettingsNotificationsVpnNetwork


class ApplicationSettingsNotificationsVpn(
    OktaObject
):
    """
    A class for ApplicationSettingsNotificationsVpn objects.
    """

    def __init__(self, config=None):
        if config:
            self.help_url = config["helpUrl"]\
                if "helpUrl" in config else None
            self.message = config["message"]\
                if "message" in config else None
            if "network" in config:
                if isinstance(config["network"],
                              ApplicationSettingsNotificationsVpnNetwork):
                    self.network = config["network"]
                else:
                    self.network = ApplicationSettingsNotificationsVpnNetwork(
                        config["network"]
                    )
            else:
                self.network = None
        else:
            self.help_url = None
            self.message = None
            self.network = None

    def request_format(self):
        return {
            "helpUrl": self.help_url,
            "message": self.message,
            "network": self.network
        }
