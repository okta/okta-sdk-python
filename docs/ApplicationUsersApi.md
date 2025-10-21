# okta.ApplicationUsersApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user_to_application**](ApplicationUsersApi.md#assign_user_to_application) | **POST** /api/v1/apps/{appId}/users | Assign a User
[**get_application_user**](ApplicationUsersApi.md#get_application_user) | **GET** /api/v1/apps/{appId}/users/{userId} | Retrieve an assigned User
[**list_application_users**](ApplicationUsersApi.md#list_application_users) | **GET** /api/v1/apps/{appId}/users | List all assigned Users
[**unassign_user_from_application**](ApplicationUsersApi.md#unassign_user_from_application) | **DELETE** /api/v1/apps/{appId}/users/{userId} | Unassign an App User
[**update_application_user**](ApplicationUsersApi.md#update_application_user) | **POST** /api/v1/apps/{appId}/users/{userId} | Update an App Profile for an assigned User


# **assign_user_to_application**
> AppUser assign_user_to_application(app_id, app_user)

Assign a User

Assigns a user to an app with credentials and an app-specific [profile](/openapi/okta-management/management/tag/Application/#tag/Application/operation/assignUserToApplication!c=200&path=profile&t=response). Profile mappings defined for the app are applied first before applying any profile properties that are specified in the request.  > **Notes:** > * You need to specify the `id` and omit the `credentials` parameter in the request body only for `signOnMode` or authentication schemes (`credentials.scheme`) that don't require credentials. > * You can only specify profile properties that aren't defined by profile mappings when Universal Directory is enabled. > * If your SSO app requires a profile but doesn't have provisioning enabled, you need to add a profile to the request body.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_user import AppUser
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
    api_instance = okta.ApplicationUsersApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    app_user = okta.AppUser() # AppUser | 

    try:
        # Assign a User
        api_response = api_instance.assign_user_to_application(app_id, app_user)
        print("The response of ApplicationUsersApi->assign_user_to_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->assign_user_to_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **app_user** | [**AppUser**](AppUser.md)|  | 

### Return type

[**AppUser**](AppUser.md)

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

# **get_application_user**
> AppUser get_application_user(app_id, user_id, expand=expand)

Retrieve an assigned User

Retrieves a specific user assignment for app by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_user import AppUser
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
    api_instance = okta.ApplicationUsersApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    user_id = 'user_id_example' # str | 
    expand = 'expand_example' # str |  (optional)

    try:
        # Retrieve an assigned User
        api_response = api_instance.get_application_user(app_id, user_id, expand=expand)
        print("The response of ApplicationUsersApi->get_application_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->get_application_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **user_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**AppUser**](AppUser.md)

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

# **list_application_users**
> List[AppUser] list_application_users(app_id, q=q, query_scope=query_scope, after=after, limit=limit, filter=filter, expand=expand)

List all assigned Users

Lists all assigned users for an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_user import AppUser
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
    api_instance = okta.ApplicationUsersApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    q = 'q_example' # str |  (optional)
    query_scope = 'query_scope_example' # str |  (optional)
    after = 'after_example' # str | specifies the pagination cursor for the next page of assignments (optional)
    limit = -1 # int | specifies the number of results for a page (optional) (default to -1)
    filter = 'filter_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)

    try:
        # List all assigned Users
        api_response = api_instance.list_application_users(app_id, q=q, query_scope=query_scope, after=after, limit=limit, filter=filter, expand=expand)
        print("The response of ApplicationUsersApi->list_application_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->list_application_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **q** | **str**|  | [optional] 
 **query_scope** | **str**|  | [optional] 
 **after** | **str**| specifies the pagination cursor for the next page of assignments | [optional] 
 **limit** | **int**| specifies the number of results for a page | [optional] [default to -1]
 **filter** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 

### Return type

[**List[AppUser]**](AppUser.md)

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

# **unassign_user_from_application**
> unassign_user_from_application(app_id, user_id, send_email=send_email)

Unassign an App User

Unassigns a user from an application

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
    api_instance = okta.ApplicationUsersApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    user_id = 'user_id_example' # str | 
    send_email = False # bool |  (optional) (default to False)

    try:
        # Unassign an App User
        api_instance.unassign_user_from_application(app_id, user_id, send_email=send_email)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->unassign_user_from_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | [optional] [default to False]

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

# **update_application_user**
> AppUser update_application_user(app_id, user_id, app_user)

Update an App Profile for an assigned User

Updates a user's profile for an application

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_user import AppUser
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
    api_instance = okta.ApplicationUsersApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    user_id = 'user_id_example' # str | 
    app_user = okta.AppUser() # AppUser | 

    try:
        # Update an App Profile for an assigned User
        api_response = api_instance.update_application_user(app_id, user_id, app_user)
        print("The response of ApplicationUsersApi->update_application_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->update_application_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **user_id** | **str**|  | 
 **app_user** | [**AppUser**](AppUser.md)|  | 

### Return type

[**AppUser**](AppUser.md)

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

