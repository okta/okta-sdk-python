import pytest
from tests.mocks import MockOktaClient
from okta.models import DomainResponse


class TestDomainResource:
    """
    Integration Tests for the Domain Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_domains(self, fs):
        client = MockOktaClient(fs)
        domains_list_resp, _, err = await client.list_domains()
        for domain in domains_list_resp.domains:
            assert isinstance(domain, DomainResponse)
            assert domain.domain

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_and_delete_domain(self, fs):
        client = MockOktaClient(fs)
        domain_config = {
            "domain": "login.example.com",
            "certificateSourceType": "MANUAL"
        }
        domain, _, err = await client.create_domain(domain_config)
        assert err is None
        try:
            assert isinstance(domain, DomainResponse)
            assert domain.id
        finally:
            _, err = await client.delete_domain(domain.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_domain(self, fs):
        client = MockOktaClient(fs)
        domain_config = {
            "domain": "login.example.com",
            "certificateSourceType": "MANUAL"
        }
        domain, _, err = await client.create_domain(domain_config)
        assert err is None
        try:
            get_domain, _, err = await client.get_domain(domain.id)
            assert isinstance(domain, DomainResponse)
            assert domain.id == get_domain.id
            assert domain.domain == get_domain.domain
        finally:
            _, err = await client.delete_domain(domain.id)
            assert err is None
