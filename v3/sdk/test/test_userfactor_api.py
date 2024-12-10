
import unittest
import time
import uuid

from okta.api.user_factor_api import UserFactorApi
from okta.api.user_api import UserApi
from okta.okta_configuration import OktaConfiguration
from okta.api_client import ApiClient

from okta.models import (
    CreateUserRequest,
    UserProfile,
    UserType,
    UserFactor,
    SmsUserFactor,
    SmsUserFactorProfile,
    UserCredentials,
    PasswordCredential,
    FactorType
)

class TestUserFactorApi(unittest.TestCase):
    """UserFactorApi unit tests"""
    def setUp(self) -> None:
        configuration = OktaConfiguration().get_configuration()
        api_client = ApiClient(configuration)
        self.userApi = UserApi(api_client)
        self.api = UserFactorApi(api_client)

    def tearDown(self) -> None:
    
        pass
    
    def test_enroll_sms(self) -> None:
        try:
            create_user_request = CreateUserRequest(
                type=UserType(
                    type='test_user_type', 
                    displayName='test_user_type_display_name', 
                    name='test_user_type_name'
                ),
                profile=UserProfile(
                    userType='test_user_type_profile_type', 
                    firstName='John', 
                    lastName='test_list_users',
                    email='test_list_users-python@example.com',
                    login='test_list_users-python@example.com',
                    nickName='test_list_users'
                )
            )
            
            created_user = self.userApi.create_user(create_user_request)
            
            created_user_factor = self.api.enroll_factor(created_user.id, SmsUserFactor(
                factorType=FactorType.SMS, 
                profile=SmsUserFactorProfile(
                        phoneNumber="+16284001133"
                    )
                )
            )
            
            self.assertEqual(created_user_factor.factor_type, FactorType.SMS)       
        except Exception as ex:
            self.fail(ex)
        finally:
            self.userApi.deactivate_user(created_user.id)
            self.userApi.delete_user(created_user.id)
            
    
    def test_enroll_signed_nonce(self) -> None:
        try:
            create_user_request = CreateUserRequest(
                type=UserType(
                    type='test_user_type', 
                    displayName='test_user_type_display_name', 
                    name='test_user_type_name'
                ),
                profile=UserProfile(
                    userType='test_user_type_profile_type', 
                    firstName='John', 
                    lastName='test_list_users',
                    email='test_list_users-python@example.com',
                    login='test_list_users-python@example.com',
                    nickName='test_list_users'
                )
            )
            
            created_user = self.userApi.create_user(create_user_request)
            
            created_user_factor = self.api.enroll_factor(created_user.id, UserFactor(factorType=FactorType.SIGNED_NONCE), activate=True)
            
            self.assertIsNotNone(created_user_factor)
            self.assertIsNotNone(created_user_factor.id)
            
            enrolled_factors = self.api.list_factors(created_user.id)

            self.assertTrue(len(enrolled_factors) > 0)
            enrolled_factor_types = []
            for factor in enrolled_factors:
                enrolled_factor_types.append(factor.factor_type)
                
            self.assertTrue(FactorType.SIGNED_NONCE in enrolled_factor_types)
        except Exception as ex:
            self.fail(ex)
        finally:
            self.userApi.deactivate_user(created_user.id)
            self.userApi.delete_user(created_user.id)
        
        pass
    
    def test_list_factors(self) -> None:
        try:
            create_user_request = CreateUserRequest(
                type=UserType(
                    type='test_user_type', 
                    displayName='test_user_type_display_name', 
                    name='test_user_type_name'
                ),
                profile=UserProfile(
                    userType='test_user_type_profile_type', 
                    firstName='John', 
                    lastName='test_list_factors',
                    email='test_list_factors-python@example.com',
                    login='test_list_factors-python@example.com',
                    nickName='test_list_factors'
                ),
                credentials=UserCredentials(password=PasswordCredential(value=str(uuid.uuid4())))
            )
            
            created_user = self.userApi.create_user(create_user_request)
            
            time.sleep(3)         
            enrolled_factors = self.api.list_factors(created_user.id)

            self.assertTrue(len(enrolled_factors) > 0)
        except Exception as ex:
            self.fail(ex)
        finally:
            self.userApi.deactivate_user(created_user.id)
            self.userApi.delete_user(created_user.id)
        
        pass