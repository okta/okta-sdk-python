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


class OAuth2Claim:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            self.always_include_in_token = config["alwaysIncludeInToken"]\
                if "alwaysIncludeInToken" in config else None
            self.claim_type = config["claimType"]\
                if "claimType" in config else None
            self.conditions = config["conditions"]\
                if "conditions" in config else None
            self.group_filter_type = config["group_filter_type"]\
                if "group_filter_type" in config else None
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

# End of File Generation
