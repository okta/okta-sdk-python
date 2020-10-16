import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError
from okta.client import Client


class TestFactorsResource:
    """
    Integration Tests for the Factors Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_enroll_security_question_factor(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        client = Client()

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Security-Question"
        user_profile.email = "John.Doe-Security-Question@example.com"
        user_profile.login = "John.Doe-Security-Question@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # Create and add factor
        sec_q_factor = models.SecurityQuestionUserFactor({
            "factorType": models.FactorType.QUESTION,
            "provider": models.FactorProvider.OKTA,
            "profile": models.SecurityQuestionUserFactorProfile({
                "question": "disliked_food",
                "answer": "lasagna"
            })
        })

        enrolled_factor, _, err = await \
            client.enroll_factor(created_user.id, sec_q_factor)
        assert err is None
        assert isinstance(enrolled_factor, models.SecurityQuestionUserFactor)

        # List factor to validate
        users_factors, _, err = await client.list_factors(created_user.id)
        assert err is None
        assert len(users_factors) > 0 and len(users_factors) == 1
        assert isinstance(users_factors[0], models.SecurityQuestionUserFactor)
        assert users_factors[0].factor_type == models.FactorType.QUESTION
        assert users_factors[0].id == sec_q_factor.id
        assert users_factors[0].profile.question ==\
            sec_q_factor.profile.question
        assert users_factors[0].profile.answer == sec_q_factor.profile.answer
        assert users_factors[0].profile.question_text

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_enroll_sms_factor(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-SMS"
        user_profile.email = "John.Doe-SMS@example.com"
        user_profile.login = "John.Doe-SMS@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # Create and add factor
        sms_factor = models.SmsUserFactor({
            "profile": models.SmsUserFactorProfile({
                "phoneNumber": "+12345678901"
            })
        })

        enrolled_factor, _, err = await \
            client.enroll_factor(created_user.id, sms_factor)
        assert err is None
        assert isinstance(enrolled_factor, models.SmsUserFactor)

        # List factor to validate
        users_factors, _, err = await client.list_factors(created_user.id)
        assert err is None
        assert len(users_factors) > 0 and len(users_factors) == 1
        assert isinstance(users_factors[0], models.SmsUserFactor)
        assert users_factors[0].id == enrolled_factor.id
        assert users_factors[0].factor_type == models.FactorType.SMS
        assert users_factors[0].profile.phone_number ==\
            sms_factor.profile.phone_number

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_factors_new_user(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-List-Factor"
        user_profile.email = "John.Doe-List-Factor@example.com"
        user_profile.login = "John.Doe-List-Factor@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # List factor to validate
        users_factors, _, err = await client.list_factors(created_user.id)
        assert err is None
        assert len(users_factors) == 0

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_factor(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get-Factor"
        user_profile.email = "John.Doe-Get-Factor@example.com"
        user_profile.login = "John.Doe-Get-Factor@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # Create and add factor
        sms_factor = models.SmsUserFactor({
            "profile": models.SmsUserFactorProfile({
                "phoneNumber": "+12345678901"
            })
        })

        enrolled_factor, _, err = await \
            client.enroll_factor(created_user.id, sms_factor)
        assert err is None
        assert isinstance(enrolled_factor, models.SmsUserFactor)

        # Get factor to validate
        retrieved_user_factor, _, err = await client.get_factor(
            created_user.id, enrolled_factor.id
        )
        assert err is None
        assert isinstance(retrieved_user_factor, models.SmsUserFactor)
        assert retrieved_user_factor.id == enrolled_factor.id
        assert retrieved_user_factor.factor_type == models.FactorType.SMS
        assert retrieved_user_factor.profile.phone_number ==\
            sms_factor.profile.phone_number

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_factor(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Delete-Factor"
        user_profile.email = "John.Doe-Delete-Factor@example.com"
        user_profile.login = "John.Doe-Delete-Factor@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # Create and add factor
        sms_factor = models.SmsUserFactor({
            "profile": models.SmsUserFactorProfile({
                "phoneNumber": "+12345678901"
            })
        })

        enrolled_factor, _, err = await \
            client.enroll_factor(created_user.id, sms_factor)
        assert err is None
        assert isinstance(enrolled_factor, models.SmsUserFactor)

        # Get factor to validate
        retrieved_user_factor, _, err = await client.get_factor(
            created_user.id, enrolled_factor.id
        )
        assert err is None
        assert isinstance(retrieved_user_factor, models.SmsUserFactor)
        assert retrieved_user_factor.id == enrolled_factor.id
        assert retrieved_user_factor.factor_type == models.FactorType.SMS
        assert retrieved_user_factor.profile.phone_number ==\
            sms_factor.profile.phone_number

        # Delete factor
        _, err = await client.delete_factor(created_user.id,
                                            enrolled_factor.id)
        assert err is None

        # Get factor to validate
        retrieved_user_factor, resp, err = await client.get_factor(
            created_user.id, enrolled_factor.id
        )
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert retrieved_user_factor is None
        assert resp.get_status() == HTTPStatus.NOT_FOUND

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None

    @pytest.mark.skip
    @pytest.mark.asyncio
    async def test_reset_factors(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        client = Client()

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Reset-Factor"
        user_profile.email = "John.Doe-Reset-Factor@example.com"
        user_profile.login = "John.Doe-Reset-Factor@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # Create and add factor
        sms_factor = models.SmsUserFactor({
            "profile": models.SmsUserFactorProfile({
                "phoneNumber": "+12345678901"
            })
        })

        enrolled_factor, _, err = await \
            client.enroll_factor(created_user.id, sms_factor)
        assert err is None
        assert isinstance(enrolled_factor, models.SmsUserFactor)

        # Get factor to validate
        retrieved_user_factor, _, err = await client.get_factor(
            created_user.id, enrolled_factor.id
        )
        assert err is None
        assert isinstance(retrieved_user_factor, models.SmsUserFactor)
        assert retrieved_user_factor.id == enrolled_factor.id
        assert retrieved_user_factor.factor_type == models.FactorType.SMS
        assert retrieved_user_factor.profile.phone_number ==\
            sms_factor.profile.phone_number

        # Reset factor
        _, err = await client.reset_factors(created_user.id)
        assert err is None

        # List factors to validate
        users_factors, _, err = await client.list_factors(created_user.id)
        assert err is None
        assert len(users_factors) == 0

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None

    @pytest.mark.asyncio
    @pytest.mark.skip
    async def test_list_supported_security_questions(self):
        # Instantiate Mock Client
        client = MockOktaClient(fs)
        client = Client()

        # Create User
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-List-Security-Question"
        user_profile.email = "John.Doe-List-Security-Question@example.com"
        user_profile.login = "John.Doe-List-Security-Question@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": models.UserCredentials({
                "password": models.PasswordCredential({
                    "value": "Password150kta"
                })
            }),
            "profile": user_profile
        })

        created_user, _, err = await client.create_user(create_user_req)
        assert err is None
        assert isinstance(created_user, models.User)

        # Create and add factor
        sec_q_factor = models.SecurityQuestionUserFactor({
            "factorType": models.FactorType.QUESTION,
            "provider": models.FactorProvider.OKTA,
            "profile": models.SecurityQuestionUserFactorProfile({
                "question": "disliked_food",
                "answer": "lasagna"
            })
        })

        enrolled_factor, _, err = await \
            client.enroll_factor(created_user.id, sec_q_factor)
        assert err is None
        assert isinstance(enrolled_factor, models.SecurityQuestionUserFactor)

        # List factor to validate
        users_factors, _, err = await client.list_factors(created_user.id)
        assert err is None
        assert len(users_factors) > 0 and len(users_factors) == 1
        assert isinstance(users_factors[0], models.SecurityQuestionUserFactor)
        assert users_factors[0].factor_type == models.FactorType.QUESTION
        assert users_factors[0].id == sec_q_factor.id
        assert users_factors[0].profile.question ==\
            sec_q_factor.profile.question
        assert users_factors[0].profile.answer == sec_q_factor.profile.answer
        assert users_factors[0].profile.question_text

        # List Security q's
        retrieved_questions, _, err = await \
            client.list_supported_security_questions(created_user.id)
        assert err is None
        assert next((question for question in retrieved_questions
                     if question.profile.question ==
                     enrolled_factor.profile.question))

        # Deactivate + delete user
        _, err = await client.deactivate_user(created_user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(created_user.id)
        assert err is None
