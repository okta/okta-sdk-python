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


from urllib.parse import urlencode


class AppLink:
    def __init__(self, config=None):
        if config:
            self.app_assignment_id = config["appAssignmentId"]
            self.app_instance_id = config["appInstanceId"]
            self.app_name = config["appName"]
            self.credentials_setup = config["credentialsSetup"]
            self.hidden = config["hidden"]
            self.id = config["id"]
            self.label = config["label"]
            self.link_url = config["linkUrl"]
            self.logo_url = config["logoUrl"]
            self.sort_order = config["sortOrder"]
        else:
            self.app_assignment_id = None
            self.app_instance_id = None
            self.app_name = None
            self.credentials_setup = None
            self.hidden = None
            self.id = None
            self.label = None
            self.link_url = None
            self.logo_url = None
            self.sort_order = None


# End of File Generation
