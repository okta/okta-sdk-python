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


class PasswordPolicyPasswordSettingsAge:
    def __init__(self, config=None):
        if config:
            self.expire_warn_days = config["expireWarnDays"]
            self.history_count = config["historyCount"]
            self.max_age_days = config["maxAgeDays"]
            self.min_age_minutes = config["minAgeMinutes"]
        else:
            self.expire_warn_days = "0"
            self.history_count = "0"
            self.max_age_days = "0"
            self.min_age_minutes = "0"

# End of File Generation
