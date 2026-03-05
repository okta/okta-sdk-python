# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import copy
import logging
import os

import yaml

from okta.constants import _GLOBAL_YAML_PATH, _LOCAL_YAML_PATH
from okta.utils import flatten_dict, unflatten_dict, remove_empty_values, deep_merge


class ConfigSetter:
    """
    This class sets up the configuration for the Okta Client
    """

    # Configuration constants
    _OKTA = "OKTA"
    _DEFAULT_CONFIG = {
        "client": {
            "authorizationMode": "",
            "orgUrl": "",
            "token": "",
            "clientId": "",
            "scopes": "",
            "privateKey": "",
            "userAgent": "",
            "cache": {"enabled": "", "defaultTti": "", "defaultTtl": ""},
            "logging": {
                "enabled": "",
            },
            "proxy": {"port": "", "host": "", "username": "", "password": ""},
            "rateLimit": {"maxRetries": ""},
            "oauthTokenRenewalOffset": "",
        },
        "testing": {"testingDisableHttpsCheck": ""},
    }

    def __init__(self):
        """
        Constructor for Configuration Setter class. Sets default config
        and checks for configuration settings to update config.
        """
        # Create configuration using deep copy of default config
        # This prevents shared mutable state across instances
        self._config = copy.deepcopy(ConfigSetter._DEFAULT_CONFIG)
        # Update configuration
        self._update_config()

    def get_config(self):
        """
        Return Okta client configuration.

        Returns a deep copy to prevent external modification of internal state
        and to avoid holding references to sensitive values.

        Returns:
            dict -- Deep copy of the client configuration dictionary
        """
        return copy.deepcopy(self._config)

    def _prune_config(self, config):
        """
        This method cleans up the configuration object by removing fields
        with no value
        """
        return remove_empty_values(config)

    def _update_config(self):
        """
        Updates the configuration of the Okta Client by:
        1. Applying default values
        2. Checking for a global OKTA config YAML
        3. Checking for a local OKTA config YAML
        4. Checking for corresponding ENV variables
        """
        # TODO: Check for the ordering of the config setter.
        # apply default config values to config
        self._apply_default_values()
        # apply existing environment variables
        self._apply_env_config()
        # check if GLOBAL yaml exists, apply if true
        if os.path.exists(_GLOBAL_YAML_PATH):
            self._apply_yaml_config(_GLOBAL_YAML_PATH)
        # check if LOCAL yaml exists, apply if true
        if os.path.exists(_LOCAL_YAML_PATH):
            self._apply_yaml_config(_LOCAL_YAML_PATH)

    def _apply_default_values(self):
        """Apply default values to default client configuration"""
        # Set defaults
        self._config["client"]["authorizationMode"] = "SSWS"
        self._config["client"]["connectionTimeout"] = 30
        self._config["client"]["cache"] = {
            "enabled": False,
            "defaultTtl": 300,
            "defaultTti": 300,
        }
        self._config["client"]["logging"] = {"enabled": False, "logLevel": logging.INFO}
        self._config["client"]["userAgent"] = ""
        self._config["client"]["requestTimeout"] = 0
        self._config["client"]["rateLimit"] = {"maxRetries": 2}
        self._config["client"]["oauthTokenRenewalOffset"] = 5

        self._config["testing"]["testingDisableHttpsCheck"] = False

    def _apply_config(self, new_config: dict):
        """This method applies a config dictionary to the current config,
           overwriting values and adding new entries (if present).

        Arguments:
            new_config {dict} -- A dictionary of client configuration details
        """
        # Update current configuration with new configuration using deep merge
        # Use 'or {}' to handle None values from YAML (e.g., "client: null")
        if "client" in new_config:
            self._config["client"] = deep_merge(
                self._config["client"],
                new_config.get("client") or {}
            )
        if "testing" in new_config:
            self._config["testing"] = deep_merge(
                self._config["testing"],
                new_config.get("testing") or {}
            )

    def _apply_yaml_config(self, path: str):
        """This method applies a YAML configuration to the Okta Client Config

        Arguments:
            path {string} -- The filepath of the corresponding YAML file

        Raises:
            ValueError: If config file exceeds maximum allowed size
        """
        # Check file size before loading (prevent memory exhaustion)
        MAX_CONFIG_SIZE = 1_048_576  # 1 MB - generous for config files
        file_size = os.path.getsize(path)
        if file_size > MAX_CONFIG_SIZE:
            raise ValueError(
                f"Config file {path} ({file_size} bytes) exceeds maximum "
                f"allowed size of {MAX_CONFIG_SIZE} bytes"
            )

        # Start with empty config
        config = {}
        with open(path, "r") as file:
            # Open file stream and attempt to load YAML
            config = yaml.load(file, Loader=yaml.SafeLoader)
        # Handle empty YAML files or files with only comments
        if config is None:
            config = {}
        # Apply acquired config to configuration
        self._apply_config(config.get("okta", {}))

    def _apply_env_config(self):
        """
        This method checks the environment variables for any OKTA
        configuration parameters and applies them if available.
        """
        # Flatten current config with :: delimiter for internal processing
        # (for environment variable format)
        flattened_config = flatten_dict(self._config, delimiter="::")
        flattened_keys = flattened_config.keys()

        # Create empty result config and populate
        updated_config = {}

        # Go through keys and search for it in the environment vars
        # using the format described in the README
        for key in flattened_keys:
            # Convert internal :: delimiter to _ for environment variable name
            env_key = ConfigSetter._OKTA + "_" + key.replace("::", "_").upper()
            env_value = os.environ.get(env_key, None)

            if env_value is not None:
                # If value is found, add to config
                if "scopes" in env_key.lower():
                    updated_config[key] = env_value.split(",")
                else:
                    updated_config[key] = env_value

        # Apply to current configuration
        self._apply_config(unflatten_dict(updated_config, delimiter="::"))
