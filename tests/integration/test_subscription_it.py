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
        resp, _, err = await client.list_subscriptions_role('SUPER_ADMIN')
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
        notification_type = models.NotificationType.OKTA_ISSUE.value
        resp, _, err = await client.get_subscriptions_notification_type_role('SUPER_ADMIN', notification_type)
        assert isinstance(resp, models.Subscription)
        assert resp.notification_type == models.NotificationType.OKTA_ISSUE.value

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_subscribe_unsubscribe_role_by_notification_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        notification_type = models.NotificationType.OKTA_ISSUE.value
        _, _, err = await client.subscribe_by_notification_type_role('SUPER_ADMIN', notification_type)
        assert err is None

        resp, _, err = await client.get_subscriptions_notification_type_role('SUPER_ADMIN', notification_type)
        assert isinstance(resp, models.Subscription)
        assert resp.notification_type == models.NotificationType.OKTA_ISSUE.value
        assert resp.status == models.SubscriptionStatus.SUBSCRIBED.value

        try:
            _, _, err = await client.unsubscribe_by_notification_type_role('SUPER_ADMIN', notification_type)
            assert err is None
            resp, _, err = await client.get_subscriptions_notification_type_role('SUPER_ADMIN', notification_type)
            assert isinstance(resp, models.Subscription)
            assert resp.notification_type == models.NotificationType.OKTA_ISSUE.value
            assert resp.status == models.SubscriptionStatus.UNSUBSCRIBED.value

        finally:
            # restore subscription
            _, _, err = await client.subscribe_by_notification_type_role('SUPER_ADMIN', notification_type)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_subscribe_unsubscribe_user(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        users, _, err = await client.list_users()
        assert err is None
        user = users[0]

        notification_type = models.NotificationType.OKTA_ISSUE.value
        _, _, err = await client.subscribe_by_notification_type_user(notification_type, user.id)
        assert err is None

        resp, _, err = await client.get_subscriptions_notification_type_user(notification_type, user.id)
        assert resp.notification_type == models.NotificationType.OKTA_ISSUE.value
        assert resp.status == models.SubscriptionStatus.SUBSCRIBED.value

        _, _, err = await client.unsubscribe_by_notification_type_user(notification_type, user.id)
        assert err is None

        resp, _, err = await client.get_subscriptions_notification_type_user(notification_type, user.id)
        assert resp.notification_type == models.NotificationType.OKTA_ISSUE.value
        assert resp.status == models.SubscriptionStatus.UNSUBSCRIBED.value
