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


class Application(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]\
                if "_embedded" in config else None
            self.links = config["_links"]\
                if "_links" in config else None
            self.accessibility = config["accessibility"]\
                if "accessibility" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.credentials = config["credentials"]\
                if "credentials" in config else None
            self.features = config["features"]\
                if "features" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.label = config["label"]\
                if "label" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.licensing = config["licensing"]\
                if "licensing" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.profile = config["profile"]\
                if "profile" in config else None
            self.settings = config["settings"]\
                if "settings" in config else None
            self.sign_on_mode = config["signOnMode"]\
                if "signOnMode" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.visibility = config["visibility"]\
                if "visibility" in config else None
        else:
            self.embedded = None
            self.links = None
            self.accessibility = None
            self.created = None
            self.credentials = None
            self.features = None
            self.id = None
            self.label = None
            self.last_updated = None
            self.licensing = None
            self.name = None
            self.profile = None
            self.settings = None
            self.sign_on_mode = None
            self.status = None
            self.visibility = None

# End of File Generation
