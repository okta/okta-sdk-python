# okta.RoleECustomPermissionApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_permission**](RoleECustomPermissionApi.md#create_role_permission) | **POST** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Create a custom role permission
[**delete_role_permission**](RoleECustomPermissionApi.md#delete_role_permission) | **DELETE** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Delete a custom role permission
[**get_role_permission**](RoleECustomPermissionApi.md#get_role_permission) | **GET** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Retrieve a custom role permission
[**list_role_permissions**](RoleECustomPermissionApi.md#list_role_permissions) | **GET** /api/v1/iam/roles/{roleIdOrLabel}/permissions | List all custom role permissions
[**replace_role_permission**](RoleECustomPermissionApi.md#replace_role_permission) | **PUT** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Replace a custom role permission


# **create_role_permission**
> create_role_permission(role_id_or_label, permission_type, instance=instance)

Create a custom role permission

Creates a permission (specified by `permissionType`) for a custom role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_update_iam_role_permission_request import CreateUpdateIamRolePermissionRequest
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
    api_instance = okta.RoleECustomPermissionApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An Okta [permission](/openapi/okta-management/guides/permissions)
    instance = okta.CreateUpdateIamRolePermissionRequest() # CreateUpdateIamRolePermissionRequest |  (optional)

    try:
        # Create a custom role permission
        api_instance.create_role_permission(role_id_or_label, permission_type, instance=instance)
    except Exception as e:
        print("Exception when calling RoleECustomPermissionApi->create_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An Okta [permission](/openapi/okta-management/guides/permissions) | 
 **instance** | [**CreateUpdateIamRolePermissionRequest**](CreateUpdateIamRolePermissionRequest.md)|  | [optional] 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_permission**
> delete_role_permission(role_id_or_label, permission_type)

Delete a custom role permission

Deletes a permission (identified by `permissionType`) from a custom role

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
    api_instance = okta.RoleECustomPermissionApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An Okta [permission](/openapi/okta-management/guides/permissions)

    try:
        # Delete a custom role permission
        api_instance.delete_role_permission(role_id_or_label, permission_type)
    except Exception as e:
        print("Exception when calling RoleECustomPermissionApi->delete_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An Okta [permission](/openapi/okta-management/guides/permissions) | 

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

# **get_role_permission**
> Permission get_role_permission(role_id_or_label, permission_type)

Retrieve a custom role permission

Retrieves a permission (identified by `permissionType`) for a custom role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.permission import Permission
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
    api_instance = okta.RoleECustomPermissionApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An Okta [permission](/openapi/okta-management/guides/permissions)

    try:
        # Retrieve a custom role permission
        api_response = api_instance.get_role_permission(role_id_or_label, permission_type)
        print("The response of RoleECustomPermissionApi->get_role_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleECustomPermissionApi->get_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An Okta [permission](/openapi/okta-management/guides/permissions) | 

### Return type

[**Permission**](Permission.md)

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

# **list_role_permissions**
> Permissions list_role_permissions(role_id_or_label)

List all custom role permissions

Lists all permissions for a custom role by `roleIdOrLabel`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.permissions import Permissions
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
    api_instance = okta.RoleECustomPermissionApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role

    try:
        # List all custom role permissions
        api_response = api_instance.list_role_permissions(role_id_or_label)
        print("The response of RoleECustomPermissionApi->list_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleECustomPermissionApi->list_role_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 

### Return type

[**Permissions**](Permissions.md)

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

# **replace_role_permission**
> Permission replace_role_permission(role_id_or_label, permission_type, instance=instance)

Replace a custom role permission

Replaces a permission (specified by `permissionType`) for a custom role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_update_iam_role_permission_request import CreateUpdateIamRolePermissionRequest
from okta.models.permission import Permission
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
    api_instance = okta.RoleECustomPermissionApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An Okta [permission](/openapi/okta-management/guides/permissions)
    instance = okta.CreateUpdateIamRolePermissionRequest() # CreateUpdateIamRolePermissionRequest |  (optional)

    try:
        # Replace a custom role permission
        api_response = api_instance.replace_role_permission(role_id_or_label, permission_type, instance=instance)
        print("The response of RoleECustomPermissionApi->replace_role_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleECustomPermissionApi->replace_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An Okta [permission](/openapi/okta-management/guides/permissions) | 
 **instance** | [**CreateUpdateIamRolePermissionRequest**](CreateUpdateIamRolePermissionRequest.md)|  | [optional] 

### Return type

[**Permission**](Permission.md)

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

