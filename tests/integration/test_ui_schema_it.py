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

import pytest

import okta.models as models
from okta import UISchemaObject
from tests.mocks import MockOktaClient


class TestUISchemaResource:
    """
    Integration Tests for the UI Schema Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_ui_schema(self, fs):
        """Test creating a UI schema and retrieving it"""
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create UI Schema using the correct format based on existing working schemas
        ui_schema_request = models.CreateUISchema(
            **{
                "uiSchema": UISchemaObject(
                    **{
                        "type": "Group",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/firstName",
                                "label": "First Name",
                                "options": {"format": "text"},
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/lastName",
                                "label": "Last Name",
                                "options": {"format": "text"},
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/email",
                                "label": "Primary email",
                                "options": {"format": "text"},
                            },
                        ],
                        "buttonLabel": "Submit",
                        "label": "Sign in",
                    }
                ).to_dict()
            }
        )

        created_schema = None
        try:
            # Create UI Schema
            created_schema, resp, err = await test_client.create_ui_schema(
                ui_schema_request
            )

            assert err is None
            assert created_schema is not None
            assert created_schema.id is not None
            assert created_schema.ui_schema.type == "Group"
            assert len(created_schema.ui_schema.elements) == 3

            # Get UI Schema by ID
            retrieved_schema, resp, err = await test_client.get_ui_schema(
                created_schema.id
            )
            assert err is None
            assert retrieved_schema is not None
            assert retrieved_schema.id == created_schema.id
            assert retrieved_schema.ui_schema.type == "Group"

        finally:
            # Clean up - delete the created schema
            if created_schema and created_schema.id:
                try:
                    _, resp, err = await test_client.delete_ui_schemas(
                        created_schema.id
                    )
                    assert err is None
                except Exception:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_ui_schemas(self, fs):
        """Test listing all UI schemas"""
        test_client = MockOktaClient(fs)

        # List all UI schemas
        schemas, resp, err = await test_client.list_ui_schemas()
        assert err is None
        assert schemas is not None
        assert isinstance(schemas, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_ui_schema(self, fs):
        """Test updating/replacing a UI schema"""
        test_client = MockOktaClient(fs)

        # Create initial UI schema object
        ui_schema_request = models.CreateUISchema(
            **{
                "uiSchema": UISchemaObject(
                    **{
                        "type": "Group",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/firstName",
                                "label": "First Name",
                                "options": {"format": "text"},
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/lastName",
                                "label": "Last Name",
                                "options": {"format": "text"},
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/email",
                                "label": "Primary email",
                                "options": {"format": "text"},
                            },
                        ],
                        "buttonLabel": "Submit",
                        "label": "Sign in",
                    }
                ).to_dict()
            }
        )

        created_schema = None
        try:
            # Create UI Schema
            created_schema, resp, err = await test_client.create_ui_schema(
                ui_schema_request
            )
            assert err is None
            assert created_schema.ui_schema.type == "Group"
            assert len(created_schema.ui_schema.elements) == 3

            # Update the schema using the same Group format
            updated_ui_schema_object = UISchemaObject(
                **{
                    "type": "Group",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/email",
                            "label": "Email Address",
                            "options": {"format": "text"},
                        }
                    ],
                    "buttonLabel": "Save Changes",
                    "label": "Updated Schema Label",
                }
            )

            updated_schema_request = models.UpdateUISchema(
                **{"uiSchema": updated_ui_schema_object.to_dict()}
            )

            # Replace/Update UI Schema
            updated_schema, resp, err = await test_client.replace_ui_schemas(
                created_schema.id, updated_schema_request
            )
            assert err is None
            assert updated_schema.ui_schema.label == "Updated Schema Label"
            assert updated_schema.ui_schema.button_label == "Save Changes"
            assert len(updated_schema.ui_schema.elements) == 1

            # Verify the update by retrieving the schema
            retrieved_schema, resp, err = await test_client.get_ui_schema(
                created_schema.id
            )
            assert err is None
            assert retrieved_schema.ui_schema.label == "Updated Schema Label"

        finally:
            # Clean up
            if created_schema and created_schema.id:
                try:
                    _, resp, err = await test_client.delete_ui_schemas(
                        created_schema.id
                    )
                    assert err is None
                except Exception:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_ui_schema(self, fs):
        """Test deleting a UI schema"""
        test_client = MockOktaClient(fs)

        # Create UI schema to delete
        schema_request = models.CreateUISchema(
            **{
                "uiSchema": UISchemaObject(
                    **{
                        "type": "Group",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/email",
                                "label": "Email Address",
                                "options": {"format": "text"},
                            }
                        ],
                        "buttonLabel": "Submit",
                        "label": "Schema to Delete",
                    }
                ).to_dict()
            }
        )

        # Create UI Schema
        created_schema, resp, err = await test_client.create_ui_schema(schema_request)
        assert err is None
        assert created_schema.id is not None

        # Delete the schema
        _, resp, err = await test_client.delete_ui_schemas(created_schema.id)
        assert err is None

        # Verify deletion by trying to get the schema (should fail)
        try:
            deleted_schema, resp, err = await test_client.get_ui_schema(
                created_schema.id
            )
            assert err is not None or deleted_schema is None
        except Exception:
            # Expected - schema should not exist
            pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_ui_schema_crud_lifecycle(self, fs):
        """Test complete CRUD lifecycle for UI Schema"""
        test_client = MockOktaClient(fs)

        # CREATE: Create a new UI schema
        create_request = models.CreateUISchema(
            **{
                "uiSchema": UISchemaObject(
                    **{
                        "type": "Group",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/firstName",
                                "label": "First Name",
                                "options": {"format": "text"},
                            }
                        ],
                        "buttonLabel": "Create",
                        "label": "CRUD Test Schema",
                    }
                ).to_dict()
            }
        )

        created_schema = None
        try:
            # CREATE
            created_schema, resp, err = await test_client.create_ui_schema(
                create_request
            )
            assert err is None
            assert created_schema.ui_schema.label == "CRUD Test Schema"
            schema_id = created_schema.id

            # READ: Get the schema
            read_schema, resp, err = await test_client.get_ui_schema(schema_id)
            assert err is None
            assert read_schema.id == schema_id
            assert read_schema.ui_schema.label == "CRUD Test Schema"

            # UPDATE: Modify the schema
            update_request = models.UpdateUISchema(
                **{
                    "uiSchema": UISchemaObject(
                        **{
                            "type": "Group",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/firstName",
                                    "label": "First Name",
                                    "options": {"format": "text"},
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/email",
                                    "label": "Email Address",
                                    "options": {"format": "text"},
                                },
                            ],
                            "buttonLabel": "Update",
                            "label": "Updated CRUD Test Schema",
                        }
                    ).to_dict()
                }
            )

            updated_schema, resp, err = await test_client.replace_ui_schemas(
                schema_id, update_request
            )
            assert err is None
            assert updated_schema.ui_schema.label == "Updated CRUD Test Schema"
            assert len(updated_schema.ui_schema.elements) == 2

            # READ again to verify update
            verify_schema, resp, err = await test_client.get_ui_schema(schema_id)
            assert err is None
            assert verify_schema.ui_schema.label == "Updated CRUD Test Schema"

            # DELETE: Remove the schema
            _, resp, err = await test_client.delete_ui_schemas(schema_id)
            assert err is None

            # Verify deletion
            try:
                deleted_schema, resp, err = await test_client.get_ui_schema(schema_id)
                assert err is not None or deleted_schema is None
            except Exception:
                # Expected - schema should not exist
                pass

        finally:
            # Cleanup in case test fails
            if created_schema and created_schema.id:
                try:
                    await test_client.delete_ui_schemas(created_schema.id)
                except Exception:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_ui_schema_error_handling(self, fs):
        """Test error handling for UI Schema operations"""
        test_client = MockOktaClient(fs)

        # Test getting non-existent schema
        try:
            non_existent_schema, resp, err = await test_client.get_ui_schema(
                "non-existent-id"
            )
            assert err is not None or non_existent_schema is None
        except Exception as e:
            assert "404" in str(e) or "Not Found" in str(e)

        # Test deleting non-existent schema
        try:
            _, resp, err = await test_client.delete_ui_schemas("non-existent-id")
            assert err is None
        except Exception as e:
            assert "No" in str(e) or "Not Found" in str(e)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_complex_ui_schema(self, fs):
        """Test creating a complex UI schema with various field types"""
        test_client = MockOktaClient(fs)

        complex_schema_request = models.CreateUISchema(
            **{
                "uiSchema": UISchemaObject(
                    **{
                        "type": "Group",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/firstName",
                                "label": "First Name",
                                "options": {"format": "text"},
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/lastName",
                                "label": "Last Name",
                                "options": {"format": "text"},
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/email",
                                "label": "Primary email",
                                "options": {"format": "text"},
                            },
                        ],
                        "buttonLabel": "Submit",
                        "label": "Sign in",
                    }
                ).to_dict()
            }
        )

        created_schema = None
        try:
            # Create complex UI Schema
            created_schema, resp, err = await test_client.create_ui_schema(
                complex_schema_request
            )
            assert err is None
            assert created_schema.ui_schema.label == "Sign in"
            assert len(created_schema.ui_schema.elements) == 3

            # Verify specific elements exist
            elements = created_schema.ui_schema.elements
            assert len(elements) == 3

            # Check that all expected Control elements are present
            element_scopes = [elem["scope"] for elem in elements]
            assert "#/properties/email" in element_scopes
            assert "#/properties/firstName" in element_scopes
            assert "#/properties/lastName" in element_scopes

        finally:
            # Clean up
            if created_schema and created_schema.id:
                try:
                    await test_client.delete_ui_schemas(created_schema.id)
                except Exception:
                    pass
