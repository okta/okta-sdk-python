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
from okta.models import authenticator_provider\
    as authenticator_provider
from okta.models import authenticator_settings\
    as authenticator_settings
from okta.models import authenticator_status\
    as authenticator_status
from okta.models import authenticator_type\
    as authenticator_type


class Authenticator(
    OktaObject
):
    """
    A class for Authenticator objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "_links" in config:
                self.links = config["_links"]
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.key = config["key"]\
                if "key" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "provider" in config:
                if isinstance(config["provider"],
                              authenticator_provider.AuthenticatorProvider):
                    self.provider = config["provider"]
                elif config["provider"] is not None:
                    self.provider = authenticator_provider.AuthenticatorProvider(
                        config["provider"]
                    )
                else:
                    self.provider = None
            else:
                self.provider = None
            if "settings" in config:
                if isinstance(config["settings"],
                              authenticator_settings.AuthenticatorSettings):
                    self.settings = config["settings"]
                elif config["settings"] is not None:
                    self.settings = authenticator_settings.AuthenticatorSettings(
                        config["settings"]
                    )
                else:
                    self.settings = None
            else:
                self.settings = None
            if "status" in config:
                if isinstance(config["status"],
                              authenticator_status.AuthenticatorStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = authenticator_status.AuthenticatorStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            if "type" in config:
                if isinstance(config["type"],
                              authenticator_type.AuthenticatorType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = authenticator_type.AuthenticatorType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
        else:
            self.links = None
            self.created = None
            self.id = None
            self.key = None
            self.last_updated = None
            self.name = None
            self.provider = None
            self.settings = None
            self.status = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "created": self.created,
            "id": self.id,
            "key": self.key,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "provider": self.provider,
            "settings": self.settings,
            "status": self.status,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
