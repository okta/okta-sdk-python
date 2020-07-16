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
from okta.models.feature_stage\
    import FeatureStage
from okta.models.enabled_status\
    import EnabledStatus
from okta.models.feature_type\
    import FeatureType


class Feature(
    OktaObject
):
    """
    A class for Feature objects.
    """

    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "stage" in config:
                if isinstance(config["stage"],
                              FeatureStage):
                    self.stage = config["stage"]
                else:
                    self.stage = FeatureStage(
                        config["stage"]
                    )
            else:
                self.stage = None
            if "status" in config:
                if isinstance(config["status"],
                              EnabledStatus):
                    self.status = config["status"]
                else:
                    self.status = EnabledStatus(
                        config["status"]
                    )
            else:
                self.status = None
            if "type" in config:
                if isinstance(config["type"],
                              FeatureType):
                    self.type = config["type"]
                else:
                    self.type = FeatureType(
                        config["type"]
                    )
            else:
                self.type = None
        else:
            self.links = None
            self.description = None
            self.id = None
            self.name = None
            self.stage = None
            self.status = None
            self.type = None
