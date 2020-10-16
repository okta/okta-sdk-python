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


class PasswordPolicyPasswordSettingsAge(
    OktaObject
):
    """
    A class for PasswordPolicyPasswordSettingsAge objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.expire_warn_days = config["expireWarnDays"]\
                if "expireWarnDays" in config else 0
            self.history_count = config["historyCount"]\
                if "historyCount" in config else 0
            self.max_age_days = config["maxAgeDays"]\
                if "maxAgeDays" in config else 0
            self.min_age_minutes = config["minAgeMinutes"]\
                if "minAgeMinutes" in config else 0
        else:
            self.expire_warn_days = 0
            self.history_count = 0
            self.max_age_days = 0
            self.min_age_minutes = 0

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expireWarnDays": self.expire_warn_days,
            "historyCount": self.history_count,
            "maxAgeDays": self.max_age_days,
            "minAgeMinutes": self.min_age_minutes
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
