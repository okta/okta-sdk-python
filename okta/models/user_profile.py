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


class UserProfile(
    OktaObject
):
    """
    A class for UserProfile objects.
    """

    BASIC_ATTRIBUTES = (
        "city",
        "costCenter",
        "countryCode",
        "department",
        "displayName",
        "division",
        "email",
        "employeeNumber",
        "firstName",
        "honorificPrefix",
        "honorificSuffix",
        "lastName",
        "locale",
        "login",
        "manager",
        "managerId",
        "middleName",
        "mobilePhone",
        "nickName",
        "organization",
        "postalAddress",
        "preferredLanguage",
        "primaryPhone",
        "profileUrl",
        "secondEmail",
        "state",
        "streetAddress",
        "timezone",
        "title",
        "userType",
        "zipCode",
    )

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.city = config["city"]\
                if "city" in config else None
            self.cost_center = config["costCenter"]\
                if "costCenter" in config else None
            self.country_code = config["countryCode"]\
                if "countryCode" in config else None
            self.department = config["department"]\
                if "department" in config else None
            self.display_name = config["displayName"]\
                if "displayName" in config else None
            self.division = config["division"]\
                if "division" in config else None
            self.email = config["email"]\
                if "email" in config else None
            self.employee_number = config["employeeNumber"]\
                if "employeeNumber" in config else None
            self.first_name = config["firstName"]\
                if "firstName" in config else None
            self.honorific_prefix = config["honorificPrefix"]\
                if "honorificPrefix" in config else None
            self.honorific_suffix = config["honorificSuffix"]\
                if "honorificSuffix" in config else None
            self.last_name = config["lastName"]\
                if "lastName" in config else None
            self.locale = config["locale"]\
                if "locale" in config else None
            self.login = config["login"]\
                if "login" in config else None
            self.manager = config["manager"]\
                if "manager" in config else None
            self.manager_id = config["managerId"]\
                if "managerId" in config else None
            self.middle_name = config["middleName"]\
                if "middleName" in config else None
            self.mobile_phone = config["mobilePhone"]\
                if "mobilePhone" in config else None
            self.nick_name = config["nickName"]\
                if "nickName" in config else None
            self.organization = config["organization"]\
                if "organization" in config else None
            self.postal_address = config["postalAddress"]\
                if "postalAddress" in config else None
            self.preferred_language = config["preferredLanguage"]\
                if "preferredLanguage" in config else None
            self.primary_phone = config["primaryPhone"]\
                if "primaryPhone" in config else None
            self.profile_url = config["profileUrl"]\
                if "profileUrl" in config else None
            self.second_email = config["secondEmail"]\
                if "secondEmail" in config else None
            self.state = config["state"]\
                if "state" in config else None
            self.street_address = config["streetAddress"]\
                if "streetAddress" in config else None
            self.timezone = config["timezone"]\
                if "timezone" in config else None
            self.title = config["title"]\
                if "title" in config else None
            self.user_type = config["userType"]\
                if "userType" in config else None
            self.zip_code = config["zipCode"]\
                if "zipCode" in config else None
            # set custom attributes not defined in model, do not change string case
            for attr_name in config:
                lower_camel_case = to_lower_camel_case(attr_name)
                if lower_camel_case not in UserProfile.BASIC_ATTRIBUTES:
                    setattr(self, attr_name, config[attr_name])
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

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "city": self.city,
            "costCenter": self.cost_center,
            "countryCode": self.country_code,
            "department": self.department,
            "displayName": self.display_name,
            "division": self.division,
            "email": self.email,
            "employeeNumber": self.employee_number,
            "firstName": self.first_name,
            "honorificPrefix": self.honorific_prefix,
            "honorificSuffix": self.honorific_suffix,
            "lastName": self.last_name,
            "locale": self.locale,
            "login": self.login,
            "manager": self.manager,
            "managerId": self.manager_id,
            "middleName": self.middle_name,
            "mobilePhone": self.mobile_phone,
            "nickName": self.nick_name,
            "organization": self.organization,
            "postalAddress": self.postal_address,
            "preferredLanguage": self.preferred_language,
            "primaryPhone": self.primary_phone,
            "profileUrl": self.profile_url,
            "secondEmail": self.second_email,
            "state": self.state,
            "streetAddress": self.street_address,
            "timezone": self.timezone,
            "title": self.title,
            "userType": self.user_type,
            "zipCode": self.zip_code
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
        raise AttributeError(f"'UserProfile' object has no attribute '{attr_name}'")

    def __setattr__(self, attr_name, attr_value):
        """
        Keep custom attributes unchanged and keep backward compatibility for basic attributes.
        """
        lower_camel_case = to_lower_camel_case(attr_name)
        if lower_camel_case in UserProfile.BASIC_ATTRIBUTES:
            super(UserProfile, self).__setattr__(lower_camel_case, attr_value)
        else:
            super(UserProfile, self).__setattr__(attr_name, attr_value)
