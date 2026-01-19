# okta.ApplicationCrossAppAccessConnectionsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cross_app_access_connection**](ApplicationCrossAppAccessConnectionsApi.md#create_cross_app_access_connection) | **POST** /api/v1/apps/{appId}/cwo/connections | Create a Cross App Access connection
[**delete_cross_app_access_connection**](ApplicationCrossAppAccessConnectionsApi.md#delete_cross_app_access_connection) | **DELETE** /api/v1/apps/{appId}/cwo/connections/{connectionId} | Delete a Cross App Access connection
[**get_all_cross_app_access_connections**](ApplicationCrossAppAccessConnectionsApi.md#get_all_cross_app_access_connections) | **GET** /api/v1/apps/{appId}/cwo/connections | Retrieve all Cross App Access connections
[**get_cross_app_access_connection**](ApplicationCrossAppAccessConnectionsApi.md#get_cross_app_access_connection) | **GET** /api/v1/apps/{appId}/cwo/connections/{connectionId} | Retrieve a Cross App Access connection
[**update_cross_app_access_connection**](ApplicationCrossAppAccessConnectionsApi.md#update_cross_app_access_connection) | **PATCH** /api/v1/apps/{appId}/cwo/connections/{connectionId} | Update a Cross App Access connection


# **create_cross_app_access_connection**
> OrgCrossAppAccessConnection create_cross_app_access_connection(app_id, org_cross_app_access_connection)

Create a Cross App Access connection

Creates a Cross App Access connection 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_cross_app_access_connection import OrgCrossAppAccessConnection
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
    api_instance = okta.ApplicationCrossAppAccessConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    org_cross_app_access_connection = okta.OrgCrossAppAccessConnection() # OrgCrossAppAccessConnection | 

    try:
        # Create a Cross App Access connection
        api_response = api_instance.create_cross_app_access_connection(app_id, org_cross_app_access_connection)
        print("The response of ApplicationCrossAppAccessConnectionsApi->create_cross_app_access_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCrossAppAccessConnectionsApi->create_cross_app_access_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **org_cross_app_access_connection** | [**OrgCrossAppAccessConnection**](OrgCrossAppAccessConnection.md)|  | 

### Return type

[**OrgCrossAppAccessConnection**](OrgCrossAppAccessConnection.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cross_app_access_connection**
> delete_cross_app_access_connection(app_id, connection_id)

Delete a Cross App Access connection

Deletes a Cross App Access connection with the specified ID 

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
    api_instance = okta.ApplicationCrossAppAccessConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    connection_id = '0oafxqCAJWWGELFTYASJ' # str | Connection ID

    try:
        # Delete a Cross App Access connection
        api_instance.delete_cross_app_access_connection(app_id, connection_id)
    except Exception as e:
        print("Exception when calling ApplicationCrossAppAccessConnectionsApi->delete_cross_app_access_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **connection_id** | **str**| Connection ID | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cross_app_access_connections**
> List[OrgCrossAppAccessConnection] get_all_cross_app_access_connections(app_id, after=after, limit=limit)

Retrieve all Cross App Access connections

Retrieves inbound and outbound Cross App Access connections associated with an app 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_cross_app_access_connection import OrgCrossAppAccessConnection
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
    api_instance = okta.ApplicationCrossAppAccessConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    after = 'after_example' # str | Specifies the pagination cursor for the next page of connection results (optional)
    limit = -1 # int | Specifies the number of results to return per page. The values:   * -1: Return all results (up to system maximum)   * 0: Return an empty result set   * Positive integer: Return up to that many results (capped at system maximum)  (optional) (default to -1)

    try:
        # Retrieve all Cross App Access connections
        api_response = api_instance.get_all_cross_app_access_connections(app_id, after=after, limit=limit)
        print("The response of ApplicationCrossAppAccessConnectionsApi->get_all_cross_app_access_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCrossAppAccessConnectionsApi->get_all_cross_app_access_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **after** | **str**| Specifies the pagination cursor for the next page of connection results | [optional] 
 **limit** | **int**| Specifies the number of results to return per page. The values:   * -1: Return all results (up to system maximum)   * 0: Return an empty result set   * Positive integer: Return up to that many results (capped at system maximum)  | [optional] [default to -1]

### Return type

[**List[OrgCrossAppAccessConnection]**](OrgCrossAppAccessConnection.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_app_access_connection**
> OrgCrossAppAccessConnection get_cross_app_access_connection(app_id, connection_id)

Retrieve a Cross App Access connection

Retrieves the Cross App Access connection with the specified ID 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_cross_app_access_connection import OrgCrossAppAccessConnection
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
    api_instance = okta.ApplicationCrossAppAccessConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    connection_id = '0oafxqCAJWWGELFTYASJ' # str | Connection ID

    try:
        # Retrieve a Cross App Access connection
        api_response = api_instance.get_cross_app_access_connection(app_id, connection_id)
        print("The response of ApplicationCrossAppAccessConnectionsApi->get_cross_app_access_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCrossAppAccessConnectionsApi->get_cross_app_access_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **connection_id** | **str**| Connection ID | 

### Return type

[**OrgCrossAppAccessConnection**](OrgCrossAppAccessConnection.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cross_app_access_connection**
> OrgCrossAppAccessConnection update_cross_app_access_connection(app_id, connection_id, org_cross_app_access_connection_patch_request)

Update a Cross App Access connection

Updates the Cross App Access connection with the specified ID 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_cross_app_access_connection import OrgCrossAppAccessConnection
from okta.models.org_cross_app_access_connection_patch_request import OrgCrossAppAccessConnectionPatchRequest
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
    api_instance = okta.ApplicationCrossAppAccessConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    connection_id = '0oafxqCAJWWGELFTYASJ' # str | Connection ID
    org_cross_app_access_connection_patch_request = okta.OrgCrossAppAccessConnectionPatchRequest() # OrgCrossAppAccessConnectionPatchRequest | 

    try:
        # Update a Cross App Access connection
        api_response = api_instance.update_cross_app_access_connection(app_id, connection_id, org_cross_app_access_connection_patch_request)
        print("The response of ApplicationCrossAppAccessConnectionsApi->update_cross_app_access_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCrossAppAccessConnectionsApi->update_cross_app_access_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **connection_id** | **str**| Connection ID | 
 **org_cross_app_access_connection_patch_request** | [**OrgCrossAppAccessConnectionPatchRequest**](OrgCrossAppAccessConnectionPatchRequest.md)|  | 

### Return type

[**OrgCrossAppAccessConnection**](OrgCrossAppAccessConnection.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

