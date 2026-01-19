# okta.AuthorizationServerAssocApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_associated_servers**](AuthorizationServerAssocApi.md#create_associated_servers) | **POST** /api/v1/authorizationServers/{authServerId}/associatedServers | Create an associated authorization server
[**delete_associated_server**](AuthorizationServerAssocApi.md#delete_associated_server) | **DELETE** /api/v1/authorizationServers/{authServerId}/associatedServers/{associatedServerId} | Delete an associated authorization server
[**list_associated_servers_by_trusted_type**](AuthorizationServerAssocApi.md#list_associated_servers_by_trusted_type) | **GET** /api/v1/authorizationServers/{authServerId}/associatedServers | List all associated authorization servers


# **create_associated_servers**
> List[AuthorizationServer] create_associated_servers(auth_server_id, associated_server_mediated)

Create an associated authorization server

Creates trusted relationships between the given authorization server and other authorization servers

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.associated_server_mediated import AssociatedServerMediated
from okta.models.authorization_server import AuthorizationServer
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
    api_instance = okta.AuthorizationServerAssocApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    associated_server_mediated = okta.AssociatedServerMediated() # AssociatedServerMediated | 

    try:
        # Create an associated authorization server
        api_response = api_instance.create_associated_servers(auth_server_id, associated_server_mediated)
        print("The response of AuthorizationServerAssocApi->create_associated_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerAssocApi->create_associated_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **associated_server_mediated** | [**AssociatedServerMediated**](AssociatedServerMediated.md)|  | 

### Return type

[**List[AuthorizationServer]**](AuthorizationServer.md)

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

# **delete_associated_server**
> delete_associated_server(auth_server_id, associated_server_id)

Delete an associated authorization server

Deletes an associated Authorization Server

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
    api_instance = okta.AuthorizationServerAssocApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    associated_server_id = 'aus6xt9jKPmCyn6kg0g4' # str | `id` of the associated Authorization Server

    try:
        # Delete an associated authorization server
        api_instance.delete_associated_server(auth_server_id, associated_server_id)
    except Exception as e:
        print("Exception when calling AuthorizationServerAssocApi->delete_associated_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **associated_server_id** | **str**| &#x60;id&#x60; of the associated Authorization Server | 

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

# **list_associated_servers_by_trusted_type**
> List[AuthorizationServer] list_associated_servers_by_trusted_type(auth_server_id, trusted=trusted, q=q, limit=limit, after=after)

List all associated authorization servers

Lists all associated Authorization Servers by trusted type for the given `authServerId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server import AuthorizationServer
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
    api_instance = okta.AuthorizationServerAssocApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    trusted = True # bool | Searches trusted authorization servers when `true` or searches untrusted authorization servers when `false` (optional)
    q = 'customasone' # str | Searches for the name or audience of the associated authorization servers (optional)
    limit = 200 # int | Specifies the number of results for a page (optional) (default to 200)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of the associated authorization servers (optional)

    try:
        # List all associated authorization servers
        api_response = api_instance.list_associated_servers_by_trusted_type(auth_server_id, trusted=trusted, q=q, limit=limit, after=after)
        print("The response of AuthorizationServerAssocApi->list_associated_servers_by_trusted_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerAssocApi->list_associated_servers_by_trusted_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **trusted** | **bool**| Searches trusted authorization servers when &#x60;true&#x60; or searches untrusted authorization servers when &#x60;false&#x60; | [optional] 
 **q** | **str**| Searches for the name or audience of the associated authorization servers | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to 200]
 **after** | **str**| Specifies the pagination cursor for the next page of the associated authorization servers | [optional] 

### Return type

[**List[AuthorizationServer]**](AuthorizationServer.md)

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

