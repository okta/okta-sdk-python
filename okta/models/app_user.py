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


class AppUser(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]\
                if "_embedded" in config else None
            self.links = config["_links"]\
                if "_links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.credentials = config["credentials"]\
                if "credentials" in config else None
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

# End of File Generation
