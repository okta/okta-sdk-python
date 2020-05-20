import os
import yaml
from flatdict import FlatDict


class ConfigSetter():
    """
    This class sets up the configuration for the Okta Client
    """

    # Configuration constants
    _OKTA = "OKTA"
    _DEFAULT_CONFIG = {
        "client": {
            "authorizationMode": '',
            "orgUrl": '',
            "token": '',
            "clientId": '',
            "scopes": '',
            "privateKey": ''
        }
    }
    _GLOBAL_YAML_PATH = os.path.join(os.path.expanduser('~'), ".okta",
                                     "okta.yaml")
    _LOCAL_YAML_PATH = os.path.join(os.getcwd(), "okta.yaml")

    def __init__(self):
        """
        Consructor for Configuration Setter class. Sets default config
        and checks for configuration settings to update config.
        """
        # Create configuration using default config
        self._config = ConfigSetter._DEFAULT_CONFIG
        # Update configuration
        self.update_config()

    def getConfig(self):
        """
        Return Okta client configuration

        Returns:
            dict -- Dictionary containing the client configuration
        """
        return self._config

    def update_config(self):
        """
        Updates the configuration of the Okta Client by:
        1. Applying default values
        2. Checking for a global OKTA config YAML
        3. Checking for a local OKTA config YAML
        4. Checking for corresponding ENV variables
        """
        # apply default config values to config
        self.apply_default_values()
        # check if GLOBAL yaml exists, apply if true
        if (os.path.exists(ConfigSetter._GLOBAL_YAML_PATH)):
            self.apply_yaml_config(ConfigSetter._GLOBAL_YAML_PATH)
        # check if LOCAL yaml exists, apply if true
        if (os.path.exists(ConfigSetter._LOCAL_YAML_PATH)):
            self.apply_yaml_config(ConfigSetter._LOCAL_YAML_PATH)
        # apply existing environment variables
        self.apply_env_config()

    def apply_default_values(self):
        """Apply default values to default client configuration
        """
        # Set default authorization mode to SSWS
        self._config["authorizationMode"] = "SSWS"

    def apply_config(self, new_config: dict):
        """This method applies a config dictionary to the current config,
           overwriting values and adding new entries (if present).

        Arguments:
            config {dict} -- A dictionary of client configuration details
        """
        # Update current configuration with new configuration
        self._config.update(new_config)

    def apply_yaml_config(self, path: str):
        """This method applies a YAML configuration to the Okta Client Config

        Arguments:
            path {string} -- The filepath of the corresponding YAML file
        """
        # Start with empty config
        config = {}
        with open(path, 'r') as file:
            try:
                # Open file stream and attempt to load YAML
                config = yaml.load(file, Loader=yaml.SafeLoader)
            except yaml.YAMLError as err:
                # Error handling if YAML doesn't load properly
                # TODO check error handling on YAML
                print(err)
        # Apply acquired config to configuration
        self.apply_config(config.get("okta", {}))

    def apply_env_config(self):
        """
        This method checks the environment variables for any OKTA
        configuration parameters and applies them if available.
        """
        # Flatten current config and join with underscores
        # (for environment variable format)
        flattened_config = FlatDict(self._config, delimiter='_')
        flattened_keys = flattened_config.keys()

        # Create empty result config and populate
        updated_config = FlatDict({}, delimiter='_')

        # Go through keys and search for it in the environment vars
        # using the format described in the README
        for key in flattened_keys:
            env_key = ConfigSetter._OKTA + "_" + key.upper()
            env_value = os.getenv(env_key)
            if env_value is not None:
                # If value is found, add to config
                updated_config[env_key] = env_value
        # apply to current configuration
        self._config = updated_config.as_dict()
