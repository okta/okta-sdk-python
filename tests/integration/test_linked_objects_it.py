import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestLinkedObjectsResource:
    """
    Integration Tests for the Linked Objects Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_add_get_linked_object(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Add Linked Object definition
        linked_object_model = models.LinkedObject({
            "primary": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_primary_test",
                "title": "Primary",
                "description": "Primary Link Property",
                "type": models.LinkedObjectDetailsType.USER
            }),
            "associated": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_assoc_test",
                "title": "Associated",
                "description": "Associated Link Property",
                "type": models.LinkedObjectDetailsType.USER
            })
        })

        created_linked_object_definition, _, err = await client.\
            add_linked_object_definition(linked_object_model)
        assert err is None
        assert isinstance(created_linked_object_definition,
                          models.LinkedObject)
        assert created_linked_object_definition.primary
        assert created_linked_object_definition.associated

        # Retrieve by Primary Name
        retrieved_linked_object_definition, _, err = await \
            client.get_linked_object_definition(
                linked_object_model.primary.name)
        assert err is None
        assert isinstance(retrieved_linked_object_definition,
                          models.LinkedObject)
        assert retrieved_linked_object_definition.primary.name ==\
            created_linked_object_definition.primary.name
        assert retrieved_linked_object_definition.associated.name ==\
            created_linked_object_definition.associated.name
        assert retrieved_linked_object_definition.primary.title ==\
            created_linked_object_definition.primary.title
        assert retrieved_linked_object_definition.associated.title ==\
            created_linked_object_definition.associated.title
        assert retrieved_linked_object_definition.primary.type ==\
            created_linked_object_definition.primary.type
        assert retrieved_linked_object_definition.associated.type ==\
            created_linked_object_definition.associated.type

        # Retrieve by Associated Name
        retrieved_linked_object_definition, _, err = await \
            client.get_linked_object_definition(
                linked_object_model.associated.name)
        assert err is None
        assert isinstance(retrieved_linked_object_definition,
                          models.LinkedObject)
        assert retrieved_linked_object_definition.primary.name ==\
            created_linked_object_definition.primary.name
        assert retrieved_linked_object_definition.associated.name ==\
            created_linked_object_definition.associated.name
        assert retrieved_linked_object_definition.primary.title ==\
            created_linked_object_definition.primary.title
        assert retrieved_linked_object_definition.associated.title ==\
            created_linked_object_definition.associated.title
        assert retrieved_linked_object_definition.primary.type ==\
            created_linked_object_definition.primary.type
        assert retrieved_linked_object_definition.associated.type ==\
            created_linked_object_definition.associated.type

        # Delete Linked Object definition
        _, err = await \
            client.delete_linked_object_definition(
                linked_object_model.primary.name)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_all_linked_objects(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Add Linked Object definition
        linked_object_model_1 = models.LinkedObject({
            "primary": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_primary_t1",
                "title": "Primary",
                "description": "Primary Link Property",
                "type": models.LinkedObjectDetailsType.USER
            }),
            "associated": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_assoc_t1",
                "title": "Associated",
                "description": "Associated Link Property",
                "type": models.LinkedObjectDetailsType.USER
            })
        })

        linked_object_model_2 = models.LinkedObject({
            "primary": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_primary_t2",
                "title": "Primary",
                "description": "Primary Link Property",
                "type": models.LinkedObjectDetailsType.USER
            }),
            "associated": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_assoc_t2",
                "title": "Associated",
                "description": "Associated Link Property",
                "type": models.LinkedObjectDetailsType.USER
            })
        })

        created_linked_object_definition, _, err = await client.\
            add_linked_object_definition(linked_object_model_1)
        assert err is None
        assert isinstance(created_linked_object_definition,
                          models.LinkedObject)
        assert created_linked_object_definition.primary
        assert created_linked_object_definition.associated

        created_linked_object_definition_2, _, err = await client.\
            add_linked_object_definition(linked_object_model_2)
        assert err is None
        assert isinstance(created_linked_object_definition_2,
                          models.LinkedObject)
        assert created_linked_object_definition_2.primary
        assert created_linked_object_definition_2.associated

        # List
        all_linked_obj_defs, _, err = await\
            client.list_linked_object_definitions()
        assert err is None
        assert len(all_linked_obj_defs) > 0
        assert next((lo for lo in all_linked_obj_defs
                     if linked_object_model_1.primary.name == lo.primary.name))
        assert next((lo for lo in all_linked_obj_defs
                     if linked_object_model_2.primary.name == lo.primary.name))

        # Delete Linked Object definition
        _, err = await \
            client.delete_linked_object_definition(
                linked_object_model_1.primary.name)
        _, err = await \
            client.delete_linked_object_definition(
                linked_object_model_2.primary.name)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_linked_object(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Add Linked Object definition
        linked_object_model = models.LinkedObject({
            "primary": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_primary_test",
                "title": "Primary",
                "description": "Primary Link Property",
                "type": models.LinkedObjectDetailsType.USER
            }),
            "associated": models.LinkedObjectDetails({
                "name": f"{TestLinkedObjectsResource.SDK_PREFIX}_assoc_test",
                "title": "Associated",
                "description": "Associated Link Property",
                "type": models.LinkedObjectDetailsType.USER
            })
        })

        created_linked_object_definition, _, err = await client.\
            add_linked_object_definition(linked_object_model)
        assert err is None
        assert isinstance(created_linked_object_definition,
                          models.LinkedObject)
        assert created_linked_object_definition.primary
        assert created_linked_object_definition.associated

        # Retrieve by Primary Name
        retrieved_linked_object_definition, _, err = await \
            client.get_linked_object_definition(
                linked_object_model.primary.name)
        assert err is None
        assert isinstance(retrieved_linked_object_definition,
                          models.LinkedObject)
        assert retrieved_linked_object_definition.primary.name ==\
            created_linked_object_definition.primary.name
        assert retrieved_linked_object_definition.associated.name ==\
            created_linked_object_definition.associated.name
        assert retrieved_linked_object_definition.primary.title ==\
            created_linked_object_definition.primary.title
        assert retrieved_linked_object_definition.associated.title ==\
            created_linked_object_definition.associated.title
        assert retrieved_linked_object_definition.primary.type ==\
            created_linked_object_definition.primary.type
        assert retrieved_linked_object_definition.associated.type ==\
            created_linked_object_definition.associated.type

        # Delete Linked Object definition
        _, err = await \
            client.delete_linked_object_definition(
                linked_object_model.primary.name)

        # Retrieve by Primary Name
        retrieved_linked_object_definition, resp, err = await \
            client.get_linked_object_definition(
                linked_object_model.primary.name)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_linked_object_definition is None
