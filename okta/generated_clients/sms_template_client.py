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
from okta.utils import format_url
from okta.models.sms_template\
    import SmsTemplate


class SmsTemplateClient():
    """
    A Client object for the SmsTemplate resource.
    """
    def __init__(self):
        self._base_url = ""

    async def list_sms_templates(
            self, query_params
    ):
        """
        Enumerates custom SMS templates in your organization. A
        subset of templates can be returned that match a templ
        ate type.
        Args:
            query_params {dict}: Map of query parameters for request
            [query_params.templateType] {str}
        Returns:
            list: Collection of SmsTemplate instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/templates/sms
            """)
        encoded_query_params = urlencode(query_params)
        api_url += f"/?{encoded_query_params}"

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
        try:
            result = []
            for item in response.get_body():
                result.append(SmsTemplate(item))
        except Exception as error:
            return (None, error)

        return (result, None)

    async def create_sms_template(
            self, sms_template
    ):
        """
        Adds a new custom SMS template to your organization.
        Args:
            {sms_template}
        Returns:
            SmsTemplate
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/templates/sms
            """)

        body = sms_template.as_dict()
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
            result = SmsTemplate(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def delete_sms_template(
            self, templateId
    ):
        """
        Removes an SMS template.
        Args:
            template_id {str}
        """
        http_method = "delete".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/templates/sms/{templateId}
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

    async def get_sms_template(
            self, templateId
    ):
        """
        Fetches a specific template by `id`
        Args:
            template_id {str}
        Returns:
            SmsTemplate
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/templates/sms/{templateId}
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
        try:
            result = SmsTemplate(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def partial_update_sms_template(
            self, templateId, sms_template
    ):
        """
        Updates only some of the SMS template properties:
        Args:
            template_id {str}
            {sms_template}
        Returns:
            SmsTemplate
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/templates/sms/{templateId}
            """)

        body = sms_template.as_dict()
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
            result = SmsTemplate(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)

    async def update_sms_template(
            self, templateId, sms_template
    ):
        """
        Updates the SMS template.
        Args:
            template_id {str}
            {sms_template}
        Returns:
            SmsTemplate
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/templates/sms/{templateId}
            """)

        body = sms_template.as_dict()
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
            result = SmsTemplate(
                response.get_body()
            )
        except Exception as error:
            return (None, error)

        return (result, None)


# End of File Generation