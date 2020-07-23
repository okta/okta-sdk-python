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
from okta.models.group_condition\
    import GroupCondition
from okta.models.user_condition\
    import UserCondition


class PolicyPeopleCondition(
    OktaObject
):
    """
    A class for PolicyPeopleCondition objects.
    """

    def __init__(self, config=None):
        if config:
            if "groups" in config:
                if isinstance(config["groups"],
                              GroupCondition):
                    self.groups = config["groups"]
                else:
                    self.groups = GroupCondition(
                        config["groups"]
                    )
            else:
                self.groups = None
            if "users" in config:
                if isinstance(config["users"],
                              UserCondition):
                    self.users = config["users"]
                else:
                    self.users = UserCondition(
                        config["users"]
                    )
            else:
                self.users = None
        else:
            self.groups = None
            self.users = None

    def request_format(self):
        return {
            "groups": self.groups,
            "users": self.users
        }
