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

from okta.models.user_factor\
    import UserFactor
from okta.models.factor_result_type\
    import FactorResultType
from okta.models.push_user_factor_profile\
    import PushUserFactorProfile


class PushUserFactor(
    UserFactor
):
    """
    A class for PushUserFactor objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            if "factorResult" in config:
                if isinstance(config["factorResult"],
                              FactorResultType):
                    self.factor_result = config["factorResult"]
                else:
                    self.factor_result = FactorResultType(
                        config["factorResult"]
                    )
            else:
                self.factor_result = None
            if "profile" in config:
                if isinstance(config["profile"],
                              PushUserFactorProfile):
                    self.profile = config["profile"]
                else:
                    self.profile = PushUserFactorProfile(
                        config["profile"]
                    )
            else:
                self.profile = None
        else:
            self.expires_at = None
            self.factor_result = None
            self.profile = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expiresAt": self.expires_at,
            "factorResult": self.factor_result,
            "profile": self.profile
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
