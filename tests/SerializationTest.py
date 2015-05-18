from okta.framework.Utils import Utils
from okta.framework.Serializer import Serializer
from okta.models.event.Event import Event
from okta.models.user.User import User
from okta.models.auth.AuthResult import AuthResult
import unittest
import json
import types
import six


class SerializationTest(unittest.TestCase):

    def test_list_deserialization(self):
        json_str = '''
        [{
            "eventId": "tevJaSvrF0CQYO_HbEMa03zYg1428346536000",
            "sessionId": "trsXfYxlFT6SJiG4rhi-EskUQ",
            "requestId": "reqjDcKHbAKTMewdiRIAI__-Q",
            "published": "2015-04-06T18:55:36.000Z",
            "action": {
                "message": "App configuration updated ",
                "categories": [],
                "objectType": "app.generic.config.app_updated",
                "requestUri": "/fake"
            },
            "actors": [{
                "id": "00uh7tCkIn4yHncnR0g3",
                "displayName": "BB",
                "login": "q@vinegar.com",
                "objectType": "User"
            }, {
                "id": "Jakarta Commons-HttpClient/3.1",
                "displayName": "UNKNOWN",
                "ipAddress": "127.0.0.1",
                "objectType": "Client"
            }],
            "targets": [{
                "id": "0oah8iGK5tNBNwX6e0g3",
                "displayName": "Okta Administration",
                "objectType": "AppInstance"
            }]
        }]
        '''

        result = Utils.deserialize(json_str, Event)

        self.assertGreaterEqual(len(result[0].actors), 1, "Cannot deserialize nested lists of objects")

        serialized = json.dumps(result, cls=Serializer)

        self.assertTrue("00uh7tCkIn4yHncnR0g3" in serialized, "Nested lists aren't serialized properly")

    def test_links_deserialization(self):
        json_str = '''
        {
            "id": "00uhk18ujVSWoEnZa0g3",
            "status": "STAGED",
            "created": "2015-04-08T18:34:43.000Z",
            "activated": null,
            "statusChanged": null,
            "lastLogin": null,
            "lastUpdated": "2015-04-08T18:34:43.000Z",
            "passwordChanged": null,
            "profile": {
                "mobilePhone": null,
                "email": "asdfh@example.com",
                "secondEmail": "",
                "firstName": "Some",
                "lastName": "One",
                "login": "asdfh@example.com"
            },
            "credentials": {
                "provider": {
                    "type": "OKTA",
                    "name": "OKTA"
                }
            },
            "_links": {
                "activate": {
                    "href": "http://example.okta.com/api/v1/users/00uhk18ujVSWoEnZa0g3/lifecycle/activate",
                    "method": "POST"
                },
                "deactivate": {
                    "href": "http://example.okta.com/api/v1/users/00uhk18ujVSWoEnZa0g3/lifecycle/deactivate",
                    "method": "POST"
                },
                "logo": [
                    {
                        "href": "https://example.okta.com/img/logos/groups/okta-medium.png",
                        "name": "medium",
                        "type": "image/png"
                    },
                    {
                        "href": "https://example.okta.com/img/logos/groups/okta-large.png",
                        "name": "large",
                        "type": "image/png"
                    }
                ],
                "next": {
                  "name": "activate",
                  "href": "https://example.okta.com/api/v1/authn/factors/ostf2xjtDKWFPZIKYDZV/lifecycle/activate",
                  "hints": {
                    "allow": [
                      "POST"
                    ]
                  }
                }
            }
        }
        '''

        result = Utils.deserialize(json_str, User)
        self.assertIsNotNone(result.links, "Links aren't populated properly")

        list_type = types.ListType if six.PY2 else list
        self.assertTrue(isinstance(result.links['logo'], list_type), "Lists of links aren't deserialized properly")

        self.assertEqual(result.links['next'].hints['allow'][0], 'POST', "Hints in links aren't deserialized properly")

    def test_embedded_deserialization(self):
        json_str = '''
        {
            "stateToken": "00FpGOgqHfl-6KZxh1bLXJDz35ENsShIY-lc5XHPzc",
            "expiresAt": "2014-11-02T23:35:28.269Z",
            "status": "MFA_REQUIRED",
            "relayState": "/myapp/some/deep/link/i/want/to/return/to",
            "_embedded": {
                "user": {
                    "id": "00ub0oNGTSWTBKOLGLNR",
                    "profile": {
                        "login": "isaac@example.org",
                        "firstName": "Isaac",
                        "lastName": "Brock",
                        "locale": "en_US",
                        "timeZone": "America/Los_Angeles"
                    }
                },
                "factors": [{
                    "id": "ufsm3jZGDQXPJDEIXZMP",
                    "factorType": "question",
                    "provider": "OKTA",
                    "profile": {
                        "question": "disliked_food",
                        "questionText": "What is the food you least liked as a child?"
                    },
                    "_links": {
                        "verify": {
                            "href": "https://your-domain.okta.com/api/v1/authn/factors/ufsm3jZGDQXPJDEIXZMP/verify",
                            "hints": {
                                "allow": [
                                    "POST"
                                ]
                            }
                        }
                    }
                }, {
                    "id": "sms193zUBEROPBNZKPPE",
                    "factorType": "sms",
                    "provider": "OKTA",
                    "profile": {
                        "phoneNumber": "+1 XXX-XXX-1337"
                    },
                    "_links": {
                        "verify": {
                            "href": "https://your-domain.okta.com/api/v1/authn/factors/sms193zUBEROPBNZKPPE/verify",
                            "hints": {
                                "allow": [
                                    "POST"
                                ]
                            }
                        }
                    }
                }]
            },
            "_links": {
                "cancel": {
                    "href": "https://your-domain.okta.com/api/v1/authn/cancel",
                    "hints": {
                        "allow": [
                            "POST"
                        ]
                    }
                }
            }
        }
        '''

        result = Utils.deserialize(json_str, AuthResult)

        self.assertTrue(isinstance(result.embedded.user, User), "Embedded User attribute isn't deserialized properly")

        self.assertEqual(len(result.embedded.factors), 2, "Embedded factors attribute isn't deserialized properly")