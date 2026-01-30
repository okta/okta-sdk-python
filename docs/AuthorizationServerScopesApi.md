# okta.AuthorizationServerScopesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth2_scope**](AuthorizationServerScopesApi.md#create_o_auth2_scope) | **POST** /api/v1/authorizationServers/{authServerId}/scopes | Create a custom token scope
[**delete_o_auth2_scope**](AuthorizationServerScopesApi.md#delete_o_auth2_scope) | **DELETE** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | Delete a custom token scope
[**get_o_auth2_scope**](AuthorizationServerScopesApi.md#get_o_auth2_scope) | **GET** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | Retrieve a custom token scope
[**list_o_auth2_scopes**](AuthorizationServerScopesApi.md#list_o_auth2_scopes) | **GET** /api/v1/authorizationServers/{authServerId}/scopes | List all custom token scopes
[**replace_o_auth2_scope**](AuthorizationServerScopesApi.md#replace_o_auth2_scope) | **PUT** /api/v1/authorizationServers/{authServerId}/scopes/{scopeId} | Replace a custom token scope


# **create_o_auth2_scope**
> OAuth2Scope create_o_auth2_scope(auth_server_id, o_auth2_scope)

Create a custom token scope

Creates a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope import OAuth2Scope
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
    api_instance = okta.AuthorizationServerScopesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    o_auth2_scope = okta.OAuth2Scope() # OAuth2Scope | 

    try:
        # Create a custom token scope
        api_response = api_instance.create_o_auth2_scope(auth_server_id, o_auth2_scope)
        print("The response of AuthorizationServerScopesApi->create_o_auth2_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerScopesApi->create_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **o_auth2_scope** | [**OAuth2Scope**](OAuth2Scope.md)|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_scope**
> delete_o_auth2_scope(auth_server_id, scope_id)

Delete a custom token scope

Deletes a custom token scope

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
    api_instance = okta.AuthorizationServerScopesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    scope_id = '0TMRpCWXRKFjP7HiPFNM' # str | `id` of Scope

    try:
        # Delete a custom token scope
        api_instance.delete_o_auth2_scope(auth_server_id, scope_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerScopesApi->delete_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **scope_id** | **str**| &#x60;id&#x60; of Scope | 

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

# **get_o_auth2_scope**
> OAuth2Scope get_o_auth2_scope(auth_server_id, scope_id)

Retrieve a custom token scope

Retrieves a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope import OAuth2Scope
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
    api_instance = okta.AuthorizationServerScopesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    scope_id = '0TMRpCWXRKFjP7HiPFNM' # str | `id` of Scope

    try:
        # Retrieve a custom token scope
        api_response = api_instance.get_o_auth2_scope(auth_server_id, scope_id)
        print("The response of AuthorizationServerScopesApi->get_o_auth2_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerScopesApi->get_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **scope_id** | **str**| &#x60;id&#x60; of Scope | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

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

# **list_o_auth2_scopes**
> List[OAuth2Scope] list_o_auth2_scopes(auth_server_id, q=q, filter=filter, after=after, limit=limit)

List all custom token scopes

Lists all custom token scopes

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope import OAuth2Scope
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
    api_instance = okta.AuthorizationServerScopesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    q = 'q_example' # str | Searches the `name` of Custom Token Scopes for matching values (optional)
    filter = 'filter_example' # str | Filter expression for Custom Token Scopes (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of scopes. Treat the after cursor as an opaque value and obtain it through the next link relationship. See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)
    limit = 56 # int | Specifies the number of objects to return per page. If there are multiple pages of results, the Link header contains a `next` link that you need to use as an opaque value (follow it, don't parse it). See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)

    try:
        # List all custom token scopes
        api_response = api_instance.list_o_auth2_scopes(auth_server_id, q=q, filter=filter, after=after, limit=limit)
        print("The response of AuthorizationServerScopesApi->list_o_auth2_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerScopesApi->list_o_auth2_scopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **q** | **str**| Searches the &#x60;name&#x60; of Custom Token Scopes for matching values | [optional] 
 **filter** | **str**| Filter expression for Custom Token Scopes | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of scopes. Treat the after cursor as an opaque value and obtain it through the next link relationship. See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 
 **limit** | **int**| Specifies the number of objects to return per page. If there are multiple pages of results, the Link header contains a &#x60;next&#x60; link that you need to use as an opaque value (follow it, don&#39;t parse it). See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 

### Return type

[**List[OAuth2Scope]**](OAuth2Scope.md)

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

# **replace_o_auth2_scope**
> OAuth2Scope replace_o_auth2_scope(auth_server_id, scope_id, o_auth2_scope)

Replace a custom token scope

Replaces a custom token scope

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope import OAuth2Scope
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
    api_instance = okta.AuthorizationServerScopesApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    scope_id = '0TMRpCWXRKFjP7HiPFNM' # str | `id` of Scope
    o_auth2_scope = okta.OAuth2Scope() # OAuth2Scope | 

    try:
        # Replace a custom token scope
        api_response = api_instance.replace_o_auth2_scope(auth_server_id, scope_id, o_auth2_scope)
        print("The response of AuthorizationServerScopesApi->replace_o_auth2_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerScopesApi->replace_o_auth2_scope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **scope_id** | **str**| &#x60;id&#x60; of Scope | 
 **o_auth2_scope** | [**OAuth2Scope**](OAuth2Scope.md)|  | 

### Return type

[**OAuth2Scope**](OAuth2Scope.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
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

