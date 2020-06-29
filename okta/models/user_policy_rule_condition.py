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


class UserPolicyRuleCondition:
    def __init__(self, config=None):
        if config:
            self.exclude = config["exclude"]
            self.inactivity = config["inactivity"]
            self.include = config["include"]
            self.lifecycle_expiration = config["lifecycleExpiration"]
            self.password_expiration = config["passwordExpiration"]
            self.user_lifecycle_attribute = config["userLifecycleAttribute"]
        else:
            self.exclude = None
            self.inactivity = None
            self.include = None
            self.lifecycle_expiration = None
            self.password_expiration = None
            self.user_lifecycle_attribute = None

# End of File Generation
