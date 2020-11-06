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
from okta.models import application_settings_application\
    as application_settings_application
from okta.models import application_settings_notifications\
    as application_settings_notifications


class ApplicationSettings(
    OktaObject
):
    """
    A class for ApplicationSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "app" in config:
                if isinstance(config["app"],
                              application_settings_application.ApplicationSettingsApplication):
                    self.app = config["app"]
                elif config["app"] is not None:
                    self.app = application_settings_application.ApplicationSettingsApplication(
                        config["app"]
                    )
                else:
                    self.app = None
            else:
                self.app = None
            self.implicit_assignment = config["implicitAssignment"]\
                if "implicitAssignment" in config else None
            self.inline_hook_id = config["inlineHookId"]\
                if "inlineHookId" in config else None
            if "notifications" in config:
                if isinstance(config["notifications"],
                              application_settings_notifications.ApplicationSettingsNotifications):
                    self.notifications = config["notifications"]
                elif config["notifications"] is not None:
                    self.notifications = application_settings_notifications.ApplicationSettingsNotifications(
                        config["notifications"]
                    )
                else:
                    self.notifications = None
            else:
                self.notifications = None
        else:
            self.app = None
            self.implicit_assignment = None
            self.inline_hook_id = None
            self.notifications = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "app": self.app,
            "implicitAssignment": self.implicit_assignment,
            "inlineHookId": self.inline_hook_id,
            "notifications": self.notifications
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
