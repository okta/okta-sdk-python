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
            "privateKey": '',
            "userAgent": '',
            "cache": {
                "enabled": '',
                "defaultTti": '',
                "defaultTtl": ''
            },
            "rateLimit": {
                "maxRetries": ''
            }
        },
        "testing": {
            "testingDisableHttpsCheck": ''
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
        self._update_config()
        # Prune configuration to remove unnecessary values
        self._prune_config()

    def get_config(self):
        """
        Return Okta client configuration

        Returns:
            dict -- Dictionary containing the client configuration
        """
        return self._config

    def _prune_config(self):
        """
        This method cleans up the configuration object by removing fields
        with no value
        """
        # Flatten dictionary to account for nested dictionary
        flat_current_config = FlatDict(self._config, delimiter='_')
        # Iterate through keys and remove if value is still empty string
        for key in flat_current_config.keys():
            if flat_current_config.get(key) == "":
                del flat_current_config[key]

        self._config = flat_current_config.as_dict()

    def _update_config(self):
        """
        Updates the configuration of the Okta Client by:
        1. Applying default values
        2. Checking for a global OKTA config YAML
        3. Checking for a local OKTA config YAML
        4. Checking for corresponding ENV variables
        """
        # apply default config values to config
        self._apply_default_values()
        # check if GLOBAL yaml exists, apply if true
        if (os.path.exists(ConfigSetter._GLOBAL_YAML_PATH)):
            self._apply_yaml_config(ConfigSetter._GLOBAL_YAML_PATH)
        # check if LOCAL yaml exists, apply if true
        if (os.path.exists(ConfigSetter._LOCAL_YAML_PATH)):
            self._apply_yaml_config(ConfigSetter._LOCAL_YAML_PATH)
        # apply existing environment variables
        self._apply_env_config()

    def _apply_default_values(self):
        """Apply default values to default client configuration
        """
        # Set defaults
        self._config["client"]["authorizationMode"] = "SSWS"
        self._config["client"]["connectionTimeout"] = 30
        self._config["client"]["cache"] = {
            "enabled": True,
            "defaultTtl": 300,
            "defaultTti": 300
        }
        self._config["client"]["userAgent"] = ""
        self._config["client"]["requestTimeout"] = 0
        self._config["client"]["rateLimit"] = {
            "maxRetries": 2
        }
        self._config["testing"]["testingDisableHttpsCheck"] = False

    def _apply_config(self, new_config: dict):
        """This method applies a config dictionary to the current config,
           overwriting values and adding new entries (if present).

        Arguments:
            config {dict} -- A dictionary of client configuration details
        """
        # Update current configuration with new configuration
        # Flatten both dictionaries to account for nested dictionary values
        flat_current_config = FlatDict(self._config, delimiter='_')
        flat_new_config = FlatDict(new_config, delimiter='_')
        # Update values in current config and unflatten
        flat_current_config.update(flat_new_config)
        self._config = flat_current_config.as_dict()

    def _apply_yaml_config(self, path: str):
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
        self._apply_config(config.get("okta", {}))

    def _apply_env_config(self):
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
        self._apply_config(updated_config.as_dict())
