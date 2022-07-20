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

from okta.models.subscription\
    import Subscription
from okta.utils import format_url
from okta.api_client import APIClient


class SubscriptionClient(APIClient):
    """
    A Client object for the Subscription resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_role_subscriptions(
            self, roleTypeOrRoleId,
            keep_empty_params=False
    ):
        """
        When roleType List all subscriptions of a Role. Else wh
        en roleId List subscriptions of a Custom Role
        Args:
            role_type_or_role_id {str}
        Returns:
            list: Collection of Subscription instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/roles/{roleTypeOrRoleId}/subscriptions
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Subscription)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(Subscription(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_role_subscription_by_notification_type(
            self, roleTypeOrRoleId, notificationType,
            keep_empty_params=False
    ):
        """
        When roleType Get subscriptions of a Role with a specif
        ic notification type. Else when roleId Get subscription
        of a Custom Role with a specific notification type.
        Args:
            role_type_or_role_id {str}
            notification_type {str}
        Returns:
            Subscription
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/roles/{roleTypeOrRoleId}/subscriptions
                /{notificationType}
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Subscription)

        if error:
            return (None, response, error)

        try:
            result = Subscription(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def subscribe_role_subscription_by_notification_type(
            self, roleTypeOrRoleId, notificationType,
            keep_empty_params=False
    ):
        """
        When roleType Subscribes a Role to a specific notificat
        ion type. When you change the subscription status of a
        Role, it overrides the subscription of any individual u
        ser of that Role. Else when roleId Subscribes a Custom
        Role to a specific notification type. When you change t
        he subscription status of a Custom Role, it overrides t
        he subscription of any individual user of that Custom R
        ole.
        Args:
            role_type_or_role_id {str}
            notification_type {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/roles/{roleTypeOrRoleId}/subscriptions
                /{notificationType}/subscribe
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def unsubscribe_role_subscription_by_notification_type(
            self, roleTypeOrRoleId, notificationType,
            keep_empty_params=False
    ):
        """
        When roleType Unsubscribes a Role from a specific notif
        ication type. When you change the subscription status o
        f a Role, it overrides the subscription of any individu
        al user of that Role. Else when roleId Unsubscribes a C
        ustom Role from a specific notification type. When you
        change the subscription status of a Custom Role, it ove
        rrides the subscription of any individual user of that
        Custom Role.
        Args:
            role_type_or_role_id {str}
            notification_type {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/roles/{roleTypeOrRoleId}/subscriptions
                /{notificationType}/unsubscribe
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def subscribe_user_subscription_by_notification_type(
            self, userId, notificationType,
            keep_empty_params=False
    ):
        """
        Subscribes a User to a specific notification type. Only
        the current User can subscribe to a specific notificat
        ion type. An AccessDeniedException message is sent if r
        equests are made from other users.
        Args:
            user_id {str}
            notification_type {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/subscriptions
                /{notificationType}/subscribe
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def unsubscribe_user_subscription_by_notification_type(
            self, userId, notificationType,
            keep_empty_params=False
    ):
        """
        Unsubscribes a User from a specific notification type.
        Only the current User can unsubscribe from a specific n
        otification type. An AccessDeniedException message is s
        ent if requests are made from other users.
        Args:
            user_id {str}
            notification_type {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/users/{userId}/subscriptions
                /{notificationType}/unsubscribe
            """)

        body = {}
        headers = {}
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)
