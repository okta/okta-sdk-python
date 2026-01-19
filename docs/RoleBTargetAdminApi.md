# okta.RoleBTargetAdminApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_all_apps_as_target_to_role_for_user**](RoleBTargetAdminApi.md#assign_all_apps_as_target_to_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/catalog/apps | Assign all apps as target to admin role
[**assign_app_instance_target_to_app_admin_role_for_user**](RoleBTargetAdminApi.md#assign_app_instance_target_to_app_admin_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName}/{appId} | Assign an admin role app instance target
[**assign_app_target_to_admin_role_for_user**](RoleBTargetAdminApi.md#assign_app_target_to_admin_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName} | Assign an admin role app target
[**assign_group_target_to_user_role**](RoleBTargetAdminApi.md#assign_group_target_to_user_role) | **PUT** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/groups/{groupId} | Assign an admin role group target
[**get_role_targets_by_user_id_and_role_id**](RoleBTargetAdminApi.md#get_role_targets_by_user_id_and_role_id) | **GET** /api/v1/users/{userId}/roles/{roleIdOrEncodedRoleId}/targets | Retrieve a role target by assignment type
[**list_application_targets_for_application_administrator_role_for_user**](RoleBTargetAdminApi.md#list_application_targets_for_application_administrator_role_for_user) | **GET** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/catalog/apps | List all admin role app targets
[**list_group_targets_for_role**](RoleBTargetAdminApi.md#list_group_targets_for_role) | **GET** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/groups | List all admin role group targets
[**unassign_app_instance_target_from_admin_role_for_user**](RoleBTargetAdminApi.md#unassign_app_instance_target_from_admin_role_for_user) | **DELETE** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName}/{appId} | Unassign an admin role app instance target
[**unassign_app_target_from_app_admin_role_for_user**](RoleBTargetAdminApi.md#unassign_app_target_from_app_admin_role_for_user) | **DELETE** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/catalog/apps/{appName} | Unassign an admin role app target
[**unassign_group_target_from_user_admin_role**](RoleBTargetAdminApi.md#unassign_group_target_from_user_admin_role) | **DELETE** /api/v1/users/{userId}/roles/{roleAssignmentId}/targets/groups/{groupId} | Unassign an admin role group target


# **assign_all_apps_as_target_to_role_for_user**
> Success assign_all_apps_as_target_to_role_for_user(user_id, role_assignment_id)

Assign all apps as target to admin role

Assigns all apps as target to an `APP_ADMIN` role

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Assign all apps as target to admin role
        api_response = api_instance.assign_all_apps_as_target_to_role_for_user(user_id, role_assignment_id)
        print("The response of RoleBTargetAdminApi->assign_all_apps_as_target_to_role_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->assign_all_apps_as_target_to_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 

### Return type

[**Success**](Success.md)

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

# **assign_app_instance_target_to_app_admin_role_for_user**
> assign_app_instance_target_to_app_admin_role_for_user(user_id, role_assignment_id, app_name, app_id)

Assign an admin role app instance target

Assigns an app instance target to an `APP_ADMIN` role assignment to an admin user. When you assign the first OIN app or app instance target, you reduce the scope of the role assignment. The role no longer applies to all app targets, but applies only to the specified target.  > **Note:** You can target a mixture of both OIN app and app instance targets, but can't assign permissions to manage all instances of an OIN app and then assign a subset of permission to the same OIN app. > For example, you can't specify that an admin has access to manage all instances of the Salesforce app and then also manage specific configurations of the Salesforce app. 

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Assign an admin role app instance target
        api_instance.assign_app_instance_target_to_app_admin_role_for_user(user_id, role_assignment_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->assign_app_instance_target_to_app_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **assign_app_target_to_admin_role_for_user**
> Success assign_app_target_to_admin_role_for_user(user_id, role_assignment_id, app_name)

Assign an admin role app target

Assigns an OIN app target for an `APP_ADMIN` role assignment to an admin user. When you assign the first app target, you reduce the scope of the role assignment. The role no longer applies to all app targets, but applies only to the specified target.  Assigning an OIN app target overrides any existing app instance targets of the OIN app. For example, if a user was assigned to administer a specific Facebook instance, a successful request to add an OIN app target with `facebook` for `appName` makes that user the admin for all Facebook instances. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)

    try:
        # Assign an admin role app target
        api_response = api_instance.assign_app_target_to_admin_role_for_user(user_id, role_assignment_id, app_name)
        print("The response of RoleBTargetAdminApi->assign_app_target_to_admin_role_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->assign_app_target_to_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **app_name** | **str**| Name of the app definition (the OIN catalog app key name) | 

### Return type

[**Success**](Success.md)

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

# **assign_group_target_to_user_role**
> assign_group_target_to_user_role(user_id, role_assignment_id, group_id)

Assign an admin role group target

Assigns a group target for a `USER_ADMIN`, `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to an admin user. When you assign the first group target, you reduce the scope of the role assignment. The role no longer applies to all targets but applies only to the specified target. 

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Assign an admin role group target
        api_instance.assign_group_target_to_user_role(user_id, role_assignment_id, group_id)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->assign_group_target_to_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **get_role_targets_by_user_id_and_role_id**
> List[RoleTarget] get_role_targets_by_user_id_and_role_id(user_id, role_id_or_encoded_role_id, assignment_type=assignment_type, after=after, limit=limit)

Retrieve a role target by assignment type

Retrieves all role targets for an `APP_ADMIN`, `USER_ADMIN`, `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to an admin user by user or group assignment type. If the role isn't scoped to specific group targets or any app targets, an empty array `[]` is returned. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role_target import RoleTarget
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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_id_or_encoded_role_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role or Base32 encoded `id` of the role name
    assignment_type = 'GROUP' # str | Specifies the assignment type of the user (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # Retrieve a role target by assignment type
        api_response = api_instance.get_role_targets_by_user_id_and_role_id(user_id, role_id_or_encoded_role_id, assignment_type=assignment_type, after=after, limit=limit)
        print("The response of RoleBTargetAdminApi->get_role_targets_by_user_id_and_role_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->get_role_targets_by_user_id_and_role_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_id_or_encoded_role_id** | **str**| The &#x60;id&#x60; of the role or Base32 encoded &#x60;id&#x60; of the role name | 
 **assignment_type** | **str**| Specifies the assignment type of the user | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**List[RoleTarget]**](RoleTarget.md)

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

# **list_application_targets_for_application_administrator_role_for_user**
> List[CatalogApplication] list_application_targets_for_application_administrator_role_for_user(user_id, role_assignment_id, after=after, limit=limit)

List all admin role app targets

Lists all app targets for an `APP_ADMIN` role assigned to a user. The response is a list that includes OIN-cataloged apps or app instances. The response payload for an app instance contains the `id` property, but an OIN-cataloged app payload doesn't.

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all admin role app targets
        api_response = api_instance.list_application_targets_for_application_administrator_role_for_user(user_id, role_assignment_id, after=after, limit=limit)
        print("The response of RoleBTargetAdminApi->list_application_targets_for_application_administrator_role_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->list_application_targets_for_application_administrator_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **list_group_targets_for_role**
> List[Group] list_group_targets_for_role(user_id, role_assignment_id, after=after, limit=limit)

List all admin role group targets

Lists all group targets for a `USER_ADMIN`, `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to an admin user. If the role isn't scoped to specific group targets, an empty array `[]` is returned. 

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all admin role group targets
        api_response = api_instance.list_group_targets_for_role(user_id, role_assignment_id, after=after, limit=limit)
        print("The response of RoleBTargetAdminApi->list_group_targets_for_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->list_group_targets_for_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **unassign_app_instance_target_from_admin_role_for_user**
> unassign_app_instance_target_from_admin_role_for_user(user_id, role_assignment_id, app_name, app_id)

Unassign an admin role app instance target

Unassigns an app instance target from an `APP_ADMIN` role assignment to an admin user.  > **Note:** You can't remove the last app instance target from a role assignment since this causes an exception. > If you need a role assignment that applies to all apps, delete the `APP_ADMIN` role assignment and recreate a new one.

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Unassign an admin role app instance target
        api_instance.unassign_app_instance_target_from_admin_role_for_user(user_id, role_assignment_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->unassign_app_instance_target_from_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **unassign_app_target_from_app_admin_role_for_user**
> unassign_app_target_from_app_admin_role_for_user(user_id, role_assignment_id, app_name)

Unassign an admin role app target

Unassigns an OIN app target from an `APP_ADMIN` role assignment to an admin user.  > **Note:** You can't remove the last OIN app target from a role assignment since this causes an exception. > If you need a role assignment that applies to all apps, delete the `APP_ADMIN` role assignment to the user and recreate a new one. 

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    app_name = 'google' # str | Name of the app definition (the OIN catalog app key name)

    try:
        # Unassign an admin role app target
        api_instance.unassign_app_target_from_app_admin_role_for_user(user_id, role_assignment_id, app_name)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->unassign_app_target_from_app_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **unassign_group_target_from_user_admin_role**
> unassign_group_target_from_user_admin_role(user_id, role_assignment_id, group_id)

Unassign an admin role group target

Unassigns a group target from a `USER_ADMIN`, `HELP_DESK_ADMIN`, or `GROUP_MEMBERSHIP_ADMIN` role assignment to an admin user.  > **Note:** You can't remove the last group target from a role assignment since this causes an exception. > If you need a role assignment that applies to all groups, delete the role assignment to the user and recreate a new one. 

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
    api_instance = okta.RoleBTargetAdminApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Unassign an admin role group target
        api_instance.unassign_group_target_from_user_admin_role(user_id, role_assignment_id, group_id)
    except Exception as e:
        print("Exception when calling RoleBTargetAdminApi->unassign_group_target_from_user_admin_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

