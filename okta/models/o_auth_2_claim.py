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
from okta.models import o_auth_2_claim_conditions\
    as o_auth_2_claim_conditions


class OAuth2Claim(
    OktaObject
):
    """
    A class for OAuth2Claim objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.always_include_in_token = config["alwaysIncludeInToken"]\
                if "alwaysIncludeInToken" in config else None
            self.claim_type = config["claimType"]\
                if "claimType" in config else None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              o_auth_2_claim_conditions.OAuth2ClaimConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = o_auth_2_claim_conditions.OAuth2ClaimConditions(
                        config["conditions"]
                    )
                else:
                    self.conditions = None
            else:
                self.conditions = None
            self.group_filter_type = config["groupFilterType"]\
                if "groupFilterType" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.system = config["system"]\
                if "system" in config else None
            self.value = config["value"]\
                if "value" in config else None
            self.value_type = config["valueType"]\
                if "valueType" in config else None
        else:
            self.links = None
            self.always_include_in_token = None
            self.claim_type = None
            self.conditions = None
            self.group_filter_type = None
            self.id = None
            self.name = None
            self.status = None
            self.system = None
            self.value = None
            self.value_type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "alwaysIncludeInToken": self.always_include_in_token,
            "claimType": self.claim_type,
            "conditions": self.conditions,
            "group_filter_type": self.group_filter_type,
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "system": self.system,
            "value": self.value,
            "valueType": self.value_type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
