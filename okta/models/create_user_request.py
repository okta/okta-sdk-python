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
from okta.models.user_credentials\
    import UserCredentials
from okta.models.user_profile\
    import UserProfile
from okta.models.user_type\
    import UserType


class CreateUserRequest(
    OktaObject
):
    """
    A class for CreateUserRequest objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "credentials" in config:
                if isinstance(config["credentials"],
                              UserCredentials):
                    self.credentials = config["credentials"]
                else:
                    self.credentials = UserCredentials(
                        config["credentials"]
                    )
            else:
                self.credentials = None
            self.group_ids = config["groupIds"]\
                if "groupIds" in config else None
            if "profile" in config:
                if isinstance(config["profile"],
                              UserProfile):
                    self.profile = config["profile"]
                else:
                    self.profile = UserProfile(
                        config["profile"]
                    )
            else:
                self.profile = None
            if "type" in config:
                if isinstance(config["type"],
                              UserType):
                    self.type = config["type"]
                else:
                    self.type = UserType(
                        config["type"]
                    )
            else:
                self.type = None
        else:
            self.credentials = None
            self.group_ids = None
            self.profile = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "credentials": self.credentials,
            "groupIds": self.group_ids,
            "profile": self.profile,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
