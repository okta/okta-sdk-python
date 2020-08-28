import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestInlineHooksResource:
    """
    Integration Tests for the Inline Hooks Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_inline_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Inline Hook
        inline_hook_model = models.InlineHook({
            "name": f"{TestInlineHooksResource.SDK_PREFIX} Test Inline Hook",
            "version": "1.0.0",
            "type": models.InlineHookType.COM_OKTA_OAUTH_2_TOKENS_TRANSFORM,
            "channel": models.InlineHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.InlineHookChannelConfig({
                    "uri": "https://www.example.com/inlineHook",
                    "headers": [
                        models.InlineHookChannelConfigHeaders({
                            "key": "X-Test-Header",
                            "value": "Test Header Value"
                        })
                    ],
                    "authScheme": models.InlineHookChannelConfigAuthScheme({
                        "type": "HEADER",
                        "key": "Authorization",
                        "value": "Test-Api-Key"
                    })
                })
            })
        })

        created_inline_hook, _, err = await \
            client.create_inline_hook(inline_hook_model)
        assert err is None
        assert isinstance(created_inline_hook, models.InlineHook)
        assert created_inline_hook.id
        assert created_inline_hook.name == inline_hook_model.name
        assert created_inline_hook.channel
        assert created_inline_hook.channel.config
        assert created_inline_hook.channel.config.uri ==\
            inline_hook_model.channel.config.uri

        # Retrieve
        retrieved_inline_hook, _, err = await \
            client.get_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(retrieved_inline_hook, models.InlineHook)
        assert retrieved_inline_hook.id == created_inline_hook.id
        assert retrieved_inline_hook.name == created_inline_hook.name

        # Deactivate & Delete
        deactivated_inline_hook, _, err = await \
            client.deactivate_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(deactivated_inline_hook, models.InlineHook)
        assert deactivated_inline_hook.status == "INACTIVE"

        _, err = await client.delete_inline_hook(created_inline_hook.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_inline_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Inline Hook
        inline_hook_model = models.InlineHook({
            "name": f"{TestInlineHooksResource.SDK_PREFIX} Test Inline Hook",
            "version": "1.0.0",
            "type": models.InlineHookType.COM_OKTA_OAUTH_2_TOKENS_TRANSFORM,
            "channel": models.InlineHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.InlineHookChannelConfig({
                    "uri": "https://www.example.com/inlineHook",
                    "headers": [
                        models.InlineHookChannelConfigHeaders({
                            "key": "X-Test-Header",
                            "value": "Test Header Value"
                        })
                    ],
                    "authScheme": models.InlineHookChannelConfigAuthScheme({
                        "type": "HEADER",
                        "key": "Authorization",
                        "value": "Test-Api-Key"
                    })
                })
            })
        })

        created_inline_hook, _, err = await \
            client.create_inline_hook(inline_hook_model)
        assert err is None
        assert isinstance(created_inline_hook, models.InlineHook)
        assert created_inline_hook.id
        assert created_inline_hook.name == inline_hook_model.name
        assert created_inline_hook.channel
        assert created_inline_hook.channel.config
        assert created_inline_hook.channel.config.uri ==\
            inline_hook_model.channel.config.uri

        # Update
        updated_inline_hook_model = models.InlineHook({
            "name": inline_hook_model.name + "UPDATE",
            "version": "1.0.0",
            "type": models.InlineHookType.COM_OKTA_OAUTH_2_TOKENS_TRANSFORM,
            "channel": models.InlineHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.InlineHookChannelConfig({
                    "uri": inline_hook_model.channel.config.uri + "UPDATE",
                    "headers": [
                        models.InlineHookChannelConfigHeaders({
                            "key": "X-Test-Header",
                            "value": "Test Header Value UPDATE"
                        })
                    ],
                    "authScheme": models.InlineHookChannelConfigAuthScheme({
                        "type": "HEADER",
                        "key": "Authorization",
                        "value": "Test-Api-Key-UPDATE"
                    })
                })
            })
        })
        updated_inline_hook, _, err = await \
            client.update_inline_hook(
                created_inline_hook.id, updated_inline_hook_model)
        assert err is None
        assert updated_inline_hook.id == created_inline_hook.id
        assert updated_inline_hook.name == updated_inline_hook_model.name
        assert updated_inline_hook.channel.config.uri == \
            updated_inline_hook_model.channel.config.uri

        # Retrieve
        retrieved_inline_hook, _, err = await \
            client.get_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(retrieved_inline_hook, models.InlineHook)
        assert retrieved_inline_hook.id == created_inline_hook.id
        assert retrieved_inline_hook.name == updated_inline_hook.name
        assert retrieved_inline_hook.version == created_inline_hook.version
        assert retrieved_inline_hook.type ==\
            models.InlineHookType.COM_OKTA_OAUTH_2_TOKENS_TRANSFORM
        assert retrieved_inline_hook.channel.config.uri ==\
            updated_inline_hook.channel.config.uri

        # Deactivate & Delete
        deactivated_inline_hook, _, err = await \
            client.deactivate_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(deactivated_inline_hook, models.InlineHook)
        assert deactivated_inline_hook.status == "INACTIVE"

        _, err = await client.delete_inline_hook(created_inline_hook.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_inline_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Inline Hook
        inline_hook_model = models.InlineHook({
            "name": f"{TestInlineHooksResource.SDK_PREFIX} Test Inline Hook",
            "version": "1.0.0",
            "type": models.InlineHookType.COM_OKTA_OAUTH_2_TOKENS_TRANSFORM,
            "channel": models.InlineHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.InlineHookChannelConfig({
                    "uri": "https://www.example.com/inlineHook",
                    "headers": [
                        models.InlineHookChannelConfigHeaders({
                            "key": "X-Test-Header",
                            "value": "Test Header Value"
                        })
                    ],
                    "authScheme": models.InlineHookChannelConfigAuthScheme({
                        "type": "HEADER",
                        "key": "Authorization",
                        "value": "Test-Api-Key"
                    })
                })
            })
        })

        created_inline_hook, _, err = await \
            client.create_inline_hook(inline_hook_model)
        assert err is None
        assert isinstance(created_inline_hook, models.InlineHook)
        assert created_inline_hook.id
        assert created_inline_hook.name == inline_hook_model.name
        assert created_inline_hook.channel
        assert created_inline_hook.channel.config
        assert created_inline_hook.channel.config.uri ==\
            inline_hook_model.channel.config.uri

        # Deactivate & Delete
        deactivated_inline_hook, _, err = await \
            client.deactivate_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(deactivated_inline_hook, models.InlineHook)
        assert deactivated_inline_hook.status == "INACTIVE"

        _, err = await client.delete_inline_hook(created_inline_hook.id)
        assert err is None

        # Retrieve
        retrieved_inline_hook, resp, err = await \
            client.get_inline_hook(created_inline_hook.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_inline_hook is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_deactivate_inline_hook(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Inline Hook
        inline_hook_model = models.InlineHook({
            "name": f"{TestInlineHooksResource.SDK_PREFIX} Test Inline Hook",
            "version": "1.0.0",
            "type": models.InlineHookType.COM_OKTA_OAUTH_2_TOKENS_TRANSFORM,
            "channel": models.InlineHookChannel({
                "type": "HTTP",
                "version": "1.0.0",
                "config": models.InlineHookChannelConfig({
                    "uri": "https://www.example.com/inlineHook",
                    "headers": [
                        models.InlineHookChannelConfigHeaders({
                            "key": "X-Test-Header",
                            "value": "Test Header Value"
                        })
                    ],
                    "authScheme": models.InlineHookChannelConfigAuthScheme({
                        "type": "HEADER",
                        "key": "Authorization",
                        "value": "Test-Api-Key"
                    })
                })
            })
        })

        created_inline_hook, _, err = await \
            client.create_inline_hook(inline_hook_model)
        assert err is None
        assert isinstance(created_inline_hook, models.InlineHook)
        assert created_inline_hook.id
        assert created_inline_hook.name == inline_hook_model.name
        assert created_inline_hook.channel
        assert created_inline_hook.channel.config
        assert created_inline_hook.channel.config.uri ==\
            inline_hook_model.channel.config.uri
        assert created_inline_hook.status == "ACTIVE"

        # Deactivate
        deactivated_inline_hook, _, err = await \
            client.deactivate_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(deactivated_inline_hook, models.InlineHook)
        assert deactivated_inline_hook.status == "INACTIVE"

        # Retrieve
        retrieved_inline_hook, _, err = await \
            client.get_inline_hook(created_inline_hook.id)
        assert err is None
        assert retrieved_inline_hook.status == "INACTIVE"

        # Activate
        activated_inline_hook, _, err = await \
            client.activate_inline_hook(created_inline_hook.id)
        assert err is None
        assert isinstance(activated_inline_hook, models.InlineHook)
        assert activated_inline_hook.status == "ACTIVE"

        # Retrieve
        retrieved_inline_hook, _, err = await \
            client.get_inline_hook(created_inline_hook.id)
        assert err is None
        assert retrieved_inline_hook.status == "ACTIVE"

        # Delete & Deactivate
        _, _, err = await \
            client.deactivate_inline_hook(created_inline_hook.id)
        assert err is None
        _, err = await client.delete_inline_hook(created_inline_hook.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_inline_hooks(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Inline Hooks
        NUMBER_OF_HOOKS = 3
        created_inline_hooks = []
        for index in range(NUMBER_OF_HOOKS):
            inline_hook_model = models.InlineHook({
                "name": f"{TestInlineHooksResource.SDK_PREFIX} IH{index}",
                "version": "1.0.0",
                "type": models.InlineHookType.
                COM_OKTA_OAUTH_2_TOKENS_TRANSFORM,
                "channel": models.InlineHookChannel({
                    "type": "HTTP",
                    "version": "1.0.0",
                    "config": models.InlineHookChannelConfig({
                        "uri": "https://www.example.com/inlineHook",
                        "headers": [
                            models.InlineHookChannelConfigHeaders({
                                "key": "X-Test-Header",
                                "value": f"Test Header {index}"
                            })
                        ],
                        "authScheme": models.
                        InlineHookChannelConfigAuthScheme({
                            "type": "HEADER",
                            "key": "Authorization",
                            "value": f"Test-Api-Key-{index}"
                        })
                    })
                })
            })

            created_inline_hook, _, err = await \
                client.create_inline_hook(inline_hook_model)
            assert err is None
            assert isinstance(created_inline_hook, models.InlineHook)
            assert created_inline_hook.id
            assert created_inline_hook.name == inline_hook_model.name
            assert created_inline_hook.channel
            assert created_inline_hook.channel.config
            assert created_inline_hook.channel.config.uri ==\
                inline_hook_model.channel.config.uri
            created_inline_hooks.append(created_inline_hook.id)

        # List
        all_inline_hooks, _, err = await client.list_inline_hooks()
        assert err is None
        assert isinstance(all_inline_hooks, list)
        for inline_hook_id in created_inline_hooks:
            assert next((ih for ih in all_inline_hooks
                         if ih.id == inline_hook_id))

        # Deactivate & Delete
        for inline_hook_id in created_inline_hooks:
            _, _, err = await \
                client.deactivate_inline_hook(inline_hook_id)
            assert err is None
            _, err = await client.delete_inline_hook(inline_hook_id)
            assert err is None
