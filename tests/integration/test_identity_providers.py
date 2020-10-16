import pytest
from tests.mocks import MockOktaClient
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError
import okta.models as models


class TestIdentityProvidersResource:
    """
    Integration Tests for the Identity Providers Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_add_get_generic_idp(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        ISSUER_URL = "https://idp.example.com"
        idp_model = models.IdentityProvider({
            "type": "OIDC",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} generic",
            "protocol": models.Protocol({
                "algorithms": models.ProtocolAlgorithms({
                    "request": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "REQUEST"
                        })
                    }),
                    "response": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "ANY"
                        })
                    })
                }),
                "endpoints": models.ProtocolEndpoints({
                    "acs": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "type": "INSTANCE"
                    }),
                    "authorization": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/authorize"
                    }),
                    "token": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "url": ISSUER_URL + "/token"
                    }),
                    "userInfo": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/userinfo"
                    }),
                    "jwks": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/keys"
                    })
                }),
                "scopes": ["openid", "profile", "email"],
                "type": "OIDC",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                }),
                "issuer": models.ProtocolEndpoint({
                    "url": ISSUER_URL
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.name == idp_model.name
        assert retrieved_idp.type == idp_model.type
        assert retrieved_idp.status == "ACTIVE"
        prot_endp = retrieved_idp.protocol.endpoints
        assert prot_endp.authorization.url == ISSUER_URL + "/authorize"
        assert prot_endp.authorization.binding == "HTTP-REDIRECT"
        assert prot_endp.token.url == ISSUER_URL + "/token"
        assert prot_endp.token.binding == "HTTP-POST"
        assert prot_endp.user_info.url == ISSUER_URL + "/userinfo"
        assert prot_endp.user_info.binding == "HTTP-REDIRECT"
        assert prot_endp.jwks.url == ISSUER_URL + "/keys"
        assert prot_endp.jwks.binding == "HTTP-REDIRECT"
        assert set(retrieved_idp.protocol.scopes) == set(
            idp_model.protocol.scopes)
        assert retrieved_idp.protocol.issuer.url == ISSUER_URL
        assert retrieved_idp.protocol.credentials.client.client_id ==\
            "your-client-id"
        assert retrieved_idp.protocol.credentials.client.client_secret ==\
            "your-client-secret"
        prov = retrieved_idp.policy.provisioning
        assert prov.action == "AUTO"
        assert prov.profile_master is False
        assert prov.groups.action == "NONE"
        assert prov.conditions.deprovisioned.action == "NONE"
        assert prov.conditions.suspended.action == "NONE"
        assert retrieved_idp.policy.account_link.action == "AUTO"
        subj = retrieved_idp.policy.subject
        assert subj.user_name_template.template == "idpuser.email"
        assert subj.filter is None
        assert subj.match_type == models.PolicySubjectMatchType.USERNAME
        assert subj.match_attribute is None

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_add_get_facebook_idp(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        idp_model = models.IdentityProvider({
            "type": "FACEBOOK",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["public_profile", "email"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.name == idp_model.name
        assert retrieved_idp.type == idp_model.type
        assert retrieved_idp.status == "ACTIVE"
        assert set(retrieved_idp.protocol.scopes) == set(
            idp_model.protocol.scopes)
        assert retrieved_idp.protocol.credentials.client.client_id ==\
            "your-client-id"
        assert retrieved_idp.protocol.credentials.client.client_secret ==\
            "your-client-secret"
        prov = retrieved_idp.policy.provisioning
        assert prov.action == "AUTO"
        assert prov.profile_master is True
        assert prov.groups.action == "NONE"
        assert prov.conditions.deprovisioned.action == "NONE"
        assert prov.conditions.suspended.action == "NONE"
        assert retrieved_idp.policy.account_link.action == "AUTO"
        subj = retrieved_idp.policy.subject
        assert subj.user_name_template.template == "idpuser.email"
        assert subj.filter is None
        assert subj.match_type == models.PolicySubjectMatchType.USERNAME

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_add_get_linkedin_idp(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        idp_model = models.IdentityProvider({
            "type": "LINKEDIN",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["r_basicprofile", "r_emailaddress"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.name == idp_model.name
        assert retrieved_idp.type == idp_model.type
        assert retrieved_idp.status == "ACTIVE"
        assert set(retrieved_idp.protocol.scopes) == set(
            idp_model.protocol.scopes)
        assert retrieved_idp.protocol.credentials.client.client_id ==\
            "your-client-id"
        assert retrieved_idp.protocol.credentials.client.client_secret ==\
            "your-client-secret"
        prov = retrieved_idp.policy.provisioning
        assert prov.action == "AUTO"
        assert prov.profile_master is True
        assert prov.groups.action == "NONE"
        assert prov.conditions.deprovisioned.action == "NONE"
        assert prov.conditions.suspended.action == "NONE"
        assert retrieved_idp.policy.account_link.action == "AUTO"
        subj = retrieved_idp.policy.subject
        assert subj.user_name_template.template == "idpuser.email"
        assert subj.filter is None
        assert subj.match_type == models.PolicySubjectMatchType.USERNAME

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_idps(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        ISSUER_URL = "https://idp.example.com"
        idp_model = models.IdentityProvider({
            "type": "OIDC",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} generic",
            "protocol": models.Protocol({
                "algorithms": models.ProtocolAlgorithms({
                    "request": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "REQUEST"
                        })
                    }),
                    "response": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "ANY"
                        })
                    })
                }),
                "endpoints": models.ProtocolEndpoints({
                    "acs": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "type": "INSTANCE"
                    }),
                    "authorization": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/authorize"
                    }),
                    "token": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "url": ISSUER_URL + "/token"
                    }),
                    "userInfo": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/userinfo"
                    }),
                    "jwks": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/keys"
                    })
                }),
                "scopes": ["openid", "profile", "email"],
                "type": "OIDC",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                }),
                "issuer": models.ProtocolEndpoint({
                    "url": ISSUER_URL
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # List IDPs
        idp_list, _, err = await client.list_identity_providers()
        assert err is None
        assert isinstance(idp_list, list)
        assert next((idp for idp in idp_list
                     if idp.id == created_idp.id), None) is not None

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_deactivate_idp(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        ISSUER_URL = "https://idp.example.com"
        idp_model = models.IdentityProvider({
            "type": "OIDC",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} generic",
            "protocol": models.Protocol({
                "algorithms": models.ProtocolAlgorithms({
                    "request": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "REQUEST"
                        })
                    }),
                    "response": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "ANY"
                        })
                    })
                }),
                "endpoints": models.ProtocolEndpoints({
                    "acs": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "type": "INSTANCE"
                    }),
                    "authorization": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/authorize"
                    }),
                    "token": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "url": ISSUER_URL + "/token"
                    }),
                    "userInfo": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/userinfo"
                    }),
                    "jwks": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/keys"
                    })
                }),
                "scopes": ["openid", "profile", "email"],
                "type": "OIDC",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                }),
                "issuer": models.ProtocolEndpoint({
                    "url": ISSUER_URL
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.status == "ACTIVE"

        # Deactivate
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.status == "INACTIVE"

        # Reactivate
        reactivated_idp, _, err = await \
            client.activate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(reactivated_idp, models.IdentityProvider)

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.status == "ACTIVE"

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_idp(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        ISSUER_URL = "https://idp.example.com"
        idp_model = models.IdentityProvider({
            "type": "OIDC",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} generic",
            "protocol": models.Protocol({
                "algorithms": models.ProtocolAlgorithms({
                    "request": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "REQUEST"
                        })
                    }),
                    "response": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "ANY"
                        })
                    })
                }),
                "endpoints": models.ProtocolEndpoints({
                    "acs": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "type": "INSTANCE"
                    }),
                    "authorization": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/authorize"
                    }),
                    "token": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "url": ISSUER_URL + "/token"
                    }),
                    "userInfo": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/userinfo"
                    }),
                    "jwks": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/keys"
                    })
                }),
                "scopes": ["openid", "profile", "email"],
                "type": "OIDC",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                }),
                "issuer": models.ProtocolEndpoint({
                    "url": ISSUER_URL
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.status == "ACTIVE"

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

        # Retrieve for verification
        retrieved_idp, resp, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_idp is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_idp(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        ISSUER_URL = "https://idp.example.com"
        idp_model = models.IdentityProvider({
            "type": "OIDC",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} generic",
            "protocol": models.Protocol({
                "algorithms": models.ProtocolAlgorithms({
                    "request": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "REQUEST"
                        })
                    }),
                    "response": models.ProtocolAlgorithmType({
                        "signature": models.ProtocolAlgorithmTypeSignature({
                            "algorithm": "SHA-256",
                            "scope": "ANY"
                        })
                    })
                }),
                "endpoints": models.ProtocolEndpoints({
                    "acs": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "type": "INSTANCE"
                    }),
                    "authorization": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/authorize"
                    }),
                    "token": models.ProtocolEndpoint({
                        "binding": "HTTP-POST",
                        "url": ISSUER_URL + "/token"
                    }),
                    "userInfo": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/userinfo"
                    }),
                    "jwks": models.ProtocolEndpoint({
                        "binding": "HTTP-REDIRECT",
                        "url": ISSUER_URL + "/keys"
                    })
                }),
                "scopes": ["openid", "profile", "email"],
                "type": "OIDC",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                }),
                "issuer": models.ProtocolEndpoint({
                    "url": ISSUER_URL
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.status == "ACTIVE"

        # Update
        created_idp.name = created_idp.name + "UPDATE"
        updated_idp, _, err = await \
            client.update_identity_provider(created_idp.id, created_idp)
        assert err is None
        assert isinstance(updated_idp, models.IdentityProvider)
        assert updated_idp.id == created_idp.id
        assert updated_idp.name != idp_model.name

        # Retrieve for verification
        retrieved_idp, _, err = await client.\
            get_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(retrieved_idp, models.IdentityProvider)
        assert retrieved_idp.id == created_idp.id
        assert retrieved_idp.name == idp_model.name + "UPDATE"

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_key(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Key
        key = "MIIDnjCCAoagAwIBAgIGAVG3MN+PMA0GCSqGSIb3DQEBBQUAMIGPMQswCQYDV\
            QQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5ja\
            XNjbzENMAsGA1UECgwET2t0YTEUMBIGA1UECwwLU1NPUHJvdmlkZXIxEDAOBgNVB\
            AMMB2V4YW1wbGUxHDAaBgkqhkiG9w0BCQEWDWluZm9Ab2t0YS5jb20wHhcNMTUxM\
            jE4MjIyMjMyWhcNMjUxMjE4MjIyMzMyWjCBjzELMAkGA1UEBhMCVVMxEzARBgNVB\
            AgMCkNhbGlmb3JuaWExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDTALBgNVBAoMB\
            E9rdGExFDASBgNVBAsMC1NTT1Byb3ZpZGVyMRAwDgYDVQQDDAdleGFtcGxlMRwwG\
            gYJKoZIhvcNAQkBFg1pbmZvQG9rdGEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCA\
            Q8AMIIBCgKCAQEAtcnyvuVCrsFEKCwHDenS3Ocjed8eWDv3zLtD2K/iZfE8BMj2w\
            pTfn6Ry8zCYey3mWlKdxIybnV9amrujGRnE0ab6Q16v9D6RlFQLOG6dwqoRKuZy3\
            3Uyg8PGdEudZjGbWuKCqqXEp+UKALJHV+k4wWeVH8g5d1n3KyR2TVajVJpCrPhLF\
            mq1Il4G/IUnPe4MvjXqB6CpKkog1+ThWsItPRJPAM+RweFHXq7KfChXsYE7Mmful\
            y8sDQlvBmQyxZnFHVuiPfCvGHJjpvHy11YlHdOjfgqHRvZbmo30+y0X/oY/yV4YE\
            J00LL6eJWU4wi7ViY3HP6/VCdRjHoRdr5L/DwIDAQABMA0GCSqGSIb3DQEBBQUAA\
            4IBAQCzzhOFkvyYLNFj2WDcq1YqD4sBy1iCia9QpRH3rjQvMKDwQDYWbi6EdOX0T\
            Q/IYR7UWGj+2pXd6v0t33lYtoKocp/4lUvT3tfBnWZ5KnObi+J2uY2teUqoYkASN\
            7F+GRPVOuMVoVgm05ss8tuMb2dLc9vsx93sDt+XlMTv/2qi5VPwaDtqduKkzwW9l\
            Ufn4xIMkTiVvCpe0X2HneD2Bpuao3/U8Rk0uiPfq6TooWaoW3kjsmErhEAs9bA7x\
            uqo1KKY9CdHcFhkSsMhoeaZylZHtzbnoipUlQKSLMdJQiiYZQ0bYL83/Ta9fulr1\
            EERICMFt3GUmtYaZZKHpWSfdJp9"

        jwk_model = models.JsonWebKey({
            "x5C": [key]
        })
        created_key, _, err = await client.\
            create_identity_provider_key(jwk_model)
        assert err is None
        assert isinstance(created_key, models.JsonWebKey)
        assert key in created_key.x_5_c

        # Retrieve
        retrieved_key, _, err = await client.\
            get_identity_provider_key(created_key.kid)
        assert err is None
        assert isinstance(retrieved_key, models.JsonWebKey)
        assert retrieved_key.kid == created_key.kid
        assert key in retrieved_key.x_5_c

        # Delete
        _, err = await client.delete_identity_provider_key(created_key.kid)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_keys(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Key
        key = "MIIDnjCCAoagAwIBAgIGAVG3MN+PMA0GCSqGSIb3DQEBBQUAMIGPMQswCQYDV\
            QQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5ja\
            XNjbzENMAsGA1UECgwET2t0YTEUMBIGA1UECwwLU1NPUHJvdmlkZXIxEDAOBgNVB\
            AMMB2V4YW1wbGUxHDAaBgkqhkiG9w0BCQEWDWluZm9Ab2t0YS5jb20wHhcNMTUxM\
            jE4MjIyMjMyWhcNMjUxMjE4MjIyMzMyWjCBjzELMAkGA1UEBhMCVVMxEzARBgNVB\
            AgMCkNhbGlmb3JuaWExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDTALBgNVBAoMB\
            E9rdGExFDASBgNVBAsMC1NTT1Byb3ZpZGVyMRAwDgYDVQQDDAdleGFtcGxlMRwwG\
            gYJKoZIhvcNAQkBFg1pbmZvQG9rdGEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCA\
            Q8AMIIBCgKCAQEAtcnyvuVCrsFEKCwHDenS3Ocjed8eWDv3zLtD2K/iZfE8BMj2w\
            pTfn6Ry8zCYey3mWlKdxIybnV9amrujGRnE0ab6Q16v9D6RlFQLOG6dwqoRKuZy3\
            3Uyg8PGdEudZjGbWuKCqqXEp+UKALJHV+k4wWeVH8g5d1n3KyR2TVajVJpCrPhLF\
            mq1Il4G/IUnPe4MvjXqB6CpKkog1+ThWsItPRJPAM+RweFHXq7KfChXsYE7Mmful\
            y8sDQlvBmQyxZnFHVuiPfCvGHJjpvHy11YlHdOjfgqHRvZbmo30+y0X/oY/yV4YE\
            J00LL6eJWU4wi7ViY3HP6/VCdRjHoRdr5L/DwIDAQABMA0GCSqGSIb3DQEBBQUAA\
            4IBAQCzzhOFkvyYLNFj2WDcq1YqD4sBy1iCia9QpRH3rjQvMKDwQDYWbi6EdOX0T\
            Q/IYR7UWGj+2pXd6v0t33lYtoKocp/4lUvT3tfBnWZ5KnObi+J2uY2teUqoYkASN\
            7F+GRPVOuMVoVgm05ss8tuMb2dLc9vsx93sDt+XlMTv/2qi5VPwaDtqduKkzwW9l\
            Ufn4xIMkTiVvCpe0X2HneD2Bpuao3/U8Rk0uiPfq6TooWaoW3kjsmErhEAs9bA7x\
            uqo1KKY9CdHcFhkSsMhoeaZylZHtzbnoipUlQKSLMdJQiiYZQ0bYL83/Ta9fulr1\
            EERICMFt3GUmtYaZZKHpWSfdJp9"

        jwk_model = models.JsonWebKey({
            "x5C": [key]
        })
        created_key, _, err = await client.\
            create_identity_provider_key(jwk_model)
        assert err is None
        assert isinstance(created_key, models.JsonWebKey)
        assert key in created_key.x_5_c

        # List
        idp_keys, _, err = await client.list_identity_provider_keys()
        assert err is None
        assert isinstance(idp_keys, list)
        assert next((key for key in idp_keys if key.kid == created_key.kid),
                    None) is not None

        # Delete
        _, err = await client.delete_identity_provider_key(created_key.kid)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_key(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Key
        key = "MIIDnjCCAoagAwIBAgIGAVG3MN+PMA0GCSqGSIb3DQEBBQUAMIGPMQswCQYDV\
            QQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5ja\
            XNjbzENMAsGA1UECgwET2t0YTEUMBIGA1UECwwLU1NPUHJvdmlkZXIxEDAOBgNVB\
            AMMB2V4YW1wbGUxHDAaBgkqhkiG9w0BCQEWDWluZm9Ab2t0YS5jb20wHhcNMTUxM\
            jE4MjIyMjMyWhcNMjUxMjE4MjIyMzMyWjCBjzELMAkGA1UEBhMCVVMxEzARBgNVB\
            AgMCkNhbGlmb3JuaWExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDTALBgNVBAoMB\
            E9rdGExFDASBgNVBAsMC1NTT1Byb3ZpZGVyMRAwDgYDVQQDDAdleGFtcGxlMRwwG\
            gYJKoZIhvcNAQkBFg1pbmZvQG9rdGEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCA\
            Q8AMIIBCgKCAQEAtcnyvuVCrsFEKCwHDenS3Ocjed8eWDv3zLtD2K/iZfE8BMj2w\
            pTfn6Ry8zCYey3mWlKdxIybnV9amrujGRnE0ab6Q16v9D6RlFQLOG6dwqoRKuZy3\
            3Uyg8PGdEudZjGbWuKCqqXEp+UKALJHV+k4wWeVH8g5d1n3KyR2TVajVJpCrPhLF\
            mq1Il4G/IUnPe4MvjXqB6CpKkog1+ThWsItPRJPAM+RweFHXq7KfChXsYE7Mmful\
            y8sDQlvBmQyxZnFHVuiPfCvGHJjpvHy11YlHdOjfgqHRvZbmo30+y0X/oY/yV4YE\
            J00LL6eJWU4wi7ViY3HP6/VCdRjHoRdr5L/DwIDAQABMA0GCSqGSIb3DQEBBQUAA\
            4IBAQCzzhOFkvyYLNFj2WDcq1YqD4sBy1iCia9QpRH3rjQvMKDwQDYWbi6EdOX0T\
            Q/IYR7UWGj+2pXd6v0t33lYtoKocp/4lUvT3tfBnWZ5KnObi+J2uY2teUqoYkASN\
            7F+GRPVOuMVoVgm05ss8tuMb2dLc9vsx93sDt+XlMTv/2qi5VPwaDtqduKkzwW9l\
            Ufn4xIMkTiVvCpe0X2HneD2Bpuao3/U8Rk0uiPfq6TooWaoW3kjsmErhEAs9bA7x\
            uqo1KKY9CdHcFhkSsMhoeaZylZHtzbnoipUlQKSLMdJQiiYZQ0bYL83/Ta9fulr1\
            EERICMFt3GUmtYaZZKHpWSfdJp9"

        jwk_model = models.JsonWebKey({
            "x5C": [key]
        })
        created_key, _, err = await client.\
            create_identity_provider_key(jwk_model)
        assert err is None
        assert isinstance(created_key, models.JsonWebKey)
        assert key in created_key.x_5_c

        # Delete
        _, err = await client.delete_identity_provider_key(created_key.kid)
        assert err is None

        # Retrieve
        retrieved_key, resp, err = await client.\
            get_identity_provider_key(created_key.kid)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_key is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_generate_get_idp_signing_key(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        idp_model = models.IdentityProvider({
            "type": "FACEBOOK",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["public_profile", "email"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Generate Key
        query_params_generate = {"validityYears": 2}
        generated_key, _, err = await client.\
            generate_identity_provider_signing_key(
                created_idp.id, query_params_generate)
        assert err is None
        assert isinstance(generated_key, models.JsonWebKey)
        assert generated_key is not None

        # Retrieve Key
        retrieved_key, _, err = await client.\
            get_identity_provider_signing_key(
                created_idp.id, generated_key.kid)
        assert err is None
        assert isinstance(retrieved_key, models.JsonWebKey)
        assert retrieved_key.kid == generated_key.kid

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_idp_signing_keys(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        idp_model = models.IdentityProvider({
            "type": "FACEBOOK",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["public_profile", "email"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Generate Keys
        query_params_generate = {"validityYears": 2}
        generated_key_1, _, err = await client.\
            generate_identity_provider_signing_key(
                created_idp.id, query_params_generate)
        assert err is None
        assert isinstance(generated_key_1, models.JsonWebKey)
        assert generated_key_1 is not None

        generated_key_2, _, err = await client.\
            generate_identity_provider_signing_key(
                created_idp.id, query_params_generate)
        assert err is None
        assert isinstance(generated_key_2, models.JsonWebKey)
        assert generated_key_2 is not None

        # List Keys
        idp_signing_keys, _, err = await client.\
            list_identity_provider_signing_keys(created_idp.id)
        assert err is None
        assert isinstance(idp_signing_keys, list)
        assert next((key for key in idp_signing_keys
                     if key.kid == generated_key_1.kid), None) is not None
        assert next((key for key in idp_signing_keys
                     if key.kid == generated_key_2.kid), None) is not None

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_clone_idp_signing_key(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDPs
        idp_model = models.IdentityProvider({
            "type": "FACEBOOK",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["public_profile", "email"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        idp_model_2 = models.IdentityProvider({
            "type": "LINKEDIN",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["r_basicprofile", "r_emailaddress"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        created_idp_2, _, err = await\
            client.create_identity_provider(idp_model_2)
        assert err is None
        assert isinstance(created_idp_2, models.IdentityProvider)
        assert created_idp_2.name == idp_model.name

        # Generate Key
        query_params_generate = {"validityYears": 2}
        generated_key, _, err = await client.\
            generate_identity_provider_signing_key(
                created_idp.id, query_params_generate)
        assert err is None
        assert isinstance(generated_key, models.JsonWebKey)
        assert generated_key is not None

        # Clone Key
        query_params_clone = {"targetIdpId": created_idp_2.id}
        cloned_key, _, err = await \
            client.clone_identity_provider_key(
                created_idp.id, generated_key.kid, query_params_clone)
        assert err is None
        assert isinstance(cloned_key, models.JsonWebKey)
        assert cloned_key.kid == generated_key.kid

        # Retrieve Key
        retrieved_key, _, err = await client.\
            get_identity_provider_signing_key(
                created_idp_2.id, cloned_key.kid)
        assert err is None
        assert isinstance(retrieved_key, models.JsonWebKey)
        assert retrieved_key.kid == cloned_key.kid

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp_2.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp_2.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_generate_get_csr(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        idp_model = models.IdentityProvider({
            "type": "FACEBOOK",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["public_profile", "email"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Generate CSR
        csr_metadata_model = models.CsrMetadata({
            "subject": models.CsrMetadataSubject({
                "countryName": "CAN",
                "stateOrProvinceName": "Ontario",
                "localityName": "Toronto",
                "organizationName": "Okta, Inc.",
                "organizationalUnitName": "Dev",
                "commonName": "SP Issuer"
            }),
            "subjectAltNames": models.CsrMetadataSubjectAltNames({
                "dnsNames": ["dev.okta.com"]
            })
        })
        generated_csr, _, err = await client.\
            generate_csr_for_identity_provider(
                created_idp.id, csr_metadata_model)
        assert err is None
        assert isinstance(generated_csr, models.Csr)
        assert generated_csr.kty == "RSA"

        # Retrieve
        retrieved_csr, _, err = await client.\
            get_csr_for_identity_provider(created_idp.id, generated_csr.id)
        assert err is None
        assert isinstance(retrieved_csr, models.Csr)
        assert retrieved_csr.id == generated_csr.id
        assert retrieved_csr.kty == generated_csr.kty

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_csr(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create IDP
        idp_model = models.IdentityProvider({
            "type": "FACEBOOK",
            "name": f"{TestIdentityProvidersResource.SDK_PREFIX} facebook",
            "protocol": models.Protocol({
                "scopes": ["public_profile", "email"],
                "type": "OAUTH2",
                "credentials": models.IdentityProviderCredentials({
                    "client": models.IdentityProviderCredentialsClient({
                        "clientId": "your-client-id",
                        "clientSecret": "your-client-secret"
                    })
                })
            }),
            "policy": models.IdentityProviderPolicy({
                "accountLink": models.PolicyAccountLink({
                    "action": "AUTO",
                    "filter": None
                }),
                "provisioning": models.Provisioning({
                    "action": "AUTO",
                    "profileMaster": True,
                    "conditions": models.ProvisioningConditions({
                        "deprovisioned":
                        models.ProvisioningDeprovisionedCondition({
                            "action": "NONE"
                        }),
                        "suspended": models.ProvisioningSuspendedCondition({
                            "action": "NONE"
                        })
                    }),
                    "groups": models.ProvisioningGroups({
                        "action": "NONE"
                    })
                }),
                "maxClockSkew": 120000,
                "subject": models.PolicySubject({
                    "userNameTemplate": models.PolicyUserNameTemplate({
                        "template": "idpuser.email"
                    }),
                    "matchType": models.PolicySubjectMatchType.USERNAME,
                    "filter": None
                })
            })
        })

        created_idp, _, err = await client.create_identity_provider(idp_model)
        assert err is None
        assert isinstance(created_idp, models.IdentityProvider)
        assert created_idp.name == idp_model.name

        # Generate CSR
        csr_metadata_model = models.CsrMetadata({
            "subject": models.CsrMetadataSubject({
                "countryName": "CAN",
                "stateOrProvinceName": "Ontario",
                "localityName": "Toronto",
                "organizationName": "Okta, Inc.",
                "organizationalUnitName": "Dev",
                "commonName": "SP Issuer"
            }),
            "subjectAltNames": models.CsrMetadataSubjectAltNames({
                "dnsNames": ["dev.okta.com"]
            })
        })
        generated_csr, _, err = await client.\
            generate_csr_for_identity_provider(
                created_idp.id, csr_metadata_model)
        assert err is None
        assert isinstance(generated_csr, models.Csr)
        assert generated_csr.kty == "RSA"

        # Retrieve
        retrieved_csr, _, err = await client.\
            get_csr_for_identity_provider(created_idp.id, generated_csr.id)
        assert err is None
        assert isinstance(retrieved_csr, models.Csr)
        assert retrieved_csr.id == generated_csr.id
        assert retrieved_csr.kty == generated_csr.kty

        # Revoke
        _, err = await client.\
            revoke_csr_for_identity_provider(created_idp.id, generated_csr.id)
        assert err is None

        # Retrieve for verification
        retrieved_csr, resp, err = await client.\
            get_csr_for_identity_provider(created_idp.id, generated_csr.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_csr is None

        # Deactivate and delete
        deactivated_idp, _, err = await \
            client.deactivate_identity_provider(created_idp.id)
        assert err is None
        assert isinstance(deactivated_idp, models.IdentityProvider)
        _, err = await client.delete_identity_provider(created_idp.id)
        assert err is None
