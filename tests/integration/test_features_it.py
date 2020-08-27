import pytest
from tests.mocks import MockOktaClient
import okta.models as models


class TestFeaturesResource:
    """
    Integration Tests for the Features Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_features(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List
        features, _, err = await client.list_features()
        assert err is None
        assert len(features) > 0
        assert isinstance(features[0], models.Feature)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_feature(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List
        features, _, err = await client.list_features()
        assert err is None
        assert len(features) > 0
        assert isinstance(features[0], models.Feature)

        first_feature = features[0]

        # Retrieve with ID
        retrieved_feature, _, err = await client.get_feature(first_feature.id)
        assert err is None
        assert retrieved_feature.id == first_feature.id
        assert retrieved_feature.name == first_feature.name
        assert retrieved_feature.description == first_feature.description

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_feature_dependencies(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List
        features, _, err = await client.list_features()
        assert err is None
        assert len(features) > 0
        assert isinstance(features[0], models.Feature)

        first_feature = features[0]

        # Retrieve Dependencies with ID
        feature_dependencies, _, err = await \
            client.list_feature_dependencies(first_feature.id)
        assert err is None
        assert isinstance(feature_dependencies, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_feature_dependents(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List
        features, _, err = await client.list_features()
        assert err is None
        assert len(features) > 0
        assert isinstance(features[0], models.Feature)

        first_feature = features[0]

        # Retrieve Dependencies with ID
        feature_dependents, _, err = await \
            client.list_feature_dependents(first_feature.id)
        assert err is None
        assert isinstance(feature_dependents, list)

    @pytest.mark.skip
    @pytest.mark.asyncio
    async def test_update_feature_lifecycle(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List
        features, _, err = await client.list_features()
        assert err is None
        assert len(features) > 0
        assert isinstance(features[0], models.Feature)

        first_feature = features[0]

        # Update
        first_feature_id = first_feature.id
        original_status = first_feature.status
        lifecycle = "enable" if original_status == "DISABLED"\
            else "disable"
        status_change, _, err = await \
            client.update_feature_lifecycle(first_feature_id, lifecycle)
        assert err is None
        assert isinstance(status_change, models.Feature)
        assert original_status != status_change.status

        # Revert
        lifecycle = "disable" if original_status == "DISABLED"\
            else "enable"
        updated_status_change, _, err = await \
            client.update_feature_lifecycle(first_feature_id, lifecycle)
        assert err is None
        assert isinstance(updated_status_change, models.Feature)
        assert original_status == updated_status_change.status
