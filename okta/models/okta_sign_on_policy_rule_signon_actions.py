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


class OktaSignOnPolicyRuleSignonActions(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.access = config["access"]\
                if "access" in config else None
            self.factor_lifetime = config["factorLifetime"]\
                if "factorLifetime" in config else None
            self.factor_prompt_mode = config["factorPromptMode"]\
                if "factorPromptMode" in config else None
            self.remember_device_by_default = config["rememberDeviceByDefault"]\
                if "rememberDeviceByDefault" in config else None
            self.require_factor = config["requireFactor"]\
                if "requireFactor" in config else None
            self.session = config["session"]\
                if "session" in config else None
        else:
            self.access = None
            self.factor_lifetime = None
            self.factor_prompt_mode = None
            self.remember_device_by_default = "false"
            self.require_factor = "false"
            self.session = None
