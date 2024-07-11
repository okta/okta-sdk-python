# okta.UserApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UserApi.md#activate_user) | **POST** /api/v1/users/{userId}/lifecycle/activate | Activate a User
[**change_password**](UserApi.md#change_password) | **POST** /api/v1/users/{userId}/credentials/change_password | Change Password
[**change_recovery_question**](UserApi.md#change_recovery_question) | **POST** /api/v1/users/{userId}/credentials/change_recovery_question | Change Recovery Question
[**create_user**](UserApi.md#create_user) | **POST** /api/v1/users | Create a User
[**deactivate_user**](UserApi.md#deactivate_user) | **POST** /api/v1/users/{userId}/lifecycle/deactivate | Deactivate a User
[**delete_linked_object_for_user**](UserApi.md#delete_linked_object_for_user) | **DELETE** /api/v1/users/{userId}/linkedObjects/{relationshipName} | Delete a Linked Object
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/v1/users/{userId} | Delete a User
[**expire_password**](UserApi.md#expire_password) | **POST** /api/v1/users/{userId}/lifecycle/expire_password | Expire Password
[**expire_password_and_get_temporary_password**](UserApi.md#expire_password_and_get_temporary_password) | **POST** /api/v1/users/{userId}/lifecycle/expire_password_with_temp_password | Expire Password and Set Temporary Password
[**forgot_password**](UserApi.md#forgot_password) | **POST** /api/v1/users/{userId}/credentials/forgot_password | Initiate Forgot Password
[**forgot_password_set_new_password**](UserApi.md#forgot_password_set_new_password) | **POST** /api/v1/users/{userId}/credentials/forgot_password_recovery_question | Reset Password with Recovery Question
[**generate_reset_password_token**](UserApi.md#generate_reset_password_token) | **POST** /api/v1/users/{userId}/lifecycle/reset_password | Generate a Reset Password Token
[**get_refresh_token_for_user_and_client**](UserApi.md#get_refresh_token_for_user_and_client) | **GET** /api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId} | Retrieve a Refresh Token for a Client
[**get_user**](UserApi.md#get_user) | **GET** /api/v1/users/{userId} | Retrieve a User
[**get_user_grant**](UserApi.md#get_user_grant) | **GET** /api/v1/users/{userId}/grants/{grantId} | Retrieve a User Grant
[**list_app_links**](UserApi.md#list_app_links) | **GET** /api/v1/users/{userId}/appLinks | List all Assigned Application Links
[**list_grants_for_user_and_client**](UserApi.md#list_grants_for_user_and_client) | **GET** /api/v1/users/{userId}/clients/{clientId}/grants | List all Grants for a Client
[**list_linked_objects_for_user**](UserApi.md#list_linked_objects_for_user) | **GET** /api/v1/users/{userId}/linkedObjects/{relationshipName} | List all Linked Objects
[**list_refresh_tokens_for_user_and_client**](UserApi.md#list_refresh_tokens_for_user_and_client) | **GET** /api/v1/users/{userId}/clients/{clientId}/tokens | List all Refresh Tokens for a Client
[**list_user_blocks**](UserApi.md#list_user_blocks) | **GET** /api/v1/users/{userId}/blocks | List all User Blocks
[**list_user_clients**](UserApi.md#list_user_clients) | **GET** /api/v1/users/{userId}/clients | List all Clients
[**list_user_grants**](UserApi.md#list_user_grants) | **GET** /api/v1/users/{userId}/grants | List all User Grants
[**list_user_groups**](UserApi.md#list_user_groups) | **GET** /api/v1/users/{userId}/groups | List all Groups
[**list_user_identity_providers**](UserApi.md#list_user_identity_providers) | **GET** /api/v1/users/{userId}/idps | List all Identity Providers
[**list_users**](UserApi.md#list_users) | **GET** /api/v1/users | List all Users
[**reactivate_user**](UserApi.md#reactivate_user) | **POST** /api/v1/users/{userId}/lifecycle/reactivate | Reactivate a User
[**replace_user**](UserApi.md#replace_user) | **PUT** /api/v1/users/{userId} | Replace a User
[**reset_factors**](UserApi.md#reset_factors) | **POST** /api/v1/users/{userId}/lifecycle/reset_factors | Reset all Factors
[**revoke_grants_for_user_and_client**](UserApi.md#revoke_grants_for_user_and_client) | **DELETE** /api/v1/users/{userId}/clients/{clientId}/grants | Revoke all Grants for a Client
[**revoke_token_for_user_and_client**](UserApi.md#revoke_token_for_user_and_client) | **DELETE** /api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId} | Revoke a Token for a Client
[**revoke_tokens_for_user_and_client**](UserApi.md#revoke_tokens_for_user_and_client) | **DELETE** /api/v1/users/{userId}/clients/{clientId}/tokens | Revoke all Refresh Tokens for a Client
[**revoke_user_grant**](UserApi.md#revoke_user_grant) | **DELETE** /api/v1/users/{userId}/grants/{grantId} | Revoke a User Grant
[**revoke_user_grants**](UserApi.md#revoke_user_grants) | **DELETE** /api/v1/users/{userId}/grants | Revoke all User Grants
[**revoke_user_sessions**](UserApi.md#revoke_user_sessions) | **DELETE** /api/v1/users/{userId}/sessions | Revoke all User Sessions
[**set_linked_object_for_user**](UserApi.md#set_linked_object_for_user) | **PUT** /api/v1/users/{userId}/linkedObjects/{primaryRelationshipName}/{primaryUserId} | Create a Linked Object for two Users
[**suspend_user**](UserApi.md#suspend_user) | **POST** /api/v1/users/{userId}/lifecycle/suspend | Suspend a User
[**unlock_user**](UserApi.md#unlock_user) | **POST** /api/v1/users/{userId}/lifecycle/unlock | Unlock a User
[**unsuspend_user**](UserApi.md#unsuspend_user) | **POST** /api/v1/users/{userId}/lifecycle/unsuspend | Unsuspend a User
[**update_user**](UserApi.md#update_user) | **POST** /api/v1/users/{userId} | Update a User


# **activate_user**
> UserActivationToken activate_user(user_id, send_email)

Activate a User

Activates a user. This operation can only be performed on users with a `STAGED` or `DEPROVISIONED` status. Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation. The user will have a status of `ACTIVE` when the activation process is complete. > **Multibrand and User activation**<br> If you want to send a branded User Activation email, change the subdomain of your request to the custom domain that's associated with the brand. For example, change `subdomain.okta.com` to `custom.domain.one`. See [Multibrand and custom domains](https://developer.okta.com/docs/concepts/brands/#multibrand-and-custom-domains). <br><br> > **Legal disclaimer**<br> After a user is added to the Okta directory, they receive an activation email. As part of signing up for this service, you agreed not to use Okta's service/product to spam and/or send unsolicited messages. Please refrain from adding unrelated accounts to the directory as Okta is not responsible for, and disclaims any and all liability associated with, the activation email's content. You, and you alone, bear responsibility for the emails sent to any recipients.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_activation_token import UserActivationToken
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    send_email = True # bool | Sends an activation email to the user if true (default to True)

    try:
        # Activate a User
        api_response = api_instance.activate_user(user_id, send_email)
        print("The response of UserApi->activate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->activate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**| Sends an activation email to the user if true | [default to True]

### Return type

[**UserActivationToken**](UserActivationToken.md)

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

# **change_password**
> UserCredentials change_password(user_id, change_password_request, strict=strict)

Change Password

Changes a user's password by validating the user's current password. This operation can only be performed on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid password credential

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.change_password_request import ChangePasswordRequest
from okta.models.user_credentials import UserCredentials
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    change_password_request = okta.ChangePasswordRequest() # ChangePasswordRequest | 
    strict = True # bool |  (optional)

    try:
        # Change Password
        api_response = api_instance.change_password(user_id, change_password_request, strict=strict)
        print("The response of UserApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 
 **strict** | **bool**|  | [optional] 

### Return type

[**UserCredentials**](UserCredentials.md)

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

# **change_recovery_question**
> UserCredentials change_recovery_question(user_id, user_credentials)

Change Recovery Question

Changes a user's recovery question & answer credential by validating the user's current password.  This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** `status` that have a valid password credential

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_credentials import UserCredentials
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    user_credentials = okta.UserCredentials() # UserCredentials | 

    try:
        # Change Recovery Question
        api_response = api_instance.change_recovery_question(user_id, user_credentials)
        print("The response of UserApi->change_recovery_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->change_recovery_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_credentials** | [**UserCredentials**](UserCredentials.md)|  | 

### Return type

[**UserCredentials**](UserCredentials.md)

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

# **create_user**
> User create_user(body, activate=activate, provider=provider, next_login=next_login)

Create a User

Creates a new user in your Okta organization with or without credentials<br> > **Legal Disclaimer**<br> After a user is added to the Okta directory, they receive an activation email. As part of signing up for this service, you agreed not to use Okta's service/product to spam and/or send unsolicited messages. Please refrain from adding unrelated accounts to the directory as Okta is not responsible for, and disclaims any and all liability associated with, the activation email's content. You, and you alone, bear responsibility for the emails sent to any recipients.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_user_request import CreateUserRequest
from okta.models.user import User
from okta.models.user_next_login import UserNextLogin
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
    api_instance = okta.UserApi(api_client)
    body = okta.CreateUserRequest() # CreateUserRequest | 
    activate = True # bool | Executes activation lifecycle operation when creating the user (optional) (default to True)
    provider = False # bool | Indicates whether to create a user with a specified authentication provider (optional) (default to False)
    next_login = okta.UserNextLogin() # UserNextLogin | With activate=true, set nextLogin to \"changePassword\" to have the password be EXPIRED, so user must change it the next time they log in. (optional)

    try:
        # Create a User
        api_response = api_instance.create_user(body, activate=activate, provider=provider, next_login=next_login)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **activate** | **bool**| Executes activation lifecycle operation when creating the user | [optional] [default to True]
 **provider** | **bool**| Indicates whether to create a user with a specified authentication provider | [optional] [default to False]
 **next_login** | [**UserNextLogin**](.md)| With activate&#x3D;true, set nextLogin to \&quot;changePassword\&quot; to have the password be EXPIRED, so user must change it the next time they log in. | [optional] 

### Return type

[**User**](User.md)

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

# **deactivate_user**
> deactivate_user(user_id, send_email=send_email)

Deactivate a User

Deactivates a user. This operation can only be performed on users that do not have a `DEPROVISIONED` status. While the asynchronous operation (triggered by HTTP header `Prefer: respond-async`) is proceeding the user's `transitioningToStatus` property is `DEPROVISIONED`. The user's status is `DEPROVISIONED` when the deactivation process is complete.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    send_email = False # bool |  (optional) (default to False)

    try:
        # Deactivate a User
        api_instance.deactivate_user(user_id, send_email=send_email)
    except Exception as e:
        print("Exception when calling UserApi->deactivate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_object_for_user**
> delete_linked_object_for_user(user_id, relationship_name)

Delete a Linked Object

Deletes linked objects for a user, relationshipName can be ONLY a primary relationship name

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    relationship_name = 'relationship_name_example' # str | 

    try:
        # Delete a Linked Object
        api_instance.delete_linked_object_for_user(user_id, relationship_name)
    except Exception as e:
        print("Exception when calling UserApi->delete_linked_object_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **relationship_name** | **str**|  | 

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

# **delete_user**
> delete_user(user_id, send_email=send_email)

Delete a User

Deletes a user permanently. This operation can only be performed on users that have a `DEPROVISIONED` status.  **This action cannot be recovered!**. Calling this on an `ACTIVE` user will transition the user to `DEPROVISIONED`.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    send_email = False # bool |  (optional) (default to False)

    try:
        # Delete a User
        api_instance.delete_user(user_id, send_email=send_email)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_password**
> User expire_password(user_id)

Expire Password

Expires a user's password and transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user import User
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Expire Password
        api_response = api_instance.expire_password(user_id)
        print("The response of UserApi->expire_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->expire_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**User**](User.md)

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

# **expire_password_and_get_temporary_password**
> TempPassword expire_password_and_get_temporary_password(user_id, revoke_sessions=revoke_sessions)

Expire Password and Set Temporary Password

Expires a user's password and transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login, and also sets the user's password to a temporary password returned in the response

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.temp_password import TempPassword
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    revoke_sessions = False # bool | When set to `true` (and the session is a user session), all user sessions are revoked except the current session. (optional) (default to False)

    try:
        # Expire Password and Set Temporary Password
        api_response = api_instance.expire_password_and_get_temporary_password(user_id, revoke_sessions=revoke_sessions)
        print("The response of UserApi->expire_password_and_get_temporary_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->expire_password_and_get_temporary_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **revoke_sessions** | **bool**| When set to &#x60;true&#x60; (and the session is a user session), all user sessions are revoked except the current session. | [optional] [default to False]

### Return type

[**TempPassword**](TempPassword.md)

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

# **forgot_password**
> ForgotPasswordResponse forgot_password(user_id, send_email=send_email)

Initiate Forgot Password

Initiates the forgot password flow. Generates a one-time token (OTT) that can be used to reset a user's password.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.forgot_password_response import ForgotPasswordResponse
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    send_email = True # bool |  (optional) (default to True)

    try:
        # Initiate Forgot Password
        api_response = api_instance.forgot_password(user_id, send_email=send_email)
        print("The response of UserApi->forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->forgot_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | [optional] [default to True]

### Return type

[**ForgotPasswordResponse**](ForgotPasswordResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset url |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password_set_new_password**
> UserCredentials forgot_password_set_new_password(user_id, user_credentials, send_email=send_email)

Reset Password with Recovery Question

Resets the user's password to the specified password if the provided answer to the recovery question is correct

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_credentials import UserCredentials
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    user_credentials = okta.UserCredentials() # UserCredentials | 
    send_email = True # bool |  (optional) (default to True)

    try:
        # Reset Password with Recovery Question
        api_response = api_instance.forgot_password_set_new_password(user_id, user_credentials, send_email=send_email)
        print("The response of UserApi->forgot_password_set_new_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->forgot_password_set_new_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_credentials** | [**UserCredentials**](UserCredentials.md)|  | 
 **send_email** | **bool**|  | [optional] [default to True]

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credentials |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_reset_password_token**
> ResetPasswordToken generate_reset_password_token(user_id, send_email, revoke_sessions=revoke_sessions)

Generate a Reset Password Token

Generates a one-time token (OTT) that can be used to reset a user's password.  The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.reset_password_token import ResetPasswordToken
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    send_email = True # bool | 
    revoke_sessions = False # bool | When set to `true` (and the session is a user session), all user sessions are revoked except the current session. (optional) (default to False)

    try:
        # Generate a Reset Password Token
        api_response = api_instance.generate_reset_password_token(user_id, send_email, revoke_sessions=revoke_sessions)
        print("The response of UserApi->generate_reset_password_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->generate_reset_password_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | 
 **revoke_sessions** | **bool**| When set to &#x60;true&#x60; (and the session is a user session), all user sessions are revoked except the current session. | [optional] [default to False]

### Return type

[**ResetPasswordToken**](ResetPasswordToken.md)

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

# **get_refresh_token_for_user_and_client**
> OAuth2RefreshToken get_refresh_token_for_user_and_client(user_id, client_id, token_id, expand=expand, limit=limit, after=after)

Retrieve a Refresh Token for a Client

Retrieves a refresh token issued for the specified User and Client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token
    expand = 'expand_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)
    after = 'after_example' # str |  (optional)

    try:
        # Retrieve a Refresh Token for a Client
        api_response = api_instance.get_refresh_token_for_user_and_client(user_id, client_id, token_id, expand=expand, limit=limit, after=after)
        print("The response of UserApi->get_refresh_token_for_user_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_refresh_token_for_user_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **after** | **str**|  | [optional] 

### Return type

[**OAuth2RefreshToken**](OAuth2RefreshToken.md)

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

# **get_user**
> User get_user(user_id)

Retrieve a User

Retrieves a user from your Okta organization

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user import User
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Retrieve a User
        api_response = api_instance.get_user(user_id)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**User**](User.md)

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

# **get_user_grant**
> OAuth2ScopeConsentGrant get_user_grant(user_id, grant_id, expand=expand)

Retrieve a User Grant

Retrieves a grant for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    grant_id = 'iJoqkwx50mrgX4T9LcaH' # str | ID of the Grant
    expand = 'expand_example' # str |  (optional)

    try:
        # Retrieve a User Grant
        api_response = api_instance.get_user_grant(user_id, grant_id, expand=expand)
        print("The response of UserApi->get_user_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **grant_id** | **str**| ID of the Grant | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)

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

# **list_app_links**
> List[AppLink] list_app_links(user_id)

List all Assigned Application Links

Lists all appLinks for all direct or indirect (via group membership) assigned applications

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.app_link import AppLink
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Assigned Application Links
        api_response = api_instance.list_app_links(user_id)
        print("The response of UserApi->list_app_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_app_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[AppLink]**](AppLink.md)

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

# **list_grants_for_user_and_client**
> List[OAuth2ScopeConsentGrant] list_grants_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)

List all Grants for a Client

Lists all grants for a specified user and client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    expand = 'expand_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Grants for a Client
        api_response = api_instance.list_grants_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)
        print("The response of UserApi->list_grants_for_user_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_grants_for_user_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**List[OAuth2ScopeConsentGrant]**](OAuth2ScopeConsentGrant.md)

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

# **list_linked_objects_for_user**
> List[object] list_linked_objects_for_user(user_id, relationship_name, after=after, limit=limit)

List all Linked Objects

Lists all linked objects for a user, relationshipName can be a primary or associated relationship name

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    relationship_name = 'relationship_name_example' # str | 
    after = 'after_example' # str |  (optional)
    limit = -1 # int |  (optional) (default to -1)

    try:
        # List all Linked Objects
        api_response = api_instance.list_linked_objects_for_user(user_id, relationship_name, after=after, limit=limit)
        print("The response of UserApi->list_linked_objects_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_linked_objects_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **relationship_name** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

**List[object]**

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

# **list_refresh_tokens_for_user_and_client**
> List[OAuth2RefreshToken] list_refresh_tokens_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)

List all Refresh Tokens for a Client

Lists all refresh tokens issued for the specified User and Client

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    expand = 'expand_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Refresh Tokens for a Client
        api_response = api_instance.list_refresh_tokens_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)
        print("The response of UserApi->list_refresh_tokens_for_user_and_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_refresh_tokens_for_user_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**List[OAuth2RefreshToken]**](OAuth2RefreshToken.md)

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

# **list_user_blocks**
> List[UserBlock] list_user_blocks(user_id)

List all User Blocks

Lists information about how the user is blocked from accessing their account

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_block import UserBlock
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all User Blocks
        api_response = api_instance.list_user_blocks(user_id)
        print("The response of UserApi->list_user_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[UserBlock]**](UserBlock.md)

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

# **list_user_clients**
> List[OAuth2Client] list_user_clients(user_id)

List all Clients

Lists all client resources for which the specified user has grants or tokens

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client import OAuth2Client
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Clients
        api_response = api_instance.list_user_clients(user_id)
        print("The response of UserApi->list_user_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[OAuth2Client]**](OAuth2Client.md)

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

# **list_user_grants**
> List[OAuth2ScopeConsentGrant] list_user_grants(user_id, scope_id=scope_id, expand=expand, after=after, limit=limit)

List all User Grants

Lists all grants for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    scope_id = 'scope_id_example' # str |  (optional)
    expand = 'expand_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all User Grants
        api_response = api_instance.list_user_grants(user_id, scope_id=scope_id, expand=expand, after=after, limit=limit)
        print("The response of UserApi->list_user_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **scope_id** | **str**|  | [optional] 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**List[OAuth2ScopeConsentGrant]**](OAuth2ScopeConsentGrant.md)

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

# **list_user_groups**
> List[Group] list_user_groups(user_id)

List all Groups

Lists all groups of which the user is a member

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Groups
        api_response = api_instance.list_user_groups(user_id)
        print("The response of UserApi->list_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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

# **list_user_identity_providers**
> List[IdentityProvider] list_user_identity_providers(user_id)

List all Identity Providers

Lists the IdPs associated with the user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_provider import IdentityProvider
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # List all Identity Providers
        api_response = api_instance.list_user_identity_providers(user_id)
        print("The response of UserApi->list_user_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**List[IdentityProvider]**](IdentityProvider.md)

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

# **list_users**
> List[User] list_users(q=q, after=after, limit=limit, filter=filter, search=search, sort_by=sort_by, sort_order=sort_order)

List all Users

Lists all users that do not have a status of 'DEPROVISIONED' (by default), up to the maximum (200 for most orgs), with pagination.  A subset of users can be returned that match a supported filter expression or search criteria.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user import User
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
    api_instance = okta.UserApi(api_client)
    q = 'q_example' # str | Finds a user that matches firstName, lastName, and email properties (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](/#pagination) for more information. (optional)
    limit = 200 # int | Specifies the number of results returned. Defaults to 10 if `q` is provided. (optional) (default to 200)
    filter = 'filter_example' # str | Filters users with a supported expression for a subset of properties (optional)
    search = 'search_example' # str | Searches for users with a supported filtering expression for most properties. Okta recommends using this parameter for search for best performance. (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_order = 'sort_order_example' # str | Sorting is done in ASCII sort order (that is, by ASCII character value), but isn't case sensitive. (optional)

    try:
        # List all Users
        api_response = api_instance.list_users(q=q, after=after, limit=limit, filter=filter, search=search, sort_by=sort_by, sort_order=sort_order)
        print("The response of UserApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Finds a user that matches firstName, lastName, and email properties | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](/#pagination) for more information. | [optional] 
 **limit** | **int**| Specifies the number of results returned. Defaults to 10 if &#x60;q&#x60; is provided. | [optional] [default to 200]
 **filter** | **str**| Filters users with a supported expression for a subset of properties | [optional] 
 **search** | **str**| Searches for users with a supported filtering expression for most properties. Okta recommends using this parameter for search for best performance. | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**| Sorting is done in ASCII sort order (that is, by ASCII character value), but isn&#39;t case sensitive. | [optional] 

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_user**
> UserActivationToken reactivate_user(user_id, send_email=send_email)

Reactivate a User

Reactivates a user.  This operation can only be performed on users with a `PROVISIONED` status.  This operation restarts the activation workflow if for some reason the user activation was not completed when using the activationToken from [Activate User](#activate-user).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_activation_token import UserActivationToken
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    send_email = False # bool | Sends an activation email to the user if true (optional) (default to False)

    try:
        # Reactivate a User
        api_response = api_instance.reactivate_user(user_id, send_email=send_email)
        print("The response of UserApi->reactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->reactivate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**| Sends an activation email to the user if true | [optional] [default to False]

### Return type

[**UserActivationToken**](UserActivationToken.md)

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

# **replace_user**
> User replace_user(user_id, user, strict=strict)

Replace a User

Replaces a user's profile and/or credentials using strict-update semantics

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user import User
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    user = okta.User() # User | 
    strict = True # bool |  (optional)

    try:
        # Replace a User
        api_response = api_instance.replace_user(user_id, user, strict=strict)
        print("The response of UserApi->replace_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->replace_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user** | [**User**](User.md)|  | 
 **strict** | **bool**|  | [optional] 

### Return type

[**User**](User.md)

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

# **reset_factors**
> reset_factors(user_id)

Reset all Factors

Resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user's status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Reset all Factors
        api_instance.reset_factors(user_id)
    except Exception as e:
        print("Exception when calling UserApi->reset_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_grants_for_user_and_client**
> revoke_grants_for_user_and_client(user_id, client_id)

Revoke all Grants for a Client

Revokes all grants for the specified user and client

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app

    try:
        # Revoke all Grants for a Client
        api_instance.revoke_grants_for_user_and_client(user_id, client_id)
    except Exception as e:
        print("Exception when calling UserApi->revoke_grants_for_user_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 

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

# **revoke_token_for_user_and_client**
> revoke_token_for_user_and_client(user_id, client_id, token_id)

Revoke a Token for a Client

Revokes the specified refresh token

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token

    try:
        # Revoke a Token for a Client
        api_instance.revoke_token_for_user_and_client(user_id, client_id, token_id)
    except Exception as e:
        print("Exception when calling UserApi->revoke_token_for_user_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 

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

# **revoke_tokens_for_user_and_client**
> revoke_tokens_for_user_and_client(user_id, client_id)

Revoke all Refresh Tokens for a Client

Revokes all refresh tokens issued for the specified User and Client

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    client_id = '52Uy4BUWVBOjFItcg2jWsmnd83Ad8dD' # str | `client_id` of the app

    try:
        # Revoke all Refresh Tokens for a Client
        api_instance.revoke_tokens_for_user_and_client(user_id, client_id)
    except Exception as e:
        print("Exception when calling UserApi->revoke_tokens_for_user_and_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**| &#x60;client_id&#x60; of the app | 

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

# **revoke_user_grant**
> revoke_user_grant(user_id, grant_id)

Revoke a User Grant

Revokes one grant for a specified user

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    grant_id = 'iJoqkwx50mrgX4T9LcaH' # str | ID of the Grant

    try:
        # Revoke a User Grant
        api_instance.revoke_user_grant(user_id, grant_id)
    except Exception as e:
        print("Exception when calling UserApi->revoke_user_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **grant_id** | **str**| ID of the Grant | 

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

# **revoke_user_grants**
> revoke_user_grants(user_id)

Revoke all User Grants

Revokes all grants for a specified user

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Revoke all User Grants
        api_instance.revoke_user_grants(user_id)
    except Exception as e:
        print("Exception when calling UserApi->revoke_user_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **revoke_user_sessions**
> revoke_user_sessions(user_id, oauth_tokens=oauth_tokens)

Revoke all User Sessions

Revokes all active identity provider sessions of the user. This forces the user to authenticate on the next operation. Optionally revokes OpenID Connect and OAuth refresh and access tokens issued to the user.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    oauth_tokens = False # bool | Revoke issued OpenID Connect and OAuth refresh and access tokens (optional) (default to False)

    try:
        # Revoke all User Sessions
        api_instance.revoke_user_sessions(user_id, oauth_tokens=oauth_tokens)
    except Exception as e:
        print("Exception when calling UserApi->revoke_user_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **oauth_tokens** | **bool**| Revoke issued OpenID Connect and OAuth refresh and access tokens | [optional] [default to False]

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

# **set_linked_object_for_user**
> set_linked_object_for_user(user_id, primary_relationship_name, primary_user_id)

Create a Linked Object for two Users

Creates a Linked Object for two users

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    primary_relationship_name = 'primary_relationship_name_example' # str | 
    primary_user_id = 'ctxeQ5JnAVdGFBB7Zr7W' # str | `id` of primary User

    try:
        # Create a Linked Object for two Users
        api_instance.set_linked_object_for_user(user_id, primary_relationship_name, primary_user_id)
    except Exception as e:
        print("Exception when calling UserApi->set_linked_object_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **primary_relationship_name** | **str**|  | 
 **primary_user_id** | **str**| &#x60;id&#x60; of primary User | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_user**
> suspend_user(user_id)

Suspend a User

Suspends a user.  This operation can only be performed on users with an `ACTIVE` status.  The user will have a status of `SUSPENDED` when the process is complete.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Suspend a User
        api_instance.suspend_user(user_id)
    except Exception as e:
        print("Exception when calling UserApi->suspend_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> unlock_user(user_id)

Unlock a User

Unlocks a user with a `LOCKED_OUT` status or unlocks a user with an `ACTIVE` status that is blocked from unknown devices. Unlocked users have an `ACTIVE` status and can sign in with their current password.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Unlock a User
        api_instance.unlock_user(user_id)
    except Exception as e:
        print("Exception when calling UserApi->unlock_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuspend_user**
> unsuspend_user(user_id)

Unsuspend a User

Unsuspends a user and returns them to the `ACTIVE` state.  This operation can only be performed on users that have a `SUSPENDED` status.

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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Unsuspend a User
        api_instance.unsuspend_user(user_id)
    except Exception as e:
        print("Exception when calling UserApi->unsuspend_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, user, strict=strict)

Update a User

Updates a user partially determined by the request parameters

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.update_user_request import UpdateUserRequest
from okta.models.user import User
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
    api_instance = okta.UserApi(api_client)
    user_id = 'user_id_example' # str | 
    user = okta.UpdateUserRequest() # UpdateUserRequest | 
    strict = True # bool |  (optional)

    try:
        # Update a User
        api_response = api_instance.update_user(user_id, user, strict=strict)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **strict** | **bool**|  | [optional] 

### Return type

[**User**](User.md)

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

