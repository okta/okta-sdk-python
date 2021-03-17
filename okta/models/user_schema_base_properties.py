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
from okta.models import user_schema_attribute\
    as user_schema_attribute


class UserSchemaBaseProperties(
    OktaObject
):
    """
    A class for UserSchemaBaseProperties objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "city" in config:
                if isinstance(config["city"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.city = config["city"]
                elif config["city"] is not None:
                    self.city = user_schema_attribute.UserSchemaAttribute(
                        config["city"]
                    )
                else:
                    self.city = None
            else:
                self.city = None
            if "costCenter" in config:
                if isinstance(config["costCenter"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.cost_center = config["costCenter"]
                elif config["costCenter"] is not None:
                    self.cost_center = user_schema_attribute.UserSchemaAttribute(
                        config["costCenter"]
                    )
                else:
                    self.cost_center = None
            else:
                self.cost_center = None
            if "countryCode" in config:
                if isinstance(config["countryCode"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.country_code = config["countryCode"]
                elif config["countryCode"] is not None:
                    self.country_code = user_schema_attribute.UserSchemaAttribute(
                        config["countryCode"]
                    )
                else:
                    self.country_code = None
            else:
                self.country_code = None
            if "department" in config:
                if isinstance(config["department"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.department = config["department"]
                elif config["department"] is not None:
                    self.department = user_schema_attribute.UserSchemaAttribute(
                        config["department"]
                    )
                else:
                    self.department = None
            else:
                self.department = None
            if "displayName" in config:
                if isinstance(config["displayName"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.display_name = config["displayName"]
                elif config["displayName"] is not None:
                    self.display_name = user_schema_attribute.UserSchemaAttribute(
                        config["displayName"]
                    )
                else:
                    self.display_name = None
            else:
                self.display_name = None
            if "division" in config:
                if isinstance(config["division"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.division = config["division"]
                elif config["division"] is not None:
                    self.division = user_schema_attribute.UserSchemaAttribute(
                        config["division"]
                    )
                else:
                    self.division = None
            else:
                self.division = None
            if "email" in config:
                if isinstance(config["email"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.email = config["email"]
                elif config["email"] is not None:
                    self.email = user_schema_attribute.UserSchemaAttribute(
                        config["email"]
                    )
                else:
                    self.email = None
            else:
                self.email = None
            if "employeeNumber" in config:
                if isinstance(config["employeeNumber"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.employee_number = config["employeeNumber"]
                elif config["employeeNumber"] is not None:
                    self.employee_number = user_schema_attribute.UserSchemaAttribute(
                        config["employeeNumber"]
                    )
                else:
                    self.employee_number = None
            else:
                self.employee_number = None
            if "firstName" in config:
                if isinstance(config["firstName"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.first_name = config["firstName"]
                elif config["firstName"] is not None:
                    self.first_name = user_schema_attribute.UserSchemaAttribute(
                        config["firstName"]
                    )
                else:
                    self.first_name = None
            else:
                self.first_name = None
            if "honorificPrefix" in config:
                if isinstance(config["honorificPrefix"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.honorific_prefix = config["honorificPrefix"]
                elif config["honorificPrefix"] is not None:
                    self.honorific_prefix = user_schema_attribute.UserSchemaAttribute(
                        config["honorificPrefix"]
                    )
                else:
                    self.honorific_prefix = None
            else:
                self.honorific_prefix = None
            if "honorificSuffix" in config:
                if isinstance(config["honorificSuffix"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.honorific_suffix = config["honorificSuffix"]
                elif config["honorificSuffix"] is not None:
                    self.honorific_suffix = user_schema_attribute.UserSchemaAttribute(
                        config["honorificSuffix"]
                    )
                else:
                    self.honorific_suffix = None
            else:
                self.honorific_suffix = None
            if "lastName" in config:
                if isinstance(config["lastName"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.last_name = config["lastName"]
                elif config["lastName"] is not None:
                    self.last_name = user_schema_attribute.UserSchemaAttribute(
                        config["lastName"]
                    )
                else:
                    self.last_name = None
            else:
                self.last_name = None
            if "locale" in config:
                if isinstance(config["locale"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.locale = config["locale"]
                elif config["locale"] is not None:
                    self.locale = user_schema_attribute.UserSchemaAttribute(
                        config["locale"]
                    )
                else:
                    self.locale = None
            else:
                self.locale = None
            if "login" in config:
                if isinstance(config["login"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.login = config["login"]
                elif config["login"] is not None:
                    self.login = user_schema_attribute.UserSchemaAttribute(
                        config["login"]
                    )
                else:
                    self.login = None
            else:
                self.login = None
            if "manager" in config:
                if isinstance(config["manager"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.manager = config["manager"]
                elif config["manager"] is not None:
                    self.manager = user_schema_attribute.UserSchemaAttribute(
                        config["manager"]
                    )
                else:
                    self.manager = None
            else:
                self.manager = None
            if "managerId" in config:
                if isinstance(config["managerId"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.manager_id = config["managerId"]
                elif config["managerId"] is not None:
                    self.manager_id = user_schema_attribute.UserSchemaAttribute(
                        config["managerId"]
                    )
                else:
                    self.manager_id = None
            else:
                self.manager_id = None
            if "middleName" in config:
                if isinstance(config["middleName"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.middle_name = config["middleName"]
                elif config["middleName"] is not None:
                    self.middle_name = user_schema_attribute.UserSchemaAttribute(
                        config["middleName"]
                    )
                else:
                    self.middle_name = None
            else:
                self.middle_name = None
            if "mobilePhone" in config:
                if isinstance(config["mobilePhone"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.mobile_phone = config["mobilePhone"]
                elif config["mobilePhone"] is not None:
                    self.mobile_phone = user_schema_attribute.UserSchemaAttribute(
                        config["mobilePhone"]
                    )
                else:
                    self.mobile_phone = None
            else:
                self.mobile_phone = None
            if "nickName" in config:
                if isinstance(config["nickName"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.nick_name = config["nickName"]
                elif config["nickName"] is not None:
                    self.nick_name = user_schema_attribute.UserSchemaAttribute(
                        config["nickName"]
                    )
                else:
                    self.nick_name = None
            else:
                self.nick_name = None
            if "organization" in config:
                if isinstance(config["organization"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.organization = config["organization"]
                elif config["organization"] is not None:
                    self.organization = user_schema_attribute.UserSchemaAttribute(
                        config["organization"]
                    )
                else:
                    self.organization = None
            else:
                self.organization = None
            if "postalAddress" in config:
                if isinstance(config["postalAddress"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.postal_address = config["postalAddress"]
                elif config["postalAddress"] is not None:
                    self.postal_address = user_schema_attribute.UserSchemaAttribute(
                        config["postalAddress"]
                    )
                else:
                    self.postal_address = None
            else:
                self.postal_address = None
            if "preferredLanguage" in config:
                if isinstance(config["preferredLanguage"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.preferred_language = config["preferredLanguage"]
                elif config["preferredLanguage"] is not None:
                    self.preferred_language = user_schema_attribute.UserSchemaAttribute(
                        config["preferredLanguage"]
                    )
                else:
                    self.preferred_language = None
            else:
                self.preferred_language = None
            if "primaryPhone" in config:
                if isinstance(config["primaryPhone"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.primary_phone = config["primaryPhone"]
                elif config["primaryPhone"] is not None:
                    self.primary_phone = user_schema_attribute.UserSchemaAttribute(
                        config["primaryPhone"]
                    )
                else:
                    self.primary_phone = None
            else:
                self.primary_phone = None
            if "profileUrl" in config:
                if isinstance(config["profileUrl"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.profile_url = config["profileUrl"]
                elif config["profileUrl"] is not None:
                    self.profile_url = user_schema_attribute.UserSchemaAttribute(
                        config["profileUrl"]
                    )
                else:
                    self.profile_url = None
            else:
                self.profile_url = None
            if "secondEmail" in config:
                if isinstance(config["secondEmail"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.second_email = config["secondEmail"]
                elif config["secondEmail"] is not None:
                    self.second_email = user_schema_attribute.UserSchemaAttribute(
                        config["secondEmail"]
                    )
                else:
                    self.second_email = None
            else:
                self.second_email = None
            if "state" in config:
                if isinstance(config["state"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.state = config["state"]
                elif config["state"] is not None:
                    self.state = user_schema_attribute.UserSchemaAttribute(
                        config["state"]
                    )
                else:
                    self.state = None
            else:
                self.state = None
            if "streetAddress" in config:
                if isinstance(config["streetAddress"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.street_address = config["streetAddress"]
                elif config["streetAddress"] is not None:
                    self.street_address = user_schema_attribute.UserSchemaAttribute(
                        config["streetAddress"]
                    )
                else:
                    self.street_address = None
            else:
                self.street_address = None
            if "timezone" in config:
                if isinstance(config["timezone"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.timezone = config["timezone"]
                elif config["timezone"] is not None:
                    self.timezone = user_schema_attribute.UserSchemaAttribute(
                        config["timezone"]
                    )
                else:
                    self.timezone = None
            else:
                self.timezone = None
            if "title" in config:
                if isinstance(config["title"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.title = config["title"]
                elif config["title"] is not None:
                    self.title = user_schema_attribute.UserSchemaAttribute(
                        config["title"]
                    )
                else:
                    self.title = None
            else:
                self.title = None
            if "userType" in config:
                if isinstance(config["userType"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.user_type = config["userType"]
                elif config["userType"] is not None:
                    self.user_type = user_schema_attribute.UserSchemaAttribute(
                        config["userType"]
                    )
                else:
                    self.user_type = None
            else:
                self.user_type = None
            if "zipCode" in config:
                if isinstance(config["zipCode"],
                              user_schema_attribute.UserSchemaAttribute):
                    self.zip_code = config["zipCode"]
                elif config["zipCode"] is not None:
                    self.zip_code = user_schema_attribute.UserSchemaAttribute(
                        config["zipCode"]
                    )
                else:
                    self.zip_code = None
            else:
                self.zip_code = None
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
        parent_req_format.update(current_obj_format)
        return parent_req_format
