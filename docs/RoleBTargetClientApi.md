# okta.RoleBTargetClientApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_app_target_instance_role_for_client**](RoleBTargetClientApi.md#assign_app_target_instance_role_for_client) | **PUT** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName}/{appId} | Assign a client role app instance target
[**assign_app_target_role_to_client**](RoleBTargetClientApi.md#assign_app_target_role_to_client) | **PUT** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName} | Assign a client role app target
[**assign_group_target_role_for_client**](RoleBTargetClientApi.md#assign_group_target_role_for_client) | **PUT** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/groups/{groupId} | Assign a client role group target
[**list_app_target_role_to_client**](RoleBTargetClientApi.md#list_app_target_role_to_client) | **GET** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/catalog/apps | List all client role app targets
[**list_group_target_role_for_client**](RoleBTargetClientApi.md#list_group_target_role_for_client) | **GET** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/groups | List all client role group targets
[**remove_app_target_instance_role_for_client**](RoleBTargetClientApi.md#remove_app_target_instance_role_for_client) | **DELETE** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName}/{appId} | Unassign a client role app instance target
[**remove_app_target_role_from_client**](RoleBTargetClientApi.md#remove_app_target_role_from_client) | **DELETE** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName} | Unassign a client role app target
[**remove_group_target_role_from_client**](RoleBTargetClientApi.md#remove_group_target_role_from_client) | **DELETE** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId}/targets/groups/{groupId} | Unassign a client role group target


# **assign_app_target_instance_role_for_client**
> assign_app_target_instance_role_for_client(client_id, role_assignment_id, app_name, app_id)

Assign a client role app instance target

Assigns an app instance target to an `APP_ADMIN` role assignment to a client. When you assign the first OIN app or app instance target, you reduce the scope of the role assignment. The role no longer applies to all app targets, but applies only to the specified target.  > **Note:** You can target a mixture of both OIN app and app instance targets, but you can't assign permissions to manage all instances of an OIN app and then assign a subset of permissions to the same app. For example, you can't specify that an admin has access to manage all instances of the Salesforce app and then also manage only specific configurations of the Salesforce app.

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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Assign a client role app instance target
        api_instance.assign_app_target_instance_role_for_client(client_id, role_assignment_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->assign_app_target_instance_role_for_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **app_name** | **str**| Name of the app definition (the OIN catalog app key name) | 
 **app_id** | **str**| Application ID | 

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

# **assign_app_target_role_to_client**
> assign_app_target_role_to_client(client_id, role_assignment_id, app_name)

Assign a client role app target

Assigns an OIN app target for an `APP_ADMIN` role assignment to a client. When you assign an app target from the OIN catalog, you reduce the scope of the role assignment. The role assignment applies to only app instances that are included in the specified OIN app target.  An assigned OIN app target overrides any existing app instance targets. For example, if a user is assigned to administer a specific Facebook instance, a successful request to add an OIN app target with `facebook` for `appName` makes that user the administrator for all Facebook instances.

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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)

    try:
        # Assign a client role app target
        api_instance.assign_app_target_role_to_client(client_id, role_assignment_id, app_name)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->assign_app_target_role_to_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **app_name** | **str**| Name of the app definition (the OIN catalog app key name) | 

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

# **assign_group_target_role_for_client**
> assign_group_target_role_for_client(client_id, role_assignment_id, group_id)

Assign a client role group target

Assigns a group target to a [`USER_ADMIN`](/openapi/okta-management/guides/roles/#standard-roles), `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to a client app. When you assign the first group target, you reduce the scope of the role assignment. The role no longer applies to all targets, but applies only to the specified target.

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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Assign a client role group target
        api_instance.assign_group_target_role_for_client(client_id, role_assignment_id, group_id)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->assign_group_target_role_for_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 

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

# **list_app_target_role_to_client**
> List[CatalogApplication] list_app_target_role_to_client(client_id, role_assignment_id, after=after, limit=limit)

List all client role app targets

Lists all OIN app targets for an `APP_ADMIN` role that's assigned to a client (by `clientId`).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.catalog_application import CatalogApplication
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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all client role app targets
        api_response = api_instance.list_app_target_role_to_client(client_id, role_assignment_id, after=after, limit=limit)
        print("The response of RoleBTargetClientApi->list_app_target_role_to_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->list_app_target_role_to_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**List[CatalogApplication]**](CatalogApplication.md)

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

# **list_group_target_role_for_client**
> List[Group] list_group_target_role_for_client(client_id, role_assignment_id, after=after, limit=limit)

List all client role group targets

Lists all group targets for a [`USER_ADMIN`](/openapi/okta-management/guides/roles/#standard-roles), `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to a client. If the role isn't scoped to specific group targets, Okta returns an empty array `[]`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group import Group
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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all client role group targets
        api_response = api_instance.list_group_target_role_for_client(client_id, role_assignment_id, after=after, limit=limit)
        print("The response of RoleBTargetClientApi->list_group_target_role_for_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->list_group_target_role_for_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**List[Group]**](Group.md)

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

# **remove_app_target_instance_role_for_client**
> remove_app_target_instance_role_for_client(client_id, role_assignment_id, app_name, app_id)

Unassign a client role app instance target

Unassigns an app instance target from a role assignment to a client app  > **Note:** You can't remove the last app instance target from a role assignment. > If you need a role assignment that applies to all the apps, delete the role assignment with the instance target and create another one.  See [Unassign a client role](/openapi/okta-management/management/tag/RoleAssignmentClient/#tag/RoleAssignmentClient/operation/deleteRoleFromClient).

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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Unassign a client role app instance target
        api_instance.remove_app_target_instance_role_for_client(client_id, role_assignment_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->remove_app_target_instance_role_for_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **app_name** | **str**| Name of the app definition (the OIN catalog app key name) | 
 **app_id** | **str**| Application ID | 

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

# **remove_app_target_role_from_client**
> remove_app_target_role_from_client(client_id, role_assignment_id, app_name)

Unassign a client role app target

Unassigns an OIN app target for a role assignment to a client app  > **Note:** You can't remove the last OIN app target from a role assignment. > If you need a role assignment that applies to all apps, delete the role assignment with the target and create another one. See [Unassign a client role](/openapi/okta-management/management/tag/RoleAssignmentClient/#tag/RoleAssignmentClient/operation/deleteRoleFromClient).

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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)

    try:
        # Unassign a client role app target
        api_instance.remove_app_target_role_from_client(client_id, role_assignment_id, app_name)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->remove_app_target_role_from_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **app_name** | **str**| Name of the app definition (the OIN catalog app key name) | 

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

# **remove_group_target_role_from_client**
> remove_group_target_role_from_client(client_id, role_assignment_id, group_id)

Unassign a client role group target

Unassigns a Group target from a `USER_ADMIN`, `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to a client app.  > **Note:** You can't remove the last group target from a role assignment. If you need a role assignment that applies to all groups, delete the role assignment with the target and create another one. See [Unassign a client role](/openapi/okta-management/management/tag/RoleAssignmentClient/#tag/RoleAssignmentClient/operation/deleteRoleFromClient).

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
    api_instance = okta.RoleBTargetClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Unassign a client role group target
        api_instance.remove_group_target_role_from_client(client_id, role_assignment_id, group_id)
    except Exception as e:
        print("Exception when calling RoleBTargetClientApi->remove_group_target_role_from_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 

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

