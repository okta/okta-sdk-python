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

from okta.models.application\
    import Application


class BasicAuthApplication(
    Application
):
    def __init__(self, config=None):
        if config:
            self.credentials = config["credentials"]\
                if "credentials" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.settings = config["settings"]\
                if "settings" in config else None
        else:
            self.credentials = None
            self.name = "template_basic_auth"
            self.settings = None
