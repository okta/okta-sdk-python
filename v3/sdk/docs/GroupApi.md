# openapi_client.GroupApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_group_rule**](GroupApi.md#activate_group_rule) | **POST** /api/v1/groups/rules/{groupRuleId}/lifecycle/activate | Activate a Group Rule
[**assign_group_owner**](GroupApi.md#assign_group_owner) | **POST** /api/v1/groups/{groupId}/owners | Assign a Group Owner
[**assign_user_to_group**](GroupApi.md#assign_user_to_group) | **PUT** /api/v1/groups/{groupId}/users/{userId} | Assign a User
[**create_group**](GroupApi.md#create_group) | **POST** /api/v1/groups | Create a Group
[**create_group_rule**](GroupApi.md#create_group_rule) | **POST** /api/v1/groups/rules | Create a Group Rule
[**deactivate_group_rule**](GroupApi.md#deactivate_group_rule) | **POST** /api/v1/groups/rules/{groupRuleId}/lifecycle/deactivate | Deactivate a Group Rule
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /api/v1/groups/{groupId} | Delete a Group
[**delete_group_owner**](GroupApi.md#delete_group_owner) | **DELETE** /api/v1/groups/{groupId}/owners/{ownerId} | Delete a Group Owner
[**delete_group_rule**](GroupApi.md#delete_group_rule) | **DELETE** /api/v1/groups/rules/{groupRuleId} | Delete a group Rule
[**get_group**](GroupApi.md#get_group) | **GET** /api/v1/groups/{groupId} | Retrieve a Group
[**get_group_rule**](GroupApi.md#get_group_rule) | **GET** /api/v1/groups/rules/{groupRuleId} | Retrieve a Group Rule
[**list_assigned_applications_for_group**](GroupApi.md#list_assigned_applications_for_group) | **GET** /api/v1/groups/{groupId}/apps | List all Assigned Applications
[**list_group_owners**](GroupApi.md#list_group_owners) | **GET** /api/v1/groups/{groupId}/owners | List all Group Owners
[**list_group_rules**](GroupApi.md#list_group_rules) | **GET** /api/v1/groups/rules | List all Group Rules
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /api/v1/groups/{groupId}/users | List all Member Users
[**list_groups**](GroupApi.md#list_groups) | **GET** /api/v1/groups | List all Groups
[**replace_group**](GroupApi.md#replace_group) | **PUT** /api/v1/groups/{groupId} | Replace a Group
[**replace_group_rule**](GroupApi.md#replace_group_rule) | **PUT** /api/v1/groups/rules/{groupRuleId} | Replace a Group Rule
[**unassign_user_from_group**](GroupApi.md#unassign_user_from_group) | **DELETE** /api/v1/groups/{groupId}/users/{userId} | Unassign a User


# **activate_group_rule**
> activate_group_rule(group_rule_id)

Activate a Group Rule

Activates a specific group rule by `groupRuleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule

    try:
        # Activate a Group Rule
        api_instance.activate_group_rule(group_rule_id)
    except Exception as e:
        print("Exception when calling GroupApi->activate_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 

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

# **assign_group_owner**
> GroupOwner assign_group_owner(group_id, assign_group_owner_request_body)

Assign a Group Owner

Assigns a group owner

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.assign_group_owner_request_body import AssignGroupOwnerRequestBody
from openapi_client.models.group_owner import GroupOwner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    assign_group_owner_request_body = openapi_client.AssignGroupOwnerRequestBody() # AssignGroupOwnerRequestBody | 

    try:
        # Assign a Group Owner
        api_response = api_instance.assign_group_owner(group_id, assign_group_owner_request_body)
        print("The response of GroupApi->assign_group_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->assign_group_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **assign_group_owner_request_body** | [**AssignGroupOwnerRequestBody**](AssignGroupOwnerRequestBody.md)|  | 

### Return type

[**GroupOwner**](GroupOwner.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_user_to_group**
> assign_user_to_group(group_id, user_id)

Assign a User

Assigns a user to a group with 'OKTA_GROUP' type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    user_id = 'user_id_example' # str | 

    try:
        # Assign a User
        api_instance.assign_user_to_group(group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupApi->assign_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **user_id** | **str**|  | 

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

# **create_group**
> Group create_group(group)

Create a Group

Creates a new group with `OKTA_GROUP` type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group import Group
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group = openapi_client.Group() # Group | 

    try:
        # Create a Group
        api_response = api_instance.create_group(group)
        print("The response of GroupApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->create_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

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

# **create_group_rule**
> GroupRule create_group_rule(group_rule)

Create a Group Rule

Creates a group rule to dynamically add users to the specified group if they match the condition

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_rule import GroupRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_rule = openapi_client.GroupRule() # GroupRule | 

    try:
        # Create a Group Rule
        api_response = api_instance.create_group_rule(group_rule)
        print("The response of GroupApi->create_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->create_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule** | [**GroupRule**](GroupRule.md)|  | 

### Return type

[**GroupRule**](GroupRule.md)

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

# **deactivate_group_rule**
> deactivate_group_rule(group_rule_id)

Deactivate a Group Rule

Deactivates a specific group rule by `groupRuleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule

    try:
        # Deactivate a Group Rule
        api_instance.deactivate_group_rule(group_rule_id)
    except Exception as e:
        print("Exception when calling GroupApi->deactivate_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 

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

# **delete_group**
> delete_group(group_id)

Delete a Group

Deletes a group with `OKTA_GROUP` type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Delete a Group
        api_instance.delete_group(group_id)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_group_owner**
> delete_group_owner(group_id, owner_id)

Delete a Group Owner

Deletes a group owner from a specific group

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    owner_id = '00u1emaK22TWRYd3TtG' # str | The `id` of the group owner

    try:
        # Delete a Group Owner
        api_instance.delete_group_owner(group_id, owner_id)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **owner_id** | **str**| The &#x60;id&#x60; of the group owner | 

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

# **delete_group_rule**
> delete_group_rule(group_rule_id, remove_users=remove_users)

Delete a group Rule

Deletes a specific group rule by `groupRuleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule
    remove_users = True # bool | Indicates whether to keep or remove users from groups assigned by this rule. (optional)

    try:
        # Delete a group Rule
        api_instance.delete_group_rule(group_rule_id, remove_users=remove_users)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 
 **remove_users** | **bool**| Indicates whether to keep or remove users from groups assigned by this rule. | [optional] 

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
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_id)

Retrieve a Group

Retrieves a group by `groupId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group import Group
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Retrieve a Group
        api_response = api_instance.get_group(group_id)
        print("The response of GroupApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 

### Return type

[**Group**](Group.md)

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

# **get_group_rule**
> GroupRule get_group_rule(group_rule_id, expand=expand)

Retrieve a Group Rule

Retrieves a specific group rule by `groupRuleId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_rule import GroupRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule
    expand = 'expand_example' # str |  (optional)

    try:
        # Retrieve a Group Rule
        api_response = api_instance.get_group_rule(group_rule_id, expand=expand)
        print("The response of GroupApi->get_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 
 **expand** | **str**|  | [optional] 

### Return type

[**GroupRule**](GroupRule.md)

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

# **list_assigned_applications_for_group**
> List[Application] list_assigned_applications_for_group(group_id, after=after, limit=limit)

List all Assigned Applications

Lists all applications that are assigned to a group

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.application import Application
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    after = 'after_example' # str | Specifies the pagination cursor for the next page of apps (optional)
    limit = 20 # int | Specifies the number of app results for a page (optional) (default to 20)

    try:
        # List all Assigned Applications
        api_response = api_instance.list_assigned_applications_for_group(group_id, after=after, limit=limit)
        print("The response of GroupApi->list_assigned_applications_for_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_assigned_applications_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **after** | **str**| Specifies the pagination cursor for the next page of apps | [optional] 
 **limit** | **int**| Specifies the number of app results for a page | [optional] [default to 20]

### Return type

[**List[Application]**](Application.md)

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

# **list_group_owners**
> List[GroupOwner] list_group_owners(group_id, filter=filter, after=after, limit=limit)

List all Group Owners

Lists all owners for a specific group

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_owner import GroupOwner
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    filter = 'filter_example' # str | SCIM Filter expression for group owners. Allows to filter owners by type. (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of owners (optional)
    limit = 1000 # int | Specifies the number of owner results in a page (optional) (default to 1000)

    try:
        # List all Group Owners
        api_response = api_instance.list_group_owners(group_id, filter=filter, after=after, limit=limit)
        print("The response of GroupApi->list_group_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_group_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **filter** | **str**| SCIM Filter expression for group owners. Allows to filter owners by type. | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of owners | [optional] 
 **limit** | **int**| Specifies the number of owner results in a page | [optional] [default to 1000]

### Return type

[**List[GroupOwner]**](GroupOwner.md)

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

# **list_group_rules**
> List[GroupRule] list_group_rules(limit=limit, after=after, search=search, expand=expand)

List all Group Rules

Lists all group rules

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_rule import GroupRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    limit = 50 # int | Specifies the number of rule results in a page (optional) (default to 50)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of rules (optional)
    search = 'search_example' # str | Specifies the keyword to search fules for (optional)
    expand = 'expand_example' # str | If specified as `groupIdToGroupNameMap`, then show group names (optional)

    try:
        # List all Group Rules
        api_response = api_instance.list_group_rules(limit=limit, after=after, search=search, expand=expand)
        print("The response of GroupApi->list_group_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_group_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Specifies the number of rule results in a page | [optional] [default to 50]
 **after** | **str**| Specifies the pagination cursor for the next page of rules | [optional] 
 **search** | **str**| Specifies the keyword to search fules for | [optional] 
 **expand** | **str**| If specified as &#x60;groupIdToGroupNameMap&#x60;, then show group names | [optional] 

### Return type

[**List[GroupRule]**](GroupRule.md)

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

# **list_group_users**
> List[User] list_group_users(group_id, after=after, limit=limit)

List all Member Users

Lists all users that are a member of a group

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    after = 'after_example' # str | Specifies the pagination cursor for the next page of users (optional)
    limit = 1000 # int | Specifies the number of user results in a page (optional) (default to 1000)

    try:
        # List all Member Users
        api_response = api_instance.list_group_users(group_id, after=after, limit=limit)
        print("The response of GroupApi->list_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **after** | **str**| Specifies the pagination cursor for the next page of users | [optional] 
 **limit** | **int**| Specifies the number of user results in a page | [optional] [default to 1000]

### Return type

[**List[User]**](User.md)

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

# **list_groups**
> List[Group] list_groups(q=q, filter=filter, after=after, limit=limit, expand=expand, search=search, sort_by=sort_by, sort_order=sort_order)

List all Groups

Lists all groups with pagination support. A subset of groups can be returned that match a supported filter expression or query.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group import Group
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    q = 'q_example' # str | Searches the name property of groups for matching value (optional)
    filter = 'filter_example' # str | Filter expression for groups (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of groups (optional)
    limit = 10000 # int | Specifies the number of group results in a page (optional) (default to 10000)
    expand = 'expand_example' # str | If specified, it causes additional metadata to be included in the response. (optional)
    search = 'search_example' # str | Searches for groups with a supported filtering expression for all attributes except for _embedded, _links, and objectClass (optional)
    sort_by = 'lastUpdated' # str | Specifies field to sort by and can be any single property (for search queries only). (optional)
    sort_order = 'asc' # str | Specifies sort order `asc` or `desc` (for search queries only). This parameter is ignored if `sortBy` is not present. Groups with the same value for the `sortBy` parameter are ordered by `id`. (optional) (default to 'asc')

    try:
        # List all Groups
        api_response = api_instance.list_groups(q=q, filter=filter, after=after, limit=limit, expand=expand, search=search, sort_by=sort_by, sort_order=sort_order)
        print("The response of GroupApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Searches the name property of groups for matching value | [optional] 
 **filter** | **str**| Filter expression for groups | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of groups | [optional] 
 **limit** | **int**| Specifies the number of group results in a page | [optional] [default to 10000]
 **expand** | **str**| If specified, it causes additional metadata to be included in the response. | [optional] 
 **search** | **str**| Searches for groups with a supported filtering expression for all attributes except for _embedded, _links, and objectClass | [optional] 
 **sort_by** | **str**| Specifies field to sort by and can be any single property (for search queries only). | [optional] 
 **sort_order** | **str**| Specifies sort order &#x60;asc&#x60; or &#x60;desc&#x60; (for search queries only). This parameter is ignored if &#x60;sortBy&#x60; is not present. Groups with the same value for the &#x60;sortBy&#x60; parameter are ordered by &#x60;id&#x60;. | [optional] [default to &#39;asc&#39;]

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_group**
> Group replace_group(group_id, group)

Replace a Group

Replaces the profile for a group with `OKTA_GROUP` type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group import Group
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    group = openapi_client.Group() # Group | 

    try:
        # Replace a Group
        api_response = api_instance.replace_group(group_id, group)
        print("The response of GroupApi->replace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->replace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **group** | [**Group**](Group.md)|  | 

### Return type

[**Group**](Group.md)

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

# **replace_group_rule**
> GroupRule replace_group_rule(group_rule_id, group_rule)

Replace a Group Rule

Replaces a group rule. Only `INACTIVE` rules can be updated.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_rule import GroupRule
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_rule_id = '0pr3f7zMZZHPgUoWO0g4' # str | The `id` of the group rule
    group_rule = openapi_client.GroupRule() # GroupRule | 

    try:
        # Replace a Group Rule
        api_response = api_instance.replace_group_rule(group_rule_id, group_rule)
        print("The response of GroupApi->replace_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->replace_group_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_rule_id** | **str**| The &#x60;id&#x60; of the group rule | 
 **group_rule** | [**GroupRule**](GroupRule.md)|  | 

### Return type

[**GroupRule**](GroupRule.md)

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

# **unassign_user_from_group**
> unassign_user_from_group(group_id, user_id)

Unassign a User

Unassigns a user from a group with 'OKTA_GROUP' type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    user_id = 'user_id_example' # str | 

    try:
        # Unassign a User
        api_instance.unassign_user_from_group(group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupApi->unassign_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **user_id** | **str**|  | 

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

