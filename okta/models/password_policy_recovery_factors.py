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


class PasswordPolicyRecoveryFactors(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.okta_call = config["okta_call"]\
                if "okta_call" in config else None
            self.okta_email = config["okta_email"]\
                if "okta_email" in config else None
            self.okta_sms = config["okta_sms"]\
                if "okta_sms" in config else None
            self.recovery_question = config["recovery_question"]\
                if "recovery_question" in config else None
        else:
            self.okta_call = None
            self.okta_email = None
            self.okta_sms = None
            self.recovery_question = None
