from okta.config.config_setter import ConfigSetter
from okta.config.config_validator import ConfigValidator
from okta.request_executor import RequestExecutor
from okta.oauth import OAuth
from okta.cache.no_op_cache import NoOpCache
from okta.cache.okta_cache import OktaCache


class Client:
    """An Okta client object"""

    def __init__(self, user_config: dict = {}):
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
        self._oauth = None

        # set private key variables
        if self._authorization_mode == 'PrivateKey':
            self._client_id = self._config["client"]["clientId"]
            self._scopes = self._config["client"]["scopes"]
            self._private_key = self._config["client"]["privateKey"]
            self._oauth = OAuth(self)

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
            user_config.get("request_executor",
                            RequestExecutor(
                                self._config,
                                cache,
                                user_config.get("httpClient", None),
                            ))

    """
    Getters
    """

    def get_config(self):
        return self._config

    def get_scopes(self):
        return None if self._scopes is None else self._scopes

    def get_base_url(self):
        return self._base_url