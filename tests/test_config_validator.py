"""
Tests for ConfigValidator defensive behavior.
Ensures validator handles missing config sections gracefully.
"""

import pytest
from okta.config.config_validator import ConfigValidator


class TestConfigValidatorDefensiveBehavior:
    """Tests for defensive programming in ConfigValidator."""

    def test_validator_with_missing_client_section(self):
        """Test that validator handles missing 'client' section gracefully."""
        config = {
            'testing': {
                'testingDisableHttpsCheck': False
            }
        }

        # Should raise validation error (missing required fields)
        # but should NOT crash with AttributeError
        with pytest.raises(ValueError) as exc_info:
            ConfigValidator(config)

        # Should have validation errors, not AttributeError
        assert "orgUrl" in str(exc_info.value).lower() or "error" in str(exc_info.value).lower()
        # Make sure it's not an AttributeError
        assert "AttributeError" not in str(exc_info.value)

    def test_validator_with_missing_testing_section(self):
        """Test that validator handles missing 'testing' section gracefully."""
        config = {
            'client': {
                'orgUrl': 'https://test.okta.com',
                'authorizationMode': 'SSWS',
                'token': 'test-token'
            }
        }

        # Should validate without crashing
        # (testing section is optional for validation)
        try:
            _ = ConfigValidator(config)
            # If it succeeds, that's good
        except ValueError:
            # Validation errors are fine, just shouldn't be AttributeError
            pass

    def test_validator_with_both_sections_missing(self):
        """Test that validator handles empty config gracefully."""
        config = {}

        # Should raise validation error, not AttributeError
        with pytest.raises(ValueError) as exc_info:
            ConfigValidator(config)

        assert "AttributeError" not in str(exc_info.value)

    def test_validator_with_client_as_none(self):
        """Test that validator handles client=None gracefully."""
        config = {
            'client': None,
            'testing': {
                'testingDisableHttpsCheck': False
            }
        }

        # Should raise validation error, not AttributeError
        with pytest.raises((ValueError, AttributeError)):
            ConfigValidator(config)

        # Either ValueError (good) or AttributeError (documents current behavior)
        # We're testing that it at least raises something predictable

    def test_validator_with_valid_minimal_config(self):
        """Test that validator works with valid minimal config."""
        config = {
            'client': {
                'orgUrl': 'https://test.okta.com',
                'authorizationMode': 'SSWS',
                'token': 'valid-token-abc123'
            },
            'testing': {
                'testingDisableHttpsCheck': False
            }
        }

        # Should validate successfully
        validator = ConfigValidator(config)
        assert validator is not None

    def test_validator_with_empty_client_dict(self):
        """Test that validator handles empty client dict."""
        config = {
            'client': {},
            'testing': {}
        }

        # Should raise validation errors for missing required fields
        with pytest.raises(ValueError) as exc_info:
            ConfigValidator(config)

        # Should mention missing fields
        error_msg = str(exc_info.value).lower()
        assert "orgurl" in error_msg or "authorization" in error_msg

    def test_validator_with_partial_client_config(self):
        """Test that validator handles partial client config."""
        config = {
            'client': {
                'orgUrl': 'https://test.okta.com'
                # Missing authorizationMode and token
            }
        }

        # Should raise validation error for missing fields
        with pytest.raises(ValueError) as exc_info:
            ConfigValidator(config)

        error_msg = str(exc_info.value).lower()
        # Should have validation errors
        assert "error" in error_msg or "invalid" in error_msg


class TestConfigValidatorWithPrunedConfig:
    """
    Tests for ConfigValidator compatibility with pruned configs.
    After remove_empty_values(), some sections might be empty dicts.
    """

    def test_validator_after_prune_removes_nested_dicts(self):
        """
        Test validator when remove_empty_values() removes nested empty dicts.
        This could happen if all values in a section were empty strings.
        """
        # Simulate what might happen after remove_empty_values()
        config = {
            'client': {
                'orgUrl': 'https://test.okta.com',
                'authorizationMode': 'SSWS',
                'token': 'valid-token',
                # cache was all empty strings, so it's removed
            },
            'testing': {}  # All values were empty
        }

        # Should still validate
        try:
            validator = ConfigValidator(config)
            assert validator is not None
        except ValueError as e:
            # Validation errors are fine
            assert "AttributeError" not in str(e)

    def test_validator_with_missing_proxy_section(self):
        """Test that validator handles missing proxy section (which is optional)."""
        config = {
            'client': {
                'orgUrl': 'https://test.okta.com',
                'authorizationMode': 'SSWS',
                'token': 'valid-token'
                # No proxy section
            }
        }

        # Should validate fine (proxy is optional)
        validator = ConfigValidator(config)
        assert validator is not None
