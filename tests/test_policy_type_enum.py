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
Unit tests for the `PolicyType` enum.

These guard against a regression where api.yaml listed the enum value as
`<x-lifecycle class="ea"></x-lifecycle> DEVICE_SIGNAL_COLLECTION` (a documentation
lifecycle badge leaked into the value itself). The generator turned that into an enum
member whose value contained the HTML tag, so the plain `DEVICE_SIGNAL_COLLECTION`
string returned by the API was rejected and any policy of that type raised a
pydantic ValidationError on deserialization (e.g. from get_policy / list_policies).
"""

import json

import pytest

from okta.models.device_signal_collection_policy import DeviceSignalCollectionPolicy
from okta.models.policy import Policy
from okta.models.policy_type import PolicyType

ALL_POLICY_TYPES = [
    "ACCESS_POLICY",
    "DEVICE_SIGNAL_COLLECTION",
    "ENTITY_RISK",
    "IDP_DISCOVERY",
    "MFA_ENROLL",
    "OKTA_SIGN_ON",
    "PASSWORD",
    "POST_AUTH_SESSION",
    "PROFILE_ENROLLMENT",
]


def _policy_payload(policy_type):
    return {
        "id": "rst1abcdEFGH2345ijkl",
        "name": "Example policy",
        "type": policy_type,
        "status": "ACTIVE",
        "system": False,
        "priority": 1,
    }


def test_device_signal_collection_is_a_valid_policy_type():
    assert PolicyType("DEVICE_SIGNAL_COLLECTION") is PolicyType.DEVICE_SIGNAL_COLLECTION


def test_policy_type_values_contain_no_markup():
    for member in PolicyType:
        assert "<" not in member.value and ">" not in member.value, member.value
        assert member.value == member.value.strip()
        assert member.name == member.value


def test_policy_type_from_json():
    assert PolicyType.from_json('"DEVICE_SIGNAL_COLLECTION"') is PolicyType.DEVICE_SIGNAL_COLLECTION


def test_device_signal_collection_policy_deserializes_via_discriminator():
    policy = Policy.from_dict(_policy_payload("DEVICE_SIGNAL_COLLECTION"))
    assert isinstance(policy, DeviceSignalCollectionPolicy)
    assert policy.type == PolicyType.DEVICE_SIGNAL_COLLECTION


def test_device_signal_collection_policy_round_trips():
    payload = _policy_payload("DEVICE_SIGNAL_COLLECTION")
    policy = Policy.from_json(json.dumps(payload))
    assert policy.to_dict()["type"] == "DEVICE_SIGNAL_COLLECTION"


@pytest.mark.parametrize("policy_type", ALL_POLICY_TYPES)
def test_every_documented_policy_type_is_accepted(policy_type):
    assert PolicyType(policy_type).value == policy_type
