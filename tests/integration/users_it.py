import pytest
import okta.models as models
from tests.mocks import MockOktaClient as Client
from okta.errors.okta_api_error import OktaAPIError
from okta.client import Client as OktaClient


class TestUsersResource:
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_user(self):
        test_client = Client()
        test_client = OktaClient()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe"
        user_profile.email = "John.Doe@example.com"
        user_profile.login = "John.Doe@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params = {"activate": "False"}

        user, resp, err = await test_client.create_user(
            create_user_req, query_params)

        got_user, resp, err = await test_client.get_user(user.id)
        assert got_user.id == user.id

        got_user_with_string, resp, err = await test_client.get_user(
            user_profile.login)
        assert got_user_with_string.id == user.id

        assert user.profile.first_name == user_profile.first_name
        assert user.profile.last_name == user_profile.last_name
        assert user.profile.email == user_profile.email
        assert user.profile.login == user_profile.login

        user_id = user.id

        _, err = await test_client.deactivate_or_delete_user(user_id)
        assert err is None

        _, err = await test_client.deactivate_or_delete_user(user_id)
        assert err is None

        user, _, err = await test_client.get_user(user_id)
        assert user is None
        assert isinstance(err, OktaAPIError)

    def test_activate_user(self):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe"
        user_profile.email = "John.Doe@example.com"
        user_profile.login = "John.Doe@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "False"}
        user, resp, err = test_client.create_user(
            create_user_req, query_params_create)

        query_params_activate = {"sendEmail": "False"}
        token, resp, err = test_client.activate_user(
            user.id, query_params_activate)

        assert err is None
        assert token is not None
        assert isinstance(token, models.UserActivationToken)

        query_params_list = {"filter": "status eq \"ACTIVE\""}
        users, resp, err = test_client.list_users(query_params_list)
        assert err is None

        assert next((usr for usr in users if usr.id ==
                     user.id), None) is not None

        _, err = test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = test_client.deactivate_or_delete_user(user.id)
        assert err is None

    def test_update_user(self):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe"
        user_profile.email = "John.Doe@example.com"
        user_profile.login = "John.Doe@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "False"}
        user, resp, err = test_client.create_user(
            create_user_req, query_params_create)

        new_profile = user.profile
        new_profile.nick_name = "JD"
        updated_user = models.User({"profile": new_profile})

        test_client.update_user(user.id, updated_user)
