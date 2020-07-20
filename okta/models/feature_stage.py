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
from okta.models.feature_stage_state\
    import FeatureStageState
from okta.models.feature_stage_value\
    import FeatureStageValue


class FeatureStage(
    OktaObject
):
    """
    A class for FeatureStage objects.
    """

    def __init__(self, config=None):
        if config:
            if "state" in config:
                if isinstance(config["state"],
                              FeatureStageState):
                    self.state = config["state"]
                else:
                    self.state = FeatureStageState(
                        config["state"]
                    )
            else:
                self.state = None
            if "value" in config:
                if isinstance(config["value"],
                              FeatureStageValue):
                    self.value = config["value"]
                else:
                    self.value = FeatureStageValue(
                        config["value"]
                    )
            else:
                self.value = None
        else:
            self.state = None
            self.value = None

    def request_format(self):
        return {
            "state": self.state,
            "value": self.value
        }
