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


class PolicyRule:
    def __init__(self):
        pass

    # Updates a policy rule.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
            """)

        body = policy_rule
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        try:
            result = PolicyRule(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Removes a policy rule.
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
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/policies/{policyId}/rules/{ruleId}
            """)

        body = None
        headers = None

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers
        )

        if error:
            return (None, error)

        response, error = await self._request_executor\
            .execute(request)

        if error:
            return (None, error)
        return (response, None)


# End of File Generation
