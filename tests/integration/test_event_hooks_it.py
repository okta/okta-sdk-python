import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestEventHooksResource:
    """
    Integration Tests for the Event Hooks Resource
    """
    SDK_PREFIX = "python_sdk"
    EVENT_TYPE = "EVENT_TYPE"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_event_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # create Event Hook
        event_hook_model = models.EventHook({
            "name": TestEventHooksResource.EVENT_TYPE,
            "events": models.EventSubscriptions({
                "items": ["user.lifecycle.create",
                          "user.lifecycle.activate"],
                "type": TestEventHooksResource.EVENT_TYPE
            }),
            "channel": models.EventHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.EventHookChannelConfig({
                    "uri": "https://www.example.com/eventHooks",
                    "headers": [
                        models.EventHookChannelConfigHeader({
                            "key": "X-Test-Header",
                            "value": "Test Header value"
                        })
                    ],
                    "authScheme": models.EventHookChannelConfigAuthScheme({
                        "key": "Authorization",
                        "value": "Test-API-Key",
                        "type": models.EventHookChannelConfigAuthSchemeType
                        .HEADER
                    })
                })
            })
        })

        created_event_hook, _, err = await client.create_event_hook(
            event_hook_model)
        # Verify details
        assert err is None
        assert isinstance(created_event_hook, models.EventHook)
        assert created_event_hook.id is not None
        assert created_event_hook.name == event_hook_model.name
        assert created_event_hook.events is not None
        assert len(created_event_hook.events.items) == 2
        assert created_event_hook.channel is not None
        assert created_event_hook.channel.config.uri ==\
            event_hook_model.channel.config.uri
        assert len(created_event_hook.channel.config.headers) == 1
        assert isinstance(created_event_hook.channel.config.headers[0],
                          models.EventHookChannelConfigHeader)

        # Retrieve
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name

        # Deactivate + Delete
        _, _, err = await client.deactivate_event_hook(created_event_hook.id)
        assert err is None
        _, err = await client.delete_event_hook(created_event_hook.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_event_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # create Event Hook
        event_hook_model = models.EventHook({
            "name": TestEventHooksResource.EVENT_TYPE,
            "events": models.EventSubscriptions({
                "items": ["user.lifecycle.create",
                          "user.lifecycle.activate"],
                "type": TestEventHooksResource.EVENT_TYPE
            }),
            "channel": models.EventHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.EventHookChannelConfig({
                    "uri": "https://www.example.com/eventHooks",
                    "headers": [
                        models.EventHookChannelConfigHeader({
                            "key": "X-Test-Header",
                            "value": "Test Header value"
                        })
                    ],
                    "authScheme": models.EventHookChannelConfigAuthScheme({
                        "key": "Authorization",
                        "value": "Test-API-Key",
                        "type": models.EventHookChannelConfigAuthSchemeType
                        .HEADER
                    })
                })
            })
        })

        created_event_hook, _, err = await client.create_event_hook(
            event_hook_model)
        # Verify details
        assert err is None
        assert isinstance(created_event_hook, models.EventHook)
        assert created_event_hook.id is not None
        assert created_event_hook.name == event_hook_model.name
        assert created_event_hook.events is not None
        assert len(created_event_hook.events.items) == 2
        assert created_event_hook.channel is not None
        assert created_event_hook.channel.config.uri ==\
            event_hook_model.channel.config.uri

        # Retrieve
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name

        # Update
        updated_event_hook_model = models.EventHook({
            "name": TestEventHooksResource.EVENT_TYPE,
            "events": models.EventSubscriptions({
                "items": ["user.lifecycle.create",
                          "user.lifecycle.activate",
                          "user.lifecycle.deactivate"],  # new
                "type": TestEventHooksResource.EVENT_TYPE
            }),
            "channel": models.EventHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.EventHookChannelConfig({
                    "uri": "https://www.example.com/eventHooks-UPDATE",  # new
                    "headers": [
                        models.EventHookChannelConfigHeader({
                            "key": "X-Test-Header",
                            "value": "Test Header value updated"  # new
                        })
                    ],
                    "authScheme": models.EventHookChannelConfigAuthScheme({
                        "key": "Authorization",
                        "value": "Test-API-Key-updated",  # new
                        "type": models.EventHookChannelConfigAuthSchemeType
                        .HEADER
                    })
                })
            })
        })
        updated_event_hook, _, err = await client.update_event_hook(
            created_event_hook.id, updated_event_hook_model
        )
        assert err is None
        assert isinstance(updated_event_hook, models.EventHook)
        assert updated_event_hook.id == created_event_hook.id

        # Retrieve for validation
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == updated_event_hook.id
        assert retrieved_event_hook.name == updated_event_hook.name
        assert len(retrieved_event_hook.events.items) > len(
            created_event_hook.events.items)
        assert len(retrieved_event_hook.events.items) == 3
        assert "user.lifecycle.deactivate" in retrieved_event_hook.events.items
        assert retrieved_event_hook.channel.config.uri == \
            "https://www.example.com/eventHooks-UPDATE"

        # Deactivate + Delete
        _, _, err = await client.deactivate_event_hook(created_event_hook.id)
        assert err is None
        _, err = await client.delete_event_hook(created_event_hook.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_event_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # create Event Hook
        event_hook_model = models.EventHook({
            "name": TestEventHooksResource.EVENT_TYPE,
            "events": models.EventSubscriptions({
                "items": ["user.lifecycle.create",
                          "user.lifecycle.activate"],
                "type": TestEventHooksResource.EVENT_TYPE
            }),
            "channel": models.EventHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.EventHookChannelConfig({
                    "uri": "https://www.example.com/eventHooks",
                    "headers": [
                        models.EventHookChannelConfigHeader({
                            "key": "X-Test-Header",
                            "value": "Test Header value"
                        })
                    ],
                    "authScheme": models.EventHookChannelConfigAuthScheme({
                        "key": "Authorization",
                        "value": "Test-API-Key",
                        "type": models.EventHookChannelConfigAuthSchemeType
                        .HEADER
                    })
                })
            })
        })

        created_event_hook, _, err = await client.create_event_hook(
            event_hook_model)
        # Verify details
        assert err is None
        assert isinstance(created_event_hook, models.EventHook)
        assert created_event_hook.id is not None
        assert created_event_hook.name == event_hook_model.name
        assert created_event_hook.events is not None
        assert len(created_event_hook.events.items) == 2
        assert created_event_hook.channel is not None
        assert created_event_hook.channel.config.uri ==\
            event_hook_model.channel.config.uri

        # Retrieve
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name

        # Deactivate + Delete
        _, _, err = await client.deactivate_event_hook(created_event_hook.id)
        assert err is None
        _, err = await client.delete_event_hook(created_event_hook.id)
        assert err is None

        # Retrieve for validation
        retrieved_event_hook, resp, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_event_hook is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_event_hooks(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        EVENT_HOOKS_COUNT = 3
        # Keep IDs
        created_event_hook_ids = []

        # create Event Hooks
        for index in range(EVENT_HOOKS_COUNT):
            event_hook_model = models.EventHook({
                "name": TestEventHooksResource.EVENT_TYPE + str(index),
                "events": models.EventSubscriptions({
                    "items": ["user.lifecycle.create",
                              "user.lifecycle.activate"],
                    "type": TestEventHooksResource.EVENT_TYPE
                }),
                "channel": models.EventHookChannel({
                    "type": "HTTP",
                    "version": "1.0.0",
                    "config": models.EventHookChannelConfig({
                        "uri": "https://www.example.com/eventHooks",
                        "headers": [
                            models.EventHookChannelConfigHeader({
                                "key": "X-Test-Header",
                                "value": "Test Header value"
                            })
                        ],
                        "authScheme": models.EventHookChannelConfigAuthScheme({
                            "key": "Authorization",
                            "value": "Test-API-Key",
                            "type": models.EventHookChannelConfigAuthSchemeType
                            .HEADER
                        })
                    })
                })
            })

            created_event_hook, _, err = await client.create_event_hook(
                event_hook_model)
            # Verify details
            assert err is None
            assert isinstance(created_event_hook, models.EventHook)
            assert created_event_hook.id is not None
            assert created_event_hook.name == event_hook_model.name
            assert created_event_hook.events is not None
            assert len(created_event_hook.events.items) == 2
            assert created_event_hook.channel is not None
            assert created_event_hook.channel.config.uri ==\
                event_hook_model.channel.config.uri
            created_event_hook_ids.append(created_event_hook.id)

        # List
        all_event_hooks, _, err = await client.list_event_hooks()
        assert err is None
        assert len(all_event_hooks) > 0
        assert len(all_event_hooks) == EVENT_HOOKS_COUNT
        for event_hook_id in created_event_hook_ids:
            assert((eh_id for eh_id in all_event_hooks
                    if eh_id.id == event_hook_id))

        # Deactivate + Delete
        for event_hook_id in created_event_hook_ids:
            _, _, err = await client.deactivate_event_hook(event_hook_id)
            assert err is None
            _, err = await client.delete_event_hook(event_hook_id)
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_deactivate_event_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # create Event Hook
        event_hook_model = models.EventHook({
            "name": TestEventHooksResource.EVENT_TYPE,
            "events": models.EventSubscriptions({
                "items": ["user.lifecycle.create",
                          "user.lifecycle.activate"],
                "type": TestEventHooksResource.EVENT_TYPE
            }),
            "channel": models.EventHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.EventHookChannelConfig({
                    "uri": "https://www.example.com/eventHooks",
                    "headers": [
                        models.EventHookChannelConfigHeader({
                            "key": "X-Test-Header",
                            "value": "Test Header value"
                        })
                    ],
                    "authScheme": models.EventHookChannelConfigAuthScheme({
                        "key": "Authorization",
                        "value": "Test-API-Key",
                        "type": models.EventHookChannelConfigAuthSchemeType
                        .HEADER
                    })
                })
            })
        })

        created_event_hook, _, err = await client.create_event_hook(
            event_hook_model)
        # Verify details
        assert err is None
        assert isinstance(created_event_hook, models.EventHook)
        assert created_event_hook.id is not None
        assert created_event_hook.name == event_hook_model.name
        assert created_event_hook.events is not None
        assert len(created_event_hook.events.items) == 2
        assert created_event_hook.channel is not None
        assert created_event_hook.channel.config.uri ==\
            event_hook_model.channel.config.uri
        assert created_event_hook.status == "ACTIVE"

        # Retrieve
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name
        assert retrieved_event_hook.status == "ACTIVE"

        # Deactivate
        _, _, err = await client.deactivate_event_hook(created_event_hook.id)
        assert err is None

        # Verify
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name
        assert retrieved_event_hook.status == "INACTIVE"

        # Delete
        _, err = await client.delete_event_hook(created_event_hook.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_event_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # create Event Hook
        event_hook_model = models.EventHook({
            "name": TestEventHooksResource.EVENT_TYPE,
            "events": models.EventSubscriptions({
                "items": ["user.lifecycle.create",
                          "user.lifecycle.activate"],
                "type": TestEventHooksResource.EVENT_TYPE
            }),
            "channel": models.EventHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.EventHookChannelConfig({
                    "uri": "https://www.example.com/eventHooks",
                    "headers": [
                        models.EventHookChannelConfigHeader({
                            "key": "X-Test-Header",
                            "value": "Test Header value"
                        })
                    ],
                    "authScheme": models.EventHookChannelConfigAuthScheme({
                        "key": "Authorization",
                        "value": "Test-API-Key",
                        "type": models.EventHookChannelConfigAuthSchemeType
                        .HEADER
                    })
                })
            })
        })

        created_event_hook, _, err = await client.create_event_hook(
            event_hook_model)
        # Verify details
        assert err is None
        assert isinstance(created_event_hook, models.EventHook)
        assert created_event_hook.id is not None
        assert created_event_hook.name == event_hook_model.name
        assert created_event_hook.events is not None
        assert len(created_event_hook.events.items) == 2
        assert created_event_hook.channel is not None
        assert created_event_hook.channel.config.uri ==\
            event_hook_model.channel.config.uri
        assert created_event_hook.status == "ACTIVE"

        # Retrieve
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name
        assert retrieved_event_hook.status == "ACTIVE"

        # Deactivate
        _, _, err = await client.deactivate_event_hook(created_event_hook.id)
        assert err is None

        # Verify
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name
        assert retrieved_event_hook.status == "INACTIVE"

        # Activate
        _, _, err = await \
            client.activate_event_hook(created_event_hook.id)
        assert err is None

        # Verify
        retrieved_event_hook, _, err = await client.get_event_hook(
            created_event_hook.id)
        assert err is None
        assert isinstance(retrieved_event_hook, models.EventHook)
        assert retrieved_event_hook.id == created_event_hook.id
        assert retrieved_event_hook.name == created_event_hook.name
        assert retrieved_event_hook.status == "ACTIVE"

        # Deactivate
        _, _, err = await client.deactivate_event_hook(created_event_hook.id)
        assert err is None
        # Delete
        _, err = await client.delete_event_hook(created_event_hook.id)
        assert err is None
