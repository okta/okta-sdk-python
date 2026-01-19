# okta.RoleCResourceSetResourceApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_set_resource**](RoleCResourceSetResourceApi.md#add_resource_set_resource) | **POST** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/resources | Add a resource set resource with conditions
[**add_resource_set_resources**](RoleCResourceSetResourceApi.md#add_resource_set_resources) | **PATCH** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/resources | Add more resources to a resource set
[**delete_resource_set_resource**](RoleCResourceSetResourceApi.md#delete_resource_set_resource) | **DELETE** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/resources/{resourceId} | Delete a resource set resource
[**get_resource_set_resource**](RoleCResourceSetResourceApi.md#get_resource_set_resource) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/resources/{resourceId} | Retrieve a resource set resource
[**list_resource_set_resources**](RoleCResourceSetResourceApi.md#list_resource_set_resources) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/resources | List all resource set resources
[**replace_resource_set_resource**](RoleCResourceSetResourceApi.md#replace_resource_set_resource) | **PUT** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/resources/{resourceId} | Replace the resource set resource conditions


# **add_resource_set_resource**
> ResourceSetResource add_resource_set_resource(resource_set_id_or_label, instance)

Add a resource set resource with conditions

Adds a resource with conditions for a resource set

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_resource import ResourceSetResource
from okta.models.resource_set_resource_post_request import ResourceSetResourcePostRequest
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
    api_instance = okta.RoleCResourceSetResourceApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    instance = okta.ResourceSetResourcePostRequest() # ResourceSetResourcePostRequest | 

    try:
        # Add a resource set resource with conditions
        api_response = api_instance.add_resource_set_resource(resource_set_id_or_label, instance)
        print("The response of RoleCResourceSetResourceApi->add_resource_set_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetResourceApi->add_resource_set_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **instance** | [**ResourceSetResourcePostRequest**](ResourceSetResourcePostRequest.md)|  | 

### Return type

[**ResourceSetResource**](ResourceSetResource.md)

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

# **add_resource_set_resources**
> ResourceSet add_resource_set_resources(resource_set_id_or_label, instance)

Add more resources to a resource set

Adds more resources to a resource set

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set import ResourceSet
from okta.models.resource_set_resource_patch_request import ResourceSetResourcePatchRequest
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
    api_instance = okta.RoleCResourceSetResourceApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    instance = okta.ResourceSetResourcePatchRequest() # ResourceSetResourcePatchRequest | 

    try:
        # Add more resources to a resource set
        api_response = api_instance.add_resource_set_resources(resource_set_id_or_label, instance)
        print("The response of RoleCResourceSetResourceApi->add_resource_set_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetResourceApi->add_resource_set_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **instance** | [**ResourceSetResourcePatchRequest**](ResourceSetResourcePatchRequest.md)|  | 

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_set_resource**
> delete_resource_set_resource(resource_set_id_or_label, resource_id)

Delete a resource set resource

Deletes a resource (identified by `resourceId`) from a resource set

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
    api_instance = okta.RoleCResourceSetResourceApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    resource_id = 'ire106sQKoHoXXsAe0g4' # str | `id` of the resource

    try:
        # Delete a resource set resource
        api_instance.delete_resource_set_resource(resource_set_id_or_label, resource_id)
    except Exception as e:
        print("Exception when calling RoleCResourceSetResourceApi->delete_resource_set_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **resource_id** | **str**| &#x60;id&#x60; of the resource | 

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

# **get_resource_set_resource**
> ResourceSetResource get_resource_set_resource(resource_set_id_or_label, resource_id)

Retrieve a resource set resource

Retrieves a resource identified by `resourceId` in a resource set

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_resource import ResourceSetResource
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
    api_instance = okta.RoleCResourceSetResourceApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    resource_id = 'ire106sQKoHoXXsAe0g4' # str | `id` of the resource

    try:
        # Retrieve a resource set resource
        api_response = api_instance.get_resource_set_resource(resource_set_id_or_label, resource_id)
        print("The response of RoleCResourceSetResourceApi->get_resource_set_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetResourceApi->get_resource_set_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **resource_id** | **str**| &#x60;id&#x60; of the resource | 

### Return type

[**ResourceSetResource**](ResourceSetResource.md)

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

# **list_resource_set_resources**
> ResourceSetResources list_resource_set_resources(resource_set_id_or_label, after=after, limit=limit)

List all resource set resources

Lists all resources for the resource set

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_resources import ResourceSetResources
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
    api_instance = okta.RoleCResourceSetResourceApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    after = 'after_example' # str | Specifies the pagination cursor for the next page of targets (optional)
    limit = 100 # int | Specifies the number of results returned. Defaults to `100`. (optional) (default to 100)

    try:
        # List all resource set resources
        api_response = api_instance.list_resource_set_resources(resource_set_id_or_label, after=after, limit=limit)
        print("The response of RoleCResourceSetResourceApi->list_resource_set_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetResourceApi->list_resource_set_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **after** | **str**| Specifies the pagination cursor for the next page of targets | [optional] 
 **limit** | **int**| Specifies the number of results returned. Defaults to &#x60;100&#x60;. | [optional] [default to 100]

### Return type

[**ResourceSetResources**](ResourceSetResources.md)

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

# **replace_resource_set_resource**
> ResourceSetResource replace_resource_set_resource(resource_set_id_or_label, resource_id, resource_set_resource_put_request)

Replace the resource set resource conditions

Replaces the conditions of a resource identified by `resourceId` in a resource set

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_resource import ResourceSetResource
from okta.models.resource_set_resource_put_request import ResourceSetResourcePutRequest
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
    api_instance = okta.RoleCResourceSetResourceApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    resource_id = 'ire106sQKoHoXXsAe0g4' # str | `id` of the resource
    resource_set_resource_put_request = okta.ResourceSetResourcePutRequest() # ResourceSetResourcePutRequest | 

    try:
        # Replace the resource set resource conditions
        api_response = api_instance.replace_resource_set_resource(resource_set_id_or_label, resource_id, resource_set_resource_put_request)
        print("The response of RoleCResourceSetResourceApi->replace_resource_set_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleCResourceSetResourceApi->replace_resource_set_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **resource_id** | **str**| &#x60;id&#x60; of the resource | 
 **resource_set_resource_put_request** | [**ResourceSetResourcePutRequest**](ResourceSetResourcePutRequest.md)|  | 

### Return type

[**ResourceSetResource**](ResourceSetResource.md)

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

