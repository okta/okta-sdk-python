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


class ProvisioningGroups:
    def __init__(self, config=None):
        if config:
            self.action = config["action"]\
                if "action" in config else None
            self.assignments = config["assignments"]\
                if "assignments" in config else None
            self.filter = config["filter"]\
                if "filter" in config else None
            self.source_attribute_name = config["sourceAttributeName"]\
                if "sourceAttributeName" in config else None
        else:
            self.action = None
            self.assignments = None
            self.filter = None
            self.source_attribute_name = None

# End of File Generation
