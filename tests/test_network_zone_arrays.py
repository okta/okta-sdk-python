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
Unit tests for the array-typed `asns` / `locations` fields on the generated
DynamicNetworkZone and EnhancedDynamicNetworkZone models.

These tests guard against regressions of the bug where api.yaml declared these fields
as `allOf: [$ref: <array schema>, description: ...]`. OpenAPI Generator 7.7.0 treated
that wrapper as an object and generated empty, field-less models
(e.g. EnhancedDynamicNetworkZoneAllOfAsnsInclude), so any list returned by the API —
including the empty list `[]` — raised a pydantic ValidationError and broke
list_network_zones(). After the spec fix the fields are plain arrays:
`List[str]` for ASNs and `List[NetworkZoneLocation]` for locations.
"""

import json

from pydantic import ValidationError

import pytest

import okta.models
from okta.models.dynamic_network_zone import DynamicNetworkZone
from okta.models.enhanced_dynamic_network_zone import EnhancedDynamicNetworkZone
from okta.models.enhanced_dynamic_network_zone_all_of_asns import (
    EnhancedDynamicNetworkZoneAllOfAsns,
)
from okta.models.enhanced_dynamic_network_zone_all_of_ip_service_categories import (
    EnhancedDynamicNetworkZoneAllOfIpServiceCategories,
)
from okta.models.enhanced_dynamic_network_zone_all_of_locations import (
    EnhancedDynamicNetworkZoneAllOfLocations,
)
from okta.models.network_zone import NetworkZone
from okta.models.network_zone_location import NetworkZoneLocation

BASE_ZONE = {
    "id": "nzo1example0000000001",
    "name": "Example Zone",
    "status": "ACTIVE",
    "usage": "BLOCKLIST",
    "system": False,
}

# Shape returned by the API for an Enhanced Dynamic Network Zone with nothing configured
EMPTY_EDNZ_PAYLOAD = {
    **BASE_ZONE,
    "type": "DYNAMIC_V2",
    "asns": {"include": [], "exclude": []},
    "locations": {"include": [], "exclude": []},
    "ipServiceCategories": {"include": ["ALL_ANONYMIZERS"], "exclude": []},
}

FULL_EDNZ_PAYLOAD = {
    **BASE_ZONE,
    "type": "DYNAMIC_V2",
    "asns": {"include": ["64496", "64497"], "exclude": ["64511"]},
    "locations": {
        "include": [{"country": "US", "region": "US-CA"}, {"country": "DE"}],
        "exclude": [{"country": "FR"}],
    },
}

FULL_DNZ_PAYLOAD = {
    **BASE_ZONE,
    "type": "DYNAMIC",
    "asns": ["64496", "64497"],
    "locations": [{"country": "US", "region": "US-CA"}, {"country": "DE"}],
}


class TestEnhancedDynamicNetworkZoneFromDict:
    """Deserialization of DYNAMIC_V2 zones from wire-format dicts."""

    def test_from_dict_accepts_empty_asns_and_locations(self):
        zone = EnhancedDynamicNetworkZone.from_dict(EMPTY_EDNZ_PAYLOAD)

        assert zone is not None
        assert zone.asns.include == []
        assert zone.asns.exclude == []
        assert zone.locations.include == []
        assert zone.locations.exclude == []

    def test_from_dict_preserves_asn_values(self):
        zone = EnhancedDynamicNetworkZone.from_dict(FULL_EDNZ_PAYLOAD)

        assert zone.asns.include == ["64496", "64497"]
        assert zone.asns.exclude == ["64511"]

    def test_from_dict_hydrates_locations_as_models(self):
        zone = EnhancedDynamicNetworkZone.from_dict(FULL_EDNZ_PAYLOAD)

        assert all(isinstance(loc, NetworkZoneLocation) for loc in zone.locations.include)
        assert zone.locations.include[0].country == "US"
        assert zone.locations.include[0].region == "US-CA"
        assert zone.locations.include[1].country == "DE"
        assert zone.locations.include[1].region is None
        assert zone.locations.exclude[0].country == "FR"

    def test_from_dict_ignores_missing_asns_and_locations(self):
        zone = EnhancedDynamicNetworkZone.from_dict({**BASE_ZONE, "type": "DYNAMIC_V2"})

        assert zone is not None
        assert zone.asns is None
        assert zone.locations is None

    def test_from_dict_accepts_null_location_lists(self):
        locations = EnhancedDynamicNetworkZoneAllOfLocations.from_dict(
            {"include": None, "exclude": None}
        )

        assert locations.include is None
        assert locations.exclude is None

    def test_from_dict_rejects_non_string_asns(self):
        with pytest.raises(ValidationError):
            EnhancedDynamicNetworkZoneAllOfAsns.from_dict({"include": [64496]})


class TestDynamicNetworkZoneFromDict:
    """Deserialization of DYNAMIC zones, where asns/locations are top-level arrays."""

    def test_from_dict_preserves_asns_and_locations(self):
        zone = DynamicNetworkZone.from_dict(FULL_DNZ_PAYLOAD)

        assert zone is not None
        assert zone.asns == ["64496", "64497"]
        assert all(isinstance(loc, NetworkZoneLocation) for loc in zone.locations)
        assert zone.locations[0].country == "US"
        assert zone.locations[0].region == "US-CA"

    def test_from_dict_accepts_empty_arrays(self):
        zone = DynamicNetworkZone.from_dict(
            {**BASE_ZONE, "type": "DYNAMIC", "asns": [], "locations": []}
        )

        assert zone.asns == []
        assert zone.locations == []

    def test_from_dict_rejects_non_string_asns(self):
        with pytest.raises(ValidationError):
            DynamicNetworkZone.from_dict({**BASE_ZONE, "type": "DYNAMIC", "asns": [64496]})


class TestNetworkZoneDiscriminator:
    """list_network_zones() deserializes through the NetworkZone base class."""

    def test_dynamic_v2_with_empty_arrays_routes_to_enhanced_zone(self):
        zone = NetworkZone.from_dict(EMPTY_EDNZ_PAYLOAD)

        assert isinstance(zone, EnhancedDynamicNetworkZone)
        assert zone.asns.include == []
        assert zone.locations.include == []

    def test_dynamic_routes_to_dynamic_zone(self):
        zone = NetworkZone.from_dict(FULL_DNZ_PAYLOAD)

        assert isinstance(zone, DynamicNetworkZone)
        assert zone.asns == ["64496", "64497"]


class TestNetworkZoneToDict:
    """Serialization back to wire-format dicts keeps the array shape."""

    def test_enhanced_zone_to_dict_preserves_array_shape(self):
        out = EnhancedDynamicNetworkZone.from_dict(FULL_EDNZ_PAYLOAD).to_dict()

        assert out["asns"] == FULL_EDNZ_PAYLOAD["asns"]
        assert out["locations"] == FULL_EDNZ_PAYLOAD["locations"]

    def test_enhanced_zone_to_dict_preserves_empty_arrays(self):
        out = EnhancedDynamicNetworkZone.from_dict(EMPTY_EDNZ_PAYLOAD).to_dict()

        assert out["asns"] == {"include": [], "exclude": []}
        assert out["locations"] == {"include": [], "exclude": []}

    def test_location_to_dict_keeps_explicit_null(self):
        locations = EnhancedDynamicNetworkZoneAllOfLocations.from_dict(
            {"include": None, "exclude": None}
        )

        # include/exclude are nullable, so a null set at init is emitted rather than dropped
        assert locations.to_dict() == {"include": None, "exclude": None}

    def test_dynamic_zone_to_dict_preserves_array_shape(self):
        out = DynamicNetworkZone.from_dict(FULL_DNZ_PAYLOAD).to_dict()

        assert out["asns"] == FULL_DNZ_PAYLOAD["asns"]
        assert out["locations"] == FULL_DNZ_PAYLOAD["locations"]


class TestNetworkZoneJsonRoundtrip:
    def test_enhanced_zone_round_trips_via_json(self):
        zone = EnhancedDynamicNetworkZone.from_json(json.dumps(FULL_EDNZ_PAYLOAD))
        out = json.loads(zone.to_json())

        assert out["asns"] == FULL_EDNZ_PAYLOAD["asns"]
        assert out["locations"] == FULL_EDNZ_PAYLOAD["locations"]

    def test_dynamic_zone_round_trips_via_json(self):
        zone = DynamicNetworkZone.from_json(json.dumps(FULL_DNZ_PAYLOAD))
        out = json.loads(zone.to_json())

        assert out["asns"] == FULL_DNZ_PAYLOAD["asns"]
        assert out["locations"] == FULL_DNZ_PAYLOAD["locations"]


class TestNetworkZoneEdgeCases:
    """Remaining generated paths on the affected models: None / model-instance input,
    string helpers, nested JSON helpers, _links, nullable locations and proxyType."""

    IP_SERVICE_CATEGORIES = {"include": ["ALL_ANONYMIZERS"], "exclude": []}

    ALL_MODELS = [
        DynamicNetworkZone,
        EnhancedDynamicNetworkZone,
        EnhancedDynamicNetworkZoneAllOfAsns,
        EnhancedDynamicNetworkZoneAllOfLocations,
        EnhancedDynamicNetworkZoneAllOfIpServiceCategories,
    ]

    @pytest.mark.parametrize("model", ALL_MODELS)
    def test_from_dict_returns_none_for_none_input(self, model):
        assert model.from_dict(None) is None

    @pytest.mark.parametrize(
        "model, payload",
        [
            (DynamicNetworkZone, FULL_DNZ_PAYLOAD),
            (EnhancedDynamicNetworkZone, FULL_EDNZ_PAYLOAD),
            (EnhancedDynamicNetworkZoneAllOfAsns, FULL_EDNZ_PAYLOAD["asns"]),
            (EnhancedDynamicNetworkZoneAllOfLocations, FULL_EDNZ_PAYLOAD["locations"]),
            (EnhancedDynamicNetworkZoneAllOfIpServiceCategories, IP_SERVICE_CATEGORIES),
        ],
    )
    def test_from_dict_accepts_model_instance(self, model, payload):
        instance = model.from_dict(payload)

        assert model.from_dict(instance) == instance

    @pytest.mark.parametrize(
        "model, payload, expected",
        [
            (DynamicNetworkZone, FULL_DNZ_PAYLOAD, "64496"),
            (EnhancedDynamicNetworkZone, FULL_EDNZ_PAYLOAD, "64496"),
            (EnhancedDynamicNetworkZoneAllOfAsns, FULL_EDNZ_PAYLOAD["asns"], "64496"),
            (EnhancedDynamicNetworkZoneAllOfLocations, FULL_EDNZ_PAYLOAD["locations"], "US-CA"),
            (EnhancedDynamicNetworkZoneAllOfIpServiceCategories, IP_SERVICE_CATEGORIES, "ALL_ANONYMIZERS"),
        ],
    )
    def test_to_str_includes_array_values(self, model, payload, expected):
        assert expected in model.from_dict(payload).to_str()

    def test_asns_json_round_trip(self):
        asns = EnhancedDynamicNetworkZoneAllOfAsns.from_json(json.dumps(FULL_EDNZ_PAYLOAD["asns"]))

        assert json.loads(asns.to_json()) == FULL_EDNZ_PAYLOAD["asns"]

    def test_locations_json_round_trip(self):
        locations = EnhancedDynamicNetworkZoneAllOfLocations.from_json(
            json.dumps(FULL_EDNZ_PAYLOAD["locations"])
        )

        assert json.loads(locations.to_json()) == FULL_EDNZ_PAYLOAD["locations"]

    def test_ip_service_categories_json_round_trip(self):
        categories = EnhancedDynamicNetworkZoneAllOfIpServiceCategories.from_json(
            json.dumps(self.IP_SERVICE_CATEGORIES)
        )

        assert json.loads(categories.to_json()) == self.IP_SERVICE_CATEGORIES

    @pytest.mark.parametrize(
        "model, payload",
        [
            (DynamicNetworkZone, FULL_DNZ_PAYLOAD),
            (EnhancedDynamicNetworkZone, FULL_EDNZ_PAYLOAD),
        ],
    )
    def test_to_dict_serializes_links_via_nested_to_dict(self, model, payload):
        href = "https://example.okta.com/api/v1/zones/nzo1example0000000001"
        zone = model.from_dict({**payload, "_links": {"self": {"href": href}}})

        assert zone.to_dict()["_links"]["self"]["href"] == href

    def test_dynamic_zone_to_dict_keeps_explicit_null_locations(self):
        zone = DynamicNetworkZone.from_dict({**BASE_ZONE, "type": "DYNAMIC", "locations": None})

        # locations is nullable, so a null set at init is emitted rather than dropped
        assert zone.to_dict()["locations"] is None

    def test_dynamic_zone_accepts_known_proxy_type(self):
        zone = DynamicNetworkZone.from_dict({**FULL_DNZ_PAYLOAD, "proxyType": "Tor"})

        assert zone.proxy_type == "Tor"

    def test_dynamic_zone_rejects_unknown_proxy_type(self):
        with pytest.raises(ValidationError):
            DynamicNetworkZone.from_dict({**FULL_DNZ_PAYLOAD, "proxyType": "NotAProxyType"})


MAX_ITEMS = 75


def _items(kind, count):
    """Build `count` synthetic entries of the item type for `kind`."""
    if kind == "locations":
        return [{"country": "US"} for _ in range(count)]
    if kind == "ip_service_categories":
        return ["ALL_ANONYMIZERS"] * count
    return [str(64496 + i) for i in range(count)]


class TestNetworkZoneArrayMaxItems:
    """The upstream spec declares `maxItems: 75` on every network zone array, which
    generates `Field(max_length=75)`. Validation applies on parse, on construction,
    and on assignment (the models set validate_assignment=True)."""

    CASES = [
        (DynamicNetworkZone, "asns", "asns"),
        (DynamicNetworkZone, "locations", "locations"),
        (EnhancedDynamicNetworkZoneAllOfAsns, "include", "asns"),
        (EnhancedDynamicNetworkZoneAllOfAsns, "exclude", "asns"),
        (EnhancedDynamicNetworkZoneAllOfLocations, "include", "locations"),
        (EnhancedDynamicNetworkZoneAllOfLocations, "exclude", "locations"),
        (EnhancedDynamicNetworkZoneAllOfIpServiceCategories, "include", "ip_service_categories"),
        (EnhancedDynamicNetworkZoneAllOfIpServiceCategories, "exclude", "ip_service_categories"),
    ]

    @staticmethod
    def _payload(model, field, kind, count):
        if model is DynamicNetworkZone:
            return {**BASE_ZONE, "type": "DYNAMIC", field: _items(kind, count)}
        return {field: _items(kind, count)}

    @pytest.mark.parametrize("model, field, kind", CASES)
    def test_accepts_max_items(self, model, field, kind):
        instance = model.from_dict(self._payload(model, field, kind, MAX_ITEMS))

        assert len(getattr(instance, field)) == MAX_ITEMS

    @pytest.mark.parametrize("model, field, kind", CASES)
    def test_rejects_more_than_max_items(self, model, field, kind):
        with pytest.raises(ValidationError) as exc:
            model.from_dict(self._payload(model, field, kind, MAX_ITEMS + 1))

        assert exc.value.errors()[0]["type"] == "too_long"

    @pytest.mark.parametrize("model, field, kind", CASES)
    def test_rejects_more_than_max_items_on_assignment(self, model, field, kind):
        instance = model.from_dict(self._payload(model, field, kind, 1))
        too_many = model.from_dict(self._payload(model, field, kind, MAX_ITEMS)).model_dump()[field]
        too_many.append(too_many[0])

        with pytest.raises(ValidationError):
            setattr(instance, field, too_many)

    def test_parent_zone_rejects_oversized_nested_list(self):
        payload = {**BASE_ZONE, "type": "DYNAMIC_V2", "asns": {"include": _items("asns", MAX_ITEMS + 1)}}

        with pytest.raises(ValidationError):
            NetworkZone.from_dict(payload)


class TestRemovedWrapperModels:
    """Regression guard for the api.yaml allOf-wrapper bug.

    The empty wrapper models generated from the old spec must no longer be exported,
    and the affected fields must be declared as lists.
    """

    @pytest.mark.parametrize(
        "name",
        [
            "DynamicNetworkZoneAllOfAsns",
            "DynamicNetworkZoneAllOfLocations",
            "EnhancedDynamicNetworkZoneAllOfAsnsInclude",
            "EnhancedDynamicNetworkZoneAllOfAsnsExclude",
            "EnhancedDynamicNetworkZoneAllOfLocationsInclude",
            "EnhancedDynamicNetworkZoneAllOfLocationsExclude",
        ],
    )
    def test_wrapper_model_is_not_exported(self, name):
        assert name not in okta.models._LAZY_IMPORT_MAP

    @pytest.mark.parametrize(
        "model, field",
        [
            (DynamicNetworkZone, "asns"),
            (DynamicNetworkZone, "locations"),
            (EnhancedDynamicNetworkZoneAllOfAsns, "include"),
            (EnhancedDynamicNetworkZoneAllOfAsns, "exclude"),
            (EnhancedDynamicNetworkZoneAllOfLocations, "include"),
            (EnhancedDynamicNetworkZoneAllOfLocations, "exclude"),
        ],
    )
    def test_field_is_declared_as_list(self, model, field):
        assert "List[" in str(model.model_fields[field].annotation)
