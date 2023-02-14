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


class ThreatInsightConfiguration(
    OktaObject
):
    """
    A class for ThreatInsightConfiguration objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.action = config["action"]\
                if "action" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.exclude_zones = OktaCollection.form_list(
                config["excludeZones"] if "excludeZones"\
                    in config else [],
                str
            )
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
        else:
            self.links = None
            self.action = None
            self.created = None
            self.exclude_zones = []
            self.last_updated = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "action": self.action,
            "created": self.created,
            "excludeZones": self.exclude_zones,
            "lastUpdated": self.last_updated
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
