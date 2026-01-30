# okta.IdentitySourceApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_source_session**](IdentitySourceApi.md#create_identity_source_session) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions | Create an identity source session
[**create_identity_source_user**](IdentitySourceApi.md#create_identity_source_user) | **POST** /api/v1/identity-sources/{identitySourceId}/users | Create an identity source user
[**delete_identity_source_session**](IdentitySourceApi.md#delete_identity_source_session) | **DELETE** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId} | Delete an identity source session
[**delete_identity_source_user**](IdentitySourceApi.md#delete_identity_source_user) | **DELETE** /api/v1/identity-sources/{identitySourceId}/users/{externalId} | Delete an identity source user
[**get_identity_source_session**](IdentitySourceApi.md#get_identity_source_session) | **GET** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId} | Retrieve an identity source session
[**get_identity_source_user**](IdentitySourceApi.md#get_identity_source_user) | **GET** /api/v1/identity-sources/{identitySourceId}/users/{externalId} | Retrieve an identity source user
[**list_identity_source_sessions**](IdentitySourceApi.md#list_identity_source_sessions) | **GET** /api/v1/identity-sources/{identitySourceId}/sessions | List all identity source sessions
[**replace_existing_identity_source_user**](IdentitySourceApi.md#replace_existing_identity_source_user) | **PUT** /api/v1/identity-sources/{identitySourceId}/users/{externalId} | Replace an existing identity source user
[**start_import_from_identity_source**](IdentitySourceApi.md#start_import_from_identity_source) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/start-import | Start the import from the identity source
[**update_identity_source_users**](IdentitySourceApi.md#update_identity_source_users) | **PATCH** /api/v1/identity-sources/{identitySourceId}/users/{externalId} | Update an identity source user
[**upload_identity_source_data_for_delete**](IdentitySourceApi.md#upload_identity_source_data_for_delete) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-delete | Upload the data to be deleted in Okta
[**upload_identity_source_data_for_upsert**](IdentitySourceApi.md#upload_identity_source_data_for_upsert) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-upsert | Upload the data to be upserted in Okta
[**upload_identity_source_group_memberships_for_delete**](IdentitySourceApi.md#upload_identity_source_group_memberships_for_delete) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-group-memberships-delete | Upload the group memberships to be deleted in Okta
[**upload_identity_source_group_memberships_for_upsert**](IdentitySourceApi.md#upload_identity_source_group_memberships_for_upsert) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-group-memberships-upsert | Upload the group memberships to be upserted in Okta
[**upload_identity_source_groups_data_for_delete**](IdentitySourceApi.md#upload_identity_source_groups_data_for_delete) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-groups-delete | Upload the group external IDs to be deleted in Okta
[**upload_identity_source_groups_for_upsert**](IdentitySourceApi.md#upload_identity_source_groups_for_upsert) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-groups-upsert | Upload the group profiles without memberships to be upserted in Okta


# **create_identity_source_session**
> IdentitySourceSession create_identity_source_session(identity_source_id)

Create an identity source session

Creates an identity source session for the given identity source instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_source_session import IdentitySourceSession
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created

    try:
        # Create an identity source session
        api_response = api_instance.create_identity_source_session(identity_source_id)
        print("The response of IdentitySourceApi->create_identity_source_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->create_identity_source_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 

### Return type

[**IdentitySourceSession**](IdentitySourceSession.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_identity_source_user**
> create_identity_source_user(identity_source_id, user_request_schema=user_request_schema)

Create an identity source user

Creates a user in an identity source for the given identity source instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_request_schema import UserRequestSchema
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    user_request_schema = okta.UserRequestSchema() # UserRequestSchema |  (optional)

    try:
        # Create an identity source user
        api_instance.create_identity_source_user(identity_source_id, user_request_schema=user_request_schema)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->create_identity_source_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **user_request_schema** | [**UserRequestSchema**](UserRequestSchema.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_source_session**
> delete_identity_source_session(identity_source_id, session_id)

Delete an identity source session

Deletes an identity source session for a given identity source ID and session Id

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session

    try:
        # Delete an identity source session
        api_instance.delete_identity_source_session(identity_source_id, session_id)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->delete_identity_source_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_source_user**
> delete_identity_source_user(identity_source_id, external_id)

Delete an identity source user

Deletes a user in an identity source for the given identity source instance and external ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    external_id = '00u7m9p9ZT8k2S2EX1f7' # str | The external ID of the user

    try:
        # Delete an identity source user
        api_instance.delete_identity_source_user(identity_source_id, external_id)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->delete_identity_source_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **external_id** | **str**| The external ID of the user | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_source_session**
> IdentitySourceSession get_identity_source_session(identity_source_id, session_id)

Retrieve an identity source session

Retrieves an identity source session for a given identity source ID and session ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_source_session import IdentitySourceSession
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session

    try:
        # Retrieve an identity source session
        api_response = api_instance.get_identity_source_session(identity_source_id, session_id)
        print("The response of IdentitySourceApi->get_identity_source_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->get_identity_source_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 

### Return type

[**IdentitySourceSession**](IdentitySourceSession.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_source_user**
> UserResponseSchema get_identity_source_user(identity_source_id, external_id)

Retrieve an identity source user

Retrieves a user by external ID in an identity source for the given identity source instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_response_schema import UserResponseSchema
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    external_id = '00u7m9p9ZT8k2S2EX1f7' # str | The external ID of the user

    try:
        # Retrieve an identity source user
        api_response = api_instance.get_identity_source_user(identity_source_id, external_id)
        print("The response of IdentitySourceApi->get_identity_source_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->get_identity_source_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **external_id** | **str**| The external ID of the user | 

### Return type

[**UserResponseSchema**](UserResponseSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_identity_source_sessions**
> List[IdentitySourceSession] list_identity_source_sessions(identity_source_id)

List all identity source sessions

Lists all identity source sessions for the given identity source instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_source_session import IdentitySourceSession
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created

    try:
        # List all identity source sessions
        api_response = api_instance.list_identity_source_sessions(identity_source_id)
        print("The response of IdentitySourceApi->list_identity_source_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->list_identity_source_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 

### Return type

[**List[IdentitySourceSession]**](IdentitySourceSession.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_existing_identity_source_user**
> UserResponseSchema replace_existing_identity_source_user(identity_source_id, external_id, user_request_schema=user_request_schema)

Replace an existing identity source user

Replaces an existing user for the given identity source instance and external ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_request_schema import UserRequestSchema
from okta.models.user_response_schema import UserResponseSchema
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    external_id = '00u7m9p9ZT8k2S2EX1f7' # str | The external ID of the user
    user_request_schema = okta.UserRequestSchema() # UserRequestSchema |  (optional)

    try:
        # Replace an existing identity source user
        api_response = api_instance.replace_existing_identity_source_user(identity_source_id, external_id, user_request_schema=user_request_schema)
        print("The response of IdentitySourceApi->replace_existing_identity_source_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->replace_existing_identity_source_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **external_id** | **str**| The external ID of the user | 
 **user_request_schema** | [**UserRequestSchema**](UserRequestSchema.md)|  | [optional] 

### Return type

[**UserResponseSchema**](UserResponseSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_import_from_identity_source**
> IdentitySourceSession start_import_from_identity_source(identity_source_id, session_id)

Start the import from the identity source

Starts the import from the identity source described by the uploaded bulk operations

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_source_session import IdentitySourceSession
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session

    try:
        # Start the import from the identity source
        api_response = api_instance.start_import_from_identity_source(identity_source_id, session_id)
        print("The response of IdentitySourceApi->start_import_from_identity_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->start_import_from_identity_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 

### Return type

[**IdentitySourceSession**](IdentitySourceSession.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity_source_users**
> UserResponseSchema update_identity_source_users(identity_source_id, external_id, users_update_request_schema=users_update_request_schema)

Update an identity source user

Updates a user to an identity source for the given identity source instance and external ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_response_schema import UserResponseSchema
from okta.models.users_update_request_schema import UsersUpdateRequestSchema
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    external_id = '00u7m9p9ZT8k2S2EX1f7' # str | The external ID of the user
    users_update_request_schema = okta.UsersUpdateRequestSchema() # UsersUpdateRequestSchema |  (optional)

    try:
        # Update an identity source user
        api_response = api_instance.update_identity_source_users(identity_source_id, external_id, users_update_request_schema=users_update_request_schema)
        print("The response of IdentitySourceApi->update_identity_source_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->update_identity_source_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **external_id** | **str**| The external ID of the user | 
 **users_update_request_schema** | [**UsersUpdateRequestSchema**](UsersUpdateRequestSchema.md)|  | [optional] 

### Return type

[**UserResponseSchema**](UserResponseSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_data_for_delete**
> upload_identity_source_data_for_delete(identity_source_id, session_id, bulk_delete_request_body=bulk_delete_request_body)

Upload the data to be deleted in Okta

Uploads external IDs of entities that need to be deleted in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bulk_delete_request_body import BulkDeleteRequestBody
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session
    bulk_delete_request_body = okta.BulkDeleteRequestBody() # BulkDeleteRequestBody |  (optional)

    try:
        # Upload the data to be deleted in Okta
        api_instance.upload_identity_source_data_for_delete(identity_source_id, session_id, bulk_delete_request_body=bulk_delete_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_data_for_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 
 **bulk_delete_request_body** | [**BulkDeleteRequestBody**](BulkDeleteRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_data_for_upsert**
> upload_identity_source_data_for_upsert(identity_source_id, session_id, bulk_upsert_request_body=bulk_upsert_request_body)

Upload the data to be upserted in Okta

Uploads entities that need to be inserted or updated in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bulk_upsert_request_body import BulkUpsertRequestBody
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session
    bulk_upsert_request_body = okta.BulkUpsertRequestBody() # BulkUpsertRequestBody |  (optional)

    try:
        # Upload the data to be upserted in Okta
        api_instance.upload_identity_source_data_for_upsert(identity_source_id, session_id, bulk_upsert_request_body=bulk_upsert_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_data_for_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 
 **bulk_upsert_request_body** | [**BulkUpsertRequestBody**](BulkUpsertRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_group_memberships_for_delete**
> upload_identity_source_group_memberships_for_delete(identity_source_id, session_id, bulk_group_memberships_delete_request_body=bulk_group_memberships_delete_request_body)

Upload the group memberships to be deleted in Okta

Uploads the group memberships that need to be deleted in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bulk_group_memberships_delete_request_body import BulkGroupMembershipsDeleteRequestBody
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session
    bulk_group_memberships_delete_request_body = okta.BulkGroupMembershipsDeleteRequestBody() # BulkGroupMembershipsDeleteRequestBody |  (optional)

    try:
        # Upload the group memberships to be deleted in Okta
        api_instance.upload_identity_source_group_memberships_for_delete(identity_source_id, session_id, bulk_group_memberships_delete_request_body=bulk_group_memberships_delete_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_group_memberships_for_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 
 **bulk_group_memberships_delete_request_body** | [**BulkGroupMembershipsDeleteRequestBody**](BulkGroupMembershipsDeleteRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_group_memberships_for_upsert**
> upload_identity_source_group_memberships_for_upsert(identity_source_id, session_id, bulk_group_memberships_upsert_request_body=bulk_group_memberships_upsert_request_body)

Upload the group memberships to be upserted in Okta

Uploads the group memberships that need to be inserted or updated in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bulk_group_memberships_upsert_request_body import BulkGroupMembershipsUpsertRequestBody
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session
    bulk_group_memberships_upsert_request_body = okta.BulkGroupMembershipsUpsertRequestBody() # BulkGroupMembershipsUpsertRequestBody |  (optional)

    try:
        # Upload the group memberships to be upserted in Okta
        api_instance.upload_identity_source_group_memberships_for_upsert(identity_source_id, session_id, bulk_group_memberships_upsert_request_body=bulk_group_memberships_upsert_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_group_memberships_for_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 
 **bulk_group_memberships_upsert_request_body** | [**BulkGroupMembershipsUpsertRequestBody**](BulkGroupMembershipsUpsertRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_groups_data_for_delete**
> upload_identity_source_groups_data_for_delete(identity_source_id, session_id, bulk_group_delete_request_body=bulk_group_delete_request_body)

Upload the group external IDs to be deleted in Okta

Uploads external IDs of groups that need to be deleted in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bulk_group_delete_request_body import BulkGroupDeleteRequestBody
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session
    bulk_group_delete_request_body = okta.BulkGroupDeleteRequestBody() # BulkGroupDeleteRequestBody |  (optional)

    try:
        # Upload the group external IDs to be deleted in Okta
        api_instance.upload_identity_source_groups_data_for_delete(identity_source_id, session_id, bulk_group_delete_request_body=bulk_group_delete_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_groups_data_for_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 
 **bulk_group_delete_request_body** | [**BulkGroupDeleteRequestBody**](BulkGroupDeleteRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_groups_for_upsert**
> upload_identity_source_groups_for_upsert(identity_source_id, session_id, bulk_group_upsert_request_body=bulk_group_upsert_request_body)

Upload the group profiles without memberships to be upserted in Okta

Uploads the group profiles without memberships that need to be inserted or updated in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.bulk_group_upsert_request_body import BulkGroupUpsertRequestBody
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.IdentitySourceApi(api_client)
    identity_source_id = '0oa3l6l6WK6h0R0QW0g4' # str | The ID of the identity source for which the session is created
    session_id = 'aps1qqonvr2SZv6o70h8' # str | The ID of the identity source session
    bulk_group_upsert_request_body = okta.BulkGroupUpsertRequestBody() # BulkGroupUpsertRequestBody |  (optional)

    try:
        # Upload the group profiles without memberships to be upserted in Okta
        api_instance.upload_identity_source_groups_for_upsert(identity_source_id, session_id, bulk_group_upsert_request_body=bulk_group_upsert_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_groups_for_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**| The ID of the identity source for which the session is created | 
 **session_id** | **str**| The ID of the identity source session | 
 **bulk_group_upsert_request_body** | [**BulkGroupUpsertRequestBody**](BulkGroupUpsertRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

