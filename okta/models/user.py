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
from okta.models import user_credentials\
    as user_credentials
from okta.models import user_profile\
    as user_profile
from okta.models import user_status\
    as user_status
from okta.models import user_type\
    as user_type


class User(
    OktaObject
):
    """
    A class for User objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
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
                              user_credentials.UserCredentials):
                    self.credentials = config["credentials"]
                elif config["credentials"] is not None:
                    self.credentials = user_credentials.UserCredentials(
                        config["credentials"]
                    )
                else:
                    self.credentials = None
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
                              user_profile.UserProfile):
                    self.profile = config["profile"]
                elif config["profile"] is not None:
                    self.profile = user_profile.UserProfile(
                        config["profile"]
                    )
                else:
                    self.profile = None
            else:
                self.profile = None
            if "status" in config:
                if isinstance(config["status"],
                              user_status.UserStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = user_status.UserStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            self.status_changed = config["statusChanged"]\
                if "statusChanged" in config else None
            if "transitioningToStatus" in config:
                if isinstance(config["transitioningToStatus"],
                              user_status.UserStatus):
                    self.transitioning_to_status = config["transitioningToStatus"]
                elif config["transitioningToStatus"] is not None:
                    self.transitioning_to_status = user_status.UserStatus(
                        config["transitioningToStatus"].upper()
                    )
                else:
                    self.transitioning_to_status = None
            else:
                self.transitioning_to_status = None
            if "type" in config:
                if isinstance(config["type"],
                              user_type.UserType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = user_type.UserType(
                        config["type"]
                    )
                else:
                    self.type = None
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
        parent_req_format = super().request_format()
        current_obj_format = {
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
        parent_req_format.update(current_obj_format)
        return parent_req_format
