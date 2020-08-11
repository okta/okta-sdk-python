[<img src="https://aws1.discourse-cdn.com/standard14/uploads/oktadev/original/1X/0c6402653dfb70edc661d4976a43a46f33e5e919.png" align="right" width="256px"/>](https://devforum.okta.com/)
[![Build Status](https://img.shields.io/travis/okta/okta-sdk-python.svg?logo=travis)](https://travis-ci.org/okta/okta-sdk-python)
![Beta Release](https://img.shields.io/badge/Beta-Upcoming-inactive.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Support](https://img.shields.io/badge/support-Developer%20Forum-blue.svg)][devforum]

![PyPI](https://img.shields.io/pypi/v/okta)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/okta)
![Code Style](https://img.shields.io/badge/Code%20Style-flake8-informational.svg)


# Okta Python Management SDK
* [Release status](#release-status)
* [Need help?](#need-help)
* [Getting started](#getting-started)
* [Usage guide](#usage-guide)
* [Configuration reference](#configuration-reference)
* [Building the SDK](#building-the-sdk)
* [Contributing](#contributing)

This repository contains the Okta management SDK for Python. This SDK can be used in your server-side code to interact with the Okta management API and
* Create and update users with the [Users API](https://developer.okta.com/docs/api/resources/users)
* Add security factors to users with the [Factors API](https://developer.okta.com/docs/api/resources/factors)
* Manage groups with the [Groups API](https://developer.okta.com/docs/api/resources/groups)
* Manage applications with the [Apps API](https://developer.okta.com/docs/api/resources/apps)
* Much more!

> Requires Python version 3.6.0 or higher.

You can also learn more on the [Okta + Python][lang-landing-page] page in our documentation.

## Release status
This library uses semantic versioning and follows Okta's [library version policy](https://developer.okta.com/code/library-versions/).

| Version | Status                             |
| ------- | ---------------------------------- |
| 0.x     |  :warning: Beta Release (Retired)  |
| 1.x     |  :heavy_check_mark: Release        |
| 2.x     |  :construction: Pre-Release        |

The latest release can always be found on the [releases page][github-releases].

## Need help?

If you run into problems using the SDK, you can
* Ask questions on the [Okta Developer Forums][devforum]
* Post [issues][github-issues] here on GitHub (for code errors)

## Getting started
To install the Okta Python SDK in your project:

```sh
pip install okta
```

You'll also need

* An Okta account, called an _organization_ (sign up for a free [developer organization](https://developer.okta.com/signup) if you need one)
* An [API token](https://developer.okta.com/docs/api/getting_started/getting_a_token)

Construct a client instance by passing it your Okta domain name and API token:

```py
from okta.client import Client as OktaClient
config = {
    "orgUrl": "https://test.okta.com",
    "token": "YOUR_API_TOKEN"
}
my_okta_client = OktaClient(config)
```

Hard-coding the Okta domain and API token works for quick tests, but for real projects you should use a more secure way of storing these values (such as environment variables). This library supports a few different configuration sources, covered in the [configuration reference](#configuration-reference) section.

### OAuth 2.0
Okta allows you to interact with Okta APIs using scoped OAuth 2.0 access tokens. Each access token enables the bearer to perform specific actions on specific Okta endpoints, with that ability controlled by which scopes the access token contains.

This SDK supports this feature (OAuth 2.0) only for service-to-service applications. Check out [our guides](https://developer.okta.com/docs/guides/implement-oauth-for-okta/overview/) to learn more about how to register a new service application using a private and public key pair.

When using this approach you won't need an API Token because the SDK will request an access token for you. In order to use OAuth 2.0, construct a client instance by passing the following parameters:

```py
from okta.client import Client as OktaClient
config = {
    "orgUrl": "https://test.okta.com",
    "authorizationMode": "PrivateKey",
    "clientId": "clientID",
    "scopes": ["okta.users.manage"],
    "privateKey": {'JsonWebKey'}
}
client = OktaClient(config)
```

### Extending the Client
When creating a new client, we allow for you to pass custom instances of `okta.request_executor`, `okta.http_client` and `okta.cache.cache`.

```py
from okta.client import Client as OktaClient
# Assuming implementations are in project.custom
from project.custom.request_executor_impl import RequestExecImpl
from project.custom.http_client_impl import HTTPClientImpl
from project.custom.cache_impl import CacheImpl
config = {
    "orgUrl": "https://test.okta.com",
    "token": "YOUR_API_TOKEN",
    "requestExecutor": RequestExecImpl,
    "httpClient": HTTPClientImpl,
    "cacheManager": CacheImpl
}
Python Code Segment coming soon
  - Build client with HTTP client, Cache object and other parameters
```

### Extending or Creating New Cache Manager
You can create a custom cache driver by implementing `okta.cache.cache`

```py
from okta.cache.cache import Cache

class CustomCache(Cache):
  def __init__(self, params):
    super().__init__()
    # Constructor

  # Must implement all methods from the Cache class
  def get(self, key):
    # Implementation
  
  # Rest of methods
  ...
```

## Usage guide
These examples will help you understand how to use this library.

Once you initialize a `client`, you can call methods to make requests to the Okta API. Most methods are grouped by the API endpoint they belong to. For example, methods that call the [Users API](https://developer.okta.com/docs/api/resources/users) are organized under `Python segment coming`.

### Authenticate a User
This library should only be used with the Okta management API. To call the [Authentication API](https://developer.okta.com/docs/api/resources/authn), you should construct your own HTTP requests.

### Get a User
```
Python Code Segment coming soon
```

### List all Users
```
Python Code Segment coming soon
```

### Filter or search for Users
```
Python Code Segment coming soon
```

### Create a User
```
Python Code Segment coming soon
```

### Update a User
```
Python Code Segment coming soon
```

### Get and set custom attributes
Custom attributes must first be defined in the Okta profile editor. Then, you can work with custom attributes on a user:
```
Python Code Segment coming soon
```

### Remove a User
You must first deactivate the user, and then you can delete the user.
```
Python Code Segment coming soon
```

### List a User's Groups
```
Python Code Segment coming soon
```

### Create a Group
```
Python Code Segment coming soon
```

### Add a User to a Group
```
Python Code Segment coming soon
```

### List a User's enrolled Factors
```
Python Code Segment coming soon
```

### Enroll a User in a new Factor
```
Python Code Segment coming soon
```

### Activate a Factor
```
Python Code Segment coming soon
```

### Verify a Factor
```
Python Code Segment coming soon
```

### List all Applications
```
Python Code Segment coming soon
```

### Get an Application
```
Python Code Segment coming soon
```

### Create a SWA Application
```
Python Code Segment coming soon
```

### Call other API endpoints
Not every API endpoint is represented by a method in this library. You can call any Okta management API endpoint using this generic syntax:
```
Python Code Segment coming soon
```

## Configuration reference
This library looks for configuration in the following sources:

0. An `okta.yaml` file in a `.okta` folder in the current user's home directory (`~/.okta/okta.yaml` or `%userprofile\.okta\okta.yaml`)
0. A `.okta.yaml` file in the application or project's root directory
0. Environment variables
0. Configuration explicitly passed to the constructor (see the example in [Getting started](#getting-started))

Higher numbers win. In other words, configuration passed via the constructor will override configuration found in environment variables, which will override configuration in `okta.yaml` (if any), and so on.

### YAML configuration
When you use an API Token instead of OAuth 2.0 the full YAML configuration looks like:

```yaml
okta:
  client:
    connectionTimeout: 30 # seconds
    orgUrl: "https://{yourOktaDomain}"
    proxy:
      port: null
      host: null
      username: null
      password: null
    token: {apiToken}
```

When you use OAuth 2.0 the full YAML configuration looks like:

```yaml
okta:
  client:
    connectionTimeout: 30 # seconds
    orgUrl: "https://{yourOktaDomain}"
    proxy:
      port: null
      host: null
      username: null
      password: null
    authorizationMode: "PrivateKey"
    clientId: "{yourClientId}"
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

### Environment variables
Each one of the configuration values above can be turned into an environment variable name with the `_` (underscore) character and UPPERCASE characters:

* `OKTA_CLIENT_CONNECTIONTIMEOUT`
* `OKTA_CLIENT_TOKEN`
* and so on

## Building the SDK
In most cases, you won't need to build the SDK from source. If you want to build it yourself, you'll need these prerequisites:

- Clone the repo
- Run `python setup.py build` from the root of the project (assuming Python is installed)

## Contributing
We're happy to accept contributions and PRs! Please see the [Contribution Guide](CONTRIBUTING.md) to understand how to structure a contribution.

[devforum]: https://devforum.okta.com/
[github-issues]: https://github.com/okta/okta-sdk-python/issues
[github-releases]: https://github.com/okta/okta-sdk-python/releases
[Okta Developer Forum]: https://devforum.okta.com/
[lang-landing-page]: https://developer.okta.com/code/python/
[sdkapiref]: https://godoc.org/github.com/okta/okta-sdk-golang/okta
