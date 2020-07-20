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
from okta.models.user_status\
    import UserStatus
from okta.models.user_type\
    import UserType


class User(
    OktaObject
):
    """
    A class for User objects.
    """

    def __init__(self, config=None):
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            self.activated = config["activated"]\
                if "activated" in config else None
            self.created = config["created"]\
                if "created" in config else None
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
            self.id = config["id"]\
                if "id" in config else None
            self.last_login = config["lastLogin"]\
                if "lastLogin" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.password_changed = config["passwordChanged"]\
                if "passwordChanged" in config else None
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
            if "status" in config:
                if isinstance(config["status"],
                              UserStatus):
                    self.status = config["status"]
                else:
                    self.status = UserStatus(
                        config["status"]
                    )
            else:
                self.status = None
            self.status_changed = config["statusChanged"]\
                if "statusChanged" in config else None
            if "transitioningToStatus" in config:
                if isinstance(config["transitioningToStatus"],
                              UserStatus):
                    self.transitioning_to_status = config["transitioningToStatus"]
                else:
                    self.transitioning_to_status = UserStatus(
                        config["transitioningToStatus"]
                    )
            else:
                self.transitioning_to_status = None
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
            self.embedded = None
            self.links = None
            self.activated = None
            self.created = None
            self.credentials = None
            self.id = None
            self.last_login = None
            self.last_updated = None
            self.password_changed = None
            self.profile = None
            self.status = None
            self.status_changed = None
            self.transitioning_to_status = None
            self.type = None

    def request_format(self):
        return {
            "_embedded": self.embedded,
            "_links": self.links,
            "activated": self.activated,
            "created": self.created,
            "credentials": self.credentials,
            "id": self.id,
            "lastLogin": self.last_login,
            "lastUpdated": self.last_updated,
            "passwordChanged": self.password_changed,
            "profile": self.profile,
            "status": self.status,
            "statusChanged": self.status_changed,
            "transitioningToStatus": self.transitioning_to_status,
            "type": self.type
        }
