# okta.RoleApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /api/v1/iam/roles | Create a Role
[**create_role_permission**](RoleApi.md#create_role_permission) | **POST** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Create a Permission
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /api/v1/iam/roles/{roleIdOrLabel} | Delete a Role
[**delete_role_permission**](RoleApi.md#delete_role_permission) | **DELETE** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Delete a Permission
[**get_role**](RoleApi.md#get_role) | **GET** /api/v1/iam/roles/{roleIdOrLabel} | Retrieve a Role
[**get_role_permission**](RoleApi.md#get_role_permission) | **GET** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Retrieve a Permission
[**list_role_permissions**](RoleApi.md#list_role_permissions) | **GET** /api/v1/iam/roles/{roleIdOrLabel}/permissions | List all Permissions
[**list_roles**](RoleApi.md#list_roles) | **GET** /api/v1/iam/roles | List all Roles
[**replace_role**](RoleApi.md#replace_role) | **PUT** /api/v1/iam/roles/{roleIdOrLabel} | Replace a Role
[**replace_role_permission**](RoleApi.md#replace_role_permission) | **PUT** /api/v1/iam/roles/{roleIdOrLabel}/permissions/{permissionType} | Replace a Permission


# **create_role**
> IamRole create_role(instance)

Create a Role

Creates a new role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_iam_role_request import CreateIamRoleRequest
from okta.models.iam_role import IamRole
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
    api_instance = okta.RoleApi(api_client)
    instance = okta.CreateIamRoleRequest() # CreateIamRoleRequest | 

    try:
        # Create a Role
        api_response = api_instance.create_role(instance)
        print("The response of RoleApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**CreateIamRoleRequest**](CreateIamRoleRequest.md)|  | 

### Return type

[**IamRole**](IamRole.md)

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

# **create_role_permission**
> create_role_permission(role_id_or_label, permission_type, instance=instance)

Create a Permission

Creates a permission specified by `permissionType` to the role

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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An okta permission type
    instance = okta.CreateUpdateIamRolePermissionRequest() # CreateUpdateIamRolePermissionRequest |  (optional)

    try:
        # Create a Permission
        api_instance.create_role_permission(role_id_or_label, permission_type, instance=instance)
    except Exception as e:
        print("Exception when calling RoleApi->create_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An okta permission type | 
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

# **delete_role**
> delete_role(role_id_or_label)

Delete a Role

Deletes a role by `roleIdOrLabel`

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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role

    try:
        # Delete a Role
        api_instance.delete_role(role_id_or_label)
    except Exception as e:
        print("Exception when calling RoleApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_role_permission**
> delete_role_permission(role_id_or_label, permission_type)

Delete a Permission

Deletes a permission from a role by `permissionType`

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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An okta permission type

    try:
        # Delete a Permission
        api_instance.delete_role_permission(role_id_or_label, permission_type)
    except Exception as e:
        print("Exception when calling RoleApi->delete_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An okta permission type | 

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

# **get_role**
> IamRole get_role(role_id_or_label)

Retrieve a Role

Retrieves a role by `roleIdOrLabel`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.iam_role import IamRole
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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role

    try:
        # Retrieve a Role
        api_response = api_instance.get_role(role_id_or_label)
        print("The response of RoleApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 

### Return type

[**IamRole**](IamRole.md)

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

# **get_role_permission**
> Permission get_role_permission(role_id_or_label, permission_type)

Retrieve a Permission

Retrieves a permission by `permissionType`

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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An okta permission type

    try:
        # Retrieve a Permission
        api_response = api_instance.get_role_permission(role_id_or_label, permission_type)
        print("The response of RoleApi->get_role_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->get_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An okta permission type | 

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

List all Permissions

Lists all permissions of the role by `roleIdOrLabel`

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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role

    try:
        # List all Permissions
        api_response = api_instance.list_role_permissions(role_id_or_label)
        print("The response of RoleApi->list_role_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->list_role_permissions: %s\n" % e)
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

# **list_roles**
> IamRoles list_roles(after=after)

List all Roles

Lists all roles with pagination support

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.iam_roles import IamRoles
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
    api_instance = okta.RoleApi(api_client)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)

    try:
        # List all Roles
        api_response = api_instance.list_roles(after=after)
        print("The response of RoleApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 

### Return type

[**IamRoles**](IamRoles.md)

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

# **replace_role**
> IamRole replace_role(role_id_or_label, instance)

Replace a Role

Replaces a role by `roleIdOrLabel`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.iam_role import IamRole
from okta.models.update_iam_role_request import UpdateIamRoleRequest
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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    instance = okta.UpdateIamRoleRequest() # UpdateIamRoleRequest | 

    try:
        # Replace a Role
        api_response = api_instance.replace_role(role_id_or_label, instance)
        print("The response of RoleApi->replace_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->replace_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **instance** | [**UpdateIamRoleRequest**](UpdateIamRoleRequest.md)|  | 

### Return type

[**IamRole**](IamRole.md)

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

# **replace_role_permission**
> Permission replace_role_permission(role_id_or_label, permission_type, instance=instance)

Replace a Permission

Replaces a permission specified by `permissionType` in the role

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
    api_instance = okta.RoleApi(api_client)
    role_id_or_label = 'cr0Yq6IJxGIr0ouum0g3' # str | `id` or `label` of the role
    permission_type = 'okta.users.manage' # str | An okta permission type
    instance = okta.CreateUpdateIamRolePermissionRequest() # CreateUpdateIamRolePermissionRequest |  (optional)

    try:
        # Replace a Permission
        api_response = api_instance.replace_role_permission(role_id_or_label, permission_type, instance=instance)
        print("The response of RoleApi->replace_role_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleApi->replace_role_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id_or_label** | **str**| &#x60;id&#x60; or &#x60;label&#x60; of the role | 
 **permission_type** | **str**| An okta permission type | 
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

