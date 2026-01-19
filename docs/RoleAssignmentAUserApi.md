# okta.RoleAssignmentAUserApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_user**](RoleAssignmentAUserApi.md#assign_role_to_user) | **POST** /api/v1/users/{userId}/roles | Assign a user role
[**get_role_assignment_governance_grant**](RoleAssignmentAUserApi.md#get_role_assignment_governance_grant) | **GET** /api/v1/users/{userId}/roles/{roleAssignmentId}/governance/{grantId} | Retrieve a user role governance source
[**get_role_assignment_governance_grant_resources**](RoleAssignmentAUserApi.md#get_role_assignment_governance_grant_resources) | **GET** /api/v1/users/{userId}/roles/{roleAssignmentId}/governance/{grantId}/resources | Retrieve the user role governance source resources
[**get_user_assigned_role**](RoleAssignmentAUserApi.md#get_user_assigned_role) | **GET** /api/v1/users/{userId}/roles/{roleAssignmentId} | Retrieve a user role assignment
[**get_user_assigned_role_governance**](RoleAssignmentAUserApi.md#get_user_assigned_role_governance) | **GET** /api/v1/users/{userId}/roles/{roleAssignmentId}/governance | Retrieve all user role governance sources
[**list_assigned_roles_for_user**](RoleAssignmentAUserApi.md#list_assigned_roles_for_user) | **GET** /api/v1/users/{userId}/roles | List all user role assignments
[**list_users_with_role_assignments**](RoleAssignmentAUserApi.md#list_users_with_role_assignments) | **GET** /api/v1/iam/assignees/users | List all users with role assignments
[**unassign_role_from_user**](RoleAssignmentAUserApi.md#unassign_role_from_user) | **DELETE** /api/v1/users/{userId}/roles/{roleAssignmentId} | Unassign a user role


# **assign_role_to_user**
> AssignRoleToUser201Response assign_role_to_user(user_id, assign_role_request, disable_notifications=disable_notifications)

Assign a user role

Assigns a [standard role](/openapi/okta-management/guides/roles/#standard-roles) to a user.  You can also assign a custom role to a user, but the preferred method to assign a custom role to a user is to create a binding between the custom role, the resource set, and the user. See [Create a role resource set binding](/openapi/okta-management/management/tag/RoleDResourceSetBinding/#tag/RoleDResourceSetBinding/operation/createResourceSetBinding).  > **Notes:** > * The request payload is different for standard and custom role assignments. > * For IAM-based standard role assignments, use the request payload for standard roles. However, the response payload for IAM-based role assignments is similar to the custom role's assignment response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_to_user201_response import AssignRoleToUser201Response
from okta.models.assign_role_to_user_request import AssignRoleToUserRequest
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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    assign_role_request = okta.AssignRoleToUserRequest() # AssignRoleToUserRequest | 
    disable_notifications = False # bool | Setting this to `true` grants the user third-party admin status (optional) (default to False)

    try:
        # Assign a user role
        api_response = api_instance.assign_role_to_user(user_id, assign_role_request, disable_notifications=disable_notifications)
        print("The response of RoleAssignmentAUserApi->assign_role_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->assign_role_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **assign_role_request** | [**AssignRoleToUserRequest**](AssignRoleToUserRequest.md)|  | 
 **disable_notifications** | **bool**| Setting this to &#x60;true&#x60; grants the user third-party admin status | [optional] [default to False]

### Return type

[**AssignRoleToUser201Response**](AssignRoleToUser201Response.md)

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

# **get_role_assignment_governance_grant**
> RoleGovernanceSource get_role_assignment_governance_grant(user_id, role_assignment_id, grant_id)

Retrieve a user role governance source

Retrieves a governance source (identified by `grantId`) for a role (identified by `roleAssignmentId`) that's assigned to a user (identified by `userId`)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role_governance_source import RoleGovernanceSource
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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    grant_id = 'iJoqkwx50mrgX4T9LcaH' # str | Grant ID

    try:
        # Retrieve a user role governance source
        api_response = api_instance.get_role_assignment_governance_grant(user_id, role_assignment_id, grant_id)
        print("The response of RoleAssignmentAUserApi->get_role_assignment_governance_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->get_role_assignment_governance_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **grant_id** | **str**| Grant ID | 

### Return type

[**RoleGovernanceSource**](RoleGovernanceSource.md)

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

# **get_role_assignment_governance_grant_resources**
> RoleGovernanceResources get_role_assignment_governance_grant_resources(user_id, role_assignment_id, grant_id)

Retrieve the user role governance source resources

Retrieves the resources of a governance source (identified by `grantId`) for a role (identified by `roleAssignmentId`) that's assigned to a user (identified by `userId`)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role_governance_resources import RoleGovernanceResources
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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment
    grant_id = 'iJoqkwx50mrgX4T9LcaH' # str | Grant ID

    try:
        # Retrieve the user role governance source resources
        api_response = api_instance.get_role_assignment_governance_grant_resources(user_id, role_assignment_id, grant_id)
        print("The response of RoleAssignmentAUserApi->get_role_assignment_governance_grant_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->get_role_assignment_governance_grant_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 
 **grant_id** | **str**| Grant ID | 

### Return type

[**RoleGovernanceResources**](RoleGovernanceResources.md)

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
> AssignRoleToGroup200Response get_user_assigned_role(user_id, role_assignment_id)

Retrieve a user role assignment

Retrieves a role assigned to a user (identified by `userId`). The `roleAssignmentId` parameter is the unique identifier for either a standard role assignment object or a custom role resource set binding object.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_to_group200_response import AssignRoleToGroup200Response
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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Retrieve a user role assignment
        api_response = api_instance.get_user_assigned_role(user_id, role_assignment_id)
        print("The response of RoleAssignmentAUserApi->get_user_assigned_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->get_user_assigned_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 

### Return type

[**AssignRoleToGroup200Response**](AssignRoleToGroup200Response.md)

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

# **get_user_assigned_role_governance**
> RoleGovernance get_user_assigned_role_governance(user_id, role_assignment_id)

Retrieve all user role governance sources

Retrieves the governance sources of a role (identified by `roleAssignmentId`) that's assigned to a user (identified by `userId`)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.role_governance import RoleGovernance
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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Retrieve all user role governance sources
        api_response = api_instance.get_user_assigned_role_governance(user_id, role_assignment_id)
        print("The response of RoleAssignmentAUserApi->get_user_assigned_role_governance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->get_user_assigned_role_governance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 

### Return type

[**RoleGovernance**](RoleGovernance.md)

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
> List[ListGroupAssignedRoles200ResponseInner] list_assigned_roles_for_user(user_id, expand=expand)

List all user role assignments

Lists all roles assigned to a user (identified by `userId`)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.list_group_assigned_roles200_response_inner import ListGroupAssignedRoles200ResponseInner
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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    expand = 'targets/groups' # str | An optional parameter used to return targets configured for the standard role assignment in the `embedded` property. Supported values: `targets/groups` or `targets/catalog/apps` (optional)

    try:
        # List all user role assignments
        api_response = api_instance.list_assigned_roles_for_user(user_id, expand=expand)
        print("The response of RoleAssignmentAUserApi->list_assigned_roles_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->list_assigned_roles_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **expand** | **str**| An optional parameter used to return targets configured for the standard role assignment in the &#x60;embedded&#x60; property. Supported values: &#x60;targets/groups&#x60; or &#x60;targets/catalog/apps&#x60; | [optional] 

### Return type

[**List[ListGroupAssignedRoles200ResponseInner]**](ListGroupAssignedRoles200ResponseInner.md)

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

List all users with role assignments

Lists all users with role assignments

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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of targets (optional)
    limit = 100 # int | Specifies the number of results returned. Defaults to `100`. (optional) (default to 100)

    try:
        # List all users with role assignments
        api_response = api_instance.list_users_with_role_assignments(after=after, limit=limit)
        print("The response of RoleAssignmentAUserApi->list_users_with_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->list_users_with_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Specifies the pagination cursor for the next page of targets | [optional] 
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

# **unassign_role_from_user**
> unassign_role_from_user(user_id, role_assignment_id)

Unassign a user role

Unassigns a role assignment (identified by `roleAssignmentId`) from a user (identified by `userId`)

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
    api_instance = okta.RoleAssignmentAUserApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Unassign a user role
        api_instance.unassign_role_from_user(user_id, role_assignment_id)
    except Exception as e:
        print("Exception when calling RoleAssignmentAUserApi->unassign_role_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 

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

