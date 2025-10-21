# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

from aenum import MultiValueEnum


class OktaObject:
    """
    Base object for all Okta datatypes
    """

    def __init__(self, config=None):
        pass

    def __repr__(self):
        return str(vars(self))

    def as_dict(self):
        """
        Returns dictionary object of
        {{pascalCase model.modelName}} object.
        """
        result = {}
        for key, val in self.request_format().items():
            if val is None:
                continue
            if isinstance(val, list):
                formatted_list = []
                for item in val:
                    if isinstance(item, OktaObject):
                        formatted_list.append(item.as_dict())
                    else:
                        formatted_list.append(item)
                result[key] = formatted_list
            elif not isinstance(val, OktaObject):
                result[key] = val
            elif issubclass(type(val), MultiValueEnum):
                result[key] = val.value
            else:
                result[key] = val.as_dict()
        return result

    def request_format(self):
        return {}
