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

from okta.models.saml_application_settings\
    import SamlApplicationSettings
from okta.models import org_2_org_application_settings_app\
    as org_2_org_application_settings_app


class Org2OrgApplicationSettings(
    SamlApplicationSettings
):
    """
    A class for Org2OrgApplicationSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "app" in config:
                if isinstance(config["app"],
                              org_2_org_application_settings_app.Org2OrgApplicationSettingsApp):
                    self.app = config["app"]
                elif config["app"] is not None:
                    self.app = org_2_org_application_settings_app.Org2OrgApplicationSettingsApp(
                        config["app"]
                    )
                else:
                    self.app = None
            else:
                self.app = None
        else:
            self.app = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "app": self.app
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
