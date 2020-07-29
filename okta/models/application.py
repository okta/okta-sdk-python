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
from okta.models.application_accessibility\
    import ApplicationAccessibility
from okta.models.application_credentials\
    import ApplicationCredentials
from okta.models.application_licensing\
    import ApplicationLicensing
from okta.models.application_settings\
    import ApplicationSettings
from okta.models.application_sign_on_mode\
    import ApplicationSignOnMode
from okta.models.application_visibility\
    import ApplicationVisibility


class Application(
    OktaObject
):
    """
    A class for Application objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            if "accessibility" in config:
                if isinstance(config["accessibility"],
                              ApplicationAccessibility):
                    self.accessibility = config["accessibility"]
                else:
                    self.accessibility = ApplicationAccessibility(
                        config["accessibility"]
                    )
            else:
                self.accessibility = None
            self.created = config["created"]\
                if "created" in config else None
            if "credentials" in config:
                if isinstance(config["credentials"],
                              ApplicationCredentials):
                    self.credentials = config["credentials"]
                else:
                    self.credentials = ApplicationCredentials(
                        config["credentials"]
                    )
            else:
                self.credentials = None
            self.features = config["features"]\
                if "features" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.label = config["label"]\
                if "label" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            if "licensing" in config:
                if isinstance(config["licensing"],
                              ApplicationLicensing):
                    self.licensing = config["licensing"]
                else:
                    self.licensing = ApplicationLicensing(
                        config["licensing"]
                    )
            else:
                self.licensing = None
            self.name = config["name"]\
                if "name" in config else None
            self.profile = config["profile"]\
                if "profile" in config else None
            if "settings" in config:
                if isinstance(config["settings"],
                              ApplicationSettings):
                    self.settings = config["settings"]
                else:
                    self.settings = ApplicationSettings(
                        config["settings"]
                    )
            else:
                self.settings = None
            if "signOnMode" in config:
                if isinstance(config["signOnMode"],
                              ApplicationSignOnMode):
                    self.sign_on_mode = config["signOnMode"]
                else:
                    self.sign_on_mode = ApplicationSignOnMode(
                        config["signOnMode"]
                    )
            else:
                self.sign_on_mode = None
            self.status = config["status"]\
                if "status" in config else None
            if "visibility" in config:
                if isinstance(config["visibility"],
                              ApplicationVisibility):
                    self.visibility = config["visibility"]
                else:
                    self.visibility = ApplicationVisibility(
                        config["visibility"]
                    )
            else:
                self.visibility = None
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

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "accessibility": self.accessibility,
            "created": self.created,
            "credentials": self.credentials,
            "features": self.features,
            "id": self.id,
            "label": self.label,
            "lastUpdated": self.last_updated,
            "licensing": self.licensing,
            "name": self.name,
            "profile": self.profile,
            "settings": self.settings,
            "signOnMode": self.sign_on_mode,
            "status": self.status,
            "visibility": self.visibility
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
