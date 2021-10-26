import copy
import os
import pytest
from datetime import datetime
from tests.mocks import MockOktaClient
from okta.models import (OrgSetting,
                         OrgContactType,
                         OrgContactTypeObj,
                         OrgContactUser,
                         OrgPreferences,
                         OrgOktaCommunicationSetting,
                         OrgOktaSupportSettingsObj,
                         OrgOktaSupportSetting,
                         UserIdString)


class TestOrgResource:
    """
    Integration Tests for the Org Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_org_settings(self, fs):
        client = MockOktaClient(fs)
        org_settings, _, err = await client.get_org_settings()
        assert err is None
        assert isinstance(org_settings, OrgSetting)
        assert org_settings.status == 'ACTIVE'

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_partial_setting_update(self, fs):
        client = MockOktaClient(fs)
        get_org_settings, _, err = await client.get_org_settings()
        assert err is None

        updated_setting = {'supportPhoneNumber': '1234567890'}
        try:
            updated_org_settings, _, err = await client.partial_update_org_setting(updated_setting)
            assert err is None
            assert updated_org_settings.support_phone_number == '1234567890'
        finally:
            updated_setting = {'supportPhoneNumber': get_org_settings.support_phone_number}
            updated_org_settings, _, err = await client.partial_update_org_setting(updated_setting, keep_empty_params=True)
            assert err is None
            assert updated_org_settings.support_phone_number == get_org_settings.support_phone_number

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_setting_update(self, fs):
        client = MockOktaClient(fs)
        get_org_settings, resp, err = await client.get_org_settings()

        new_org_settings = copy.deepcopy(get_org_settings)
        new_org_settings.support_phone_number = '1234567890'
        new_org_settings.company_name = 'NewOrgName'
        try:
            updated_org_settings, _, err = await client.update_org_setting(new_org_settings)
            assert err is None
            assert updated_org_settings.support_phone_number == '1234567890'
            assert updated_org_settings.company_name == 'NewOrgName'

        finally:
            updated_org_settings, _, err = await client.update_org_setting(get_org_settings, keep_empty_params=True)
            assert err is None
            assert updated_org_settings.support_phone_number == get_org_settings.support_phone_number
            assert updated_org_settings.company_name == get_org_settings.company_name

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_org_contact_types(self, fs):
        client = MockOktaClient(fs)
        org_contact_types, _, err = await client.get_org_contact_types()
        assert err is None
        for item in org_contact_types:
            assert isinstance(item, OrgContactTypeObj)
            assert isinstance(item.contact_type, OrgContactType)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_org_contact_user(self, fs):
        client = MockOktaClient(fs)
        contact_type = OrgContactType('BILLING')
        org_contact_user, _, err = await client.get_org_contact_user(contact_type)
        assert err is None
        assert isinstance(org_contact_user, OrgContactUser)
        assert org_contact_user.user_id is not None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_org_contact_user(self, fs):
        client = MockOktaClient(fs)
        contact_type = OrgContactType('BILLING')
        org_contact_user, _, err = await client.get_org_contact_user(contact_type)
        assert err is None

        new_contact_type = OrgContactType('TECHNICAL')
        try:
            updated_user, _, err = await client.update_org_contact_user(new_contact_type,
                                                                        UserIdString({'userId': org_contact_user.user_id}))
            assert err is None
        finally:
            updated_user, _, err = await client.update_org_contact_user(contact_type,
                                                                        UserIdString({'userId': org_contact_user.user_id}))
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_org_preferences(self, fs):
        client = MockOktaClient(fs)
        org_preferences, _, err = await client.get_org_preferences()
        assert err is None
        assert isinstance(org_preferences, OrgPreferences)
        assert isinstance(org_preferences.show_end_user_footer, bool)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_hide_okta_ui_footer(self, fs):
        client = MockOktaClient(fs)
        org_preferences, _, err = await client.hide_okta_ui_footer()
        assert err is None
        assert isinstance(org_preferences, OrgPreferences)
        assert not org_preferences.show_end_user_footer

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_show_okta_ui_footer(self, fs):
        client = MockOktaClient(fs)
        org_preferences, _, err = await client.show_okta_ui_footer()
        assert err is None
        assert isinstance(org_preferences, OrgPreferences)
        assert org_preferences.show_end_user_footer

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_okta_communication_settings(self, fs):
        client = MockOktaClient(fs)
        org_communication_setting, _, err = await client.get_okta_communication_settings()
        assert err is None
        assert isinstance(org_communication_setting, OrgOktaCommunicationSetting)
        assert isinstance(org_communication_setting.opt_out_email_users, bool)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_opt_in_users_to_okta_communication_emails(self, fs):
        client = MockOktaClient(fs)
        org_communication_setting, _, err = await client.opt_in_users_to_okta_communication_emails()
        assert err is None
        assert isinstance(org_communication_setting, OrgOktaCommunicationSetting)
        assert not org_communication_setting.opt_out_email_users

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_opt_out_users_from_okta_communication_emails(self, fs):
        client = MockOktaClient(fs)
        org_communication_setting, _, err = await client.opt_out_users_from_okta_communication_emails()
        assert err is None
        assert isinstance(org_communication_setting, OrgOktaCommunicationSetting)
        assert org_communication_setting.opt_out_email_users

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_okta_support_settings(self, fs):
        client = MockOktaClient(fs)
        org_okta_support_setting, _, err = await client.get_org_okta_support_settings()
        assert err is None
        assert isinstance(org_okta_support_setting, OrgOktaSupportSettingsObj)
        assert isinstance(org_okta_support_setting.support, OrgOktaSupportSetting)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_grant_revoke_okta_support(self, fs):
        client = MockOktaClient(fs)
        try:
            org_okta_support_setting, _, err = await client.grant_okta_support()
            assert err is None
            assert isinstance(org_okta_support_setting, OrgOktaSupportSettingsObj)
            assert isinstance(org_okta_support_setting.support, OrgOktaSupportSetting)
            assert org_okta_support_setting.support == 'ENABLED'
        finally:
            org_okta_support_setting, _, err = await client.revoke_okta_support()
            assert err is None
            assert isinstance(org_okta_support_setting, OrgOktaSupportSettingsObj)
            assert isinstance(org_okta_support_setting.support, OrgOktaSupportSetting)
            assert org_okta_support_setting.support == 'DISABLED'

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_extend_okta_support(self, fs):
        client = MockOktaClient(fs)
        try:
            org_okta_support_setting, _, err = await client.grant_okta_support()
            assert err is None
            assert org_okta_support_setting.support == 'ENABLED'
            extended_org_okta_support_setting, _, err = await client.extend_okta_support()
            assert err is None
            date1 = datetime.strptime(org_okta_support_setting.expiration, "%Y-%m-%dT%H:%M:%S.%fZ")
            date2 = datetime.strptime(extended_org_okta_support_setting.expiration, "%Y-%m-%dT%H:%M:%S.%fZ")
            # should be 24h
            assert round((date2 - date1).total_seconds() / 3600) == 24
        finally:
            org_okta_support_setting, _, err = await client.revoke_okta_support()
            assert err is None

    # skip test until solution with writing cassette is found
    @pytest.mark.skip
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_upload_org_logo(self, fs):
        client = MockOktaClient(fs)
        fs.pause()
        logo = open(f'tests/integration/data/logo.png', 'rb')
        _, err = await client.update_org_logo(logo)
        fs.resume()
        assert err is None
