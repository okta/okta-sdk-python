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
from okta.models import policy_subject_match_type\
    as policy_subject_match_type
from okta.models import policy_user_name_template\
    as policy_user_name_template


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
            self.format = OktaCollection.form_list(
                config["format"] if "format"\
                    in config else [],
                str
            )
            self.match_attribute = config["matchAttribute"]\
                if "matchAttribute" in config else None
            if "matchType" in config:
                if isinstance(config["matchType"],
                              policy_subject_match_type.PolicySubjectMatchType):
                    self.match_type = config["matchType"]
                elif config["matchType"] is not None:
                    self.match_type = policy_subject_match_type.PolicySubjectMatchType(
                        config["matchType"].upper()
                    )
                else:
                    self.match_type = None
            else:
                self.match_type = None
            if "userNameTemplate" in config:
                if isinstance(config["userNameTemplate"],
                              policy_user_name_template.PolicyUserNameTemplate):
                    self.user_name_template = config["userNameTemplate"]
                elif config["userNameTemplate"] is not None:
                    self.user_name_template = policy_user_name_template.PolicyUserNameTemplate(
                        config["userNameTemplate"]
                    )
                else:
                    self.user_name_template = None
            else:
                self.user_name_template = None
        else:
            self.filter = None
            self.format = []
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
