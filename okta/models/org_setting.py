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


class OrgSetting(
    OktaObject
):
    """
    A class for OrgSetting objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.address_1 = config["address1"]\
                if "address1" in config else None
            self.address_2 = config["address2"]\
                if "address2" in config else None
            self.city = config["city"]\
                if "city" in config else None
            self.company_name = config["companyName"]\
                if "companyName" in config else None
            self.country = config["country"]\
                if "country" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.end_user_support_help_url = config["endUserSupportHelpUrl"]\
                if "endUserSupportHelpUrl" in config else None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.phone_number = config["phoneNumber"]\
                if "phoneNumber" in config else None
            self.postal_code = config["postalCode"]\
                if "postalCode" in config else None
            self.state = config["state"]\
                if "state" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.subdomain = config["subdomain"]\
                if "subdomain" in config else None
            self.support_phone_number = config["supportPhoneNumber"]\
                if "supportPhoneNumber" in config else None
            self.website = config["website"]\
                if "website" in config else None
        else:
            self.links = None
            self.address_1 = None
            self.address_2 = None
            self.city = None
            self.company_name = None
            self.country = None
            self.created = None
            self.end_user_support_help_url = None
            self.expires_at = None
            self.id = None
            self.last_updated = None
            self.phone_number = None
            self.postal_code = None
            self.state = None
            self.status = None
            self.subdomain = None
            self.support_phone_number = None
            self.website = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "address1": self.address_1,
            "address2": self.address_2,
            "city": self.city,
            "companyName": self.company_name,
            "country": self.country,
            "created": self.created,
            "endUserSupportHelpURL": self.end_user_support_help_url,
            "expiresAt": self.expires_at,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "phoneNumber": self.phone_number,
            "postalCode": self.postal_code,
            "state": self.state,
            "status": self.status,
            "subdomain": self.subdomain,
            "supportPhoneNumber": self.support_phone_number,
            "website": self.website
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
