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
from okta.models import app_user_credentials\
    as app_user_credentials


class AppUser(
    OktaObject
):
    """
    A class for AppUser objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            if "credentials" in config:
                if isinstance(config["credentials"],
                              app_user_credentials.AppUserCredentials):
                    self.credentials = config["credentials"]
                elif config["credentials"] is not None:
                    self.credentials = app_user_credentials.AppUserCredentials(
                        config["credentials"]
                    )
                else:
                    self.credentials = None
            else:
                self.credentials = None
            self.external_id = config["externalId"]\
                if "externalId" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_sync = config["lastSync"]\
                if "lastSync" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.password_changed = config["passwordChanged"]\
                if "passwordChanged" in config else None
            self.profile = config["profile"]\
                if "profile" in config else None
            self.scope = config["scope"]\
                if "scope" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.status_changed = config["statusChanged"]\
                if "statusChanged" in config else None
            self.sync_state = config["syncState"]\
                if "syncState" in config else None
        else:
            self.embedded = None
            self.links = None
            self.created = None
            self.credentials = None
            self.external_id = None
            self.id = None
            self.last_sync = None
            self.last_updated = None
            self.password_changed = None
            self.profile = None
            self.scope = None
            self.status = None
            self.status_changed = None
            self.sync_state = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "created": self.created,
            "credentials": self.credentials,
            "externalId": self.external_id,
            "id": self.id,
            "lastSync": self.last_sync,
            "lastUpdated": self.last_updated,
            "passwordChanged": self.password_changed,
            "profile": self.profile,
            "scope": self.scope,
            "status": self.status,
            "statusChanged": self.status_changed,
            "syncState": self.sync_state
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
