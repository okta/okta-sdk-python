from config_setter import ConfigSetter as ConfigSetter


class Client:
    """An Okta client instance"""

    def __init__(self, config: dict):
        # Load configuration
        client_config_setter = ConfigSetter()
        client_config_setter.apply_config(config or {})
        self._config = client_config_setter.getConfig()
