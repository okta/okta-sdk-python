# okta.RoleCResourceSetApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_set**](RoleCResourceSetApi.md#create_resource_set) | **POST** /api/v1/iam/resource-sets | Create a resource set
[**delete_resource_set**](RoleCResourceSetApi.md#delete_resource_set) | **DELETE** /api/v1/iam/resource-sets/{resourceSetIdOrLabel} | Delete a resource set
[**get_resource_set**](RoleCResourceSetApi.md#get_resource_set) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel} | Retrieve a resource set
[**list_resource_sets**](RoleCResourceSetApi.md#list_resource_sets) | **GET** /api/v1/iam/resource-sets | List all resource sets
[**replace_resource_set**](RoleCResourceSetApi.md#replace_resource_set) | **PUT** /api/v1/iam/resource-sets/{resourceSetIdOrLabel} | Replace a resource set


# **create_resource_set**
> ResourceSet create_resource_set(instance)

Create a resource set

Creates a new resource set. See [Supported resources](/openapi/okta-management/guides/roles/#supported-resources).  > **Note:** The maximum number of `resources` allowed in a resource set object is 1000. Resources are identified by either an Okta Resource Name (ORN) or by a REST URL format. See [Okta Resource Name](/openapi/okta-management/guides/roles/#okta-resource-name-orn).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_resource_set_request import CreateResourceSetRequest
from okta.models.resource_set import ResourceSet
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
    api_instance = okta.RoleCResourceSetApi(api_client)
    instance = okta.CreateResourceSetRequest() # CreateResourceSetRequest | 

    try:
        # Create a resource set
        api_response = api_instance.create_resource_set(instance)
        print("The response of RoleCResourceSetApi->create_resource_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetApi->create_resource_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**CreateResourceSetRequest**](CreateResourceSetRequest.md)|  | 

### Return type

[**ResourceSet**](ResourceSet.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_set**
> delete_resource_set(resource_set_id_or_label)

Delete a resource set

Deletes a resource set by `resourceSetIdOrLabel`

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
    api_instance = okta.RoleCResourceSetApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set

    try:
        # Delete a resource set
        api_instance.delete_resource_set(resource_set_id_or_label)
    except Exception as e:
        print("Exception when calling RoleCResourceSetApi->delete_resource_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 

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

# **get_resource_set**
> ResourceSet get_resource_set(resource_set_id_or_label)

Retrieve a resource set

Retrieves a resource set by `resourceSetIdOrLabel`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set import ResourceSet
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
    api_instance = okta.RoleCResourceSetApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set

    try:
        # Retrieve a resource set
        api_response = api_instance.get_resource_set(resource_set_id_or_label)
        print("The response of RoleCResourceSetApi->get_resource_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetApi->get_resource_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_sets**
> ResourceSets list_resource_sets(after=after)

List all resource sets

Lists all resource sets with pagination support

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_sets import ResourceSets
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
    api_instance = okta.RoleCResourceSetApi(api_client)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)

    try:
        # List all resource sets
        api_response = api_instance.list_resource_sets(after=after)
        print("The response of RoleCResourceSetApi->list_resource_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetApi->list_resource_sets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 

### Return type

[**ResourceSets**](ResourceSets.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_resource_set**
> ResourceSet replace_resource_set(resource_set_id_or_label, instance)

Replace a resource set

Replaces the label and description of a resource set. See [Supported resources](/openapi/okta-management/guides/roles/#supported-resources).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set import ResourceSet
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
    api_instance = okta.RoleCResourceSetApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    instance = okta.ResourceSet() # ResourceSet | 

    try:
        # Replace a resource set
        api_response = api_instance.replace_resource_set(resource_set_id_or_label, instance)
        print("The response of RoleCResourceSetApi->replace_resource_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetApi->replace_resource_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **instance** | [**ResourceSet**](ResourceSet.md)|  | 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

