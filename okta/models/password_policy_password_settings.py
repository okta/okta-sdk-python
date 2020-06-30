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


class PasswordPolicyPasswordSettings(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.age = config["age"]\
                if "age" in config else None
            self.complexity = config["complexity"]\
                if "complexity" in config else None
            self.lockout = config["lockout"]\
                if "lockout" in config else None
        else:
            self.age = None
            self.complexity = None
            self.lockout = None

# End of File Generation
