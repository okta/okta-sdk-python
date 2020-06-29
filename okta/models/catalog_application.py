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


class CatalogApplication:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.category = config["category"]
            self.description = config["description"]
            self.display_name = config["displayName"]
            self.features = config["features"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.name = config["name"]
            self.sign_on_modes = config["signOnModes"]
            self.status = config["status"]
            self.verification_status = config["verificationStatus"]
            self.website = config["website"]
        else:
            self.links = None
            self.category = None
            self.description = None
            self.display_name = None
            self.features = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.sign_on_modes = None
            self.status = None
            self.verification_status = None
            self.website = None

# End of File Generation
