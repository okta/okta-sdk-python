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

from okta.helpers import to_snake_case, to_lower_camel_case


class GroupProfile(
    OktaObject
):
    """
    A class for GroupProfile objects.
    """

    BASIC_ATTRIBUTES = (
        "description",
        "name",
    )

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.description = config["description"]\
                if "description" in config else None
            self.name = config["name"]\
                if "name" in config else None
            # set custom attributes not defined in model, do not change string case
            for attr_name in config:
                lower_camel_case = to_lower_camel_case(attr_name)
                if lower_camel_case not in GroupProfile.BASIC_ATTRIBUTES:
                    setattr(self, attr_name, config[attr_name])
        else:
            self.description = None
            self.name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "description": self.description,
            "name": self.name
        }
        available_attrs = vars(self)
        for attr in available_attrs:
            # do not allow overriding of base attributes
            if not attr in current_obj_format:
                current_obj_format[attr] = getattr(self, attr)
        parent_req_format.update(current_obj_format)
        return parent_req_format

    def __getattr__(self, attr_name):
        """
        Try different cases for backward compatibility.
        """
        available_attrs = vars(self)
        snake_case = to_snake_case(attr_name)
        if snake_case in available_attrs:
            return available_attrs[snake_case]
        lower_camel_case = to_lower_camel_case(attr_name)
        if lower_camel_case in available_attrs:
            return available_attrs[lower_camel_case]
        raise AttributeError(f"'GroupProfile' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, attr_value):
        """
        Keep custom attributes unchanged and keep backward compatibility for basic attributes.
        """
        lower_camel_case = to_lower_camel_case(attr_name)
        if lower_camel_case in GroupProfile.BASIC_ATTRIBUTES:
            super(GroupProfile, self).__setattr__(lower_camel_case, attr_value)
        else:
            super(GroupProfile, self).__setattr__(attr_name, attr_value)
