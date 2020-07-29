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
from okta.models.policy_subject_match_type\
    import PolicySubjectMatchType
from okta.models.policy_user_name_template\
    import PolicyUserNameTemplate


class PolicySubject(
    OktaObject
):
    """
    A class for PolicySubject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.filter = config["filter"]\
                if "filter" in config else None
            self.format = config["format"]\
                if "format" in config else None
            self.match_attribute = config["matchAttribute"]\
                if "matchAttribute" in config else None
            if "matchType" in config:
                if isinstance(config["matchType"],
                              PolicySubjectMatchType):
                    self.match_type = config["matchType"]
                else:
                    self.match_type = PolicySubjectMatchType(
                        config["matchType"]
                    )
            else:
                self.match_type = None
            if "userNameTemplate" in config:
                if isinstance(config["userNameTemplate"],
                              PolicyUserNameTemplate):
                    self.user_name_template = config["userNameTemplate"]
                else:
                    self.user_name_template = PolicyUserNameTemplate(
                        config["userNameTemplate"]
                    )
            else:
                self.user_name_template = None
        else:
            self.filter = None
            self.format = None
            self.match_attribute = None
            self.match_type = None
            self.user_name_template = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "filter": self.filter,
            "format": self.format,
            "matchAttribute": self.match_attribute,
            "matchType": self.match_type,
            "userNameTemplate": self.user_name_template
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
