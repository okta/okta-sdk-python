# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

class OktaCollection():
    "Class to build lists composed of OktaObject datatypes"

    @staticmethod
    def form_list(collection: list, data_type: type):
        if not collection:
            # If empty list or None
            return []
        for index in range(len(collection)):
            if not OktaCollection.is_formed(collection[index], data_type):
                collection[index] = data_type(collection[index])
        return collection

    @staticmethod
    def is_formed(value, data_type: type):
        return isinstance(value, data_type)
