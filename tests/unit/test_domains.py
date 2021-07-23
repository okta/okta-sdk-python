import aiohttp
import asyncio
from okta.client import Client as OktaClient
from okta.models import DnsRecord, DomainCertificate, DomainCertificateMetadata, Domain


CREATE_DOMAIN_RESP = """{
    "id": "OcDz6iRyjkaCTXkdo0g3",
    "domain": "login.example.com",
    "validationStatus": "NOT_STARTED",
    "dnsRecords": [
        {
            "fqdn": "_oktaverification.login.example.com",
            "values": [
                "79496f234c814638b1cc44f51a782781"
            ],
            "recordType": "TXT"
        },
        {
            "fqdn": "login.sigmanetcorp.us",
            "values": [
                "test.customdomains.okta1.com"
            ],
            "recordType": "CNAME"
        }
    ],
    "_links": {
        "self": {
            "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3",
            "hints": {
                "allow": [
                    "GET",
                    "DELETE"
                ]
            }
        },
        "verify": {
            "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3/verify",
            "hints": {
                "allow": [
                    "POST"
                ]
            }
        }
    }
}"""


VERIFY_DOMAIN_RESP = """{
    "id": "OcDz6iRyjkaCTXkdo0g3",
    "domain": "login.example.com",
    "certificateSourceType": "MANUAL",
    "validationStatus": "VERIFIED",
    "dnsRecords": [
        {
            "fqdn": "_oktaverification.login.example.com",
            "values": [
                "79496f234c814638b1cc44f51a782781"
            ],
            "recordType": "TXT"
        },
        {
            "fqdn": "login.sigmanetcorp.us",
            "values": [
                "test.customdomains.okta1.com"
            ],
            "recordType": "CNAME"
        }
    ],
    "_links": {
           "certificate": {
               "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3/certificate",
               "hints": {
                   "allow": [
                       "PUT"
                   ]
               }
           },
        "self": {
            "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3",
            "hints": {
                "allow": [
                    "GET",
                    "DELETE"
                ]
            }
        }
    }
}"""


GET_DOMAIN_RESP = """{
    "id": "OcDz6iRyjkaCTXkdo0g3",
    "domain": "login.example.com",
    "certificateSourceType": "MANUAL",
    "validationStatus": "COMPLETED",
    "dnsRecords": [
        {
            "fqdn": "_oktaverification.login.example.com",
            "values": [
                "79496f234c814638b1cc44f51a782781"
            ],
            "recordType": "TXT"
        },
        {
            "fqdn": "login.example.com",
            "values": [
                "test.okta.com.customdomains.okta1.com"
            ],
            "recordType": "CNAME"
        }
    ],
    "publicCertificate": {
        "subject": "CN=login.example.com",
        "fingerprint": "73:68:82:7B:83:2E:48:29:A5:5E:E8:40:41:80:B3:AA:03:C4:42:43:05:73:45:BC:AA:47:00:23:A3:70:E5:C4",
        "expiration": "2021-05-11T05:13:05.000Z"
    },
    "_links": {
        "certificate": {
            "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3/certificate",
            "hints": {
                "allow": [
                    "PUT"
                ]
            }
        },
        "self": {
            "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3",
            "hints": {
                "allow": [
                    "DELETE"
                ]
            }
        },
        "verify": {
            "href": "https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3/verify",
            "hints": {
                "allow": [
                    "POST"
                ]
            }
        }
    }
}"""


class TestDomainResource:
    """
    Unit Tests for the Domain Resource
    """

    def test_get_domain(self, monkeypatch):
        org_url = "https://test.okta.com"
        token = "TOKEN"
        config = {'orgUrl': org_url, 'token': token}
        client = OktaClient(config)

        # mock http requests
        class MockHTTPRequest():

            _mocked_response = None

            def __call__(self, **params):
                self.request_info = params
                self.headers = params['headers']
                self.url = params['url']
                self.content_type = 'application/json'
                self.links = ''
                self.text = MockHTTPRequest.mock_response_text
                self.status = 200
                return self

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

            @staticmethod
            async def mock_response_text():
                return GET_DOMAIN_RESP

        mock_http_request = MockHTTPRequest()
        monkeypatch.setattr(aiohttp, 'request', mock_http_request)

        domain_resp, _, err = asyncio.run(client.get_domain('OcDz6iRyjkaCTXkdo0g3'))
        assert err is None
        assert isinstance(domain_resp, Domain)
        assert isinstance(domain_resp.public_certificate, DomainCertificateMetadata)
        assert len(domain_resp.dns_records) > 0
        for dns_record in domain_resp.dns_records:
            assert isinstance(dns_record, DnsRecord)
        assert domain_resp.domain == 'login.example.com'

    def test_create_certificate_and_verify_domain(self, monkeypatch):
        org_url = "https://test.okta.com"
        token = "TOKEN"
        config = {'orgUrl': org_url, 'token': token}
        client = OktaClient(config)

        # mock http requests
        class MockHTTPRequest():

            _mocked_response = None

            def __call__(self, **params):
                self.request_info = params
                self.headers = params['headers']
                self.url = params['url']
                self.content_type = 'application/json'
                self.links = ''
                MockHTTPRequest._set_mocked_response(params)
                self.text = MockHTTPRequest.mock_response_text
                self.status = 200
                return self

            async def __aenter__(self):
                return self

            async def __aexit__(self, exc_type, exc, tb):
                pass

            @staticmethod
            def _set_mocked_response(params):
                if params['method'] == 'POST' and params['url'] == 'https://test.okta.com/api/v1/domains':
                    MockHTTPRequest._mocked_response = CREATE_DOMAIN_RESP
                elif params['method'] == 'PUT' and params['url'] == 'https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3/certificate':
                    MockHTTPRequest._mocked_response = '{}'
                elif params['method'] == 'POST' and params['url'] == 'https://test.okta.com/api/v1/domains/OcDz6iRyjkaCTXkdo0g3/verify':
                    MockHTTPRequest._mocked_response = VERIFY_DOMAIN_RESP

            @staticmethod
            async def mock_response_text():
                return MockHTTPRequest._mocked_response

        mock_http_request = MockHTTPRequest()
        monkeypatch.setattr(aiohttp, 'request', mock_http_request)

        domain_config = {
            "domain": "login.example.com",
            "certificateSourceType": "MANUAL"
        }
        domain_resp, _, err = asyncio.run(client.create_domain(domain_config))
        assert err is None

        cert = DomainCertificate({'type': 'PEM',
                                  'certificate': 'test_certificate',
                                  'privateKey': 'test_private_key'})
        cert_resp, err = asyncio.run(client.create_certificate(domain_resp.id, cert))
        assert err is None

        domain_resp, _, err = asyncio.run(client.verify_domain(domain_resp.id))
        assert err is None
        assert domain_resp.validation_status == 'VERIFIED'
