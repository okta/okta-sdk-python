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

from okta.models.user_factor\
    import UserFactor
from okta.models.hardware_user_factor_profile\
    import HardwareUserFactorProfile


class HardwareUserFactor(
    UserFactor
):
    """
    A class for HardwareUserFactor objects.
    """

    def __init__(self, config=None):
        if config:
            if "profile" in config:
                if isinstance(config["profile"],
                              HardwareUserFactorProfile):
                    self.profile = config["profile"]
                else:
                    self.profile = HardwareUserFactorProfile(
                        config["profile"]
                    )
            else:
                self.profile = None
        else:
            self.profile = None
