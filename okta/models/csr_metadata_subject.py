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


from urllib.parse import urlencode


class CsrMetadataSubject:
    def __init__(self, config=None):
        if config:
            self.common_name = config["commonName"]
            self.country_name = config["countryName"]
            self.locality_name = config["localityName"]
            self.organization_name = config["organizationName"]
            self.organizational_unit_name = config["organizationalUnitName"]
            self.state_or_province_name = config["stateOrProvinceName"]
        else:
            self.common_name = None
            self.country_name = None
            self.locality_name = None
            self.organization_name = None
            self.organizational_unit_name = None
            self.state_or_province_name = None


# End of File Generation
