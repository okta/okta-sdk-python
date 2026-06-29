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
Unit tests verifying that `methods` and `types` enum validators on
`AccessPolicyConstraint`, `KnowledgeConstraint`, and `PossessionConstraint`
accept lowercase values (matching the live Okta API response casing) and
reject UPPERCASE / invalid values.

Related: Alignment of OAS3 enum casing with the API.
"""

import pytest
from pydantic import ValidationError

from okta.models.access_policy_constraint import AccessPolicyConstraint
from okta.models.knowledge_constraint import KnowledgeConstraint
from okta.models.possession_constraint import PossessionConstraint


VALID_METHODS = [
    "password", "security_question", "sms", "voice", "email",
    "push", "signed_nonce", "otp", "totp", "webauthn", "duo", "idp", "cert",
]
VALID_TYPES = [
    "security_key", "phone", "email", "password",
    "security_question", "app", "federated",
]


class TestAccessPolicyConstraintEnums:
    """Validator tests for the base `AccessPolicyConstraint` model."""

    def test_lowercase_methods_accepted(self):
        obj = AccessPolicyConstraint(methods=["password", "push", "webauthn"])
        assert obj.methods == ["password", "push", "webauthn"]

    def test_lowercase_types_accepted(self):
        obj = AccessPolicyConstraint(types=["password", "security_key", "phone"])
        assert obj.types == ["password", "security_key", "phone"]

    def test_all_valid_methods_accepted(self):
        obj = AccessPolicyConstraint(methods=list(VALID_METHODS))
        assert obj.methods == VALID_METHODS

    def test_all_valid_types_accepted(self):
        obj = AccessPolicyConstraint(types=list(VALID_TYPES))
        assert obj.types == VALID_TYPES

    def test_uppercase_methods_rejected(self):
        with pytest.raises(ValidationError):
            AccessPolicyConstraint(methods=["PASSWORD"])

    def test_uppercase_types_rejected(self):
        with pytest.raises(ValidationError):
            AccessPolicyConstraint(types=["PASSWORD"])

    def test_unknown_method_rejected(self):
        with pytest.raises(ValidationError):
            AccessPolicyConstraint(methods=["not_a_real_method"])

    def test_unknown_type_rejected(self):
        with pytest.raises(ValidationError):
            AccessPolicyConstraint(types=["not_a_real_type"])

    def test_from_dict_lowercase_payload(self):
        """Simulates a real API response payload."""
        payload = {
            "methods": ["password", "push"],
            "types": ["password"],
            "required": True,
            "reauthenticateIn": "PT2H",
        }
        obj = AccessPolicyConstraint.from_dict(payload)
        assert obj.methods == ["password", "push"]
        assert obj.types == ["password"]
        assert obj.required is True
        assert obj.reauthenticate_in == "PT2H"


class TestKnowledgeConstraintEnums:
    """Validator tests for `KnowledgeConstraint` (inherits the same enums)."""

    def test_lowercase_methods_accepted(self):
        obj = KnowledgeConstraint(methods=["password"])
        assert obj.methods == ["password"]

    def test_lowercase_types_accepted(self):
        obj = KnowledgeConstraint(types=["password", "security_question"])
        assert obj.types == ["password", "security_question"]

    def test_uppercase_methods_rejected(self):
        with pytest.raises(ValidationError):
            KnowledgeConstraint(methods=["PASSWORD"])

    def test_uppercase_types_rejected(self):
        with pytest.raises(ValidationError):
            KnowledgeConstraint(types=["PASSWORD"])


class TestPossessionConstraintEnums:
    """Validator tests for `PossessionConstraint` (inherits the same enums)."""

    def test_lowercase_methods_accepted(self):
        obj = PossessionConstraint(methods=["push", "signed_nonce", "webauthn"])
        assert obj.methods == ["push", "signed_nonce", "webauthn"]

    def test_lowercase_types_accepted(self):
        obj = PossessionConstraint(types=["security_key", "phone"])
        assert obj.types == ["security_key", "phone"]

    def test_uppercase_methods_rejected(self):
        with pytest.raises(ValidationError):
            PossessionConstraint(methods=["PUSH"])

    def test_uppercase_types_rejected(self):
        with pytest.raises(ValidationError):
            PossessionConstraint(types=["SECURITY_KEY"])

