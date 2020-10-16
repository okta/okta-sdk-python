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


class CsrMetadataSubject(
    OktaObject
):
    """
    A class for CsrMetadataSubject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.common_name = config["commonName"]\
                if "commonName" in config else None
            self.country_name = config["countryName"]\
                if "countryName" in config else None
            self.locality_name = config["localityName"]\
                if "localityName" in config else None
            self.organization_name = config["organizationName"]\
                if "organizationName" in config else None
            self.organizational_unit_name = config["organizationalUnitName"]\
                if "organizationalUnitName" in config else None
            self.state_or_province_name = config["stateOrProvinceName"]\
                if "stateOrProvinceName" in config else None
        else:
            self.common_name = None
            self.country_name = None
            self.locality_name = None
            self.organization_name = None
            self.organizational_unit_name = None
            self.state_or_province_name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "commonName": self.common_name,
            "countryName": self.country_name,
            "localityName": self.locality_name,
            "organizationName": self.organization_name,
            "organizationalUnitName": self.organizational_unit_name,
            "stateOrProvinceName": self.state_or_province_name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
