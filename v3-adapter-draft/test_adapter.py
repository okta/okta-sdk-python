import asyncio
from okta.client import Client


def basic():
    from okta import models
    print(models.Application)
    from okta.client import swagger_api

#basic()

async def main():
    client = Client()
    users, resp, err = await client.list_users()
    user = users[0]
    user, resp, err = await client.get_user(user.id)
    print(type(user))

#asyncio.run(main())


import okta
import okta.models as models


async def create_user():
    client = Client()

    # Create Password
    password = models.PasswordCredential({
        "value": "Password150kta"
    })

    # Create User Credentials
    user_creds = models.UserCredentials({
        "password": password
    })

    # Create User Profile and CreateUser Request
    user_profile = models.UserProfile()
    user_profile.first_name = "John"
    user_profile.last_name = "Doe-Get"
    user_profile.email = "John.Doe-Get@example.com"
    user_profile.login = "John.Doe-Get@example.com"

    create_user_req = models.CreateUserRequest({
        "credentials": user_creds,
        "profile": user_profile
    })

    query_params_create = {"activate": "False"}

    print('-' * 50)
    print(create_user_req)
    print('-' * 50)
    # Create User
    user, resp, err = await client.create_user(create_user_req, query_params_create)
    assert err is None
    print(user)

#asyncio.run(create_user())

async def get_user_bad_id():
    client = Client()
    user_id = '00u2wgtu44OlFQB9s5d7'
    user, _, err = await client.get_user(user_id)
    #print(err)


#asyncio.run(get_user_bad_id())
asyncio.run(main())
