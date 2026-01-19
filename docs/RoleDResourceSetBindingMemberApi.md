# okta.RoleDResourceSetBindingMemberApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_to_binding**](RoleDResourceSetBindingMemberApi.md#add_members_to_binding) | **PATCH** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings/{roleIdOrLabel}/members | Add more role resource set binding members
[**get_member_of_binding**](RoleDResourceSetBindingMemberApi.md#get_member_of_binding) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings/{roleIdOrLabel}/members/{memberId} | Retrieve a role resource set binding member
[**list_members_of_binding**](RoleDResourceSetBindingMemberApi.md#list_members_of_binding) | **GET** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings/{roleIdOrLabel}/members | List all role resource set binding members
[**unassign_member_from_binding**](RoleDResourceSetBindingMemberApi.md#unassign_member_from_binding) | **DELETE** /api/v1/iam/resource-sets/{resourceSetIdOrLabel}/bindings/{roleIdOrLabel}/members/{memberId} | Unassign a role resource set binding member


# **add_members_to_binding**
> ResourceSetBindingEditResponse add_members_to_binding(resource_set_id_or_label, role_id_or_label, instance)

Add more role resource set binding members

Adds more members to a role resource set binding

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_binding_add_members_request import ResourceSetBindingAddMembersRequest
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
    api_instance = okta.RoleDResourceSetBindingMemberApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    instance = okta.ResourceSetBindingAddMembersRequest() # ResourceSetBindingAddMembersRequest | 

    try:
        # Add more role resource set binding members
        api_response = api_instance.add_members_to_binding(resource_set_id_or_label, role_id_or_label, instance)
        print("The response of RoleDResourceSetBindingMemberApi->add_members_to_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingMemberApi->add_members_to_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **instance** | [**ResourceSetBindingAddMembersRequest**](ResourceSetBindingAddMembersRequest.md)|  | 

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

# **get_member_of_binding**
> ResourceSetBindingMember get_member_of_binding(resource_set_id_or_label, role_id_or_label, member_id)

Retrieve a role resource set binding member

Retrieves a member (identified by `memberId`) that belongs to a role resource set binding

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_binding_member import ResourceSetBindingMember
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
    api_instance = okta.RoleDResourceSetBindingMemberApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    member_id = 'irb1qe6PGuMc7Oh8N0g4' # str | `id` of the member

    try:
        # Retrieve a role resource set binding member
        api_response = api_instance.get_member_of_binding(resource_set_id_or_label, role_id_or_label, member_id)
        print("The response of RoleDResourceSetBindingMemberApi->get_member_of_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingMemberApi->get_member_of_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **member_id** | **str**| &#x60;id&#x60; of the member | 

### Return type

[**ResourceSetBindingMember**](ResourceSetBindingMember.md)

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

# **list_members_of_binding**
> ResourceSetBindingMembers list_members_of_binding(resource_set_id_or_label, role_id_or_label, after=after)

List all role resource set binding members

Lists all members of a role resource set binding with pagination support

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resource_set_binding_members import ResourceSetBindingMembers
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
    api_instance = okta.RoleDResourceSetBindingMemberApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)

    try:
        # List all role resource set binding members
        api_response = api_instance.list_members_of_binding(resource_set_id_or_label, role_id_or_label, after=after)
        print("The response of RoleDResourceSetBindingMemberApi->list_members_of_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingMemberApi->list_members_of_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 

### Return type

[**ResourceSetBindingMembers**](ResourceSetBindingMembers.md)

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

# **unassign_member_from_binding**
> unassign_member_from_binding(resource_set_id_or_label, role_id_or_label, member_id)

Unassign a role resource set binding member

Unassigns a member (identified by `memberId`) from a role resource set binding

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
    api_instance = okta.RoleDResourceSetBindingMemberApi(api_client)
    resource_set_id_or_label = 'iamoJDFKaJxGIr0oamd9g' # str | `id` or `label` of the resource set
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    member_id = 'irb1qe6PGuMc7Oh8N0g4' # str | `id` of the member

    try:
        # Unassign a role resource set binding member
        api_instance.unassign_member_from_binding(resource_set_id_or_label, role_id_or_label, member_id)
    except Exception as e:
        print("Exception when calling RoleDResourceSetBindingMemberApi->unassign_member_from_binding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_set_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the resource set | 
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **member_id** | **str**| &#x60;id&#x60; of the member | 

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

