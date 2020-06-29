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


class OAuth2Scope:
    def __init__(self, config=None):
        if config:
            self.consent = config["consent"]
            self.default = config["default"]
            self.description = config["description"]
            self.display_name = config["displayName"]
            self.id = config["id"]
            self.metadata_publish = config["metadataPublish"]
            self.name = config["name"]
            self.system = config["system"]
        else:
            self.consent = None
            self.default = None
            self.description = None
            self.display_name = None
            self.id = None
            self.metadata_publish = None
            self.name = None
            self.system = None

# End of File Generation
