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
from okta.models import feature_stage_state\
    as feature_stage_state
from okta.models import feature_stage_value\
    as feature_stage_value


class FeatureStage(
    OktaObject
):
    """
    A class for FeatureStage objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "state" in config:
                if isinstance(config["state"],
                              feature_stage_state.FeatureStageState):
                    self.state = config["state"]
                elif config["state"] is not None:
                    self.state = feature_stage_state.FeatureStageState(
                        config["state"].upper()
                    )
                else:
                    self.state = None
            else:
                self.state = None
            if "value" in config:
                if isinstance(config["value"],
                              feature_stage_value.FeatureStageValue):
                    self.value = config["value"]
                elif config["value"] is not None:
                    self.value = feature_stage_value.FeatureStageValue(
                        config["value"].upper()
                    )
                else:
                    self.value = None
            else:
                self.value = None
        else:
            self.state = None
            self.value = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "state": self.state,
            "value": self.value
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
