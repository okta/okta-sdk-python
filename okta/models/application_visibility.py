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
from okta.models.application_visibility_hide\
    import ApplicationVisibilityHide


class ApplicationVisibility(
    OktaObject
):
    """
    A class for ApplicationVisibility objects.
    """

    def __init__(self, config=None):
        if config:
            self.app_links = config["appLinks"]\
                if "appLinks" in config else None
            self.auto_submit_toolbar = config["autoSubmitToolbar"]\
                if "autoSubmitToolbar" in config else None
            if "hide" in config:
                if isinstance(config["hide"],
                              ApplicationVisibilityHide):
                    self.hide = config["hide"]
                else:
                    self.hide = ApplicationVisibilityHide(
                        config["hide"]
                    )
            else:
                self.hide = None
        else:
            self.app_links = None
            self.auto_submit_toolbar = None
            self.hide = None

    def request_format(self):
        return {
            "appLinks": self.app_links,
            "autoSubmitToolbar": self.auto_submit_toolbar,
            "hide": self.hide
        }
