# okta.RoleAssignmentClientApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_role_to_client**](RoleAssignmentClientApi.md#assign_role_to_client) | **POST** /oauth2/v1/clients/{clientId}/roles | Assign a client role
[**delete_role_from_client**](RoleAssignmentClientApi.md#delete_role_from_client) | **DELETE** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId} | Unassign a client role
[**list_roles_for_client**](RoleAssignmentClientApi.md#list_roles_for_client) | **GET** /oauth2/v1/clients/{clientId}/roles | List all client role assignments
[**retrieve_client_role**](RoleAssignmentClientApi.md#retrieve_client_role) | **GET** /oauth2/v1/clients/{clientId}/roles/{roleAssignmentId} | Retrieve a client role


# **assign_role_to_client**
> AssignRoleToClient200Response assign_role_to_client(client_id, assign_role_to_client_request)

Assign a client role

Assigns a [standard role](/openapi/okta-management/guides/roles/#standard-roles) to a client app.  You can also assign a custom role to a client app, but the preferred method to assign a custom role to a client is to create a binding between the custom role, the resource set, and the client app. See [Create a role resource set binding](/openapi/okta-management/management/tag/RoleDResourceSetBinding/#tag/RoleDResourceSetBinding/operation/createResourceSetBinding).  > **Notes:** > * The request payload is different for standard and custom role assignments. > * For IAM-based standard role assignments, use the request payload for standard roles. However, the response payload for IAM-based role assignments is similar to the custom role's assignment response.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_to_client200_response import AssignRoleToClient200Response
from okta.models.assign_role_to_client_request import AssignRoleToClientRequest
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
    api_instance = okta.RoleAssignmentClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    assign_role_to_client_request = okta.AssignRoleToClientRequest() # AssignRoleToClientRequest | 

    try:
        # Assign a client role
        api_response = api_instance.assign_role_to_client(client_id, assign_role_to_client_request)
        print("The response of RoleAssignmentClientApi->assign_role_to_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentClientApi->assign_role_to_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **assign_role_to_client_request** | [**AssignRoleToClientRequest**](AssignRoleToClientRequest.md)|  | 

### Return type

[**AssignRoleToClient200Response**](AssignRoleToClient200Response.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_from_client**
> delete_role_from_client(client_id, role_assignment_id)

Unassign a client role

Unassigns a role assignment (identified by `roleAssignmentId`) from a client app (identified by `clientId`)

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
    api_instance = okta.RoleAssignmentClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Unassign a client role
        api_instance.delete_role_from_client(client_id, role_assignment_id)
    except Exception as e:
        print("Exception when calling RoleAssignmentClientApi->delete_role_from_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
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

# **list_roles_for_client**
> List[ListRolesForClient200ResponseInner] list_roles_for_client(client_id)

List all client role assignments

Lists all roles assigned to a client app identified by `clientId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.list_roles_for_client200_response_inner import ListRolesForClient200ResponseInner
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
    api_instance = okta.RoleAssignmentClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app

    try:
        # List all client role assignments
        api_response = api_instance.list_roles_for_client(client_id)
        print("The response of RoleAssignmentClientApi->list_roles_for_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentClientApi->list_roles_for_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 

### Return type

[**List[ListRolesForClient200ResponseInner]**](ListRolesForClient200ResponseInner.md)

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

# **retrieve_client_role**
> AssignRoleToClient200Response retrieve_client_role(client_id, role_assignment_id)

Retrieve a client role

Retrieves a role assignment (identified by `roleAssignmentId`) for a client app (identified by `clientId`)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_role_to_client200_response import AssignRoleToClient200Response
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
    api_instance = okta.RoleAssignmentClientApi(api_client)
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    role_assignment_id = 'JBCUYUC7IRCVGS27IFCE2SKO' # str | The `id` of the role assignment

    try:
        # Retrieve a client role
        api_response = api_instance.retrieve_client_role(client_id, role_assignment_id)
        print("The response of RoleAssignmentClientApi->retrieve_client_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleAssignmentClientApi->retrieve_client_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **role_assignment_id** | **str**| The &#x60;id&#x60; of the role assignment | 

### Return type

[**AssignRoleToClient200Response**](AssignRoleToClient200Response.md)

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

