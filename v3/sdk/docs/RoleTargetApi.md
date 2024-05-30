# openapi_client.RoleTargetApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_all_apps_as_target_to_role_for_user**](RoleTargetApi.md#assign_all_apps_as_target_to_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps | Assign all Apps as Target to Role
[**assign_app_instance_target_to_app_admin_role_for_group**](RoleTargetApi.md#assign_app_instance_target_to_app_admin_role_for_group) | **PUT** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{appId} | Assign an Application Instance Target to Application Administrator Role
[**assign_app_instance_target_to_app_admin_role_for_user**](RoleTargetApi.md#assign_app_instance_target_to_app_admin_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{appId} | Assign an Application Instance Target to an Application Administrator Role
[**assign_app_target_to_admin_role_for_group**](RoleTargetApi.md#assign_app_target_to_admin_role_for_group) | **PUT** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName} | Assign an Application Target to Administrator Role
[**assign_app_target_to_admin_role_for_user**](RoleTargetApi.md#assign_app_target_to_admin_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName} | Assign an Application Target to Administrator Role
[**assign_group_target_to_group_admin_role**](RoleTargetApi.md#assign_group_target_to_group_admin_role) | **PUT** /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId} | Assign a Group Target to a Group Role
[**assign_group_target_to_user_role**](RoleTargetApi.md#assign_group_target_to_user_role) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId} | Assign a Group Target to Role
[**list_application_targets_for_application_administrator_role_for_group**](RoleTargetApi.md#list_application_targets_for_application_administrator_role_for_group) | **GET** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps | List all Application Targets for an Application Administrator Role
[**list_application_targets_for_application_administrator_role_for_user**](RoleTargetApi.md#list_application_targets_for_application_administrator_role_for_user) | **GET** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps | List all Application Targets for Application Administrator Role
[**list_group_targets_for_group_role**](RoleTargetApi.md#list_group_targets_for_group_role) | **GET** /api/v1/groups/{groupId}/roles/{roleId}/targets/groups | List all Group Targets for a Group Role
[**list_group_targets_for_role**](RoleTargetApi.md#list_group_targets_for_role) | **GET** /api/v1/users/{userId}/roles/{roleId}/targets/groups | List all Group Targets for Role
[**unassign_app_instance_target_from_admin_role_for_user**](RoleTargetApi.md#unassign_app_instance_target_from_admin_role_for_user) | **DELETE** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{appId} | Unassign an Application Instance Target from an Application Administrator Role
[**unassign_app_instance_target_to_app_admin_role_for_group**](RoleTargetApi.md#unassign_app_instance_target_to_app_admin_role_for_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{appId} | Unassign an Application Instance Target from an Application Administrator Role
[**unassign_app_target_from_app_admin_role_for_user**](RoleTargetApi.md#unassign_app_target_from_app_admin_role_for_user) | **DELETE** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName} | Unassign an Application Target from an Application Administrator Role
[**unassign_app_target_to_admin_role_for_group**](RoleTargetApi.md#unassign_app_target_to_admin_role_for_group) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName} | Unassign an Application Target from Application Administrator Role
[**unassign_group_target_from_group_admin_role**](RoleTargetApi.md#unassign_group_target_from_group_admin_role) | **DELETE** /api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId} | Unassign a Group Target from a Group Role
[**unassign_group_target_from_user_admin_role**](RoleTargetApi.md#unassign_group_target_from_user_admin_role) | **DELETE** /api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId} | Unassign a Group Target from Role


# **assign_all_apps_as_target_to_role_for_user**
> assign_all_apps_as_target_to_role_for_user(user_id, role_id)

Assign all Apps as Target to Role

Assigns all Apps as Target to Role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role

    try:
        # Assign all Apps as Target to Role
        api_instance.assign_all_apps_as_target_to_role_for_user(user_id, role_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_all_apps_as_target_to_role_for_user: %s\n" % e)
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
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_app_instance_target_to_app_admin_role_for_group**
> assign_app_instance_target_to_app_admin_role_for_group(group_id, role_id, app_name, app_id)

Assign an Application Instance Target to Application Administrator Role

Assigns App Instance Target to App Administrator Role given to a Group

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Assign an Application Instance Target to Application Administrator Role
        api_instance.assign_app_instance_target_to_app_admin_role_for_group(group_id, role_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_app_instance_target_to_app_admin_role_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 
 **app_id** | **str**| ID of the Application | 

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

# **assign_app_instance_target_to_app_admin_role_for_user**
> assign_app_instance_target_to_app_admin_role_for_user(user_id, role_id, app_name, app_id)

Assign an Application Instance Target to an Application Administrator Role

Assigns anapplication instance target to appplication administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Assign an Application Instance Target to an Application Administrator Role
        api_instance.assign_app_instance_target_to_app_admin_role_for_user(user_id, role_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_app_instance_target_to_app_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 
 **app_id** | **str**| ID of the Application | 

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

# **assign_app_target_to_admin_role_for_group**
> assign_app_target_to_admin_role_for_group(group_id, role_id, app_name)

Assign an Application Target to Administrator Role

Assigns an application target to administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 

    try:
        # Assign an Application Target to Administrator Role
        api_instance.assign_app_target_to_admin_role_for_group(group_id, role_id, app_name)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_app_target_to_admin_role_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 

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
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_app_target_to_admin_role_for_user**
> assign_app_target_to_admin_role_for_user(user_id, role_id, app_name)

Assign an Application Target to Administrator Role

Assigns an application target to administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 

    try:
        # Assign an Application Target to Administrator Role
        api_instance.assign_app_target_to_admin_role_for_user(user_id, role_id, app_name)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_app_target_to_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 

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

# **assign_group_target_to_group_admin_role**
> assign_group_target_to_group_admin_role(group_id, role_id, target_group_id)

Assign a Group Target to a Group Role

Assigns a group target to a group role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    target_group_id = '00g1e9dfjHeLAsdX983d' # str | 

    try:
        # Assign a Group Target to a Group Role
        api_instance.assign_group_target_to_group_admin_role(group_id, role_id, target_group_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_group_target_to_group_admin_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **target_group_id** | **str**|  | 

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

# **assign_group_target_to_user_role**
> assign_group_target_to_user_role(user_id, role_id, group_id)

Assign a Group Target to Role

Assigns a Group Target to Role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Assign a Group Target to Role
        api_instance.assign_group_target_to_user_role(user_id, role_id, group_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->assign_group_target_to_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
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

# **list_application_targets_for_application_administrator_role_for_group**
> List[CatalogApplication] list_application_targets_for_application_administrator_role_for_group(group_id, role_id, after=after, limit=limit)

List all Application Targets for an Application Administrator Role

Lists all App targets for an `APP_ADMIN` Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.catalog_application import CatalogApplication
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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Application Targets for an Application Administrator Role
        api_response = api_instance.list_application_targets_for_application_administrator_role_for_group(group_id, role_id, after=after, limit=limit)
        print("The response of RoleTargetApi->list_application_targets_for_application_administrator_role_for_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleTargetApi->list_application_targets_for_application_administrator_role_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

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

# **list_application_targets_for_application_administrator_role_for_user**
> List[CatalogApplication] list_application_targets_for_application_administrator_role_for_user(user_id, role_id, after=after, limit=limit)

List all Application Targets for Application Administrator Role

Lists all App targets for an `APP_ADMIN` Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.catalog_application import CatalogApplication
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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Application Targets for Application Administrator Role
        api_response = api_instance.list_application_targets_for_application_administrator_role_for_user(user_id, role_id, after=after, limit=limit)
        print("The response of RoleTargetApi->list_application_targets_for_application_administrator_role_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleTargetApi->list_application_targets_for_application_administrator_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

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

# **list_group_targets_for_group_role**
> List[Group] list_group_targets_for_group_role(group_id, role_id, after=after, limit=limit)

List all Group Targets for a Group Role

Lists all group targets for a group role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Group Targets for a Group Role
        api_response = api_instance.list_group_targets_for_group_role(group_id, role_id, after=after, limit=limit)
        print("The response of RoleTargetApi->list_group_targets_for_group_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleTargetApi->list_group_targets_for_group_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

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

# **list_group_targets_for_role**
> List[Group] list_group_targets_for_role(user_id, role_id, after=after, limit=limit)

List all Group Targets for Role

Lists all group targets for role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Group Targets for Role
        api_response = api_instance.list_group_targets_for_role(user_id, role_id, after=after, limit=limit)
        print("The response of RoleTargetApi->list_group_targets_for_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleTargetApi->list_group_targets_for_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

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
> unassign_app_instance_target_from_admin_role_for_user(user_id, role_id, app_name, app_id)

Unassign an Application Instance Target from an Application Administrator Role

Unassigns an application instance target from an application administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Unassign an Application Instance Target from an Application Administrator Role
        api_instance.unassign_app_instance_target_from_admin_role_for_user(user_id, role_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->unassign_app_instance_target_from_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 
 **app_id** | **str**| ID of the Application | 

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

# **unassign_app_instance_target_to_app_admin_role_for_group**
> unassign_app_instance_target_to_app_admin_role_for_group(group_id, role_id, app_name, app_id)

Unassign an Application Instance Target from an Application Administrator Role

Unassigns an application instance target from application administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Unassign an Application Instance Target from an Application Administrator Role
        api_instance.unassign_app_instance_target_to_app_admin_role_for_group(group_id, role_id, app_name, app_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->unassign_app_instance_target_to_app_admin_role_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 
 **app_id** | **str**| ID of the Application | 

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
> unassign_app_target_from_app_admin_role_for_user(user_id, role_id, app_name)

Unassign an Application Target from an Application Administrator Role

Unassigns an application target from application administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 

    try:
        # Unassign an Application Target from an Application Administrator Role
        api_instance.unassign_app_target_from_app_admin_role_for_user(user_id, role_id, app_name)
    except Exception as e:
        print("Exception when calling RoleTargetApi->unassign_app_target_from_app_admin_role_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 

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

# **unassign_app_target_to_admin_role_for_group**
> unassign_app_target_to_admin_role_for_group(group_id, role_id, app_name)

Unassign an Application Target from Application Administrator Role

Unassigns an application target from application administrator role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    app_name = 'oidc_client' # str | 

    try:
        # Unassign an Application Target from Application Administrator Role
        api_instance.unassign_app_target_to_admin_role_for_group(group_id, role_id, app_name)
    except Exception as e:
        print("Exception when calling RoleTargetApi->unassign_app_target_to_admin_role_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **app_name** | **str**|  | 

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

# **unassign_group_target_from_group_admin_role**
> unassign_group_target_from_group_admin_role(group_id, role_id, target_group_id)

Unassign a Group Target from a Group Role

Unassigns a group target from a group role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    target_group_id = '00g1e9dfjHeLAsdX983d' # str | 

    try:
        # Unassign a Group Target from a Group Role
        api_instance.unassign_group_target_from_group_admin_role(group_id, role_id, target_group_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->unassign_group_target_from_group_admin_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
 **target_group_id** | **str**|  | 

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
> unassign_group_target_from_user_admin_role(user_id, role_id, group_id)

Unassign a Group Target from Role

Unassigns a Group Target from Role

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
    api_instance = openapi_client.RoleTargetApi(api_client)
    user_id = 'user_id_example' # str | 
    role_id = '3Vg1Pjp3qzw4qcCK5EdO' # str | `id` of the Role
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Unassign a Group Target from Role
        api_instance.unassign_group_target_from_user_admin_role(user_id, role_id, group_id)
    except Exception as e:
        print("Exception when calling RoleTargetApi->unassign_group_target_from_user_admin_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**| &#x60;id&#x60; of the Role | 
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

