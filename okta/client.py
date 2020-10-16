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

from okta.config.config_setter import ConfigSetter
from okta.config.config_validator import ConfigValidator
from okta.request_executor import RequestExecutor
from okta.cache.no_op_cache import NoOpCache
from okta.cache.okta_cache import OktaCache
from okta.resource_clients.application_client\
    import ApplicationClient
from okta.resource_clients.authorization_server_client\
    import AuthorizationServerClient
from okta.resource_clients.event_hook_client\
    import EventHookClient
from okta.resource_clients.feature_client\
    import FeatureClient
from okta.resource_clients.group_client\
    import GroupClient
from okta.resource_clients.identity_provider_client\
    import IdentityProviderClient
from okta.resource_clients.inline_hook_client\
    import InlineHookClient
from okta.resource_clients.log_event_client\
    import LogEventClient
from okta.resource_clients.linked_object_client\
    import LinkedObjectClient
from okta.resource_clients.user_type_client\
    import UserTypeClient
from okta.resource_clients.policy_client\
    import PolicyClient
from okta.resource_clients.session_client\
    import SessionClient
from okta.resource_clients.sms_template_client\
    import SmsTemplateClient
from okta.resource_clients.trusted_origin_client\
    import TrustedOriginClient
from okta.resource_clients.user_client\
    import UserClient
from okta.resource_clients.user_factor_client\
    import UserFactorClient


class Client(
    ApplicationClient,
    AuthorizationServerClient,
    EventHookClient,
    FeatureClient,
    GroupClient,
    IdentityProviderClient,
    InlineHookClient,
    LogEventClient,
    LinkedObjectClient,
    UserTypeClient,
    PolicyClient,
    SessionClient,
    SmsTemplateClient,
    TrustedOriginClient,
    UserClient,
    UserFactorClient
):
    """An Okta client object"""

    def __init__(self, user_config: dict = {}):
        super()
        # Load configuration
        client_config_setter = ConfigSetter()
        client_config_setter._apply_config({'client': user_config})
        self._config = client_config_setter.get_config()
        # Prune configuration to remove unnecesary fields
        self._config = client_config_setter._prune_config(self._config)
        # Validate configuration
        ConfigValidator(self._config)

        # set client variables since validation passes
        self._authorization_mode = self._config["client"]["authorizationMode"]
        self._base_url = self._config["client"]["orgUrl"]
        self._api_token = self._config["client"].get("token", None)
        self._client_id = None
        self._scopes = None
        self._private_key = None

        # Determine which cache to use
        cache = NoOpCache()
        if self._config["client"]["cache"]["enabled"] is True:
            if user_config.get("cacheManager", None) is None:
                time_to_idle = self._config["client"]["cache"]["defaultTti"]
                time_to_live = self._config["client"]["cache"]["defaultTtl"]
                cache = OktaCache(
                    time_to_live,
                    time_to_idle
                )
            else:
                cache = user_config.get("cacheManager")

        # Determine request executor to use
        self._request_executor = \
            user_config.get("requestExecutor", RequestExecutor)(
                self._config,
                cache,
                user_config.get("httpClient", None))

        # set private key variables
        if self._authorization_mode == 'PrivateKey':
            self._client_id = self._config["client"]["clientId"]
            self._scopes = self._config["client"]["scopes"]
            self._private_key = self._config["client"]["privateKey"]
    """
    Getters
    """

    def get_config(self):
        return self._config

    def get_scopes(self):
        return self._scopes

    def get_base_url(self):
        return self._base_url

    def get_request_executor(self):
        return self._request_executor
