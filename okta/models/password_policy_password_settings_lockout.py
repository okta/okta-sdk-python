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
from okta.okta_collection import OktaCollection


class PasswordPolicyPasswordSettingsLockout(
    OktaObject
):
    """
    A class for PasswordPolicyPasswordSettingsLockout objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.auto_unlock_minutes = config["autoUnlockMinutes"]\
                if "autoUnlockMinutes" in config else None
            self.max_attempts = config["maxAttempts"]\
                if "maxAttempts" in config else None
            self.show_lockout_failures = config["showLockoutFailures"]\
                if "showLockoutFailures" in config else None
            self.user_lockout_notification_channels = OktaCollection.form_list(
                config["userLockoutNotificationChannels"] if "userLockoutNotificationChannels"\
                    in config else [],
                str
            )
        else:
            self.auto_unlock_minutes = None
            self.max_attempts = None
            self.show_lockout_failures = None
            self.user_lockout_notification_channels = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "autoUnlockMinutes": self.auto_unlock_minutes,
            "maxAttempts": self.max_attempts,
            "showLockoutFailures": self.show_lockout_failures,
            "userLockoutNotificationChannels": self.user_lockout_notification_channels
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
