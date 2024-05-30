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


class Brand(
    OktaObject
):
    """
    A class for Brand objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "_links" in config:
                self.links = config["_links"]
            self.agree_to_custom_privacy_policy = config["agreeToCustomPrivacyPolicy"]\
                if "agreeToCustomPrivacyPolicy" in config else None
            self.custom_privacy_policy_url = config["customPrivacyPolicyUrl"]\
                if "customPrivacyPolicyUrl" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.remove_powered_by_okta = config["removePoweredByOkta"]\
                if "removePoweredByOkta" in config else None
        else:
            self.links = None
            self.agree_to_custom_privacy_policy = None
            self.custom_privacy_policy_url = None
            self.id = None
            self.remove_powered_by_okta = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "agreeToCustomPrivacyPolicy": self.agree_to_custom_privacy_policy,
            "customPrivacyPolicyUrl": self.custom_privacy_policy_url,
            "id": self.id,
            "removePoweredByOkta": self.remove_powered_by_okta
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
