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
from okta.models.o_auth_2_actor\
    import OAuth2Actor
from okta.models.o_auth_2_scope_consent_grant_source\
    import OAuth2ScopeConsentGrantSource
from okta.models.o_auth_2_scope_consent_grant_status\
    import OAuth2ScopeConsentGrantStatus


class OAuth2ScopeConsentGrant(
    OktaObject
):
    """
    A class for OAuth2ScopeConsentGrant objects.
    """

    def __init__(self, config=None):
        if config:
            self.embedded = config["_embedded"]\
                if "_embedded" in config else None
            self.links = config["_links"]\
                if "_links" in config else None
            self.client_id = config["clientId"]\
                if "clientId" in config else None
            self.created = config["created"]\
                if "created" in config else None
            if "createdBy" in config:
                if isinstance(config["createdBy"],
                              OAuth2Actor):
                    self.created_by = config["createdBy"]
                else:
                    self.created_by = OAuth2Actor(
                        config["createdBy"]
                    )
            else:
                self.created_by = None
            self.id = config["id"]\
                if "id" in config else None
            self.issuer = config["issuer"]\
                if "issuer" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.scope_id = config["scopeId"]\
                if "scopeId" in config else None
            if "source" in config:
                if isinstance(config["source"],
                              OAuth2ScopeConsentGrantSource):
                    self.source = config["source"]
                else:
                    self.source = OAuth2ScopeConsentGrantSource(
                        config["source"]
                    )
            else:
                self.source = None
            if "status" in config:
                if isinstance(config["status"],
                              OAuth2ScopeConsentGrantStatus):
                    self.status = config["status"]
                else:
                    self.status = OAuth2ScopeConsentGrantStatus(
                        config["status"]
                    )
            else:
                self.status = None
            self.user_id = config["userId"]\
                if "userId" in config else None
        else:
            self.embedded = None
            self.links = None
            self.client_id = None
            self.created = None
            self.created_by = None
            self.id = None
            self.issuer = None
            self.last_updated = None
            self.scope_id = None
            self.source = None
            self.status = None
            self.user_id = None
