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
- [Pagination](#pagination)
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
from okta.client import Client as OktaClient
# Instantiating with a Python dictionary in the constructor
config = {
    'orgUrl': 'https://test.okta.com',
    'token': 'YOUR_API_TOKEN'
}
okta_client = OktaClient(config)

# Instantiating without in-text credentials
okta_client = OktaClient()
```

> Using a Python dictionary to hard-code the Okta domain and API token is encouraged for development; In production, you should use a more secure way of storing these values. This library supports a few different configuration sources, covered in the [configuration reference](#configuration-reference) section.

### OAuth 2.0

Okta allows you to interact with Okta APIs using scoped OAuth 2.0 access tokens. Each access token enables the bearer to perform specific actions on specific Okta endpoints, with that ability controlled by which scopes the access token contains.

This SDK supports this feature (OAuth 2.0) only for service-to-service applications. Check out [our guides][oauth-guides] to learn more about how to register a new service application using a private and public key pair.

When using this approach you won't need an API Token because the SDK will request an access token for you. In order to use OAuth 2.0, construct a client instance by passing the following parameters:

```py
from okta.client import Client as OktaClient
config = {
    'orgUrl': 'https://test.okta.com',
    'authorizationMode': 'PrivateKey',
    'clientId': 'YOUR_CLIENT_ID',
    'scopes': ['okta.users.manage'],
    'privateKey': {'JsonWebKey'}
}
client = OktaClient(config)
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
    'orgUrl': 'https://test.okta.com',
    'token': 'YOUR_API_TOKEN',
    'requestExecutor': RequestExecImpl,
    'httpClient': HTTPClientImpl,
    'cacheManager': CacheImpl
}
```

### Extending or Creating New Classes

Example: You can create a custom cache driver by implementing `okta.cache.cache`

```py
from okta.cache.cache import Cache

class CustomCache(Cache):
  def __init__(self, params):
    super().__init__()
    # Constructor

  # Must implement all methods from the Cache class
  def get(self, key):
    # Implementation

  """Rest of methods"""
  ...
```

A similar approach can be used to extend `okta.request_executor` and `okta.http_client`.

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

```py
""" Setting attributes """
# Creating an instance through a Python Dictionary
user_profile = models.UserProfile({
  'firstName': 'John',
  'lastName': 'Foe',
  'email': 'John.Foe@okta.com',
  'login': 'John.Foe@okta.com'
})

# Creating an empty object and using variables
user_profile = models.UserProfile()
user_profile.first_name = 'John'
user_profile.last_name = 'Doe'
user_profile.email = 'John.Doe@okta.com'
user_profile.login = 'John.Doe@okta.com'

""" Getting attributes from instance """
user, resp, err = await client.get_user(user.id)
nick_name = user.profile.nick_name
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
- `OKTA_CLIENT_AUTHORIZATION_MODE`
- `OKTA_CLIENT_ORG_URL`
- `OKTA_CLIENT_TOKEN`
- `OKTA_CLIENT_CLIENT_ID`
- `OKTA_CLIENT_SCOPES`
- `OKTA_CLIENT_PRIVATE_KEY`
- `OKTA_CLIENT_USER_AGENT`
- `OKTA_CLIENT_CONNECTIONTIMEOUT`
- `OKTA_CLIENT_REQUESTTIMEOUT`
- `OKTA_CLIENT_CACHE_ENABLED`
- `OKTA_CLIENT_CACHE_DEFAULT_TTI`
- `OKTA_CLIENT_CACHE_DEFAULT_TTL`
- `OKTA_CLIENT_PROXY_PORT`
- `OKTA_CLIENT_PROXY_HOST`
- `OKTA_CLIENT_PROXY_USERNAME`
- `OKTA_CLIENT_PROXY_PASSWORD`
- `OKTA_CLIENT_RATE_LIMIT_MAX_RETRIES`
- `OKTA_TESTING_TESTING_DISABLE_HTTPS_CHECK`

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
