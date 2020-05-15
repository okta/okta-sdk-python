[<img src="https://aws1.discourse-cdn.com/standard14/uploads/oktadev/original/1X/0c6402653dfb70edc661d4976a43a46f33e5e919.png" align="right" width="256px"/>](https://devforum.okta.com/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Support](https://img.shields.io/badge/support-Developer%20Forum-blue.svg)][devforum]
# Okta Python Management SDK
Python API Client for the [Okta Platform API].

Requires Python version 3.7.0 or higher.

Need help? Contact [developers@okta.com](mailto:developers@okta.com) or use the [Okta Developer Forum].

## Installation

```sh
pip install okta
```

## PyDocs

You can view the entire PyDocs for this project here: 
```sh
Documentation coming soon
```

## Usage

All usage of this SDK begins with the creation of a client, the client handles the authentication and communication with the Okta API.  To create a client, you need to provide it with your Okta Domain and an API token.  To obtain those, see [Getting Started With the Okta APIs](https://developer.okta.com/code/rest/).

```
More coming soon
```
<!-- We also include an opt-in [default request executor](#default-request-executor) that you can configure, which will automatically handle rate limiting retries for you:

```python
Code segment coming soon
```

It is also possible to provide configuration through environment variables or YAML files.  Please see [Configuration](#configuration) for examples.

All interactions with the [Okta Platform API] is done through client methods.  Some examples are below, but for a full
 list of methods please refer to the JsDoc page for the [Client]. -->

<!-- ### OAuth 2.0 Authentication

Okta allows you to interact with Okta APIs using scoped OAuth 2.0 access tokens. Each access token enables the bearer to perform specific actions on specific Okta endpoints, with that ability controlled by which scopes the access token contains. 

This SDK supports this feature only for service-to-service applications. Please read [this guide](https://developer.okta.com/docs/guides/implement-oauth-for-okta/overview/) to learn more about how to register a new service application using a private and public key pair.

When using this approach you won't need an API Token because the SDK will request an access token for you. In order to use OAuth 2.0, construct a client instance by passing the following parameters:

```python
Code segment coming soon
```


The `privateKey` can be passed in the following ways:
- As a JSON encoded string of a JWK object
- A string in PEM format
- As a JSON object, in JWK format


## Table of Contents

* [Examples](#examples)
  * [Users](#users)
    * [Create a User](#create-a-user)
    * [Get a User](#get-a-user)
    * [Update a User](#update-a-user)
    * [Delete a User](#delete-a-user)
    * [List All Org Users](#list-all-org-users)
    * [Search for Users](#search-for-users)
  * [Groups](#groups)
    * [Create a Group](#create-a-group)
    * [Assign a User to a Group](#assign-a-user-to-a-group)
  * [Applications](#applications)
    * [Create an Application](#create-an-application)
    * [Assign a User to an Application](#assign-a-user-to-an-application)
    * [Assign a Group to an Application](#assign-a-group-to-an-application)
  * [System Log](#system-log)
    * [Get Logs](#get-logs)
  * [Call other API Endpoints](#call-other-api-endpoints)
* [Collection](#collection)
  * [each](#each)
  * [subscribe](#subscribeconfig)
* [Configuration](#configuration)
* [Caching](#caching)
* [Rate Limiting](#rate-limiting)
  * [Built-In Retry](#built-in-retry)
  * [Manual Retry](#manual-retry)
* [Request Executor](#request-executor)
  * [Default Request Executor](#default-request-executor)
  * [Base Request Executor](#base-request-executor) -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) if you would like to propose changes to this library.

[devforum]: https://devforum.okta.com/
[Sessions: Create Session with Session Token]: https://developer.okta.com/docs/api/resources/sessions.html#create-session-with-session-token
[Sessions: Session Properties]: https://developer.okta.com/docs/api/resources/sessions.html#session-properties
[Sessions: Session Operations]: https://developer.okta.com/docs/api/resources/sessions.html#session-operations
[Applications]: https://developer.okta.com/docs/api/resources/apps/
[Applications: Application User Profile]: https://developer.okta.com/docs/api/resources/apps/#application-user-profile-object
[Applications: Add Application]: https://developer.okta.com/docs/api/resources/apps/#add-application
[Applications: User Operations]:https://developer.okta.com/docs/api/resources/apps/#application-user-operations
[Basic Authentication Application]: https://developer.okta.com/docs/api/resources/apps/#add-basic-authentication-application
[Client]: https://developer.okta.com/okta-sdk-nodejs/jsdocs/Client.html
<!-- [DefaultRequestExecutor]: src/default-request-executor.js -->
[Groups: Add Group]: https://developer.okta.com/docs/api/resources/groups.html#add-group
<!-- [isomorphic-fetch]: https://github.com/matthew-andrews/isomorphic-fetch -->
[Okta Developer Forum]: https://devforum.okta.com/
[Okta Platform API]: https://developer.okta.com/docs/api/getting_started/api_test_client.html
[Pagination]: https://developer.okta.com/docs/api/getting_started/design_principles.html#pagination
[Rate Limiting at Okta]: https://developer.okta.com/docs/api/getting_started/rate-limits
<!-- [RequestExecutor]: src/request-executor.js -->
[System Log API]: https://developer.okta.com/docs/api/resources/system_log
[Users API Reference]: https://developer.okta.com/docs/api/resources/users.html
[Users: Create User]: https://developer.okta.com/docs/api/resources/users.html#create-user
[Users: Get User]: https://developer.okta.com/docs/api/resources/users.html#get-user
[Users: Lifecycle Operations]: https://developer.okta.com/docs/api/resources/users.html#lifecycle-operations
[Users: List Users]: https://developer.okta.com/docs/api/resources/users.html#list-users
[Users: Update User]: https://developer.okta.com/docs/api/resources/users.html#update-user