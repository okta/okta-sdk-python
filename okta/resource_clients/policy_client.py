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

from urllib.parse import urlencode
from okta.models.policy\
    import Policy
from okta.models.policy_rule\
    import PolicyRule
from okta.utils import format_url
from okta.api_client import APIClient
from okta.constants import find_policy_model
from okta.constants import find_policy_rule_model


class PolicyClient(APIClient):
    """
    A Client object for the Policy resource.
    """

    def __init__(self):
        self._base_url = ""

    async def list_policies(
            self, query_params={}
    ):
        """
        Gets all policies with the specified type.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.type] {str}
            [query_params.status] {str}
            [query_params.expand] {str}
        Returns:
            list: Collection of Policy instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(
                    find_policy_model(item["type"])(
                        self.form_response_body(item)
                        )
                    )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_policy(
            self, policy, query_params={}
    ):
        """
        Creates a policy.
        Args:
            {policy}
            query_params {dict}: Map of query parameters for request
            [query_params.activate] {str}
        Returns:
            Policy
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        if isinstance(policy, dict):
            body = policy
        else:
            body = policy.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_policy(
            self, policyId
    ):
        """
        Removes a policy.
        Args:
            policy_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_policy(
            self, policyId, query_params={}
    ):
        """
        Gets a policy.
        Args:
            policy_id {str}
            query_params {dict}: Map of query parameters for request
            [query_params.expand] {str}
        Returns:
            Policy
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}
            """)
        if query_params:
            encoded_query_params = urlencode(query_params)
            api_url += f"/?{encoded_query_params}"

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_policy(
            self, policyId, policy
    ):
        """
        Updates a policy.
        Args:
            policy_id {str}
            {policy}
        Returns:
            Policy
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}
            """)

        if isinstance(policy, dict):
            body = policy
        else:
            body = policy.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, Policy)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_policy(
            self, policyId
    ):
        """
        Activates a policy.
        Args:
            policy_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/lifecycle/activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_policy(
            self, policyId
    ):
        """
        Deactivates a policy.
        Args:
            policy_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/lifecycle/deactivate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def list_policy_rules(
            self, policyId
    ):
        """
        Enumerates all policy rules.
        Args:
            policy_id {str}
        Returns:
            list: Collection of PolicyRule instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, PolicyRule)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(
                    find_policy_rule_model(item["type"])(
                        self.form_response_body(item)
                        )
                    )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def create_policy_rule(
            self, policyId, policy_rule
    ):
        """
        Creates a policy rule.
        Args:
            policy_id {str}
            {policy_rule}
        Returns:
            PolicyRule
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules
            """)

        if isinstance(policy_rule, dict):
            body = policy_rule
        else:
            body = policy_rule.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, PolicyRule)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_rule_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def delete_policy_rule(
            self, policyId, ruleId
    ):
        """
        Removes a policy rule.
        Args:
            policy_id {str}
            rule_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def get_policy_rule(
            self, policyId, ruleId
    ):
        """
        Gets a policy rule.
        Args:
            policy_id {str}
            rule_id {str}
        Returns:
            PolicyRule
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, PolicyRule)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_rule_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_policy_rule(
            self, policyId, ruleId, policy_rule
    ):
        """
        Updates a policy rule.
        Args:
            policy_id {str}
            rule_id {str}
            {policy_rule}
        Returns:
            PolicyRule
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
            """)

        if isinstance(policy_rule, dict):
            body = policy_rule
        else:
            body = policy_rule.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, PolicyRule)

        if error:
            return (None, response, error)

        try:
            body = self.form_response_body(response.get_body())
            result = find_policy_rule_model(body["type"])(body)
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def activate_policy_rule(
            self, policyId, ruleId
    ):
        """
        Activates a policy rule.
        Args:
            policy_id {str}
            rule_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
                /lifecycle/activate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)

    async def deactivate_policy_rule(
            self, policyId, ruleId
    ):
        """
        Deactivates a policy rule.
        Args:
            policy_id {str}
            rule_id {str}
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
                /lifecycle/deactivate
            """)

        body = {}
        headers = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (response, error)

        return (response, None)
