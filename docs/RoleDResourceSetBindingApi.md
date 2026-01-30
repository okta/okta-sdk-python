# okta.RoleDResourceSetBindingApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_set_binding**](RoleDResourceSetBindingApi.md#create_resource_set_binding) | **POST** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings | Create a role resource set binding
[**delete_binding**](RoleDResourceSetBindingApi.md#delete_binding) | **DELETE** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings/{roleIdOrLabel} | Delete a role resource set binding
[**get_binding**](RoleDResourceSetBindingApi.md#get_binding) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings/{roleIdOrLabel} | Retrieve a role resource set binding
[**list_bindings**](RoleDResourceSetBindingApi.md#list_bindings) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings | List all role resource set bindings


# **create_resource_set_binding**
> ResourceSetBindingEditResponse create_resource_set_binding(resource_set_id_or_label, instance)

Create a role resource set binding

Creates a binding for the resource set, custom role, and members (users or groups)  > **Note:** If you use a custom role with permissions that don't apply to the resources in the resource set, it doesn't affect the admin role. For example,  the `okta.users.userprofile.manage` permission gives the admin no privileges if it's granted to a resource set that only includes `https://{yourOktaDomain}/api/v1/groups/{targetGroupId}`  resources. If you want the admin to be able to manage the users within the group, the resource set must include the corresponding `https://{yourOktaDomain}/api/v1/groups/{targetGroupId}/users` resource.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_binding_create_request import ResourceSetBindingCreateRequest
from okta.models.resource_set_binding_edit_response import ResourceSetBindingEditResponse
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
    api_instance = okta.RoleDResourceSetBindingApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    instance = okta.ResourceSetBindingCreateRequest() # ResourceSetBindingCreateRequest | 

    try:
        # Create a role resource set binding
        api_response = api_instance.create_resource_set_binding(resource_set_id_or_label, instance)
        print("The response of RoleDResourceSetBindingApi->create_resource_set_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingApi->create_resource_set_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **instance** | [**ResourceSetBindingCreateRequest**](ResourceSetBindingCreateRequest.md)|  | 

### Return type

[**ResourceSetBindingEditResponse**](ResourceSetBindingEditResponse.md)

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

# **delete_binding**
> delete_binding(resource_set_id_or_label, role_id_or_label)

Delete a role resource set binding

Deletes a binding of a role (identified by `roleIdOrLabel`) and a resource set (identified by `resourceSetIdOrLabel`)

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
    api_instance = okta.RoleDResourceSetBindingApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role

    try:
        # Delete a role resource set binding
        api_instance.delete_binding(resource_set_id_or_label, role_id_or_label)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingApi->delete_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 

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

# **get_binding**
> ResourceSetBindingResponse get_binding(resource_set_id_or_label, role_id_or_label)

Retrieve a role resource set binding

Retrieves the binding of a role (identified by `roleIdOrLabel`) for a resource set (identified by `resourceSetIdOrLabel`)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_binding_response import ResourceSetBindingResponse
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
    api_instance = okta.RoleDResourceSetBindingApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role

    try:
        # Retrieve a role resource set binding
        api_response = api_instance.get_binding(resource_set_id_or_label, role_id_or_label)
        print("The response of RoleDResourceSetBindingApi->get_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingApi->get_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 

### Return type

[**ResourceSetBindingResponse**](ResourceSetBindingResponse.md)

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

# **list_bindings**
> ResourceSetBindings list_bindings(resource_set_id_or_label, after=after)

List all role resource set bindings

Lists all bindings for a resource set with pagination support.  The returned `roles` array contains the roles for each binding associated with the specified resource set. If there are more than 100 bindings for the specified resource set, `links.next` provides the resource with pagination for the next list of bindings.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_bindings import ResourceSetBindings
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
    api_instance = okta.RoleDResourceSetBindingApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)

    try:
        # List all role resource set bindings
        api_response = api_instance.list_bindings(resource_set_id_or_label, after=after)
        print("The response of RoleDResourceSetBindingApi->list_bindings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingApi->list_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 

### Return type

[**ResourceSetBindings**](ResourceSetBindings.md)

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

