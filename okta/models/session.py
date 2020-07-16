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
from okta.models.session_identity_provider\
    import SessionIdentityProvider
from okta.models.session_status\
    import SessionStatus


class Session(
    OktaObject
):
    """
    A class for Session objects.
    """

    def __init__(self, config=None):
        if config:
            self.links = config["_links"]\
                if "_links" in config else None
            self.amr = config["amr"]\
                if "amr" in config else None
            self.created_at = config["createdAt"]\
                if "createdAt" in config else None
            self.expires_at = config["expiresAt"]\
                if "expiresAt" in config else None
            self.id = config["id"]\
                if "id" in config else None
            if "idp" in config:
                if isinstance(config["idp"],
                              SessionIdentityProvider):
                    self.idp = config["idp"]
                else:
                    self.idp = SessionIdentityProvider(
                        config["idp"]
                    )
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
                              SessionStatus):
                    self.status = config["status"]
                else:
                    self.status = SessionStatus(
                        config["status"]
                    )
            else:
                self.status = None
            self.user_id = config["userId"]\
                if "userId" in config else None
        else:
            self.links = None
            self.amr = None
            self.created_at = None
            self.expires_at = None
            self.id = None
            self.idp = None
            self.last_factor_verification = None
            self.last_password_verification = None
            self.login = None
            self.status = None
            self.user_id = None
