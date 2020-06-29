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


class UserProfile:
    def __init__(self, config=None):
        if config:
            self.city = config["city"]
            self.cost_center = config["costCenter"]
            self.country_code = config["countryCode"]
            self.department = config["department"]
            self.display_name = config["displayName"]
            self.division = config["division"]
            self.email = config["email"]
            self.employee_number = config["employeeNumber"]
            self.first_name = config["firstName"]
            self.honorific_prefix = config["honorificPrefix"]
            self.honorific_suffix = config["honorificSuffix"]
            self.last_name = config["lastName"]
            self.locale = config["locale"]
            self.login = config["login"]
            self.manager = config["manager"]
            self.manager_id = config["managerId"]
            self.middle_name = config["middleName"]
            self.mobile_phone = config["mobilePhone"]
            self.nick_name = config["nickName"]
            self.organization = config["organization"]
            self.postal_address = config["postalAddress"]
            self.preferred_language = config["preferredLanguage"]
            self.primary_phone = config["primaryPhone"]
            self.profile_url = config["profileUrl"]
            self.second_email = config["secondEmail"]
            self.state = config["state"]
            self.street_address = config["streetAddress"]
            self.timezone = config["timezone"]
            self.title = config["title"]
            self.user_type = config["userType"]
            self.zip_code = config["zipCode"]
        else:
            self.city = None
            self.cost_center = None
            self.country_code = None
            self.department = None
            self.display_name = None
            self.division = None
            self.email = None
            self.employee_number = None
            self.first_name = None
            self.honorific_prefix = None
            self.honorific_suffix = None
            self.last_name = None
            self.locale = None
            self.login = None
            self.manager = None
            self.manager_id = None
            self.middle_name = None
            self.mobile_phone = None
            self.nick_name = None
            self.organization = None
            self.postal_address = None
            self.preferred_language = None
            self.primary_phone = None
            self.profile_url = None
            self.second_email = None
            self.state = None
            self.street_address = None
            self.timezone = None
            self.title = None
            self.user_type = None
            self.zip_code = None


# End of File Generation
