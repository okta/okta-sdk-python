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


class GroupRule:
    def __init__(self, config=None):
        if config:
            self.actions = config["actions"]
            self.conditions = config["conditions"]
            self.created = config["created"]
            self.id = config["id"]
            self.last_updated = config["lastUpdated"]
            self.name = config["name"]
            self.status = config["status"]
            self.type = config["type"]
        else:
            self.actions = None
            self.conditions = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
            self.type = None

    # Updates a group rule. Only &#x60;INACTIVE&#x60; rules can be updated.
    async def update_group_rule(
            self, ruleId, group_rule
    ):
        """
            Updates a group rule. Only `INACTIVE` rules can be upda
        ted.
        Args:
            rule_id {str}
            {group_rule}
        Returns:
            GroupRule
        """
        http_method = "put".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}
            """)

        body = group_rule
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
            result = GroupRule(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    # Removes a specific group rule by id from your organization
    async def delete_group_rule(
            self, ruleId
    ):
        """
            Removes a specific group rule by id from your organizat
        ion
        Args:
            rule_id {str}
        """
        http_method = "delete".upper()
        api_url = self.format_url(f"""
            {self._base_url}
            /api/v1/groups/rules/{ruleId}
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
