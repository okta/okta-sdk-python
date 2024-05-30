# openapi_client.SessionApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](SessionApi.md#create_session) | **POST** /api/v1/sessions | Create a Session with session token
[**get_session**](SessionApi.md#get_session) | **GET** /api/v1/sessions/{sessionId} | Retrieve a Session
[**refresh_session**](SessionApi.md#refresh_session) | **POST** /api/v1/sessions/{sessionId}/lifecycle/refresh | Refresh a Session
[**revoke_session**](SessionApi.md#revoke_session) | **DELETE** /api/v1/sessions/{sessionId} | Revoke a Session


# **create_session**
> Session create_session(create_session_request)

Create a Session with session token

Creates a new Session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID to delete a session through the API instead of visiting the logout URL.

### Example

* Api Key Authentication (apiToken):

```python
import openapi_client
from openapi_client.models.create_session_request import CreateSessionRequest
from openapi_client.models.session import Session
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SessionApi(api_client)
    create_session_request = openapi_client.CreateSessionRequest() # CreateSessionRequest | 

    try:
        # Create a Session with session token
        api_response = api_instance.create_session(create_session_request)
        print("The response of SessionApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_session_request** | [**CreateSessionRequest**](CreateSessionRequest.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> Session get_session(session_id)

Retrieve a Session

Retrieves information about the Session specified by the given session ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.session import Session
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SessionApi(api_client)
    session_id = 'l7FbDVqS8zHSy65uJD85' # str | `id` of the Session

    try:
        # Retrieve a Session
        api_response = api_instance.get_session(session_id)
        print("The response of SessionApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| &#x60;id&#x60; of the Session | 

### Return type

[**Session**](Session.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_session**
> Session refresh_session(session_id)

Refresh a Session

Refreshes an existing Session using the `id` for that Session. A successful response contains the refreshed Session with an updated `expiresAt` timestamp.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.session import Session
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SessionApi(api_client)
    session_id = 'l7FbDVqS8zHSy65uJD85' # str | `id` of the Session

    try:
        # Refresh a Session
        api_response = api_instance.refresh_session(session_id)
        print("The response of SessionApi->refresh_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->refresh_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| &#x60;id&#x60; of the Session | 

### Return type

[**Session**](Session.md)

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

# **revoke_session**
> revoke_session(session_id)

Revoke a Session

Revokes the specified Session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SessionApi(api_client)
    session_id = 'l7FbDVqS8zHSy65uJD85' # str | `id` of the Session

    try:
        # Revoke a Session
        api_instance.revoke_session(session_id)
    except Exception as e:
        print("Exception when calling SessionApi->revoke_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| &#x60;id&#x60; of the Session | 

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

