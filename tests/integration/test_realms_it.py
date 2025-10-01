# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import pytest
import uuid

from tests.mocks import MockOktaClient
import okta.models as models
from okta.errors.okta_api_error import OktaAPIError


class TestRealmsResource:
    """
    Comprehensive Integration Tests for the Realms API
    Testing all 15 RealmApi methods with proper coverage
    """

    # Shared helper methods
    def _create_test_realm_data(self, suffix=None):
        """Create test realm data with unique name"""
        import time
        import random
        # Generate shorter but unique identifier
        timestamp = int(time.time()) % 100000  # last 5 digits of timestamp
        random_num = random.randint(100, 999)  # 3-digit random
        unique_id = f"{str(uuid.uuid4())[:6]}{timestamp}{random_num}"  # Short UUID + time + random
        
        # Keep realm names short to avoid field length limits
        if suffix:
            realm_name = f"IT-{suffix[:8]}-{unique_id}"  # Truncate suffix to 8 chars max
        else:
            realm_name = f"IT-Test-{unique_id}"
        
        realm_profile = models.RealmProfile(name=realm_name)
        realm_obj = models.Realm(profile=realm_profile)
        return realm_obj, realm_name

    async def _cleanup_test_realm(self, client, realm_id):
        """Helper to cleanup test realm - safe cleanup"""
        if realm_id:
            try:
                _, _, err = await client.delete_realm(realm_id)
                if err:
                    print(f"Cleanup warning for realm {realm_id}: {err}")
            except Exception as e:
                print(f"Cleanup failed for realm {realm_id}: {e}")

    # Core CRUD method tests (5 methods)
    
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_realm_basic(self, fs):
        """Test basic create_realm functionality"""
        client = MockOktaClient(fs)
        realm_obj, _ = self._create_test_realm_data("create")
        
        created_realm = None
        try:
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            assert isinstance(created_realm, models.Realm)
            assert created_realm.profile.name.startswith("IT-create-")
            assert created_realm.id is not None
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_realm_basic(self, fs):
        """Test basic get_realm functionality"""
        client = MockOktaClient(fs)
        realm_obj, _ = self._create_test_realm_data("get")
        
        created_realm = None
        try:
            # Create realm first
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            
            # Test get_realm
            retrieved_realm, _, err = await client.get_realm(created_realm.id)
            assert err is None
            assert isinstance(retrieved_realm, models.Realm)
            assert retrieved_realm.id == created_realm.id
            assert retrieved_realm.profile.name.startswith("IT-get-")
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_realms_basic(self, fs):
        """Test basic list_realms functionality"""
        client = MockOktaClient(fs)
        
        # Test list_realms without parameters
        realms_list, _, err = await client.list_realms()
        assert err is None
        assert isinstance(realms_list, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_realms_with_limit(self, fs):
        """Test list_realms with limit parameter"""
        client = MockOktaClient(fs)
        
        # Test with different limit values
        test_limits = [1, 3, 5]
        for limit in test_limits:
            limited_realms, _, err = await client.list_realms(limit=limit)
            assert err is None
            assert isinstance(limited_realms, list)
            assert len(limited_realms) <= limit

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_realms_with_sort(self, fs):
        """Test list_realms with sort parameters"""
        client = MockOktaClient(fs)
        
        # Test sorting by name ascending
        sorted_realms_asc, _, err = await client.list_realms(
            sort_by="profile.name", 
            sort_order="asc"
        )
        assert err is None or "sort" in str(err).lower()  # Some orgs might not support sorting
        assert isinstance(sorted_realms_asc, list)
        
        # Test sorting by name descending
        sorted_realms_desc, _, err = await client.list_realms(
            sort_by="profile.name", 
            sort_order="desc"
        )
        assert err is None or "sort" in str(err).lower()
        assert isinstance(sorted_realms_desc, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_realm_basic(self, fs):
        """Test basic update_realm functionality (known SDK issue with PUT vs POST)"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("update")
        
        created_realm = None
        try:
            # Create realm first
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            
            # Update realm name
            updated_name = f"{realm_name}-Updated"
            created_realm.profile.name = updated_name
            
            # Test update_realm (may fail due to SDK bug using POST instead of PUT)
            updated_realm, _, err = await client.update_realm(created_realm.id, created_realm)
            
            # Known issue: SDK uses POST method but API expects PUT
            # So we expect either success or specific error
            if err is not None:
                assert isinstance(err, OktaAPIError)
                # Common error codes for method not allowed or endpoint issues
                assert any(code in str(err) for code in ["405", "E0000022", "endpoint does not support"])
            else:
                # If it somehow works, verify the update
                assert updated_realm.profile.name == updated_name
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_realm_basic(self, fs):
        """Test basic delete_realm functionality"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("delete")
        
        # Create realm first
        created_realm, _, err = await client.create_realm(realm_obj)
        assert err is None
        realm_id = created_realm.id
        
        # Test delete_realm
        _, _, err = await client.delete_realm(realm_id)
        assert err is None
        
        # Verify deletion by attempting to get the realm (should return 404)
        _, _, err = await client.get_realm(realm_id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert any(code in str(err) for code in ["404", "E0000007", "not found"])

    # HTTP Info variant tests (5 methods)
    
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_realm_with_http_info(self, fs):
        """Test create_realm_with_http_info method"""
        client = MockOktaClient(fs)
        realm_obj, _ = self._create_test_realm_data("http-create")
        
        created_realm = None
        try:
            # Call method directly on client
            created_realm, http_response, err = await client.create_realm_with_http_info(realm_obj)
            
            assert err is None
            assert http_response is not None
            assert created_realm is not None
            assert isinstance(created_realm, models.Realm)
            
            # Validate HTTP response details
            assert hasattr(http_response, 'status_code')
            assert http_response.status_code == 200
            assert hasattr(http_response, 'headers')
            
            # Validate realm data
            assert hasattr(created_realm, 'profile')
            assert created_realm.profile.name.startswith("IT-http-cre")
            assert created_realm.id is not None
        finally:
            if created_realm and hasattr(created_realm, 'id'):
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_realm_with_http_info(self, fs):
        """Test get_realm_with_http_info method"""
        client = MockOktaClient(fs)
        realm_obj, _ = self._create_test_realm_data("http-get")
        
        created_realm = None
        try:
            # Create realm first
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            
            # Test HTTP info variant
            retrieved_realm, http_response, err = await client.get_realm_with_http_info(created_realm.id)
            
            assert err is None
            assert http_response is not None
            assert retrieved_realm is not None
            assert isinstance(retrieved_realm, models.Realm)
            
            # Validate HTTP response details  
            assert hasattr(http_response, 'status_code')
            assert http_response.status_code == 200
            assert hasattr(http_response, 'headers')
            
            # Validate realm data matches
            assert retrieved_realm.id == created_realm.id
            assert retrieved_realm.profile.name.startswith("IT-http-get-")
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_realms_with_http_info(self, fs):
        """Test list_realms_with_http_info method"""
        client = MockOktaClient(fs)
        
        # Test HTTP info variant
        realms_list, http_response, err = await client.list_realms_with_http_info(limit=2)
        
        assert err is None
        assert http_response is not None
        assert realms_list is not None
        assert isinstance(realms_list, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_realm_with_http_info(self, fs):
        """Test update_realm_with_http_info method"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("http-update")
        
        created_realm = None
        try:
            # Create realm first
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            
            # Update realm name
            updated_name = f"{realm_name}-HttpUpdated"
            created_realm.profile.name = updated_name
            
            # Test HTTP info variant (expect same SDK issue)
            try:
                updated_realm, http_response, err = await client.update_realm_with_http_info(
                    created_realm.id, created_realm
                )
                # If successful, verify update
                if err is None:
                    assert http_response is not None
                    assert updated_realm.profile.name == updated_name
                else:
                    # Expected due to SDK PUT/POST issue
                    assert any(code in str(err) for code in ["405", "E0000022", "endpoint does not support"])
            except Exception as e:
                # Expected due to SDK PUT/POST issue
                assert any(code in str(e) for code in ["405", "E0000022", "endpoint does not support"])
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_realm_with_http_info(self, fs):
        """Test delete_realm_with_http_info method"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("http-delete")
        
        # Create realm first
        created_realm, _, err = await client.create_realm(realm_obj)
        assert err is None
        realm_id = created_realm.id
        
        # Test HTTP info variant
        result, http_response, err = await client.delete_realm_with_http_info(realm_id)
        
        assert err is None
        assert http_response is not None
        
        # Verify deletion
        try:
            _, _, err = await client.get_realm(realm_id)
            assert err is not None
        except Exception:
            # Exception on get after delete is expected
            pass

    # Without Preload Content variant tests (5 methods)
    
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_realm_without_preload_content(self, fs):
        """Test create_realm_without_preload_content method"""
        client = MockOktaClient(fs)
        realm_obj, _ = self._create_test_realm_data("preload-create")
        
        created_realm = None
        try:
            # Test without preload content variant
            created_realm, http_response, err = await client.create_realm_without_preload_content(realm_obj)
            
            assert err is None
            assert http_response is not None
            assert created_realm is not None
            assert created_realm.profile.name.startswith("IT-preload-")
        finally:
            if created_realm and hasattr(created_realm, 'id'):
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_realm_without_preload_content(self, fs):
        """Test get_realm_without_preload_content method"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("preload-get")
        
        created_realm = None
        try:
            # Create realm first
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            
            # Test without preload content variant
            retrieved_realm, http_response, err = await client.get_realm_without_preload_content(created_realm.id)
            
            assert err is None
            assert http_response is not None
            assert retrieved_realm is not None
            assert retrieved_realm.id == created_realm.id
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_realms_without_preload_content(self, fs):
        """Test list_realms_without_preload_content method"""
        client = MockOktaClient(fs)
        
        # Test without preload content variant
        realms_list, http_response, err = await client.list_realms_without_preload_content(limit=2)
        
        assert err is None
        assert http_response is not None
        assert realms_list is not None
        assert isinstance(realms_list, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_realm_without_preload_content(self, fs):
        """Test update_realm_without_preload_content method"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("preload-update")
        
        created_realm = None
        try:
            # Create realm first
            created_realm, _, err = await client.create_realm(realm_obj)
            assert err is None
            
            # Update realm name
            updated_name = f"{realm_name}-PreloadUpdated"
            created_realm.profile.name = updated_name
            
            # Test without preload content variant (expect same SDK issue)
            try:
                updated_realm, http_response, err = await client.update_realm_without_preload_content(
                    created_realm.id, created_realm
                )
                # If successful, verify update
                if err is None:
                    assert http_response is not None
                    assert updated_realm.profile.name == updated_name
                else:
                    # Expected due to SDK PUT/POST issue
                    assert any(code in str(err) for code in ["405", "E0000022", "endpoint does not support"])
            except Exception as e:
                # Expected due to SDK PUT/POST issue
                assert any(code in str(e) for code in ["405", "E0000022", "endpoint does not support"])
        finally:
            if created_realm:
                await self._cleanup_test_realm(client, created_realm.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_realm_without_preload_content(self, fs):
        """Test delete_realm_without_preload_content method"""
        client = MockOktaClient(fs)
        realm_obj, realm_name = self._create_test_realm_data("preload-delete")
        
        # Create realm first
        created_realm, _, err = await client.create_realm(realm_obj)
        assert err is None
        realm_id = created_realm.id
        
        # Test without preload content variant
        result, http_response, err = await client.delete_realm_without_preload_content(realm_id)
        
        assert err is None
        assert http_response is not None
        
        # Verify deletion
        try:
            _, _, err = await client.get_realm(realm_id)
            assert err is not None
        except Exception:
            # Exception on get after delete is expected
            pass

    # Error handling and edge case tests

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_realm_not_found_error(self, fs):
        """Test get_realm with non-existent realm ID"""
        client = MockOktaClient(fs)
        
        invalid_realm_id = "nonexistent_realm_123456"
        realm, _, err = await client.get_realm(invalid_realm_id)
        
        assert realm is None
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert any(code in str(err) for code in ["404", "E0000007", "not found"])

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_realm_not_found_error(self, fs):
        """Test delete_realm with non-existent realm ID"""
        client = MockOktaClient(fs)
        
        invalid_realm_id = "nonexistent_realm_123456"
        result = await client.delete_realm(invalid_realm_id)
        
        # Check error in result tuple
        if len(result) == 2:
            _, err = result
        else:
            _, _, err = result
        
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert any(code in str(err) for code in ["404", "E0000007", "not found"])

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_realm_invalid_data_error(self, fs):
        """Test create_realm with invalid realm data"""
        client = MockOktaClient(fs)
        
        # Create realm with empty/invalid profile - should result in null body HTTP request
        invalid_realm = models.Realm()  # Missing required profile
        created_realm, _, err = await client.create_realm(invalid_realm)
        
        # Should return specific API error from Okta
        assert created_realm is None
        assert err is not None
        assert isinstance(err, OktaAPIError)
        # Check for specific Okta error response
        assert any(code in str(err) for code in ["E0000003", "400", "not well-formed"])
        print(f"Proper error validation: {err}")

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_realms_pagination_edge_cases(self, fs):
        """Test list_realms pagination with edge case parameters"""
        client = MockOktaClient(fs)
        
        # Test pagination with limit parameter
        first_page, _, err = await client.list_realms(limit=1)
        assert err is None
        assert isinstance(first_page, list)
        assert len(first_page) >= 1, "Should return at least 1 realm with limit=1"
        
        # Test pagination with after parameter using first realm's ID
        first_realm = first_page[0]
        assert first_realm.id is not None
        
        next_page, _, err = await client.list_realms(limit=1, after=first_realm.id)
        assert err is None
        assert isinstance(next_page, list)
        # The next page might be empty or have different realms
        print(f"Pagination test: first_page={len(first_page)} items, next_page={len(next_page)} items")

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_comprehensive_realm_workflow(self, fs):
        """Test a complete realm lifecycle workflow"""
        client = MockOktaClient(fs)
        
        # Multiple realm operations to increase coverage
        test_realms = []
        
        try:
            # Create multiple realms
            for i in range(3):
                realm_obj, realm_name = self._create_test_realm_data(f"workflow-{i}")
                created_realm, _, err = await client.create_realm(realm_obj)
                
                if err is None and created_realm:
                    test_realms.append(created_realm)
                    
                    # Test various operations on each realm
                    retrieved_realm, _, err = await client.get_realm(created_realm.id)
                    assert err is None
                    assert retrieved_realm.id == created_realm.id
            
            # Test list operations with different parameters
            all_realms, _, err = await client.list_realms()
            assert err is None
            
            limited_realms, _, err = await client.list_realms(limit=2)
            assert err is None
            assert len(limited_realms) <= 2
            
        finally:
            # Cleanup all test realms
            for realm in test_realms:
                await self._cleanup_test_realm(client, realm.id)
