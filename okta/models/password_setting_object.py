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
from okta.models import change_enum\
    as change_enum
from okta.models import seed_enum\
    as seed_enum
from okta.models import enabled_status\
    as enabled_status


class PasswordSettingObject(
    OktaObject
):
    """
    A class for PasswordSettingObject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "change" in config:
                if isinstance(config["change"],
                              change_enum.ChangeEnum):
                    self.change = config["change"]
                elif config["change"] is not None:
                    self.change = change_enum.ChangeEnum(
                        config["change"].upper()
                    )
                else:
                    self.change = None
            else:
                self.change = None
            if "seed" in config:
                if isinstance(config["seed"],
                              seed_enum.SeedEnum):
                    self.seed = config["seed"]
                elif config["seed"] is not None:
                    self.seed = seed_enum.SeedEnum(
                        config["seed"].upper()
                    )
                else:
                    self.seed = None
            else:
                self.seed = None
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
        else:
            self.change = None
            self.seed = None
            self.status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "change": self.change,
            "seed": self.seed,
            "status": self.status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
