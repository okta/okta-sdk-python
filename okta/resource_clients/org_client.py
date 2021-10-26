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

from okta.models.org_setting\
    import OrgSetting
from okta.models.org_contact_type_obj\
    import OrgContactTypeObj
from okta.models.org_contact_user\
    import OrgContactUser
from okta.models.org_preferences\
    import OrgPreferences
from okta.models.org_okta_communication_setting\
    import OrgOktaCommunicationSetting
from okta.models.org_okta_support_settings_obj\
    import OrgOktaSupportSettingsObj
from okta.utils import format_url
from okta.api_client import APIClient


class OrgClient(APIClient):
    """
    A Client object for the Org resource.
    """

    def __init__(self):
        self._base_url = ""

    async def get_org_settings(
            self,
            keep_empty_params=False
    ):
        """
        Get settings of your organization.
        Args:
        Returns:
            OrgSetting
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org
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
            .execute(request, OrgSetting)

        if error:
            return (None, response, error)

        try:
            result = OrgSetting(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def partial_update_org_setting(
            self, org_setting,
            keep_empty_params=False
    ):
        """
        Partial update settings of your organization.
        Args:
            {org_setting}
        Returns:
            OrgSetting
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org
            """)

        if isinstance(org_setting, dict):
            body = org_setting
        else:
            body = org_setting.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OrgSetting)

        if error:
            return (None, response, error)

        try:
            result = OrgSetting(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_org_setting(
            self, org_setting,
            keep_empty_params=False
    ):
        """
        Update settings of your organization.
        Args:
            {org_setting}
        Returns:
            OrgSetting
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org
            """)

        if isinstance(org_setting, dict):
            body = org_setting
        else:
            body = org_setting.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OrgSetting)

        if error:
            return (None, response, error)

        try:
            result = OrgSetting(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_org_contact_types(
            self,
            keep_empty_params=False
    ):
        """
        Gets Contact Types of your organization.
        Args:
        Returns:
            list: Collection of OrgContactTypeObj instances.
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/contacts
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
            .execute(request, OrgContactTypeObj)

        if error:
            return (None, response, error)

        try:
            result = []
            for item in response.get_body():
                result.append(OrgContactTypeObj(
                    self.form_response_body(item)
                    ))
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_org_contact_user(
            self, contactType,
            keep_empty_params=False
    ):
        """
        Retrieves the URL of the User associated with the speci
        fied Contact Type.
        Args:
            contact_type {str}
        Returns:
            OrgContactUser
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/contacts/{contactType}
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
            .execute(request, OrgContactUser)

        if error:
            return (None, response, error)

        try:
            result = OrgContactUser(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_org_contact_user(
            self, contactType, user_id_string,
            keep_empty_params=False
    ):
        """
        Updates the User associated with the specified Contact
        Type.
        Args:
            contact_type {str}
            {user_id_string}
        Returns:
            OrgContactUser
        """
        http_method = "put".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/contacts/{contactType}
            """)

        if isinstance(user_id_string, dict):
            body = user_id_string
        else:
            body = user_id_string.as_dict()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        form = {}

        request, error = await self._request_executor.create_request(
            http_method, api_url, body, headers, form, keep_empty_params=keep_empty_params
        )

        if error:
            return (None, None, error)

        response, error = await self._request_executor\
            .execute(request, OrgContactUser)

        if error:
            return (None, response, error)

        try:
            result = OrgContactUser(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def update_org_logo(
            self, file,
            keep_empty_params=False
    ):
        """
        Updates the logo for your organization.
        Args:
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/logo
            """)

        body = {}
        headers = {}
        form = {
            "file": file,
        }

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

    async def get_org_preferences(
            self,
            keep_empty_params=False
    ):
        """
        Gets preferences of your organization.
        Args:
        Returns:
            OrgPreferences
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/preferences
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
            .execute(request, OrgPreferences)

        if error:
            return (None, response, error)

        try:
            result = OrgPreferences(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def hide_okta_ui_footer(
            self,
            keep_empty_params=False
    ):
        """
        Hide the Okta UI footer for all end users of your organ
        ization.
        Args:
        Returns:
            OrgPreferences
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/preferences/hideEndUserFooter
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
            .execute(request, OrgPreferences)

        if error:
            return (None, response, error)

        try:
            result = OrgPreferences(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def show_okta_ui_footer(
            self,
            keep_empty_params=False
    ):
        """
        Makes the Okta UI footer visible for all end users of y
        our organization.
        Args:
        Returns:
            OrgPreferences
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/preferences/showEndUserFooter
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
            .execute(request, OrgPreferences)

        if error:
            return (None, response, error)

        try:
            result = OrgPreferences(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_okta_communication_settings(
            self,
            keep_empty_params=False
    ):
        """
        Gets Okta Communication Settings of your organization.
        Args:
        Returns:
            OrgOktaCommunicationSetting
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaCommunication
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
            .execute(request, OrgOktaCommunicationSetting)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaCommunicationSetting(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def opt_in_users_to_okta_communication_emails(
            self,
            keep_empty_params=False
    ):
        """
        Opts in all users of this org to Okta Communication ema
        ils.
        Args:
        Returns:
            OrgOktaCommunicationSetting
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaCommunication/optIn
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
            .execute(request, OrgOktaCommunicationSetting)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaCommunicationSetting(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def opt_out_users_from_okta_communication_emails(
            self,
            keep_empty_params=False
    ):
        """
        Opts out all users of this org from Okta Communication
        emails.
        Args:
        Returns:
            OrgOktaCommunicationSetting
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaCommunication/optOut
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
            .execute(request, OrgOktaCommunicationSetting)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaCommunicationSetting(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def get_org_okta_support_settings(
            self,
            keep_empty_params=False
    ):
        """
        Gets Okta Support Settings of your organization.
        Args:
        Returns:
            OrgOktaSupportSettingsObj
        """
        http_method = "get".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaSupport
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
            .execute(request, OrgOktaSupportSettingsObj)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaSupportSettingsObj(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def extend_okta_support(
            self,
            keep_empty_params=False
    ):
        """
        Extends the length of time that Okta Support can access
        your org by 24 hours. This means that 24 hours are add
        ed to the remaining access time.
        Args:
        Returns:
            OrgOktaSupportSettingsObj
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaSupport/extend
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
            .execute(request, OrgOktaSupportSettingsObj)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaSupportSettingsObj(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def grant_okta_support(
            self,
            keep_empty_params=False
    ):
        """
        Enables you to temporarily allow Okta Support to access
        your org as an administrator for eight hours.
        Args:
        Returns:
            OrgOktaSupportSettingsObj
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaSupport/grant
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
            .execute(request, OrgOktaSupportSettingsObj)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaSupportSettingsObj(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)

    async def revoke_okta_support(
            self,
            keep_empty_params=False
    ):
        """
        Revokes Okta Support access to your organization.
        Args:
        Returns:
            OrgOktaSupportSettingsObj
        """
        http_method = "post".upper()
        api_url = format_url(f"""
            {self._base_url}
            /api/v1/org/privacy/oktaSupport/revoke
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
            .execute(request, OrgOktaSupportSettingsObj)

        if error:
            return (None, response, error)

        try:
            result = OrgOktaSupportSettingsObj(
                self.form_response_body(response.get_body())
            )
        except Exception as error:
            return (None, response, error)
        return (result, response, None)
