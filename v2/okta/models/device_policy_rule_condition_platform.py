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
from okta.okta_collection import OktaCollection


class DevicePolicyRuleConditionPlatform(
    OktaObject
):
    """
    A class for DevicePolicyRuleConditionPlatform objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.supported_mdm_frameworks = OktaCollection.form_list(
                config["supportedMdmFrameworks"] if "supportedMdmFrameworks"\
                    in config else [],
                str
            )
            self.types = OktaCollection.form_list(
                config["types"] if "types"\
                    in config else [],
                str
            )
        else:
            self.supported_mdm_frameworks = []
            self.types = []

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "supportedMDMFrameworks": self.supported_mdm_frameworks,
            "types": self.types
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
