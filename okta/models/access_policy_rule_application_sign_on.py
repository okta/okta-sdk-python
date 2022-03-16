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
from okta.models import verification_method\
    as verification_method


class AccessPolicyRuleApplicationSignOn(
    OktaObject
):
    """
    A class for AccessPolicyRuleApplicationSignOn objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.access = config["access"]\
                if "access" in config else None
            if "verificationMethod" in config:
                if isinstance(config["verificationMethod"],
                              verification_method.VerificationMethod):
                    self.verification_method = config["verificationMethod"]
                elif config["verificationMethod"] is not None:
                    self.verification_method = verification_method.VerificationMethod(
                        config["verificationMethod"]
                    )
                else:
                    self.verification_method = None
            else:
                self.verification_method = None
        else:
            self.access = None
            self.verification_method = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "access": self.access,
            "verificationMethod": self.verification_method
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
