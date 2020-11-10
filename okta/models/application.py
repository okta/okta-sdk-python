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
from okta.okta_collection import OktaCollection
from okta.models import application_accessibility\
    as application_accessibility
from okta.models import application_credentials\
    as application_credentials
from okta.models import application_licensing\
    as application_licensing
from okta.models import application_settings\
    as application_settings
from okta.models import application_sign_on_mode\
    as application_sign_on_mode
from okta.models import application_visibility\
    as application_visibility


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
                              application_accessibility.ApplicationAccessibility):
                    self.accessibility = config["accessibility"]
                elif config["accessibility"] is not None:
                    self.accessibility = application_accessibility.ApplicationAccessibility(
                        config["accessibility"]
                    )
                else:
                    self.accessibility = None
            else:
                self.accessibility = None
            self.created = config["created"]\
                if "created" in config else None
            if "credentials" in config:
                if isinstance(config["credentials"],
                              application_credentials.ApplicationCredentials):
                    self.credentials = config["credentials"]
                elif config["credentials"] is not None:
                    self.credentials = application_credentials.ApplicationCredentials(
                        config["credentials"]
                    )
                else:
                    self.credentials = None
            else:
                self.credentials = None
            self.features = OktaCollection.form_list(
                config["features"] if "features"\
                    in config else [],
                str
            )
            self.id = config["id"]\
                if "id" in config else None
            self.label = config["label"]\
                if "label" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            if "licensing" in config:
                if isinstance(config["licensing"],
                              application_licensing.ApplicationLicensing):
                    self.licensing = config["licensing"]
                elif config["licensing"] is not None:
                    self.licensing = application_licensing.ApplicationLicensing(
                        config["licensing"]
                    )
                else:
                    self.licensing = None
            else:
                self.licensing = None
            self.name = config["name"]\
                if "name" in config else None
            self.profile = config["profile"]\
                if "profile" in config else None
            if "settings" in config:
                if isinstance(config["settings"],
                              application_settings.ApplicationSettings):
                    self.settings = config["settings"]
                elif config["settings"] is not None:
                    self.settings = application_settings.ApplicationSettings(
                        config["settings"]
                    )
                else:
                    self.settings = None
            else:
                self.settings = None
            if "signOnMode" in config:
                if isinstance(config["signOnMode"],
                              application_sign_on_mode.ApplicationSignOnMode):
                    self.sign_on_mode = config["signOnMode"]
                elif config["signOnMode"] is not None:
                    self.sign_on_mode = application_sign_on_mode.ApplicationSignOnMode(
                        config["signOnMode"].upper()
                    )
                else:
                    self.sign_on_mode = None
            else:
                self.sign_on_mode = None
            self.status = config["status"]\
                if "status" in config else None
            if "visibility" in config:
                if isinstance(config["visibility"],
                              application_visibility.ApplicationVisibility):
                    self.visibility = config["visibility"]
                elif config["visibility"] is not None:
                    self.visibility = application_visibility.ApplicationVisibility(
                        config["visibility"]
                    )
                else:
                    self.visibility = None
            else:
                self.visibility = None
        else:
            self.embedded = None
            self.links = None
            self.accessibility = None
            self.created = None
            self.credentials = None
            self.features = []
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
