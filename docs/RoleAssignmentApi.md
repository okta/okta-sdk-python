# okta.RoleAssignmentApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_group**](RoleAssignmentApi.md#assign_role_to_group) | **POST** /api/v1/groups/{groupId}/roles | Assign a Role to a Group
[**assign_role_to_user**](RoleAssignmentApi.md#assign_role_to_user) | **POST** /api/v1/users/{userId}/roles | Assign a Role to a User
[**get_group_assigned_role**](RoleAssignmentApi.md#get_group_assigned_role) | **GET** /api/v1/groups/{groupId}/roles/{roleId} | Retrieve a Role assigned to Group
[**get_user_assigned_role**](RoleAssignmentApi.md#get_user_assigned_role) | **GET** /api/v1/users/{userId}/roles/{roleId} | Retrieve a Role assigned to a User
[**list_assigned_roles_for_user**](RoleAssignmentApi.md#list_assigned_roles_for_user) | **GET** /api/v1/users/{userId}/roles | List all Roles assigned to a User
[**list_group_assigned_roles**](RoleAssignmentApi.md#list_group_assigned_roles) | **GET** /api/v1/groups/{groupId}/roles | List all Assigned Roles of Group
[**list_users_with_role_assignments**](RoleAssignmentApi.md#list_users_with_role_assignments) | **GET** /api/v1/iam/assignees/users | List all Users with Role Assignments
[**unassign_role_from_group**](RoleAssignmentApi.md#unassign_role_from_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId} | Unassign a Role from a Group
[**unassign_role_from_user**](RoleAssignmentApi.md#unassign_role_from_user) | **DELETE** /api/v1/users/{userId}/roles/{roleId} | Unassign a Role from a User


# **assign_role_to_group**
> Role assign_role_to_group(group_id, assign_role_request, disable_notifications=disable_notifications)

Assign a Role to a Group

Assigns a role to a group

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_request import AssignRoleRequest
from okta.models.role import Role
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
    api_instance = okta.RoleAssignmentApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    assign_role_request = okta.AssignRoleRequest() # AssignRoleRequest | 
    disable_notifications = True # bool | Setting this to `true` grants the group third-party admin status (optional)

    try:
        # Assign a Role to a Group
        api_response = api_instance.assign_role_to_group(group_id, assign_role_request, disable_notifications=disable_notifications)
        print("The response of RoleAssignmentApi->assign_role_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->assign_role_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **assign_role_request** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 
 **disable_notifications** | **bool**| Setting this to &#x60;true&#x60; grants the group third-party admin status | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_role_to_user**
> Role assign_role_to_user(user_id, assign_role_request, disable_notifications=disable_notifications)

Assign a Role to a User

Assigns a role to a user identified by `userId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_request import AssignRoleRequest
from okta.models.role import Role
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
    api_instance = okta.RoleAssignmentApi(api_client)
    user_id = 'user_id_example' # str | 
    assign_role_request = okta.AssignRoleRequest() # AssignRoleRequest | 
    disable_notifications = True # bool | Setting this to `true` grants the user third-party admin status (optional)

    try:
        # Assign a Role to a User
        api_response = api_instance.assign_role_to_user(user_id, assign_role_request, disable_notifications=disable_notifications)
        print("The response of RoleAssignmentApi->assign_role_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->assign_role_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **assign_role_request** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 
 **disable_notifications** | **bool**| Setting this to &#x60;true&#x60; grants the user third-party admin status | [optional] 

### Return type

[**Role**](Role.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_assigned_role**
> Role get_group_assigned_role(group_id, role_id)

Retrieve a Role assigned to Group

Retrieves a role identified by `roleId` assigned to group identified by `groupId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role import Role
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
    api_instance = okta.RoleAssignmentApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role

    try:
        # Retrieve a Role assigned to Group
        api_response = api_instance.get_group_assigned_role(group_id, role_id)
        print("The response of RoleAssignmentApi->get_group_assigned_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->get_group_assigned_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 

### Return type

[**Role**](Role.md)

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

# **get_user_assigned_role**
> Role get_user_assigned_role(user_id, role_id)

Retrieve a Role assigned to a User

Retrieves a role identified by `roleId` assigned to a user identified by `userId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role import Role
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
    api_instance = okta.RoleAssignmentApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role

    try:
        # Retrieve a Role assigned to a User
        api_response = api_instance.get_user_assigned_role(user_id, role_id)
        print("The response of RoleAssignmentApi->get_user_assigned_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->get_user_assigned_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 

### Return type

[**Role**](Role.md)

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

# **list_assigned_roles_for_user**
> List[Role] list_assigned_roles_for_user(user_id, expand=expand)

List all Roles assigned to a User

Lists all roles assigned to a user identified by `userId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role import Role
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
    api_instance = okta.RoleAssignmentApi(api_client)
    user_id = 'user_id_example' # str | 
    expand = 'expand_example' # str |  (optional)

    try:
        # List all Roles assigned to a User
        api_response = api_instance.list_assigned_roles_for_user(user_id, expand=expand)
        print("The response of RoleAssignmentApi->list_assigned_roles_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->list_assigned_roles_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**List[Role]**](Role.md)

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

# **list_group_assigned_roles**
> List[Role] list_group_assigned_roles(group_id, expand=expand)

List all Assigned Roles of Group

Lists all assigned roles of group identified by `groupId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role import Role
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
    api_instance = okta.RoleAssignmentApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    expand = 'expand_example' # str |  (optional)

    try:
        # List all Assigned Roles of Group
        api_response = api_instance.list_group_assigned_roles(group_id, expand=expand)
        print("The response of RoleAssignmentApi->list_group_assigned_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->list_group_assigned_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **expand** | **str**|  | [optional] 

### Return type

[**List[Role]**](Role.md)

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

# **list_users_with_role_assignments**
> RoleAssignedUsers list_users_with_role_assignments(after=after, limit=limit)

List all Users with Role Assignments

Lists all users with Role Assignments

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role_assigned_users import RoleAssignedUsers
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
    api_instance = okta.RoleAssignmentApi(api_client)
    after = 'after_example' # str |  (optional)
    limit = 100 # int | Specifies the number of results returned. Defaults to `100`. (optional) (default to 100)

    try:
        # List all Users with Role Assignments
        api_response = api_instance.list_users_with_role_assignments(after=after, limit=limit)
        print("The response of RoleAssignmentApi->list_users_with_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->list_users_with_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**| Specifies the number of results returned. Defaults to &#x60;100&#x60;. | [optional] [default to 100]

### Return type

[**RoleAssignedUsers**](RoleAssignedUsers.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_role_from_group**
> unassign_role_from_group(group_id, role_id)

Unassign a Role from a Group

Unassigns a role identified by `roleId` assigned to group identified by `groupId`

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
    api_instance = okta.RoleAssignmentApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role

    try:
        # Unassign a Role from a Group
        api_instance.unassign_role_from_group(group_id, role_id)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->unassign_role_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 

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

# **unassign_role_from_user**
> unassign_role_from_user(user_id, role_id)

Unassign a Role from a User

Unassigns a role identified by `roleId` from a user identified by `userId`

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
    api_instance = okta.RoleAssignmentApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role

    try:
        # Unassign a Role from a User
        api_instance.unassign_role_from_user(user_id, role_id)
    except Exception as e:
        print("Exception when calling RoleAssignmentApi->unassign_role_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 

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

