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


class User:
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]
            self.links = config["_links"]
            self.activated = config["activated"]
            self.created = config["created"]
            self.credentials = config["credentials"]
            self.id = config["id"]
            self.last_login = config["lastLogin"]
            self.last_updated = config["lastUpdated"]
            self.password_changed = config["passwordChanged"]
            self.profile = config["profile"]
            self.status = config["status"]
            self.status_changed = config["statusChanged"]
            self.transitioning_to_status = config["transitioningToStatus"]
            self.type = config["type"]
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

# End of File Generation
