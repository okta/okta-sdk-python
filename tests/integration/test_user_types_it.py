# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

from http import HTTPStatus

import pytest

import okta.models as models
from okta.errors.okta_api_error import OktaAPIError
from tests.mocks import MockOktaClient


class TestUserTypesResource:
    """
    Integration Tests for the User Types Resource
    """

    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_user_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create object
        TEST_DESC = f"{TestUserTypesResource.SDK_PREFIX} description"
        TEST_DISPLAY_NAME = f"{TestUserTypesResource.SDK_PREFIX} display name"
        TEST_NAME = f"{TestUserTypesResource.SDK_PREFIX}_aAaewb"
        # ^ without VCR testing, can generate random TEST_NAME suffixes

        user_type_obj = models.UserType(
            **{
                "description": TEST_DESC,
                "displayName": TEST_DISPLAY_NAME,
                "name": TEST_NAME,
            }
        )

        try:
            created, _, err = await client.create_user_type(user_type_obj)
            assert err is None
            assert created.id is not None
            assert created.description == TEST_DESC
            assert created.display_name == TEST_DISPLAY_NAME
            assert created.name == TEST_NAME

        finally:
            _, _, err = await client.delete_user_type(created.id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_user_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create object
        TEST_DESC = f"{TestUserTypesResource.SDK_PREFIX} description"
        TEST_DISPLAY_NAME = f"{TestUserTypesResource.SDK_PREFIX} display name"
        TEST_NAME = f"{TestUserTypesResource.SDK_PREFIX}_akIKx"
        # ^ without VCR testing, can generate random TEST_NAME suffixes

        user_type_obj = models.UserType(
            **{
                "description": TEST_DESC,
                "displayName": TEST_DISPLAY_NAME,
                "name": TEST_NAME,
            }
        )

        try:
            created, _, err = await client.create_user_type(user_type_obj)
            assert err is None
            assert created.id is not None

            # Retrieve
            found, _, err = await client.get_user_type(created.id)
            assert err is None
            assert found.id == created.id
            assert found.description == TEST_DESC
            assert found.display_name == TEST_DISPLAY_NAME
            assert found.name == TEST_NAME

        finally:
            _, _, err = await client.delete_user_type(created.id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_user_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create object
        TEST_DESC = f"{TestUserTypesResource.SDK_PREFIX} description"
        TEST_DISPLAY_NAME = f"{TestUserTypesResource.SDK_PREFIX} display name"
        TEST_NAME = f"{TestUserTypesResource.SDK_PREFIX}_JWXbL"
        # ^ without VCR testing, can generate random TEST_NAME suffixes

        user_type_obj = models.UserType(
            **{
                "description": TEST_DESC,
                "displayName": TEST_DISPLAY_NAME,
                "name": TEST_NAME,
            }
        )

        try:
            created, _, err = await client.create_user_type(user_type_obj)
            assert err is None
            assert created.id is not None

            # Update
            UPDATED_TEST_DESC = f"{TEST_DESC}-updated"
            UPDATED_TEST_DISPLAY_NAME = f"{TEST_DISPLAY_NAME}-updated"
            updated_obj = models.UserTypePostRequest(
                **{
                    "description": UPDATED_TEST_DESC,
                    "displayName": UPDATED_TEST_DISPLAY_NAME,
                }
            )
            updated, _, err = await client.update_user_type(created.id, updated_obj)
            assert err is None
            assert updated.id == created.id
            assert updated.description == UPDATED_TEST_DESC
            assert updated.display_name == UPDATED_TEST_DISPLAY_NAME

            # Retrieve
            found, _, err = await client.get_user_type(created.id)
            assert err is None
            assert found.id == created.id
            assert found.description == UPDATED_TEST_DESC
            assert found.display_name == UPDATED_TEST_DISPLAY_NAME

        finally:
            _, _, err = await client.delete_user_type(created.id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_replace_user_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create object
        TEST_DESC = f"{TestUserTypesResource.SDK_PREFIX} description"
        TEST_DISPLAY_NAME = f"{TestUserTypesResource.SDK_PREFIX} display name"
        TEST_NAME = f"{TestUserTypesResource.SDK_PREFIX}_XfloX"
        # ^ without VCR testing, can generate random TEST_NAME suffixes

        user_type_obj = models.UserType(
            **{
                "description": TEST_DESC,
                "displayName": TEST_DISPLAY_NAME,
                "name": TEST_NAME,
            }
        )

        try:
            created, _, err = await client.create_user_type(user_type_obj)
            assert err is None
            assert created.id is not None

            # Replace
            REPLACED_TEST_DESC = f"{TEST_DESC}-replaced"
            REPLACED_TEST_DISPLAY_NAME = f"{TEST_DISPLAY_NAME}-replaced"
            replaced_obj = models.UserTypePutRequest(
                **{
                    "description": REPLACED_TEST_DESC,
                    "displayName": REPLACED_TEST_DISPLAY_NAME,
                    "name": TEST_NAME,
                }
            )
            replaced, _, err = await client.replace_user_type(created.id, replaced_obj)
            assert err is None
            assert replaced.id == created.id
            assert replaced.description == REPLACED_TEST_DESC
            assert replaced.display_name == REPLACED_TEST_DISPLAY_NAME
            assert replaced.name == TEST_NAME

            # Retrieve
            found, _, err = await client.get_user_type(created.id)
            assert err is None
            assert found.id == created.id
            assert found.description == REPLACED_TEST_DESC
            assert found.display_name == REPLACED_TEST_DISPLAY_NAME
            assert found.name == TEST_NAME

        finally:
            _, _, err = await client.delete_user_type(created.id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_user_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create object
        TEST_DESC = f"{TestUserTypesResource.SDK_PREFIX} description"
        TEST_DISPLAY_NAME = f"{TestUserTypesResource.SDK_PREFIX} display name"
        TEST_NAME = f"{TestUserTypesResource.SDK_PREFIX}_zEVAT"
        # ^ without VCR testing, can generate random TEST_NAME suffixes

        user_type_obj = models.UserType(
            **{
                "description": TEST_DESC,
                "displayName": TEST_DISPLAY_NAME,
                "name": TEST_NAME,
            }
        )

        try:
            created, _, err = await client.create_user_type(user_type_obj)
            assert err is None
            assert created.id is not None

            # Retrieve
            found, _, err = await client.get_user_type(created.id)
            assert err is None
            assert found.id == created.id
            assert found.description == TEST_DESC
            assert found.display_name == TEST_DISPLAY_NAME
            assert found.name == TEST_NAME

            # Delete
            _, _, err = await client.delete_user_type(created.id)
            assert err is None

            # Retrieve
            found, resp, err = await client.get_user_type(created.id)
            assert err is not None
            assert isinstance(err, OktaAPIError)
            assert resp.status == HTTPStatus.NOT_FOUND
        finally:
            try:
                _, _, err = await client.delete_user_type(created.id)
            except Exception:
                pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_user_types(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create object
        TEST_DESC = f"{TestUserTypesResource.SDK_PREFIX} description"
        TEST_DISPLAY_NAME = f"{TestUserTypesResource.SDK_PREFIX} display name"
        TEST_NAME = f"{TestUserTypesResource.SDK_PREFIX}_cRuLD"
        TEST_DESC_2 = f"{TestUserTypesResource.SDK_PREFIX} description-2"
        TEST_DISPLAY_NAME_2 = f"{TestUserTypesResource.SDK_PREFIX} dn-2"
        TEST_NAME_2 = f"{TestUserTypesResource.SDK_PREFIX}_cRuLD_2"
        # ^ without VCR testing, can generate random TEST_NAME suffixes

        user_type_obj = models.UserType(
            **{
                "description": TEST_DESC,
                "displayName": TEST_DISPLAY_NAME,
                "name": TEST_NAME,
            }
        )
        user_type_obj_2 = models.UserType(
            **{
                "description": TEST_DESC_2,
                "displayName": TEST_DISPLAY_NAME_2,
                "name": TEST_NAME_2,
            }
        )

        try:
            ut1, _, err = await client.create_user_type(user_type_obj)
            assert err is None
            assert ut1.id is not None
            ut2, _, err = await client.create_user_type(user_type_obj_2)
            assert err is None
            assert ut2.id is not None

            # List
            user_types, _, err = await client.list_user_types()
            assert err is None
            assert len(user_types) > 0
            assert next((ut for ut in user_types if ut.id == ut1.id))
            assert next((ut for ut in user_types if ut.id == ut2.id))

        finally:
            errors = []
            try:
                _, _, err = await client.delete_user_type(ut1.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            try:
                _, _, err = await client.delete_user_type(ut2.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0
