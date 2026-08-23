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
Unit tests for the generated okta.models.user_type.UserType model.

These tests guard against regressions of the historical name-collision bug where the
inline `User.type` object shadowed the top-level `UserType` component schema, causing
UserType to be generated with only an `id` field. After the api.yaml fix (extracting
the inline schema into `UserTypeRef`), UserType must serialize/deserialize the full
set of fields defined by the component schema.
"""

from datetime import datetime, timezone

from okta.models.user_type import UserType

FULL_PAYLOAD = {
    "id": "oty123",
    "name": "employee",
    "displayName": "Employee",
    "description": "Employee user type",
    "default": False,
    "createdBy": "00ucreated",
    "created": "2026-01-02T03:04:05+00:00",
    "lastUpdatedBy": "00uupdated",
    "lastUpdated": "2026-01-03T04:05:06+00:00",
    "_links": {"self": {"href": "https://example.okta.com/api/v1/meta/types/user/oty123"}},
}


class TestUserTypeFromDict:
    """Deserialization from wire-format dicts (alias names)."""

    def test_from_dict_preserves_all_response_fields(self):
        ut = UserType.from_dict(FULL_PAYLOAD)

        assert ut is not None
        assert ut.id == "oty123"
        assert ut.name == "employee"
        assert ut.display_name == "Employee"
        assert ut.description == "Employee user type"
        assert ut.default is False
        assert ut.created_by == "00ucreated"
        assert ut.last_updated_by == "00uupdated"
        assert isinstance(ut.created, datetime)
        assert isinstance(ut.last_updated, datetime)
        assert ut.created == datetime(2026, 1, 2, 3, 4, 5, tzinfo=timezone.utc)
        assert ut.last_updated == datetime(2026, 1, 3, 4, 5, 6, tzinfo=timezone.utc)

    def test_from_dict_hydrates_nested_links(self):
        ut = UserType.from_dict(FULL_PAYLOAD)

        assert ut.links is not None
        # UserTypeLinks stores the `self` alias under attribute `var_self`
        assert ut.links.var_self is not None
        assert ut.links.var_self.href == "https://example.okta.com/api/v1/meta/types/user/oty123"

    def test_from_dict_returns_none_for_none_input(self):
        assert UserType.from_dict(None) is None

    def test_from_dict_ignores_missing_optional_fields(self):
        ut = UserType.from_dict({"name": "employee", "displayName": "Employee"})

        assert ut is not None
        assert ut.name == "employee"
        assert ut.display_name == "Employee"
        assert ut.id is None
        assert ut.description is None
        assert ut.created is None
        assert ut.last_updated is None
        assert ut.links is None


class TestUserTypeConstruction:
    """Model construction rules — required fields, alias support."""

    def test_requires_name_and_display_name(self):
        with pytest.raises(ValidationError) as exc:
            UserType(description="missing required fields")
        errors = {tuple(e["loc"]) for e in exc.value.errors()}
        assert ("name",) in errors
        assert ("displayName",) in errors

    def test_accepts_alias_and_field_names(self):
        via_alias = UserType(name="employee", displayName="Employee")
        via_field = UserType(name="employee", display_name="Employee")
        assert via_alias.display_name == via_field.display_name == "Employee"


class TestUserTypeToDict:
    """Serialization to wire-format dicts.

    The generated to_dict() excludes readOnly fields (created, createdBy, default,
    id, lastUpdated, lastUpdatedBy) — see excluded_fields in user_type.py. Only
    client-writable fields plus _links are emitted.
    """

    def test_to_dict_excludes_read_only_fields(self):
        ut = UserType(
            id="oty123",
            name="employee",
            displayName="Employee",
            description="Employee user type",
            default=False,
            createdBy="00ucreated",
            lastUpdatedBy="00uupdated",
        )

        assert ut.to_dict() == {
            "name": "employee",
            "displayName": "Employee",
            "description": "Employee user type",
        }

    def test_to_dict_omits_unset_optional_fields(self):
        ut = UserType(name="employee", displayName="Employee")
        assert ut.to_dict() == {"name": "employee", "displayName": "Employee"}

    def test_to_dict_serializes_links_via_nested_to_dict(self):
        ut = UserType.from_dict(FULL_PAYLOAD)
        out = ut.to_dict()
        assert "_links" in out
        assert out["_links"]["self"]["href"] == FULL_PAYLOAD["_links"]["self"]["href"]


class TestUserTypeJsonRoundtrip:
    def test_from_json_then_to_json_round_trips_writable_fields(self):
        import json

        ut = UserType.from_json(
            '{"name":"employee","displayName":"Employee","description":"d"}'
        )
        assert ut is not None
        assert json.loads(ut.to_json()) == {
            "name": "employee",
            "displayName": "Employee",
            "description": "d",
        }


class TestUserTypeVsUserTypeRef:
    """Regression guard for the api.yaml name-collision bug.

    Prior to the spec fix, UserType was generated with only `id` because the inline
    `User.type` object shadowed it. That inline shape now lives in UserTypeRef, and
    UserType must carry the full component schema.
    """

    def test_user_type_declares_full_component_fields(self):
        expected = {
            "created",
            "created_by",
            "default",
            "description",
            "display_name",
            "id",
            "last_updated",
            "last_updated_by",
            "name",
            "links",
        }
        assert expected.issubset(UserType.model_fields.keys())

    def test_user_type_ref_is_id_only(self):
        assert set(UserTypeRef.model_fields.keys()) == {"id"}
