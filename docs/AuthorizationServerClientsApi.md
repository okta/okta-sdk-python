# okta.AuthorizationServerClientsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_refresh_token_for_authorization_server_and_client**](AuthorizationServerClientsApi.md#get_refresh_token_for_authorization_server_and_client) | **GET** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId} | Retrieve a refresh token for a client
[**list_o_auth2_clients_for_authorization_server**](AuthorizationServerClientsApi.md#list_o_auth2_clients_for_authorization_server) | **GET** /api/v1/authorizationServers/{authServerId}/clients | List all client resources for an authorization server
[**list_refresh_tokens_for_authorization_server_and_client**](AuthorizationServerClientsApi.md#list_refresh_tokens_for_authorization_server_and_client) | **GET** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens | List all refresh tokens for a client
[**revoke_refresh_token_for_authorization_server_and_client**](AuthorizationServerClientsApi.md#revoke_refresh_token_for_authorization_server_and_client) | **DELETE** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId} | Revoke a refresh token for a client
[**revoke_refresh_tokens_for_authorization_server_and_client**](AuthorizationServerClientsApi.md#revoke_refresh_tokens_for_authorization_server_and_client) | **DELETE** /api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens | Revoke all refresh tokens for a client


# **get_refresh_token_for_authorization_server_and_client**
> OAuth2RefreshToken get_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id, expand=expand)

Retrieve a refresh token for a client

Retrieves a refresh token for a Client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken
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
    api_instance = okta.AuthorizationServerClientsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token
    expand = 'expand_example' # str | Valid value: `scope`. If specified, scope details are included in the `_embedded` attribute. (optional)

    try:
        # Retrieve a refresh token for a client
        api_response = api_instance.get_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id, expand=expand)
        print("The response of AuthorizationServerClientsApi->get_refresh_token_for_authorization_server_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClientsApi->get_refresh_token_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 
 **expand** | **str**| Valid value: &#x60;scope&#x60;. If specified, scope details are included in the &#x60;_embedded&#x60; attribute. | [optional] 

### Return type

[**OAuth2RefreshToken**](OAuth2RefreshToken.md)

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

# **list_o_auth2_clients_for_authorization_server**
> List[OAuth2Client] list_o_auth2_clients_for_authorization_server(auth_server_id)

List all client resources for an authorization server

Lists all client resources for which the specified authorization server has tokens.  > **Note:** To list a specific user's client resources for which they have tokens or grants, use the [List all clients endpoint in the User Resources API](/openapi/okta-management/management/tag/UserResources/#tag/UserResources/operation/listUserClients).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client import OAuth2Client
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
    api_instance = okta.AuthorizationServerClientsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all client resources for an authorization server
        api_response = api_instance.list_o_auth2_clients_for_authorization_server(auth_server_id)
        print("The response of AuthorizationServerClientsApi->list_o_auth2_clients_for_authorization_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClientsApi->list_o_auth2_clients_for_authorization_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[OAuth2Client]**](OAuth2Client.md)

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

# **list_refresh_tokens_for_authorization_server_and_client**
> List[OAuth2RefreshToken] list_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id, expand=expand, after=after, limit=limit)

List all refresh tokens for a client

Lists all refresh tokens issued by an authorization server for a specific Client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken
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
    api_instance = okta.AuthorizationServerClientsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    expand = 'expand_example' # str | Valid value: `scope`. If specified, scope details are included in the `_embedded` attribute. (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of tokens (optional)
    limit = -1 # int | The maximum number of tokens to return (maximum 200) (optional) (default to -1)

    try:
        # List all refresh tokens for a client
        api_response = api_instance.list_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id, expand=expand, after=after, limit=limit)
        print("The response of AuthorizationServerClientsApi->list_refresh_tokens_for_authorization_server_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerClientsApi->list_refresh_tokens_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **expand** | **str**| Valid value: &#x60;scope&#x60;. If specified, scope details are included in the &#x60;_embedded&#x60; attribute. | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of tokens | [optional] 
 **limit** | **int**| The maximum number of tokens to return (maximum 200) | [optional] [default to -1]

### Return type

[**List[OAuth2RefreshToken]**](OAuth2RefreshToken.md)

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

# **revoke_refresh_token_for_authorization_server_and_client**
> revoke_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id)

Revoke a refresh token for a client

Revokes a refresh token for a Client

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
    api_instance = okta.AuthorizationServerClientsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token

    try:
        # Revoke a refresh token for a client
        api_instance.revoke_refresh_token_for_authorization_server_and_client(auth_server_id, client_id, token_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerClientsApi->revoke_refresh_token_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 

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

# **revoke_refresh_tokens_for_authorization_server_and_client**
> revoke_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id)

Revoke all refresh tokens for a client

Revokes all refresh tokens for a Client

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
    api_instance = okta.AuthorizationServerClientsApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app

    try:
        # Revoke all refresh tokens for a client
        api_instance.revoke_refresh_tokens_for_authorization_server_and_client(auth_server_id, client_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerClientsApi->revoke_refresh_tokens_for_authorization_server_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 

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

