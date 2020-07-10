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


class TrustedOrigin(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.created_by = config["createdBy"]\
                if "createdBy" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.last_updated_by = config["lastUpdatedBy"]\
                if "lastUpdatedBy" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.origin = config["origin"]\
                if "origin" in config else None
            self.scopes = config["scopes"]\
                if "scopes" in config else None
            self.status = config["status"]\
                if "status" in config else None
        else:
            self.links = None
            self.created = None
            self.created_by = None
            self.id = None
            self.last_updated = None
            self.last_updated_by = None
            self.name = None
            self.origin = None
            self.scopes = None
            self.status = None
