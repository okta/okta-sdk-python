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
from okta.models import feature_stage\
    as feature_stage
from okta.models import enabled_status\
    as enabled_status
from okta.models import feature_type\
    as feature_type


class Feature(
    OktaObject
):
    """
    A class for Feature objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "stage" in config:
                if isinstance(config["stage"],
                              feature_stage.FeatureStage):
                    self.stage = config["stage"]
                elif config["stage"] is not None:
                    self.stage = feature_stage.FeatureStage(
                        config["stage"]
                    )
                else:
                    self.stage = None
            else:
                self.stage = None
            if "status" in config:
                if isinstance(config["status"],
                              enabled_status.EnabledStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = enabled_status.EnabledStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            if "type" in config:
                if isinstance(config["type"],
                              feature_type.FeatureType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = feature_type.FeatureType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
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

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "description": self.description,
            "id": self.id,
            "name": self.name,
            "stage": self.stage,
            "status": self.status,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
