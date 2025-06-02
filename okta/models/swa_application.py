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

from okta.models.browser_plugin_application\
    import BrowserPluginApplication
from okta.models import swa_application_settings\
    as swa_application_settings


class SwaApplication(
    BrowserPluginApplication
):
    """
    A class for SwaApplication objects.
    """

    def __init__(self, config=None):
        super().__init__(config=config)
        if config:
            object.__setattr__(self, "name", config.get("name", "template_swa"))

            if "settings" in config:
                if isinstance(config["settings"],
                              swa_application_settings.SwaApplicationSettings):
                    object.__setattr__(self, "settings", config.get("settings"))

                elif config["settings"] is not None:
                    object.__setattr__(self, "settings",
                                       swa_application_settings.SwaApplicationSettings(
                        **config["settings"]
                    ))
                else:
                    object.__setattr__(self, "settings", None)
            else:
                object.__setattr__(self, "settings", None)
        else:
            object.__setattr__(self, "name", "template_swa")
            object.__setattr__(self, "settings", None)

    @classmethod
    def from_config(cls, config: dict) -> "SwaApplication":
        instance = cls()
        # instance.name = config.get("name", "template_swa")
        settings = config.get("settings")
        if isinstance(settings,
                      swa_application_settings.SwaApplicationSettings):
            instance.settings = settings
        elif settings is not None:
            instance.settings = swa_application_settings.SwaApplicationSettings(**settings)
        else:
            instance.settings = None
        return instance

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "name": self.name,
            "settings": self.settings
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
