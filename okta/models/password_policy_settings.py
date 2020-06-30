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


class PasswordPolicySettings:
    def __init__(self, config=None):
        if config:
            self.delegation = config["delegation"]\
                if "delegation" in config else None
            self.password = config["password"]\
                if "password" in config else None
            self.recovery = config["recovery"]\
                if "recovery" in config else None
        else:
            self.delegation = None
            self.password = None
            self.recovery = None

# End of File Generation
