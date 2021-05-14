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
from okta.okta_collection import OktaCollection
from okta.models import session_authentication_method\
    as session_authentication_method
from okta.models import session_identity_provider\
    as session_identity_provider
from okta.models import session_status\
    as session_status


class Session(
    OktaObject
):
    """
    A class for Session objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.amr = OktaCollection.form_list(
                config["amr"] if "amr"\
                    in config else [],
                session_authentication_method.SessionAuthenticationMethod
            )
            self.created_at = config["createdAt"]\
                if "createdAt" in config else None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.id = config["id"]\
                if "id" in config else None
            if "idp" in config:
                if isinstance(config["idp"],
                              session_identity_provider.SessionIdentityProvider):
                    self.idp = config["idp"]
                elif config["idp"] is not None:
                    self.idp = session_identity_provider.SessionIdentityProvider(
                        config["idp"]
                    )
                else:
                    self.idp = None
            else:
                self.idp = None
            self.last_factor_verification = config["lastFactorVerification"]\
                if "lastFactorVerification" in config else None
            self.last_password_verification = config["lastPasswordVerification"]\
                if "lastPasswordVerification" in config else None
            self.login = config["login"]\
                if "login" in config else None
            if "status" in config:
                if isinstance(config["status"],
                              session_status.SessionStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = session_status.SessionStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            self.user_id = config["userId"]\
                if "userId" in config else None
        else:
            self.links = None
            self.amr = []
            self.created_at = None
            self.expires_at = None
            self.id = None
            self.idp = None
            self.last_factor_verification = None
            self.last_password_verification = None
            self.login = None
            self.status = None
            self.user_id = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "amr": self.amr,
            "createdAt": self.created_at,
            "expiresAt": self.expires_at,
            "id": self.id,
            "idp": self.idp,
            "lastFactorVerification": self.last_factor_verification,
            "lastPasswordVerification": self.last_password_verification,
            "login": self.login,
            "status": self.status,
            "userId": self.user_id
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
