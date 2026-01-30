# okta.RoleAssignmentBGroupApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_group**](RoleAssignmentBGroupApi.md#assign_role_to_group) | **POST** /api/v1/groups/{groupId}/roles | Assign a role to a group
[**get_group_assigned_role**](RoleAssignmentBGroupApi.md#get_group_assigned_role) | **GET** /api/v1/groups/{groupId}/roles/{roleAssignmentId} | Retrieve a group role assignment
[**list_group_assigned_roles**](RoleAssignmentBGroupApi.md#list_group_assigned_roles) | **GET** /api/v1/groups/{groupId}/roles | List all group role assignments
[**unassign_role_from_group**](RoleAssignmentBGroupApi.md#unassign_role_from_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleAssignmentId} | Unassign a group role


# **assign_role_to_group**
> AssignRoleToGroup200Response assign_role_to_group(group_id, assign_role_request, disable_notifications=disable_notifications)

Assign a role to a group

Assigns a [standard role](/openapi/okta-management/guides/roles/#standard-roles) to a group.  You can also assign a custom role to a group, but the preferred method to assign a custom role to a group is to create a binding between the custom role, the resource set, and the group. See [Create a role resource set binding](/openapi/okta-management/management/tag/RoleDResourceSetBinding/#tag/RoleDResourceSetBinding/operation/createResourceSetBinding).  > **Notes:** > * The request payload is different for standard and custom role assignments. > * For IAM-based standard role assignments, use the request payload for standard roles. However, the response payload for IAM-based role assignments is similar to the custom role's assignment response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_to_group200_response import AssignRoleToGroup200Response
from okta.models.assign_role_to_group_request import AssignRoleToGroupRequest
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
    api_instance = okta.RoleAssignmentBGroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    assign_role_request = okta.AssignRoleToGroupRequest() # AssignRoleToGroupRequest | 
    disable_notifications = False # bool | Grants the group third-party admin status when set to `true` (optional) (default to False)

    try:
        # Assign a role to a group
        api_response = api_instance.assign_role_to_group(group_id, assign_role_request, disable_notifications=disable_notifications)
        print("The response of RoleAssignmentBGroupApi->assign_role_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentBGroupApi->assign_role_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **assign_role_request** | [**AssignRoleToGroupRequest**](AssignRoleToGroupRequest.md)|  | 
 **disable_notifications** | **bool**| Grants the group third-party admin status when set to &#x60;true&#x60; | [optional] [default to False]

### Return type

[**AssignRoleToGroup200Response**](AssignRoleToGroup200Response.md)

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

# **get_group_assigned_role**
> AssignRoleToGroup200Response get_group_assigned_role(group_id, role_assignment_id)

Retrieve a group role assignment

Retrieves a role assigned to a group (identified by the `groupId`). The `roleAssignmentId` is the unique identifier for either a standard role group assignment object or a custom role resource set binding object.

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
    api_instance = okta.RoleAssignmentBGroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Retrieve a group role assignment
        api_response = api_instance.get_group_assigned_role(group_id, role_assignment_id)
        print("The response of RoleAssignmentBGroupApi->get_group_assigned_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentBGroupApi->get_group_assigned_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
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

# **list_group_assigned_roles**
> List[ListGroupAssignedRoles200ResponseInner] list_group_assigned_roles(group_id, expand=expand)

List all group role assignments

Lists all assigned roles of a group by `groupId`

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
    api_instance = okta.RoleAssignmentBGroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    expand = 'targets/groups' # str | An optional parameter used to return targets configured for the standard role assignment in the `embedded` property. Supported values: `targets/groups` or `targets/catalog/apps` (optional)

    try:
        # List all group role assignments
        api_response = api_instance.list_group_assigned_roles(group_id, expand=expand)
        print("The response of RoleAssignmentBGroupApi->list_group_assigned_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentBGroupApi->list_group_assigned_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
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

# **unassign_role_from_group**
> unassign_role_from_group(group_id, role_assignment_id)

Unassign a group role

Unassigns a role assignment (identified by `roleAssignmentId`) from a group (identified by the `groupId`)

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
    api_instance = okta.RoleAssignmentBGroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Unassign a group role
        api_instance.unassign_role_from_group(group_id, role_assignment_id)
    except Exception as e:
        print("Exception when calling RoleAssignmentBGroupApi->unassign_role_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
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

