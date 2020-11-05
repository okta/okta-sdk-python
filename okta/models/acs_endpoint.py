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


class AcsEndpoint(
    OktaObject
):
    """
    A class for AcsEndpoint objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.index = config["index"]\
                if "index" in config else None
            self.url = config["url"]\
                if "url" in config else None
        else:
            self.index = None
            self.url = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "index": self.index,
            "url": self.url
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
