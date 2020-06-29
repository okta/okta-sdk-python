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


class LogEvent:
    def __init__(self, config=None):
        if config:
            self.actor = config["actor"]
            self.authentication_context = config["authenticationContext"]
            self.client = config["client"]
            self.debug_context = config["debugContext"]
            self.display_message = config["displayMessage"]
            self.event_type = config["eventType"]
            self.legacy_event_type = config["legacyEventType"]
            self.outcome = config["outcome"]
            self.published = config["published"]
            self.request = config["request"]
            self.security_context = config["securityContext"]
            self.severity = config["severity"]
            self.target = config["target"]
            self.transaction = config["transaction"]
            self.uuid = config["uuid"]
            self.version = config["version"]
        else:
            self.actor = None
            self.authentication_context = None
            self.client = None
            self.debug_context = None
            self.display_message = None
            self.event_type = None
            self.legacy_event_type = None
            self.outcome = None
            self.published = None
            self.request = None
            self.security_context = None
            self.severity = None
            self.target = None
            self.transaction = None
            self.uuid = None
            self.version = None

# End of File Generation
