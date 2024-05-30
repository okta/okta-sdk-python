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
from okta.models import multifactor_enrollment_policy_authenticator_type\
    as multifactor_enrollment_policy_authenticator_type


class MultifactorEnrollmentPolicyAuthenticatorSettings(
    OktaObject
):
    """
    A class for MultifactorEnrollmentPolicyAuthenticatorSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.constraints = config["constraints"]\
                if "constraints" in config else None
            self.enroll = config["enroll"]\
                if "enroll" in config else None
            if "key" in config:
                if isinstance(config["key"],
                              multifactor_enrollment_policy_authenticator_type.MultifactorEnrollmentPolicyAuthenticatorType):
                    self.key = config["key"]
                elif config["key"] is not None:
                    self.key = multifactor_enrollment_policy_authenticator_type.MultifactorEnrollmentPolicyAuthenticatorType(
                        config["key"].upper()
                    )
                else:
                    self.key = None
            else:
                self.key = None
        else:
            self.constraints = None
            self.enroll = None
            self.key = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "constraints": self.constraints,
            "enroll": self.enroll,
            "key": self.key
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
