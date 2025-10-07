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

import copy
import random
from string import ascii_lowercase

import pytest

import okta.models as models
from tests.mocks import MockOktaClient

ADD_CUSTOM_ATTRIBUTE_DEFINITION = {
    "custom": {"id": "#custom", "type": "object", "properties": {"required": []}}
}

REMOVE_CUSTOM_ATTRIBUTE_DEFINITION = {
    "custom": {"id": "#custom", "type": "object", "properties": {}}
}

CUSTOM_ATTRIBUTE_PROPERTIES = {
    "title": "Test Custom Attribute",
    "description": "Custom attribute for testing purposes",
    "type": "string",
    "required": False,
    "minLength": 1,
    "maxLength": 20,
    "permissions": [{"principal": "SELF", "action": "READ_WRITE"}],
}


class TestGroupSchemaResource:
    """
    Integration Tests for the Group Schema Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_group_schema(self, fs):
        client = MockOktaClient(fs)
        resp, _, err = await client.get_group_schema()
        assert err is None
        assert isinstance(resp, models.GroupSchema)
        assert isinstance(resp.definitions, models.GroupSchemaDefinitions)
        assert isinstance(resp.definitions.base, models.GroupSchemaBase)
        assert isinstance(
            resp.definitions.base.properties, models.GroupSchemaBaseProperties
        )
        assert resp.var_schema == "http://json-schema.org/draft-04/schema#"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_add_and_remove_custom_attribute(self, fs):
        client = MockOktaClient(fs)

        # make random custom attribute name, because it takes some time for cleanup
        random.seed(2021)
        custom_attribute_name = "".join(
            [ascii_lowercase[random.randint(0, 25)] for i in range(20)]
        )
        definition = copy.deepcopy(ADD_CUSTOM_ATTRIBUTE_DEFINITION)
        definition["custom"]["properties"][
            custom_attribute_name
        ] = CUSTOM_ATTRIBUTE_PROPERTIES
        group_schema = models.GroupSchema(
            **{
                "id": "#custom",
                "type": "object",
                "properties": {
                    "required": [],
                    custom_attribute_name: CUSTOM_ATTRIBUTE_PROPERTIES,
                },
            }
        )

        try:
            resp, _, err = await client.update_group_schema(group_schema)
            assert err is None
            assert custom_attribute_name in resp.definitions.custom.properties

        finally:
            definition = copy.deepcopy(REMOVE_CUSTOM_ATTRIBUTE_DEFINITION)
            definition["custom"]["properties"][custom_attribute_name] = None
            group_schema = models.GroupSchema(
                **{
                    "id": "#custom",
                    "type": "object",
                    "properties": {custom_attribute_name: None},
                }
            )
            resp, _, err = await client.update_group_schema(group_schema)
            assert err is None
            assert custom_attribute_name not in resp.definitions.custom.properties

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_custom_attribute(self, fs):
        client = MockOktaClient(fs)

        # make random custom attribute name, because it takes some time for cleanup
        random.seed(2021)
        custom_attribute_name = "".join(
            [ascii_lowercase[random.randint(0, 25)] for i in range(20)]
        )
        definition = copy.deepcopy(ADD_CUSTOM_ATTRIBUTE_DEFINITION)
        definition["custom"]["properties"][
            custom_attribute_name
        ] = CUSTOM_ATTRIBUTE_PROPERTIES
        group_schema = models.GroupSchema(
            **{
                "id": "#custom",
                "type": "object",
                "properties": {
                    "required": [],
                    custom_attribute_name: CUSTOM_ATTRIBUTE_PROPERTIES,
                },
            }
        )

        try:
            resp, _, err = await client.update_group_schema(group_schema)
            assert err is None
            assert custom_attribute_name in resp.definitions.custom.properties
            assert (
                    resp.definitions.custom.properties[custom_attribute_name].title
                    == "Test Custom Attribute"
            )

            # update custom attribute
            resp.definitions.custom.properties[custom_attribute_name].title = (
                "New Title"
            )
            resp, _, err = await client.update_group_schema(resp)
            assert err is None
            assert (
                    resp.definitions.custom.properties[custom_attribute_name].title
                    == "New Title"
            )

        finally:
            definition = copy.deepcopy(REMOVE_CUSTOM_ATTRIBUTE_DEFINITION)
            definition["custom"]["properties"][custom_attribute_name] = None
            group_schema = models.GroupSchema(
                **{
                    "id": "#custom",
                    "type": "object",
                    "properties": {custom_attribute_name: None},
                }
            )
            resp, _, err = await client.update_group_schema(group_schema)
            assert err is None
            assert custom_attribute_name not in resp.definitions.custom.properties
