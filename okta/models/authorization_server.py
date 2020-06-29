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


class AuthorizationServer:
    def __init__(self, config=None):
        if config:
            self.links = config["_links"]
            self.audiences = config["audiences"]
            self.created = config["created"]
            self.credentials = config["credentials"]
            self.description = config["description"]
            self.id = config["id"]
            self.issuer = config["issuer"]
            self.issuer_mode = config["issuerMode"]
            self.last_updated = config["lastUpdated"]
            self.name = config["name"]
            self.status = config["status"]
        else:
            self.links = None
            self.audiences = None
            self.created = None
            self.credentials = None
            self.description = None
            self.id = None
            self.issuer = None
            self.issuer_mode = None
            self.last_updated = None
            self.name = None
            self.status = None

# End of File Generation
