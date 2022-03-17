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

from okta.models.application_settings_application\
    import ApplicationSettingsApplication


class Org2OrgApplicationSettingsApp(
    ApplicationSettingsApplication
):
    """
    A class for Org2OrgApplicationSettingsApp objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.acs_url = config["acsUrl"]\
                if "acsUrl" in config else None
            self.aud_restriction = config["audRestriction"]\
                if "audRestriction" in config else None
            self.base_url = config["baseUrl"]\
                if "baseUrl" in config else None
        else:
            self.acs_url = None
            self.aud_restriction = None
            self.base_url = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "acsUrl": self.acs_url,
            "audRestriction": self.aud_restriction,
            "baseUrl": self.base_url
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
