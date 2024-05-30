import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from okta.errors.okta_api_error import OktaAPIError


class TestSubscriptionResource:
    """
    Integration Tests for the Subscription Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_role_subsription(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        resp, _, err = await client.list_role_subscriptions('SUPER_ADMIN')
        assert len(resp) > 0
        for item in resp:
            assert isinstance(item, models.Subscription)
            assert isinstance(item.status, models.SubscriptionStatus)
            assert isinstance(item.notification_type, models.NotificationType)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_role_subscription_by_notification_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        notification_type = models.NotificationType('OKTA_ISSUE')
        resp, _, err = await client.get_role_subscription_by_notification_type('SUPER_ADMIN', notification_type)
        assert isinstance(resp, models.Subscription)
        assert resp.notification_type == models.NotificationType('OKTA_ISSUE')

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_subscribe_unsubscribe_role_by_notification_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        notification_type = models.NotificationType('OKTA_ISSUE')
        _, err = await client.subscribe_role_subscription_by_notification_type('SUPER_ADMIN', notification_type)
        assert err is None

        resp, _, err = await client.get_role_subscription_by_notification_type('SUPER_ADMIN', notification_type)
        assert isinstance(resp, models.Subscription)
        assert resp.notification_type == models.NotificationType('OKTA_ISSUE')
        assert resp.status == models.SubscriptionStatus('SUBSCRIBED')

        try:
            _, err = await client.unsubscribe_role_subscription_by_notification_type('SUPER_ADMIN', notification_type)
            assert err is None
            resp, _, err = await client.get_role_subscription_by_notification_type('SUPER_ADMIN', notification_type)
            assert isinstance(resp, models.Subscription)
            assert resp.notification_type == models.NotificationType('OKTA_ISSUE')
            assert resp.status == models.SubscriptionStatus('UNSUBSCRIBED')

        finally:
            # restore subscription
            _, err = await client.subscribe_role_subscription_by_notification_type('SUPER_ADMIN', notification_type)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_subscribe_unsubscribe_user(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        users, _, err = await client.list_users()
        assert err is None
        user = users[0]

        notification_type = models.NotificationType('OKTA_ISSUE')
        _, err = await client.subscribe_user_subscription_by_notification_type(user.id, notification_type)
        assert err is None

        resp, _, err = await client.get_user_subscription_by_notification_type(user.id, notification_type)
        assert resp.notification_type == models.NotificationType('OKTA_ISSUE')
        assert resp.status == models.SubscriptionStatus('SUBSCRIBED')

        _, err = await client.unsubscribe_user_subscription_by_notification_type(user.id, notification_type)
        assert err is None

        resp, _, err = await client.get_user_subscription_by_notification_type(user.id, notification_type)
        assert resp.notification_type == models.NotificationType('OKTA_ISSUE')
        assert resp.status == models.SubscriptionStatus('UNSUBSCRIBED')
