[<img src="https://aws1.discourse-cdn.com/standard14/uploads/oktadev/original/1X/0c6402653dfb70edc661d4976a43a46f33e5e919.png" align="right" width="256px"/>](https://devforum.okta.com/)
[![Build Status](https://img.shields.io/travis/okta/okta-sdk-python.svg?logo=travis)](https://travis-ci.org/okta/okta-sdk-python)
![Beta Release](https://img.shields.io/badge/Beta-Upcoming-inactive.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Support](https://img.shields.io/badge/support-Developer%20Forum-blue.svg)][devforum]

[![PyPI](https://img.shields.io/pypi/v/okta)](https://pypi.org/project/okta/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/okta)
![Code Style](https://img.shields.io/badge/Code%20Style-flake8-informational.svg)

# Okta Python Management SDK

- [Release Status](#release-status)
- [Need help?](#need-help)
- [Getting Started](#getting-started)
- [Usage Guide](#usage-guide)
- [Exceptions](#exceptions)
- [Pagination](#pagination)
- [Logging](#logging)
- [Configuration Reference](#configuration-reference)
- [Rate Limiting](#rate-limiting)
- [Building the SDK](#building-the-sdk)
- [Contributing](#contributing)

This repository contains the Okta management SDK for Python. This SDK can be used in your server-side code to interact with the Okta management API and

- Create and update users with the [Users API][users-api-docs]
- Add security factors to users with the [Factors API][factors-api-docs]
- Manage groups with the [Groups API][groups-api-docs]
- Manage applications with the [Apps API][apps-api-docs]
- Much more!

> Requires Python version 3.6.0 or higher.

You can also learn more on the [Okta + Python][lang-landing-page] page in our documentation.

## Release status

This library uses semantic versioning and follows Okta's [Library Version Policy][okta-library-versioning].

| Version | Status                           |
| ------- | -------------------------------- |
| 0.x     | :warning: Beta Release (Retired) |
| 1.x     | :heavy_check_mark: Release       |

The latest release can always be found on the [releases page][github-releases].

## Need help?

If you run into problems using the SDK, you can

- Ask questions on the [Okta Developer Forums][devforum]
- Post [issues on GitHub][github-issues] (for code errors)

## Getting started

To install the Okta Python SDK in your project:

```sh
pip install okta
```

You'll also need

- An Okta account, called an _organization_ (sign up for a free [developer organization][dev-okta-signup] if you need one)
- An [API token][api-token-docs]

Construct a client instance by passing it your Okta domain name and API token:

```py
import asyncio

from okta.client import Client as OktaClient

# Instantiating with a Python dictionary in the constructor
config = {
    'orgUrl': 'https://{yourOktaDomain}',
    'token': 'YOUR_API_TOKEN'
}
okta_client = OktaClient(config)

# example of usage, list all users and print their first name and last name
async def main():
    users, resp, err = await okta_client.list_users()
    for user in users:
        print(user.profile.first_name, user.profile.last_name)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Another way to instantiate okta_client (config should be provided in other place as described below):
```py
# Instantiating without in-text credentials
okta_client = OktaClient()
```

> Using a Python dictionary to hard-code the Okta domain and API token is encouraged for development; In production, you should use a more secure way of storing these values. This library supports a few different configuration sources, covered in the [configuration reference](#configuration-reference) section.

### OAuth 2.0

Okta allows you to interact with Okta APIs using scoped OAuth 2.0 access tokens. Each access token enables the bearer to perform specific actions on specific Okta endpoints, with that ability controlled by which scopes the access token contains.

This SDK supports this feature (OAuth 2.0) only for service-to-service applications. Check out [our guides](https://developer.okta.com/docs/guides/implement-oauth-for-okta-serviceapp/overview/) to learn more about how to register a new service application using a private and public key pair.

When using this approach you won't need an API Token because the SDK will request an access token for you. In order to use OAuth 2.0, construct a client instance by passing the following parameters:

```py
from okta.client import Client as OktaClient
config = {
    'orgUrl': 'https://{yourOktaDomain}',
    'authorizationMode': 'PrivateKey',
    'clientId': '{yourClientId}',
    'scopes': ['okta.users.manage'],
    'privateKey': 'YOUR_PRIVATE_JWK' # this parameter should be type of str
}
okta_client = OktaClient(config)


# example of usage, list all users and print their first name and last name
async def main():
    users, resp, err = await okta_client.list_users()
    for user in users:
        print(user.profile.first_name, user.profile.last_name)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Note, that privateKey can be passed in JWK format or in PEM format, i.e. (examples generated with https://mkjwk.org):
```
{
    "p": "4VmEO2ztlIHvalMHX797rWhETbKgB6bRbdGevYpRLZH167hKHB5vsuRjIAXJdujQw8W3rnas9Z-_Ddv1TbR5Qnz0UmhnxQAIbdDDUE9r5P_LEholrjY9Jz0P-W4jey-7cDATeITYHb3t67HcIwVbxQF5fkRdJAhfO029RqkH3OE",
    "kty": "RSA",
    "q": "x8ngsUMrDGReVVpeGdlZzGTSFxrNP89DF4WEQZ7zCpSe3_GpuUPbzgslYQEiX6XJY5ssavavVNOmmQEAt0xsMcxxVOPYCYy7LBE8cJQiFb_bMf2H1-zTlPn_KF4D10h45cLXhu-xh4c52Rh9WDMYZmKWLkAJQ6L_eueGoZkIDmU",
    "d": "R38UamnZiEhOLxD7FYUN5AKj9mHQneRWizblxfNq2T1Nfk4matfZrrlMq_nz9tYZ3-TOCu3u-7k_igM0Tml365mbU_HzkfCrD-ou7cGSrqNgnipj_VQSgJfKRFKATEf4hMfdpKSd4rZzf8OJnq8s-kpRVC4kdHJtJjja59VvHEQRIrN_dkycNHSBWu5UjZbXOO5X3mjwuIh9gpLGZ-nHTqgTpT324q5BLVsH8_ywRGifIj-HQL1O5bJO2Q2_18iL1TbnMSbDwrKdb1edb4bgDuWB4o0xSTXsherTgeXu76gN9FY28tuAKSd34yqp7GZaYcjtkskbWPRtYhOID2cOgQ",
    "e": "AQAB",
    "use": "sig",
    "kid": "test",
    "qi": "FZGFuvW1W9VF31JyrMYJy_BH7vja3d9iZlhFzttNZ-wmiXG4irrI_fLJgmXK6dI3MfIhKPAYi9nnza2kcR1qEV9QObA4NV86RWnc8sAHbDGooe9VK5eJ5jjD7Tq_ZZiLiHGOZit3HylNilOb0k3VsgMcp0F3ZQaMbg35K9rSgZE",
    "dp": "i4D6HjupvCTQDNdHmluU-d2xYxQwg2we_EgnaBkHdhmEzx8wKcYhyfIe90T92jH4gymUM1neatQw1yiS7D7MTn_CVH2zt730ed8h-kageYxsr1EmgHmtU-w2RmiLaIg9Fg99Dj_W9lqMvjtGFxwLGqN2DdfOfS79nV3bzbF4X6E",
    "alg": "RS256",
    "dq": "CT79iBacsmkeuIKDIl0du8jatDkIULCt4TPLqCHMC6xPIfwUJ7_NN17qru-XgKeyh0qSJq0d9iYJasFSICmIRFG62PvmbqK1stdlXaxtW2ZSpaCfHc4XCKj9NwgK03bGKZP314XWSHhoo_RvMJrEwVBEtQU_qIKtoil-4JGtfsU",
    "n": "r95K3WIN8-4dB-tEKHjyTIIZZUMbHz8ad5oBX2BGiGxfPGfHbz2RH4QLT9ffzL-tgEo8IKs0Myh0VTwauiwz0cdHuS2gUTasK9OsosX1h1scSu_eZ-g-__lXBogU-SvBXBAgjv8hdcZjqWYQwmhJp2Ilv0CuXKxQwZyjso775PDjWDCH5HkVcSxHyUvpThLfWfkfz5PNDZvRpuPltv55ILRaVZhwPb7VXLAm2ebfeYUdybUKpGnEogKQdaL7TdNvP-HRnUSXTiYeXWHzU04FaXJ7yLmtXOQ52FT9dwkwLrCDOmDSBGafZ9asUtgOKhKN6wQW5mndhMK_1zThfjZyxQ"
}
```
or
```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCv3krdYg3z7h0H
60QoePJMghllQxsfPxp3mgFfYEaIbF88Z8dvPZEfhAtP19/Mv62ASjwgqzQzKHRV
PBq6LDPRx0e5LaBRNqwr06yixfWHWxxK795n6D7/+VcGiBT5K8FcECCO/yF1xmOp
ZhDCaEmnYiW/QK5crFDBnKOyjvvk8ONYMIfkeRVxLEfJS+lOEt9Z+R/Pk80Nm9Gm
4+W2/nkgtFpVmHA9vtVcsCbZ5t95hR3JtQqkacSiApB1ovtN028/4dGdRJdOJh5d
YfNTTgVpcnvIua1c5DnYVP13CTAusIM6YNIEZp9n1qxS2A4qEo3rBBbmad2Ewr/X
NOF+NnLFAgMBAAECggEAR38UamnZiEhOLxD7FYUN5AKj9mHQneRWizblxfNq2T1N
fk4matfZrrlMq/nz9tYZ3+TOCu3u+7k/igM0Tml365mbU/HzkfCrD+ou7cGSrqNg
nipj/VQSgJfKRFKATEf4hMfdpKSd4rZzf8OJnq8s+kpRVC4kdHJtJjja59VvHEQR
IrN/dkycNHSBWu5UjZbXOO5X3mjwuIh9gpLGZ+nHTqgTpT324q5BLVsH8/ywRGif
Ij+HQL1O5bJO2Q2/18iL1TbnMSbDwrKdb1edb4bgDuWB4o0xSTXsherTgeXu76gN
9FY28tuAKSd34yqp7GZaYcjtkskbWPRtYhOID2cOgQKBgQDhWYQ7bO2Uge9qUwdf
v3utaERNsqAHptFt0Z69ilEtkfXruEocHm+y5GMgBcl26NDDxbeudqz1n78N2/VN
tHlCfPRSaGfFAAht0MNQT2vk/8sSGiWuNj0nPQ/5biN7L7twMBN4hNgdve3rsdwj
BVvFAXl+RF0kCF87Tb1GqQfc4QKBgQDHyeCxQysMZF5VWl4Z2VnMZNIXGs0/z0MX
hYRBnvMKlJ7f8am5Q9vOCyVhASJfpcljmyxq9q9U06aZAQC3TGwxzHFU49gJjLss
ETxwlCIVv9sx/YfX7NOU+f8oXgPXSHjlwteG77GHhznZGH1YMxhmYpYuQAlDov96
54ahmQgOZQKBgQCLgPoeO6m8JNAM10eaW5T53bFjFDCDbB78SCdoGQd2GYTPHzAp
xiHJ8h73RP3aMfiDKZQzWd5q1DDXKJLsPsxOf8JUfbO3vfR53yH6RqB5jGyvUSaA
ea1T7DZGaItoiD0WD30OP9b2Woy+O0YXHAsao3YN1859Lv2dXdvNsXhfoQKBgAk+
/YgWnLJpHriCgyJdHbvI2rQ5CFCwreEzy6ghzAusTyH8FCe/zTde6q7vl4CnsodK
kiatHfYmCWrBUiApiERRutj75m6itbLXZV2sbVtmUqWgnx3OFwio/TcICtN2ximT
99eF1kh4aKP0bzCaxMFQRLUFP6iCraIpfuCRrX7FAoGAFZGFuvW1W9VF31JyrMYJ
y/BH7vja3d9iZlhFzttNZ+wmiXG4irrI/fLJgmXK6dI3MfIhKPAYi9nnza2kcR1q
EV9QObA4NV86RWnc8sAHbDGooe9VK5eJ5jjD7Tq/ZZiLiHGOZit3HylNilOb0k3V
sgMcp0F3ZQaMbg35K9rSgZE=
-----END PRIVATE KEY-----
```

> Using a Python dictionary to hard-code the Okta domain and API token is encouraged for development; In production, you should use a more secure way of storing these values. This library supports a few different configuration sources, covered in the [configuration reference](#configuration-reference) section.

### Extending the Client

When creating a new client, we allow for you to pass custom instances of `okta.request_executor`, `okta.http_client` and `okta.cache.cache`.

```py
from okta.client import Client as OktaClient
# Assuming implementations are in project.custom
from project.custom.request_executor_impl import RequestExecImpl
from project.custom.http_client_impl import HTTPClientImpl
from project.custom.cache_impl import CacheImpl


config = {
    'orgUrl': 'https://{yourOktaDomain}',
    'token': 'YOUR_API_TOKEN',
    'requestExecutor': RequestExecImpl,
    'httpClient': HTTPClientImpl,
    'cacheManager': CacheImpl(), # pass instance of CacheImpl
    'cache': {'enabled': True}
}


async def main():
    client = OktaClient(config)
    user_info, resp, err = await client.get_user({YOUR_USER_ID})
    print(user_info)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Extending or Creating New Classes

Example: You can create a custom cache driver by implementing `okta.cache.cache`

```py
# Fully working example for Custom Cache class
from okta.cache.cache import Cache


class CacheImpl(Cache):
    def __init__(self):
        super().__init__()
        self.cache_dict = {}

    def add(self, key, value):
        self.cache_dict[key] = value

    def get(self, key):
        return self.cache_dict.get(key, None)

    def contains(self, key):
        return key in self.cache_dict

    def delete(self, key):
        if self.contains(key):
            del self.cache_dict[key]
```

A similar approach can be used to extend `okta.request_executor`:
```py
from okta.request_executor import RequestExecutor


class RequestExecImpl(RequestExecutor):
    def __init__(self, config, cache, http_client=None):
        super().__init__(config, cache, http_client)
        # custom code

    # Note, this method shoud be defined as async
    async def create_request(self, method: str, url: str, body: dict = None,
                             headers: dict = {}, oauth=False):
        """
        Creates request for request executor's HTTP client.

        Args:
            method (str): HTTP Method to be used
            url (str): URL to send request to
            body (dict, optional): Request body. Defaults to None.
            headers (dict, optional): Request headers. Defaults to {}.

        Returns:
            dict, Exception: Tuple of Dictionary repr of HTTP request and
            exception raised during execution
        """
        # custom code

    # Note, this method shoud be defined as async
    async def execute(self, request, response_type=None):
        """
        This function is the high level request execution method. Performs the
        API call and returns a formatted response object

        Args:
            request (dict): dictionary object containing request details

        Returns:
            (OktaAPIResponse, Exception): Response obj for the Okta API, Error
        """
        # custom code
```

and `okta.http_client`:
```py
from okta.http_client import HTTPClient


class HTTPClientImpl(HTTPClient):
    def __init__(self, http_config={}):
        super().__init__(http_config)
        # custom code

    # Note, this method shoud be defined as async
    async def send_request(self, request):
        """
        This method fires HTTP requests

        Arguments:
            request {dict} -- This dictionary contains all information needed
            for the request.
            - HTTP method (as str)
            - Headers (as dict)
            - Request body (as dict)

        Returns:
            Tuple(RequestInfo, ClientResponse, JSONBody, ErrorObject)
            -- A tuple containing the request and response of the HTTP call
        """
        # custom code
```

## Usage guide

These examples will help you understand how to use this library.

Once you initialize a `client`, you can call methods to make requests to the Okta API. The client uses **asynchronous** methods to operate. Most methods are grouped by the API endpoint they belong to. For example, methods that call the [Users API][users-api-docs] are organized under [the User resource client (okta.resource_clients.user_client.py)][users-client].

> Asynchronous I/O is fairly new to Python after making its debut in Python 3.5. It's powered by the `asyncio` library which provides avenues to produce concurrent code. This allows developers to define `async` functions and `await` asynchronous calls within them. For more information, you can check out the [Python docs][python-docs].

Calls using `await` must be made in an `async def` function. That function must be called by `asyncio` (see example below).

```python
from okta.client import Client as OktaClient
import asyncio

async def main():
    client = OktaClient()
    users, resp, err = await client.list_users()
    print(len(users))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Authenticate a User

This library should only be used with the Okta management API. To call the [Authentication API][authn-api], you should construct your own HTTP requests.

> Assume the client is instantiated before each example below.
>
> ```py
> from okta.client import Client as OktaClient
> import okta.models as models
> client = OktaClient({'orgUrl': 'https://test.okta.com', 'token': 'YOUR_API_TOKEN'})
> ```

### Get and set custom attributes

Custom attributes must first be defined in the Okta profile editor. Then, you can work with custom attributes on a user:
> Feature is fully supported with SDK version >= 1.2.0

```py
""" Setting attributes """
# Creating an instance through a Python Dictionary
from okta.models import UserProfile

user_profile = UserProfile({
  'firstName': 'John',
  'lastName': 'Foe',
  'email': 'John.Foe@okta.com',
  'login': 'John.Foe@okta.com',
  'customAttr': 'custom value'
})

print(user_profile.custom_attr)

# Creating an empty object and using variables
user_profile = models.UserProfile()
user_profile.first_name = 'John'
user_profile.last_name = 'Doe'
user_profile.email = 'John.Doe@okta.com'
user_profile.login = 'John.Doe@okta.com'
user_profile.custom_attr = 'custom value'
```

Full example:

```py
from okta.client import Client as OktaClient
import asyncio

async def main():
    client = OktaClient()

    # create user with custom attribute
    body = {
      "profile": {
        "firstName": "John",
        "lastName": "Smith",
        "email": "jsmith@matrix.com",
        "login": "jsmith@matrix.com",
        "customAttr": "custom value"
      },
      "credentials": {
        "password" : { "value": "Knock*knock*neo*111" }
      }
    }
    result = await client.create_user(body)

    # create user without custom attribute
    body = {
      "profile": {
        "firstName": "Neo",
        "lastName": "Anderson",
        "email": "nanderson@matrix.com",
        "login": "nanderson@matrix.com"
      },
      "credentials": {
        "password" : { "value": "Knock*knock*neo*111" }
      }
    }
    result = await client.create_user(body)

    users, resp, err = await client.list_users()
    for user in users:
        print(user.profile.first_name, user.profile.last_name)
        try:
            print(user.profile.custom_attr)
        except:
            print('User has no customAttr')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
Output should look like the following (removed pre-existing users from output):
```sh
John Smith
custom value
Neo Anderson
User has no customAttr
```

### Get and set custom headers

> Feature appears in v1.3.0

It is possible to set custom headers, which will be sent with each request:

```py
import asyncio

from okta.client import Client as OktaClient

async def main():
    client = OktaClient()

    # set custom headers
    client.set_custom_headers({'Custom-Header': 'custom value'})

    # perform different requests with custom headers
    users, resp, err = await client.list_users()
    for user in users:
        print(user.profile.first_name, user.profile.last_name)

    # clear all custom headers
    client.clear_custom_headers()

    # output should be: {}
    print(client.get_custom_headers())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Note, that custom headers will be overwritten with default headers with the same name.
This doesn't allow breaking the client. Get default headers:

```py
client.get_default_headers()
```

### Get a User

```py
user, resp, err = await client.get_user(user.id)
# OR using their login
user, resp, err = await client.get_user(user.profile.login)
```

### List all Users

```py
users, resp, err = await client.list_users()
```

### Filter or search for Users

```py
# Query parameters are optional on methods that can use them!
# Check the method definition for details on which query parameters are accepted.
query_parameters = {'filter': 'status eq "ACTIVE"'}
users, resp, err = await client.list_users(query_parameters)
```

### Create a User

```py
# Create Password
password = models.PasswordCredential({
    'value': 'Password123'
})

# Create User Credentials
user_creds = models.UserCredentials({
    'password': password
})

# Create User Profile and CreateUser Request
user_profile = models.UserProfile()
user_profile.first_name = 'John'
user_profile.last_name = 'Doe'
user_profile.email = 'John.Doe'
user_profile.login = 'John.Doe'

create_user_req = models.CreateUserRequest({
    'credentials': user_creds,
    'profile': user_profile
})

# Create User
user, resp, err = await client.create_user(create_user_req)
```

### Update a User

```py
# Assume user object saved to variable `user`
# Craft new profile and get user object
new_profile = user.profile
new_profile.nick_name = 'Oktanaut'
updated_user_obj = models.User({'profile': new_profile})

# Update User with new details
updated_user, _, err = await client.update_user(user.id, updated_user_obj)
```

### Remove a User

You must first deactivate the user, and then you can delete the user.

```py
# Assuming user starts off with a status of 'ACTIVE'

# Deactivate
resp, err = await client.deactivate_or_delete_user(user.id)
# Then delete
resp, err = await client.deactivate_or_delete_user(user.id)
```

### List a User's Groups

```py
users_groups, resp, err = await client.list_user_groups(user.id)
```

### Create a Group

```py
# Create Group Model
group_profile = models.GroupProfile({
    'name': 'Group-Test'
})
group_model = models.Group({
    'profile': group_profile
})

# Create Group
group, resp, err = await client.create_group(group_model)
```

### Add a User to a Group

```py
resp, err = await client.add_user_to_group(group.id, user.id)
```

### List a User's enrolled Factors

```py
supported_factors, resp, err = await client.list_supported_factors(user.id)
```

### Enroll a User in a new Factor

```py
# Create and enroll factor
sms_factor = models.SmsUserFactor({
    'profile': models.SmsUserFactorProfile({
        'phoneNumber': '+12345678901'
    })
})
enrolled_factor, _, err = await client.enroll_factor(created_user.id, sms_factor)
```

### Activate a Factor

```py
activate_factor_request = models.ActivateFactorRequest({
  'passCode': '123456'
})
activated_factor, resp, err = await client.activate_factor(user.id, factor.id, activate_factor_request)
```

### Verify a Factor

```py
verify_factor_request = models.ActivateFactorRequest({
  'passCode': '123456'
})
verified_factor, resp, err = await client.activate_factor(user.id, factor.id, verify_factor_request)
```

### List all Applications

```py
apps, resp, err = await client.list_applications()
```

### Get an Application

```py
app, resp, err = await client.get_application(app.id)
```

### Create a SWA Application

```py
# Create SWA Application model and SWA Application in Okta
swa_app_settings_app = models.SwaApplicationSettingsApplication({
    'buttonField': 'btn-login',
    'passwordField': 'txt-box-password',
    'usernameField': 'txt-box-username',
    'url': 'https://example.com/login.html',
    'loginUrlRegex': '^https://example.com/login.html$'
})

swa_app_settings = models.SwaApplicationSettings({
    'app': swa_app_settings_app
})

swa_app_model = models.SwaApplication({
    'label': 'SWA Test App',
    'settings': swa_app_settings,
})

app, resp, err = await client.create_application(swa_app_model)
```

### Call other API endpoints

Not every API endpoint is represented by a method in this library. You can call any Okta management API endpoint using this generic syntax:

```py
# Example that doesn't return Object
request, error = await client.get_request_executor().create_request(
  method='POST',
  url='/api/v1/users/USER_ID_HERE/lifecycle/activate',
  body={},
  headers={},
  oauth=False
)

response, error = await client.get_request_executor().execute(request, None)
response_body = response.get_body()

# Example that does return Object
request, error = await client.get_request_executor().create_request(
  method='GET',
  url='/api/v1/users/USER_ID_HERE',
  body={},
  headers={},
  oauth=False
)

response, error = await client.get_request_executor().execute(request, models.User)

response_body = client.form_response_body(response.get_body())
user = response.get_type()(response_body)
```

## Exceptions

Starting from v1.1.0 SDK introduces exceptions, which are disabled by default, thus feature is backward compatible.
To force client raise an exception instead of returning custom error, option 'raiseException' should be provided:

```py
import asyncio

from okta.client import Client as OktaClient
from okta.exceptions import OktaAPIException


async def main():
    config = {'orgUrl': 'https://{yourOktaDomain}',
              'token': 'bad_token',
              'raiseException': True}
    client = OktaClient(config)
    try:
        users, resp, err = await client.list_users()
        for user in users:
            print(user.profile.first_name, user.profile.last_name)
    except OktaAPIException as err:
        print(err)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
Result should look like:
```py
{'errorCode': 'E0000011', 'errorSummary': 'Invalid token provided', 'errorLink': 'E0000011', 'errorId': 'oaeqWcqizEUQ_-iHc2hCbH9LA', 'errorCauses': []}
```

List of available exceptions: OktaAPIException, HTTPException (to raise instead of returning errors OktaAPIError and HTTPError respectively).
It is possible to inherit and/or extend given exceptions:
```py
from okta.exceptions import HTTPException


class MyHTTPException(HTTPException):
    pass


raise MyHTTPException('My HTTP Exception')
```

## Pagination

If your request comes back with more than the default or set limit (`resp.has_next() == True`), you can request the next page.

Example of listing users 1 at a time:

```py
query_parameters = {'limit': '1'}
users, resp, err = await client.list_users(query_parameters)

# Check if there more pages follow
if resp.has_next():
  users, err = await resp.next()  # Returns list of 1 user after the last retrieved user

# Iterate through all of the rest of the pages
while resp.has_next():
  users, err = await resp.next()
  # Do stuff with users in users

print(resp.has_next()) # False
try:
  await resp.next()
except StopAsyncIteration:
  # Handle Exception raised
```

Here's a complete example:
```python
from okta.client import Client as OktaClient
import asyncio

async def main():
    client = OktaClient()
    users, resp, err = await client.list_users()
    while True:
        for user in users:
            print(user.profile.login) # Add more properties here.
        if resp.has_next():
            users, err = await resp.next()
        else:
            break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Logging

> Feature appears in version 1.5.0

SDK v1.5.0 introduces logging for debug purposes.
Logs are disabled by default, thus SDK behavior remains the same. Logging should be enabled explicitly via client configuration:

```py
from okta.client import Client as OktaClient


config = {"logging": {"enabled": True}}
client = OktaClient(config)
```

SDK utilizes standard python library `logging`. By default, log level INFO is set. You can set another log level via config:

```py
from okta.client import Client as OktaClient
import logging

config = {"logging": {"enabled": True, "logLevel": logging.DEBUG}}
client = OktaClient(config)
```

**NOTE**: DO NOT SET DEBUG LEVEL IN PRODUCTION!

Here's a complete example:
```python
from okta.client import Client as OktaClient
import asyncio
import logging

async def main():
    config = {"logging": {"enabled": True, "logLevel": logging.DEBUG}}
    client = OktaClient(config)
    users, resp, err = await client.list_users()
    assert users is not None

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

You should now see logs in your console. Actual API Tokens will be logged to the console, so use caution and never use `DEBUG` level logging in production.

What it being logged: requests, http errors, caching responses.


## Configuration reference

This library looks for configuration in the following sources:

0. An `okta.yaml` file in a `.okta` folder in the current user's home directory (`~/.okta/okta.yaml` or `%userprofile%\.okta\okta.yaml`). See a sample [YAML Configuration](#yaml-configuration)
1. A `okta.yaml` file in the application or project's root directory. See a sample [YAML Configuration](#yaml-configuration)
2. [Environment variables](#environment-variables)
3. Configuration explicitly passed to the constructor (see the example in [Getting started](#getting-started))

> Only ONE source needs to be provided!

Higher numbers win. In other words, configuration passed via the constructor will OVERRIDE configuration found in environment variables, which will override configuration in the designated `okta.yaml` files.

### YAML configuration

When you use an API Token instead of OAuth 2.0 the full YAML configuration looks like:

```yaml
okta:
  client:
    connectionTimeout: 30 # seconds
    orgUrl: "https://{yourOktaDomain}"
    proxy:
      port: {proxy_port}
      host: {proxy_host}
      username: {proxy_username}
      password: {proxy_password}
    token: "YOUR_API_TOKEN"
    requestTimeout: 0 # seconds
    rateLimit:
      maxRetries: 4
```

When you use OAuth 2.0 the full YAML configuration looks like:

```yaml
okta:
  client:
    connectionTimeout: 30 # seconds
    orgUrl: "https://{yourOktaDomain}"
    proxy:
      port: {proxy_port}
      host: {proxy_host}
      username: {proxy_username}
      password: {proxy_password}
    authorizationMode: "PrivateKey"
    clientId: "YOUR_CLIENT_ID"
    scopes:
      - scope.1
      - scope.2
    privateKey: |
      -----BEGIN RSA PRIVATE KEY-----
      MIIEogIBAAKCAQEAl4F5CrP6Wu2kKwH1Z+CNBdo0iteHhVRIXeHdeoqIB1iXvuv4
      THQdM5PIlot6XmeV1KUKuzw2ewDeb5zcasA4QHPcSVh2+KzbttPQ+RUXCUAr5t+r
      0r6gBc5Dy1IPjCFsqsPJXFwqe3RzUb...
      -----END RSA PRIVATE KEY-----
    requestTimeout: 0 # seconds
    rateLimit:
      maxRetries: 4
```

> If a proxy is not going to be used for the SDK, you may omit the `okta.client.proxy` section from your `okta.yaml` file

### Environment variables

Each one of the configuration values above can be turned into an environment variable name with the `_` (underscore) character and UPPERCASE characters. The following are accepted:

- `OKTA_CLIENT_TOKEN`
- `OKTA_CLIENT_AUTHORIZATIONMODE`
- `OKTA_CLIENT_ORGURL`
- `OKTA_CLIENT_TOKEN`
- `OKTA_CLIENT_CLIENTID`
- `OKTA_CLIENT_SCOPES`
- `OKTA_CLIENT_PRIVATEKEY`
- `OKTA_CLIENT_USERAGENT`
- `OKTA_CLIENT_CONNECTIONTIMEOUT`
- `OKTA_CLIENT_REQUESTTIMEOUT`
- `OKTA_CLIENT_CACHE_ENABLED`
- `OKTA_CLIENT_CACHE_DEFAULTTTI`
- `OKTA_CLIENT_CACHE_DEFAULTTTL`
- `OKTA_CLIENT_PROXY_PORT`
- `OKTA_CLIENT_PROXY_HOST`
- `OKTA_CLIENT_PROXY_USERNAME`
- `OKTA_CLIENT_PROXY_PASSWORD`
- `OKTA_CLIENT_RATELIMIT_MAXRETRIES`
- `OKTA_TESTING_TESTINGDISABLEHTTPSCHECK`

## Rate Limiting

The Okta API will return 429 responses if too many requests are made within a given time. Please see [Rate Limiting at Okta][rate-limiting-okta] for a complete list of which endpoints are rate limited. When a 429 error is received, the X-Rate-Limit-Reset header will tell you the time at which you can retry. This section discusses the method for handling rate limiting with this SDK.

### Built-In Retry

This SDK uses the built-in retry strategy to automatically retry on 429 errors. You can use the default configuration options for the built-in retry strategy, or provide your desired values via the client configuration.

You can configure the following options when using the built-in retry strategy:

| Configuration Option        | Description                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| client.requestTimeout       | The waiting time in seconds for a request to be resolved by the client. Less than or equal to 0 means "no timeout". The default value is `0` (None). |
| client.rateLimit.maxRetries | The number of times to retry.                                                                                                                        |

Check out the [Configuration Reference section](#configuration-reference) for more details about how to set these values via configuration.

## Building the SDK

In most cases, you won't need to build the SDK from source. If you want to build it yourself, you'll need these prerequisites:

- Clone the repo
- Run `python setup.py build` from the root of the project (assuming Python is installed)
- Ensure tests run succesfully. Install `tox` if not installed already using: `pip install tox`. Run tests using `tox` in the root directory of the project.

## Contributing

We're happy to accept contributions and PRs! Please see the [Contribution Guide](CONTRIBUTING.md) to understand how to structure a contribution.

[devforum]: https://devforum.okta.com/
[github-issues]: https://github.com/okta/okta-sdk-python/issues
[github-releases]: https://github.com/okta/okta-sdk-python/releases
[okta developer forum]: https://devforum.okta.com/
[lang-landing-page]: https://developer.okta.com/code/python/
[users-client]: okta/resource_clients/user_client.py
[rate-limiting-okta]: https://developer.okta.com/docs/reference/rate-limits/
[users-api-docs]: https://developer.okta.com/docs/api/resources/users
[groups-api-docs]: https://developer.okta.com/docs/api/resources/groups
[apps-api-docs]: https://developer.okta.com/docs/api/resources/apps
[factors-api-docs]: https://developer.okta.com/docs/api/resources/factors
[okta-library-versioning]: https://developer.okta.com/code/library-versions/
[authn-api]: https://developer.okta.com/docs/api/resources/authn
[oauth-guides]: https://developer.okta.com/docs/guides/implement-oauth-for-okta/overview/
[dev-okta-signup]: https://developer.okta.com/signup
[api-token-docs]: https://developer.okta.com/docs/api/getting_started/getting_a_token
[python-docs]: https://docs.python.org/3/library/asyncio.html
