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
Unit tests for dictionary utility functions in okta.utils module.
"""

import pytest

from okta.utils import (
    flatten_dict,
    unflatten_dict,
    deep_merge,
    remove_empty_values
)


class TestFlattenDict:
    """Tests for flatten_dict function."""

    def test_simple_nested_dict(self):
        """Test basic flattening of a simple nested dictionary."""
        input_dict = {'a': {'b': 1, 'c': 2}}
        expected = {'a::b': 1, 'a::c': 2}
        assert flatten_dict(input_dict) == expected

    def test_deep_nesting(self):
        """Test flattening of deeply nested dictionary (4+ levels)."""
        input_dict = {
            'level1': {
                'level2': {
                    'level3': {
                        'level4': 'value'
                    }
                }
            }
        }
        expected = {'level1::level2::level3::level4': 'value'}
        assert flatten_dict(input_dict) == expected

    def test_empty_dict(self):
        """Test flattening an empty dictionary."""
        assert flatten_dict({}) == {}

    def test_custom_delimiter(self):
        """Test flattening with a custom delimiter."""
        input_dict = {'a': {'b': 1}}
        expected = {'a.b': 1}
        assert flatten_dict(input_dict, delimiter='.') == expected

    def test_single_level_dict(self):
        """Test flattening a dictionary with no nesting."""
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        assert flatten_dict(input_dict) == input_dict

    def test_mixed_values(self):
        """Test flattening with various value types."""
        input_dict = {
            'string': {'nested': 'value'},
            'number': {'nested': 42},
            'boolean': {'nested': True},
            'none': {'nested': None},
            'list': {'nested': [1, 2, 3]}
        }
        expected = {
            'string::nested': 'value',
            'number::nested': 42,
            'boolean::nested': True,
            'none::nested': None,
            'list::nested': [1, 2, 3]
        }
        assert flatten_dict(input_dict) == expected

    def test_config_like_structure(self):
        """Test flattening a structure similar to Okta config."""
        input_dict = {
            'client': {
                'cache': {
                    'enabled': True,
                    'defaultTtl': 300
                },
                'orgUrl': 'https://example.okta.com'
            }
        }
        expected = {
            'client::cache::enabled': True,
            'client::cache::defaultTtl': 300,
            'client::orgUrl': 'https://example.okta.com'
        }
        assert flatten_dict(input_dict) == expected


class TestUnflattenDict:
    """Tests for unflatten_dict function."""

    def test_simple_unflatten(self):
        """Test basic unflattening."""
        input_dict = {'a::b': 1, 'a::c': 2}
        expected = {'a': {'b': 1, 'c': 2}}
        assert unflatten_dict(input_dict) == expected

    def test_deep_unflatten(self):
        """Test unflattening deeply nested structure."""
        input_dict = {'x::y::z::value': 3}
        expected = {'x': {'y': {'z': {'value': 3}}}}
        assert unflatten_dict(input_dict) == expected

    def test_empty_dict(self):
        """Test unflattening an empty dictionary."""
        assert unflatten_dict({}) == {}

    def test_custom_delimiter(self):
        """Test unflattening with custom delimiter."""
        input_dict = {'a.b.c': 1}
        expected = {'a': {'b': {'c': 1}}}
        assert unflatten_dict(input_dict, delimiter='.') == expected

    def test_single_level_dict(self):
        """Test unflattening a dictionary with no delimiters."""
        input_dict = {'a': 1, 'b': 2}
        assert unflatten_dict(input_dict) == input_dict

    def test_preserves_structure(self):
        """Test round-trip: flatten then unflatten."""
        original = {
            'client': {
                'cache': {
                    'enabled': True,
                    'defaultTtl': 300
                },
                'orgUrl': 'https://example.okta.com'
            },
            'testing': {
                'disableHttps': False
            }
        }
        flattened = flatten_dict(original)
        unflattened = unflatten_dict(flattened)
        assert unflattened == original

    def test_multiple_keys_same_parent(self):
        """Test unflattening multiple keys with same parent."""
        input_dict = {
            'parent::child1': 'value1',
            'parent::child2': 'value2',
            'parent::child3': 'value3'
        }
        expected = {
            'parent': {
                'child1': 'value1',
                'child2': 'value2',
                'child3': 'value3'
            }
        }
        assert unflatten_dict(input_dict) == expected


class TestDeepMerge:
    """Tests for deep_merge function."""

    def test_simple_merge(self):
        """Test basic merge operation."""
        base = {'a': 1, 'b': 2}
        updates = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        assert deep_merge(base, updates) == expected

    def test_deep_merge_nested(self):
        """Test deep merge with nested dictionaries."""
        base = {'a': {'b': 1, 'c': 2}}
        updates = {'a': {'c': 3, 'd': 4}}
        expected = {'a': {'b': 1, 'c': 3, 'd': 4}}
        assert deep_merge(base, updates) == expected

    def test_override_behavior(self):
        """Test that new values override old values."""
        base = {'key': 'old_value'}
        updates = {'key': 'new_value'}
        expected = {'key': 'new_value'}
        assert deep_merge(base, updates) == expected

    def test_preserve_unrelated_keys(self):
        """Test that keys not in update dict are preserved."""
        base = {'a': 1, 'b': 2, 'c': 3}
        updates = {'b': 20}
        expected = {'a': 1, 'b': 20, 'c': 3}
        assert deep_merge(base, updates) == expected

    def test_empty_base(self):
        """Test merging with empty base."""
        base = {}
        updates = {'a': 1, 'b': 2}
        assert deep_merge(base, updates) == updates

    def test_empty_updates(self):
        """Test merging with empty updates."""
        base = {'a': 1, 'b': 2}
        updates = {}
        assert deep_merge(base, updates) == base

    def test_both_empty(self):
        """Test merging two empty dicts."""
        assert deep_merge({}, {}) == {}

    def test_complex_nested_merge(self):
        """Test complex nested structure merge."""
        base = {
            'client': {
                'cache': {'enabled': False, 'ttl': 100},
                'timeout': 30
            },
            'testing': {'debug': True}
        }
        updates = {
            'client': {
                'cache': {'enabled': True},
                'retries': 3
            },
            'logging': {'level': 'INFO'}
        }
        expected = {
            'client': {
                'cache': {'enabled': True, 'ttl': 100},
                'timeout': 30,
                'retries': 3
            },
            'testing': {'debug': True},
            'logging': {'level': 'INFO'}
        }
        assert deep_merge(base, updates) == expected

    def test_replace_dict_with_non_dict(self):
        """Test replacing a dict value with a non-dict value."""
        base = {'a': {'b': 1}}
        updates = {'a': 'string'}
        expected = {'a': 'string'}
        assert deep_merge(base, updates) == expected

    def test_replace_non_dict_with_dict(self):
        """Test replacing a non-dict value with a dict value."""
        base = {'a': 'string'}
        updates = {'a': {'b': 1}}
        expected = {'a': {'b': 1}}
        assert deep_merge(base, updates) == expected

    def test_original_not_modified(self):
        """Test that original dictionaries are not modified."""
        base = {'a': 1, 'b': {'c': 2}}
        updates = {'b': {'d': 3}}
        base_copy = {'a': 1, 'b': {'c': 2}}
        updates_copy = {'b': {'d': 3}}

        deep_merge(base, updates)

        # Original dicts should not be modified
        assert base == base_copy
        assert updates == updates_copy


class TestRemoveEmptyValues:
    """Tests for remove_empty_values function."""

    def test_remove_empty_strings(self):
        """Test removing empty string values."""
        input_dict = {'a': '', 'b': 'value', 'c': ''}
        expected = {'b': 'value'}
        assert remove_empty_values(input_dict) == expected

    def test_preserve_other_falsy_values(self):
        """Test that other falsy values (None, 0, False, []) are preserved."""
        input_dict = {
            'none': None,
            'zero': 0,
            'false': False,
            'empty_list': [],
            'empty_string': '',
            'value': 'keep'
        }
        expected = {
            'none': None,
            'zero': 0,
            'false': False,
            'empty_list': [],
            'value': 'keep'
        }
        assert remove_empty_values(input_dict) == expected

    def test_nested_cleanup(self):
        """Test cleaning nested dictionaries."""
        input_dict = {
            'level1': {
                'empty': '',
                'value': 'keep',
                'level2': {
                    'empty': '',
                    'value': 'keep'
                }
            }
        }
        expected = {
            'level1': {
                'value': 'keep',
                'level2': {
                    'value': 'keep'
                }
            }
        }
        assert remove_empty_values(input_dict) == expected

    def test_empty_dict_removal(self):
        """Test that empty dicts are removed after cleanup."""
        input_dict = {
            'a': {'b': ''},
            'c': 'value'
        }
        expected = {'c': 'value'}
        assert remove_empty_values(input_dict) == expected

    def test_all_empty(self):
        """Test dict with all empty strings."""
        input_dict = {'a': '', 'b': '', 'c': ''}
        assert remove_empty_values(input_dict) == {}

    def test_no_empty_values(self):
        """Test dict with no empty values."""
        input_dict = {'a': 1, 'b': 'value', 'c': True}
        assert remove_empty_values(input_dict) == input_dict

    def test_empty_input(self):
        """Test with empty input dict."""
        assert remove_empty_values({}) == {}

    def test_config_like_structure(self):
        """Test with structure similar to Okta config."""
        input_dict = {
            'client': {
                'orgUrl': '',
                'token': 'abc123',
                'cache': {
                    'enabled': '',
                    'defaultTtl': '',
                },
                'logging': {
                    'enabled': '',
                }
            },
            'testing': {
                'testingDisableHttpsCheck': ''
            }
        }
        expected = {
            'client': {
                'token': 'abc123'
            }
        }
        assert remove_empty_values(input_dict) == expected

    def test_deeply_nested_empty_cleanup(self):
        """Test cleaning deeply nested structure."""
        input_dict = {
            'a': {
                'b': {
                    'c': {
                        'd': ''
                    }
                }
            },
            'keep': 'value'
        }
        expected = {'keep': 'value'}
        assert remove_empty_values(input_dict) == expected


class TestIntegration:
    """Integration tests combining multiple utility functions."""

    def test_flatten_unflatten_roundtrip(self):
        """Test that flatten and unflatten are inverse operations."""
        test_cases = [
            {'a': {'b': 1}},
            {'x': {'y': {'z': 3}}},
            {'client': {'cache': {'enabled': True, 'ttl': 300}}},
            {'a': 1, 'b': 2},
            {}
        ]

        for test_dict in test_cases:
            flattened = flatten_dict(test_dict)
            unflattened = unflatten_dict(flattened)
            assert unflattened == test_dict

    def test_merge_then_cleanup(self):
        """Test merging configs then removing empty values."""
        base = {
            'client': {
                'orgUrl': '',
                'token': 'old_token'
            }
        }
        updates = {
            'client': {
                'token': '',
                'clientId': 'new_id'
            }
        }
        merged = deep_merge(base, updates)
        cleaned = remove_empty_values(merged)
        expected = {
            'client': {
                'clientId': 'new_id'
            }
        }
        assert cleaned == expected

    def test_config_setter_workflow(self):
        """Test workflow similar to ConfigSetter usage."""
        # Simulate default config
        config = {
            'client': {
                'orgUrl': '',
                'token': '',
                'cache': {'enabled': '', 'ttl': ''}
            }
        }

        # Simulate YAML config
        yaml_config = {
            'client': {
                'orgUrl': 'https://example.okta.com',
                'cache': {'enabled': True}
            }
        }

        # Merge and clean
        merged = deep_merge(config, yaml_config)
        cleaned = remove_empty_values(merged)

        expected = {
            'client': {
                'orgUrl': 'https://example.okta.com',
                'cache': {'enabled': True}
            }
        }
        assert cleaned == expected
