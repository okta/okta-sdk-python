# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

"""
Unit tests for ConfigSetter to validate it works with new dict utilities.
"""

import os
import pytest
import tempfile
import yaml

from okta.config.config_setter import ConfigSetter


class TestConfigSetter:
    """Tests for ConfigSetter class using new dictionary utilities."""

    def test_config_setter_initialization(self):
        """Test that ConfigSetter initializes correctly."""
        config_setter = ConfigSetter()
        config = config_setter.get_config()

        assert config is not None
        assert "client" in config
        assert "testing" in config
        assert config["client"]["authorizationMode"] == "SSWS"

    def test_prune_config_removes_empty_strings(self):
        """Test that _prune_config removes empty strings."""
        config_setter = ConfigSetter()
        test_config = {
            "client": {
                "orgUrl": "",
                "token": "abc123",
                "cache": {
                    "enabled": "",
                    "defaultTtl": 300
                }
            }
        }

        result = config_setter._prune_config(test_config)

        assert "token" in result["client"]
        assert result["client"]["token"] == "abc123"
        assert result["client"]["cache"]["defaultTtl"] == 300
        # Empty strings should be removed
        assert "orgUrl" not in result["client"]
        assert "enabled" not in result["client"]["cache"]

    def test_apply_config_merges_nested_dicts(self):
        """Test that _apply_config properly merges nested configurations."""
        config_setter = ConfigSetter()

        # Get initial config
        initial_token = config_setter._config["client"].get("token", "")

        # Apply new config
        new_config = {
            "client": {
                "orgUrl": "https://test.okta.com",
                "token": "new_token_123",
                "cache": {
                    "enabled": True
                }
            }
        }

        config_setter._apply_config(new_config)

        # Verify merge happened correctly
        assert config_setter._config["client"]["orgUrl"] == "https://test.okta.com"
        assert config_setter._config["client"]["token"] == "new_token_123"
        assert config_setter._config["client"]["cache"]["enabled"] is True
        # Original values should be preserved if not overridden
        assert config_setter._config["client"]["cache"]["defaultTtl"] == 300

    def test_apply_yaml_config(self, tmp_path):
        """Test that _apply_yaml_config loads and applies YAML configuration."""
        config_setter = ConfigSetter()

        # Create a temporary YAML file
        yaml_content = {
            "okta": {
                "client": {
                    "orgUrl": "https://yaml-test.okta.com",
                    "token": "yaml_token_456",
                    "cache": {
                        "enabled": True,
                        "defaultTtl": 600
                    }
                }
            }
        }

        yaml_file = tmp_path / "test_config.yaml"
        with open(yaml_file, "w") as f:
            yaml.dump(yaml_content, f)

        # Apply the YAML config
        config_setter._apply_yaml_config(str(yaml_file))

        # Verify it was applied
        assert config_setter._config["client"]["orgUrl"] == "https://yaml-test.okta.com"
        assert config_setter._config["client"]["token"] == "yaml_token_456"
        assert config_setter._config["client"]["cache"]["enabled"] is True
        assert config_setter._config["client"]["cache"]["defaultTtl"] == 600

    def test_apply_env_config(self):
        """Test that _apply_env_config reads environment variables."""
        config_setter = ConfigSetter()

        # Set environment variables
        env_vars = {
            "OKTA_CLIENT_ORGURL": "https://env-test.okta.com",
            "OKTA_CLIENT_TOKEN": "env_token_789",
            "OKTA_CLIENT_CACHE_ENABLED": "true",
            "OKTA_CLIENT_SCOPES": "okta.users.read,okta.apps.read"
        }

        # Store original env values for cleanup
        original_values = {}
        for key in env_vars:
            original_values[key] = os.environ.get(key)
            os.environ[key] = env_vars[key]

        try:
            # Reset config setter to pick up env vars
            config_setter = ConfigSetter()

            # Verify env vars were applied
            assert config_setter._config["client"]["orgUrl"] == "https://env-test.okta.com"
            assert config_setter._config["client"]["token"] == "env_token_789"
            assert config_setter._config["client"]["cache"]["enabled"] == "true"
            # Scopes should be split into a list
            assert config_setter._config["client"]["scopes"] == ["okta.users.read", "okta.apps.read"]
        finally:
            # Cleanup environment variables
            for key in env_vars:
                if original_values[key] is None:
                    del os.environ[key]
                else:
                    os.environ[key] = original_values[key]

    def test_deep_nested_config_merge(self):
        """Test merging deeply nested configurations."""
        config_setter = ConfigSetter()

        # Apply multiple levels of config
        config1 = {
            "client": {
                "proxy": {
                    "host": "proxy1.example.com",
                    "port": "8080"
                }
            }
        }

        config2 = {
            "client": {
                "proxy": {
                    "port": "9090",
                    "username": "proxyuser"
                }
            }
        }

        config_setter._apply_config(config1)
        config_setter._apply_config(config2)

        # Verify deep merge worked
        assert config_setter._config["client"]["proxy"]["host"] == "proxy1.example.com"
        assert config_setter._config["client"]["proxy"]["port"] == "9090"
        assert config_setter._config["client"]["proxy"]["username"] == "proxyuser"

    def test_testing_config_section(self):
        """Test that testing configuration section is handled correctly."""
        config_setter = ConfigSetter()

        new_config = {
            "testing": {
                "testingDisableHttpsCheck": True
            }
        }

        config_setter._apply_config(new_config)

        assert config_setter._config["testing"]["testingDisableHttpsCheck"] is True

    def test_empty_config_application(self):
        """Test applying an empty config doesn't break anything."""
        config_setter = ConfigSetter()
        initial_config = config_setter._config.copy()

        config_setter._apply_config({})

        # Config should remain unchanged
        assert config_setter._config["client"]["authorizationMode"] == initial_config["client"]["authorizationMode"]

    def test_config_with_various_types(self):
        """Test that configs with various data types are handled correctly."""
        config_setter = ConfigSetter()

        new_config = {
            "client": {
                "connectionTimeout": 60,  # int
                "orgUrl": "https://test.okta.com",  # string
                "cache": {
                    "enabled": True,  # bool
                    "defaultTtl": 500  # int
                }
            }
        }

        config_setter._apply_config(new_config)

        assert config_setter._config["client"]["connectionTimeout"] == 60
        assert config_setter._config["client"]["orgUrl"] == "https://test.okta.com"
        assert config_setter._config["client"]["cache"]["enabled"] is True
        assert config_setter._config["client"]["cache"]["defaultTtl"] == 500
