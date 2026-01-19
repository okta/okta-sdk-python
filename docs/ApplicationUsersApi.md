# okta.ApplicationUsersApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user_to_application**](ApplicationUsersApi.md#assign_user_to_application) | **POST** /api/v1/apps/{appId}/users | Assign an application user
[**get_application_user**](ApplicationUsersApi.md#get_application_user) | **GET** /api/v1/apps/{appId}/users/{userId} | Retrieve an application user
[**list_application_users**](ApplicationUsersApi.md#list_application_users) | **GET** /api/v1/apps/{appId}/users | List all application users
[**unassign_user_from_application**](ApplicationUsersApi.md#unassign_user_from_application) | **DELETE** /api/v1/apps/{appId}/users/{userId} | Unassign an application user
[**update_application_user**](ApplicationUsersApi.md#update_application_user) | **POST** /api/v1/apps/{appId}/users/{userId} | Update an application user


# **assign_user_to_application**
> AppUser assign_user_to_application(app_id, app_user)

Assign an application user

Assigns a user to an app for:    * SSO only<br>     Assignments to SSO apps typically don't include a user profile.     However, if your SSO app requires a profile but doesn't have provisioning enabled, you can add profile attributes in the request body.    * SSO and provisioning<br>     Assignments to SSO and provisioning apps typically include credentials and an app-specific profile.     Profile mappings defined for the app are applied first before applying any profile properties that are specified in the request body.     > **Notes:**     > * When Universal Directory is enabled, you can only specify profile properties that aren't defined in profile mappings.     > * Omit mapped properties during assignment to minimize assignment errors.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_user import AppUser
from okta.models.app_user_assign_request import AppUserAssignRequest
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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    app_user = okta.AppUserAssignRequest() # AppUserAssignRequest | 

    try:
        # Assign an application user
        api_response = api_instance.assign_user_to_application(app_id, app_user)
        print("The response of ApplicationUsersApi->assign_user_to_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->assign_user_to_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **app_user** | [**AppUserAssignRequest**](AppUserAssignRequest.md)|  | 

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

Retrieve an application user

Retrieves a specific user assignment for a specific app

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    user_id = '00u13okQOVWZJGDOAUVR' # str | ID of an existing Okta user
    expand = 'user' # str | An optional query parameter to return the corresponding [User](/openapi/okta-management/management/tag/User/) object in the `_embedded` property. Valid value: `user` (optional)

    try:
        # Retrieve an application user
        api_response = api_instance.get_application_user(app_id, user_id, expand=expand)
        print("The response of ApplicationUsersApi->get_application_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->get_application_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **user_id** | **str**| ID of an existing Okta user | 
 **expand** | **str**| An optional query parameter to return the corresponding [User](/openapi/okta-management/management/tag/User/) object in the &#x60;_embedded&#x60; property. Valid value: &#x60;user&#x60; | [optional] 

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
> List[AppUser] list_application_users(app_id, after=after, limit=limit, q=q, expand=expand)

List all application users

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    after = '16275000448691' # str | Specifies the pagination cursor for the next page of results. Treat this as an opaque value obtained through the next link relationship. See [Pagination](/#pagination). (optional)
    limit = 50 # int | Specifies the number of objects to return per page. If there are multiple pages of results, the Link header contains a `next` link that you need to use as an opaque value (follow it, don't parse it). See [Pagination](/#pagination).  (optional) (default to 50)
    q = 'sam' # str | Specifies a filter for the list of application users returned based on their profile attributes. The value of `q` is matched against the beginning of the following profile attributes: `userName`, `firstName`, `lastName`, and `email`. This filter only supports the `startsWith` operation that matches the `q` string against the beginning of the attribute values. > **Note:** For OIDC apps, user profiles don't contain the `firstName` or `lastName` attributes. Therefore, the query only matches against the `userName` or `email` attributes.  (optional)
    expand = 'user' # str | An optional query parameter to return the corresponding [User](/openapi/okta-management/management/tag/User/) object in the `_embedded` property. Valid value: `user` (optional)

    try:
        # List all application users
        api_response = api_instance.list_application_users(app_id, after=after, limit=limit, q=q, expand=expand)
        print("The response of ApplicationUsersApi->list_application_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->list_application_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **after** | **str**| Specifies the pagination cursor for the next page of results. Treat this as an opaque value obtained through the next link relationship. See [Pagination](/#pagination). | [optional] 
 **limit** | **int**| Specifies the number of objects to return per page. If there are multiple pages of results, the Link header contains a &#x60;next&#x60; link that you need to use as an opaque value (follow it, don&#39;t parse it). See [Pagination](/#pagination).  | [optional] [default to 50]
 **q** | **str**| Specifies a filter for the list of application users returned based on their profile attributes. The value of &#x60;q&#x60; is matched against the beginning of the following profile attributes: &#x60;userName&#x60;, &#x60;firstName&#x60;, &#x60;lastName&#x60;, and &#x60;email&#x60;. This filter only supports the &#x60;startsWith&#x60; operation that matches the &#x60;q&#x60; string against the beginning of the attribute values. &gt; **Note:** For OIDC apps, user profiles don&#39;t contain the &#x60;firstName&#x60; or &#x60;lastName&#x60; attributes. Therefore, the query only matches against the &#x60;userName&#x60; or &#x60;email&#x60; attributes.  | [optional] 
 **expand** | **str**| An optional query parameter to return the corresponding [User](/openapi/okta-management/management/tag/User/) object in the &#x60;_embedded&#x60; property. Valid value: &#x60;user&#x60; | [optional] 

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

Unassign an application user

Unassigns a user from an app  For directories like Active Directory and LDAP, they act as the owner of the user's credential with Okta delegating authentication (DelAuth) to that directory. If this request is successful for a user when DelAuth is enabled, then the user is in a state with no password. You can then reset the user's password.  > **Important:** This is a destructive operation. You can't recover the user's app profile. If the app is enabled for provisioning and configured to deactivate users, the user is also deactivated in the target app.

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    user_id = '00u13okQOVWZJGDOAUVR' # str | ID of an existing Okta user
    send_email = False # bool | Sends a deactivation email to the administrator if `true` (optional) (default to False)

    try:
        # Unassign an application user
        api_instance.unassign_user_from_application(app_id, user_id, send_email=send_email)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->unassign_user_from_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **user_id** | **str**| ID of an existing Okta user | 
 **send_email** | **bool**| Sends a deactivation email to the administrator if &#x60;true&#x60; | [optional] [default to False]

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

Update an application user

Updates the profile or credentials of a user assigned to an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_user import AppUser
from okta.models.app_user_update_request import AppUserUpdateRequest
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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    user_id = '00u13okQOVWZJGDOAUVR' # str | ID of an existing Okta user
    app_user = okta.AppUserUpdateRequest() # AppUserUpdateRequest | 

    try:
        # Update an application user
        api_response = api_instance.update_application_user(app_id, user_id, app_user)
        print("The response of ApplicationUsersApi->update_application_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationUsersApi->update_application_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **user_id** | **str**| ID of an existing Okta user | 
 **app_user** | [**AppUserUpdateRequest**](AppUserUpdateRequest.md)|  | 

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

