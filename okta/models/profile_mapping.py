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
from okta.models import profile_mapping_source\
    as profile_mapping_source


class ProfileMapping(
    OktaObject
):
    """
    A class for ProfileMapping objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.properties = config["properties"]\
                if "properties" in config else None
            if "source" in config:
                if isinstance(config["source"],
                              profile_mapping_source.ProfileMappingSource):
                    self.source = config["source"]
                elif config["source"] is not None:
                    self.source = profile_mapping_source.ProfileMappingSource(
                        config["source"]
                    )
                else:
                    self.source = None
            else:
                self.source = None
            if "target" in config:
                if isinstance(config["target"],
                              profile_mapping_source.ProfileMappingSource):
                    self.target = config["target"]
                elif config["target"] is not None:
                    self.target = profile_mapping_source.ProfileMappingSource(
                        config["target"]
                    )
                else:
                    self.target = None
            else:
                self.target = None
        else:
            self.links = None
            self.id = None
            self.properties = None
            self.source = None
            self.target = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "id": self.id,
            "properties": self.properties,
            "source": self.source,
            "target": self.target
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
