# swagger_client.UserApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UserApi.md#activate_user) | **POST** /api/v1/users/{userId}/lifecycle/activate | Activate User
[**add_all_apps_as_target_to_role**](UserApi.md#add_all_apps_as_target_to_role) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps | 
[**add_application_target_to_admin_role_for_user**](UserApi.md#add_application_target_to_admin_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName} | 
[**add_application_target_to_app_admin_role_for_user**](UserApi.md#add_application_target_to_app_admin_role_for_user) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId} | Add App Instance Target to App Administrator Role given to a User
[**add_group_target_to_role**](UserApi.md#add_group_target_to_role) | **PUT** /api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId} | 
[**assign_role_to_user**](UserApi.md#assign_role_to_user) | **POST** /api/v1/users/{userId}/roles | 
[**change_password**](UserApi.md#change_password) | **POST** /api/v1/users/{userId}/credentials/change_password | Change Password
[**change_recovery_question**](UserApi.md#change_recovery_question) | **POST** /api/v1/users/{userId}/credentials/change_recovery_question | Change Recovery Question
[**clear_user_sessions**](UserApi.md#clear_user_sessions) | **DELETE** /api/v1/users/{userId}/sessions | 
[**create_user**](UserApi.md#create_user) | **POST** /api/v1/users | Create User
[**deactivate_or_delete_user**](UserApi.md#deactivate_or_delete_user) | **DELETE** /api/v1/users/{userId} | Delete User
[**deactivate_user**](UserApi.md#deactivate_user) | **POST** /api/v1/users/{userId}/lifecycle/deactivate | Deactivate User
[**expire_password**](UserApi.md#expire_password) | **POST** /api/v1/users/{userId}/lifecycle/expire_password | Expire Password
[**expire_password_and_get_temporary_password**](UserApi.md#expire_password_and_get_temporary_password) | **POST** /api/v1/users/{userId}/lifecycle/expire_password_with_temp_password | Expire Password and Set Temporary Password
[**forgot_password**](UserApi.md#forgot_password) | **POST** /api/v1/users/{userId}/credentials/forgot_password | Initiate Forgot Password
[**forgot_password_set_new_password**](UserApi.md#forgot_password_set_new_password) | **POST** /api/v1/users/{userId}/credentials/forgot_password_recovery_question | Reset Password with Recovery Question
[**get_linked_objects_for_user**](UserApi.md#get_linked_objects_for_user) | **GET** /api/v1/users/{userId}/linkedObjects/{relationshipName} | 
[**get_refresh_token_for_user_and_client**](UserApi.md#get_refresh_token_for_user_and_client) | **GET** /api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId} | 
[**get_user**](UserApi.md#get_user) | **GET** /api/v1/users/{userId} | Get User
[**get_user_grant**](UserApi.md#get_user_grant) | **GET** /api/v1/users/{userId}/grants/{grantId} | 
[**get_user_role**](UserApi.md#get_user_role) | **GET** /api/v1/users/{userId}/roles/{roleId} | 
[**list_app_links**](UserApi.md#list_app_links) | **GET** /api/v1/users/{userId}/appLinks | Get Assigned App Links
[**list_application_targets_for_application_administrator_role_for_user**](UserApi.md#list_application_targets_for_application_administrator_role_for_user) | **GET** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps | 
[**list_assigned_roles_for_user**](UserApi.md#list_assigned_roles_for_user) | **GET** /api/v1/users/{userId}/roles | 
[**list_grants_for_user_and_client**](UserApi.md#list_grants_for_user_and_client) | **GET** /api/v1/users/{userId}/clients/{clientId}/grants | 
[**list_group_targets_for_role**](UserApi.md#list_group_targets_for_role) | **GET** /api/v1/users/{userId}/roles/{roleId}/targets/groups | 
[**list_refresh_tokens_for_user_and_client**](UserApi.md#list_refresh_tokens_for_user_and_client) | **GET** /api/v1/users/{userId}/clients/{clientId}/tokens | 
[**list_user_clients**](UserApi.md#list_user_clients) | **GET** /api/v1/users/{userId}/clients | 
[**list_user_grants**](UserApi.md#list_user_grants) | **GET** /api/v1/users/{userId}/grants | 
[**list_user_groups**](UserApi.md#list_user_groups) | **GET** /api/v1/users/{userId}/groups | Get Member Groups
[**list_user_identity_providers**](UserApi.md#list_user_identity_providers) | **GET** /api/v1/users/{userId}/idps | Listing IdPs associated with a user
[**list_users**](UserApi.md#list_users) | **GET** /api/v1/users | List Users
[**partial_update_user**](UserApi.md#partial_update_user) | **POST** /api/v1/users/{userId} | 
[**reactivate_user**](UserApi.md#reactivate_user) | **POST** /api/v1/users/{userId}/lifecycle/reactivate | Reactivate User
[**remove_application_target_from_administrator_role_for_user**](UserApi.md#remove_application_target_from_administrator_role_for_user) | **DELETE** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId} | Remove App Instance Target to App Administrator Role given to a User
[**remove_application_target_from_application_administrator_role_for_user**](UserApi.md#remove_application_target_from_application_administrator_role_for_user) | **DELETE** /api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName} | 
[**remove_group_target_from_role**](UserApi.md#remove_group_target_from_role) | **DELETE** /api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId} | 
[**remove_linked_object_for_user**](UserApi.md#remove_linked_object_for_user) | **DELETE** /api/v1/users/{userId}/linkedObjects/{relationshipName} | 
[**remove_role_from_user**](UserApi.md#remove_role_from_user) | **DELETE** /api/v1/users/{userId}/roles/{roleId} | 
[**reset_factors**](UserApi.md#reset_factors) | **POST** /api/v1/users/{userId}/lifecycle/reset_factors | Reset Factors
[**reset_password**](UserApi.md#reset_password) | **POST** /api/v1/users/{userId}/lifecycle/reset_password | Reset Password
[**revoke_grants_for_user_and_client**](UserApi.md#revoke_grants_for_user_and_client) | **DELETE** /api/v1/users/{userId}/clients/{clientId}/grants | 
[**revoke_token_for_user_and_client**](UserApi.md#revoke_token_for_user_and_client) | **DELETE** /api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId} | 
[**revoke_tokens_for_user_and_client**](UserApi.md#revoke_tokens_for_user_and_client) | **DELETE** /api/v1/users/{userId}/clients/{clientId}/tokens | 
[**revoke_user_grant**](UserApi.md#revoke_user_grant) | **DELETE** /api/v1/users/{userId}/grants/{grantId} | 
[**revoke_user_grants**](UserApi.md#revoke_user_grants) | **DELETE** /api/v1/users/{userId}/grants | 
[**set_linked_object_for_user**](UserApi.md#set_linked_object_for_user) | **PUT** /api/v1/users/{associatedUserId}/linkedObjects/{primaryRelationshipName}/{primaryUserId} | Set Linked Object for User
[**suspend_user**](UserApi.md#suspend_user) | **POST** /api/v1/users/{userId}/lifecycle/suspend | Suspend User
[**unlock_user**](UserApi.md#unlock_user) | **POST** /api/v1/users/{userId}/lifecycle/unlock | Unlock User
[**unsuspend_user**](UserApi.md#unsuspend_user) | **POST** /api/v1/users/{userId}/lifecycle/unsuspend | Unsuspend User
[**update_user**](UserApi.md#update_user) | **PUT** /api/v1/users/{userId} | Update User

# **activate_user**
> UserActivationToken activate_user(user_id, send_email)

Activate User

Activates a user.  This operation can only be performed on users with a `STAGED` status.  Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `ACTIVE` when the activation process is complete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
send_email = true # bool | Sends an activation email to the user if true (default to true)

try:
    # Activate User
    api_response = api_instance.activate_user(user_id, send_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->activate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**| Sends an activation email to the user if true | [default to true]

### Return type

[**UserActivationToken**](UserActivationToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_all_apps_as_target_to_role**
> add_all_apps_as_target_to_role(user_id, role_id)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    api_instance.add_all_apps_as_target_to_role(user_id, role_id)
except ApiException as e:
    print("Exception when calling UserApi->add_all_apps_as_target_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_target_to_admin_role_for_user**
> add_application_target_to_admin_role_for_user(user_id, role_id, app_name)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 

try:
    api_instance.add_application_target_to_admin_role_for_user(user_id, role_id, app_name)
except ApiException as e:
    print("Exception when calling UserApi->add_application_target_to_admin_role_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_target_to_app_admin_role_for_user**
> add_application_target_to_app_admin_role_for_user(user_id, role_id, app_name, application_id)

Add App Instance Target to App Administrator Role given to a User

Add App Instance Target to App Administrator Role given to a User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 
application_id = 'application_id_example' # str | 

try:
    # Add App Instance Target to App Administrator Role given to a User
    api_instance.add_application_target_to_app_admin_role_for_user(user_id, role_id, app_name, application_id)
except ApiException as e:
    print("Exception when calling UserApi->add_application_target_to_app_admin_role_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_target_to_role**
> add_group_target_to_role(user_id, role_id, group_id)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
group_id = 'group_id_example' # str | 

try:
    api_instance.add_group_target_to_role(user_id, role_id, group_id)
except ApiException as e:
    print("Exception when calling UserApi->add_group_target_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_role_to_user**
> Role assign_role_to_user(body, user_id, disable_notifications=disable_notifications)



Assigns a role to a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.AssignRoleRequest() # AssignRoleRequest | 
user_id = 'user_id_example' # str | 
disable_notifications = 'disable_notifications_example' # str |  (optional)

try:
    api_response = api_instance.assign_role_to_user(body, user_id, disable_notifications=disable_notifications)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->assign_role_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 
 **user_id** | **str**|  | 
 **disable_notifications** | **str**|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> UserCredentials change_password(body, user_id, strict=strict)

Change Password

Changes a user's password by validating the user's current password. This operation can only be performed on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid password credential

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangePasswordRequest() # ChangePasswordRequest | 
user_id = 'user_id_example' # str | 
strict = true # bool |  (optional)

try:
    # Change Password
    api_response = api_instance.change_password(body, user_id, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 
 **user_id** | **str**|  | 
 **strict** | **bool**|  | [optional] 

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_recovery_question**
> UserCredentials change_recovery_question(body, user_id)

Change Recovery Question

Changes a user's recovery question & answer credential by validating the user's current password.  This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** `status` that have a valid password credential

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCredentials() # UserCredentials | 
user_id = 'user_id_example' # str | 

try:
    # Change Recovery Question
    api_response = api_instance.change_recovery_question(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->change_recovery_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCredentials**](UserCredentials.md)|  | 
 **user_id** | **str**|  | 

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_user_sessions**
> clear_user_sessions(user_id, oauth_tokens=oauth_tokens)



Removes all active identity provider sessions. This forces the user to authenticate on the next operation. Optionally revokes OpenID Connect and OAuth refresh and access tokens issued to the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
oauth_tokens = false # bool | Revoke issued OpenID Connect and OAuth refresh and access tokens (optional) (default to false)

try:
    api_instance.clear_user_sessions(user_id, oauth_tokens=oauth_tokens)
except ApiException as e:
    print("Exception when calling UserApi->clear_user_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **oauth_tokens** | **bool**| Revoke issued OpenID Connect and OAuth refresh and access tokens | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(body, activate=activate, provider=provider, next_login=next_login)

Create User

Creates a new user in your Okta organization with or without credentials.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateUserRequest() # CreateUserRequest | 
activate = true # bool | Executes activation lifecycle operation when creating the user (optional) (default to true)
provider = false # bool | Indicates whether to create a user with a specified authentication provider (optional) (default to false)
next_login = swagger_client.UserNextLogin() # UserNextLogin | With activate=true, set nextLogin to \"changePassword\" to have the password be EXPIRED, so user must change it the next time they log in. (optional)

try:
    # Create User
    api_response = api_instance.create_user(body, activate=activate, provider=provider, next_login=next_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **activate** | **bool**| Executes activation lifecycle operation when creating the user | [optional] [default to true]
 **provider** | **bool**| Indicates whether to create a user with a specified authentication provider | [optional] [default to false]
 **next_login** | [**UserNextLogin**](.md)| With activate&#x3D;true, set nextLogin to \&quot;changePassword\&quot; to have the password be EXPIRED, so user must change it the next time they log in. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_or_delete_user**
> deactivate_or_delete_user(user_id, send_email=send_email)

Delete User

Deletes a user permanently.  This operation can only be performed on users that have a `DEPROVISIONED` status.  **This action cannot be recovered!**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
send_email = false # bool |  (optional) (default to false)

try:
    # Delete User
    api_instance.deactivate_or_delete_user(user_id, send_email=send_email)
except ApiException as e:
    print("Exception when calling UserApi->deactivate_or_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_user**
> deactivate_user(user_id, send_email=send_email)

Deactivate User

Deactivates a user.  This operation can only be performed on users that do not have a `DEPROVISIONED` status.  Deactivation of a user is an asynchronous operation.  The user will have the `transitioningToStatus` property with a value of `DEPROVISIONED` during deactivation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `DEPROVISIONED` when the deactivation process is complete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
send_email = false # bool |  (optional) (default to false)

try:
    # Deactivate User
    api_instance.deactivate_user(user_id, send_email=send_email)
except ApiException as e:
    print("Exception when calling UserApi->deactivate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_password**
> User expire_password(user_id)

Expire Password

This operation transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Expire Password
    api_response = api_instance.expire_password(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->expire_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_password_and_get_temporary_password**
> TempPassword expire_password_and_get_temporary_password(user_id)

Expire Password and Set Temporary Password

This operation transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login, and also sets the user's password to a temporary password returned in the response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Expire Password and Set Temporary Password
    api_response = api_instance.expire_password_and_get_temporary_password(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->expire_password_and_get_temporary_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**TempPassword**](TempPassword.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password**
> ForgotPasswordResponse forgot_password(user_id, send_email=send_email)

Initiate Forgot Password

Initiate forgot password flow. Generates a one-time token (OTT) that can be used to reset a user's password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
send_email = true # bool |  (optional) (default to true)

try:
    # Initiate Forgot Password
    api_response = api_instance.forgot_password(user_id, send_email=send_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->forgot_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | [optional] [default to true]

### Return type

[**ForgotPasswordResponse**](ForgotPasswordResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password_set_new_password**
> UserCredentials forgot_password_set_new_password(user_id, body=body, send_email=send_email)

Reset Password with Recovery Question

Resets the user's password to the specified password if the provided answer to the recovery question is correct.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = swagger_client.UserCredentials() # UserCredentials |  (optional)
send_email = true # bool |  (optional) (default to true)

try:
    # Reset Password with Recovery Question
    api_response = api_instance.forgot_password_set_new_password(user_id, body=body, send_email=send_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->forgot_password_set_new_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**UserCredentials**](UserCredentials.md)|  | [optional] 
 **send_email** | **bool**|  | [optional] [default to true]

### Return type

[**UserCredentials**](UserCredentials.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_objects_for_user**
> list[ResponseLinks] get_linked_objects_for_user(user_id, relationship_name, after=after, limit=limit)



Get linked objects for a user, relationshipName can be a primary or associated relationship name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
relationship_name = 'relationship_name_example' # str | 
after = 'after_example' # str |  (optional)
limit = -1 # int |  (optional) (default to -1)

try:
    api_response = api_instance.get_linked_objects_for_user(user_id, relationship_name, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_linked_objects_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **relationship_name** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

[**list[ResponseLinks]**](ResponseLinks.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_token_for_user_and_client**
> OAuth2RefreshToken get_refresh_token_for_user_and_client(user_id, client_id, token_id, expand=expand, limit=limit, after=after)



Gets a refresh token issued for the specified User and Client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
client_id = 'client_id_example' # str | 
token_id = 'token_id_example' # str | 
expand = 'expand_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)
after = 'after_example' # str |  (optional)

try:
    api_response = api_instance.get_refresh_token_for_user_and_client(user_id, client_id, token_id, expand=expand, limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_refresh_token_for_user_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**|  | 
 **token_id** | **str**|  | 
 **expand** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **after** | **str**|  | [optional] 

### Return type

[**OAuth2RefreshToken**](OAuth2RefreshToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Get User

Fetches a user from your Okta organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Get User
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_grant**
> OAuth2ScopeConsentGrant get_user_grant(user_id, grant_id, expand=expand)



Gets a grant for the specified user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
grant_id = 'grant_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.get_user_grant(user_id, grant_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **grant_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2ScopeConsentGrant**](OAuth2ScopeConsentGrant.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_role**
> Role get_user_role(user_id, role_id)



Gets role that is assigned to user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    api_response = api_instance.get_user_role(user_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

[**Role**](Role.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_links**
> list[AppLink] list_app_links(user_id)

Get Assigned App Links

Fetches appLinks for all direct or indirect (via group membership) assigned applications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Get Assigned App Links
    api_response = api_instance.list_app_links(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_app_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[AppLink]**](AppLink.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_targets_for_application_administrator_role_for_user**
> list[CatalogApplication] list_application_targets_for_application_administrator_role_for_user(user_id, role_id, after=after, limit=limit)



Lists all App targets for an `APP_ADMIN` Role assigned to a User. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_application_targets_for_application_administrator_role_for_user(user_id, role_id, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_application_targets_for_application_administrator_role_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[CatalogApplication]**](CatalogApplication.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_roles_for_user**
> list[Role] list_assigned_roles_for_user(user_id, expand=expand)



Lists all roles assigned to a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
expand = 'expand_example' # str |  (optional)

try:
    api_response = api_instance.list_assigned_roles_for_user(user_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_assigned_roles_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **expand** | **str**|  | [optional] 

### Return type

[**list[Role]**](Role.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_grants_for_user_and_client**
> list[OAuth2ScopeConsentGrant] list_grants_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)



Lists all grants for a specified user and client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
client_id = 'client_id_example' # str | 
expand = 'expand_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_grants_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_grants_for_user_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**|  | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[OAuth2ScopeConsentGrant]**](OAuth2ScopeConsentGrant.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_targets_for_role**
> list[Group] list_group_targets_for_role(user_id, role_id, after=after, limit=limit)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_group_targets_for_role(user_id, role_id, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_group_targets_for_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[Group]**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refresh_tokens_for_user_and_client**
> list[OAuth2RefreshToken] list_refresh_tokens_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)



Lists all refresh tokens issued for the specified User and Client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
client_id = 'client_id_example' # str | 
expand = 'expand_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_refresh_tokens_for_user_and_client(user_id, client_id, expand=expand, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_refresh_tokens_for_user_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**|  | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**list[OAuth2RefreshToken]**](OAuth2RefreshToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_clients**
> list[OAuth2Client] list_user_clients(user_id)



Lists all client resources for which the specified user has grants or tokens.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.list_user_clients(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[OAuth2Client]**](OAuth2Client.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_grants**
> list[OAuth2ScopeConsentGrant] list_user_grants(user_id, scope_id=scope_id, expand=expand, after=after, limit=limit)



Lists all grants for the specified user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
scope_id = 'scope_id_example' # str |  (optional)
expand = 'expand_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = 20 # int |  (optional) (default to 20)

try:
    api_response = api_instance.list_user_grants(user_id, scope_id=scope_id, expand=expand, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
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

[**list[OAuth2ScopeConsentGrant]**](OAuth2ScopeConsentGrant.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> list[Group] list_user_groups(user_id)

Get Member Groups

Fetches the groups of which the user is a member.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Get Member Groups
    api_response = api_instance.list_user_groups(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[Group]**](Group.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_identity_providers**
> list[IdentityProvider] list_user_identity_providers(user_id)

Listing IdPs associated with a user

Lists the IdPs associated with the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Listing IdPs associated with a user
    api_response = api_instance.list_user_identity_providers(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_identity_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**list[IdentityProvider]**](IdentityProvider.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[User] list_users(q=q, after=after, limit=limit, filter=filter, search=search, sort_by=sort_by, sort_order=sort_order)

List Users

Lists users in your organization with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Finds a user that matches firstName, lastName, and email properties (optional)
after = 'after_example' # str | Specifies the pagination cursor for the next page of users (optional)
limit = 10 # int | Specifies the number of results returned (optional) (default to 10)
filter = 'filter_example' # str | Filters users with a supported expression for a subset of properties (optional)
search = 'search_example' # str | Searches for users with a supported filtering  expression for most properties (optional)
sort_by = 'sort_by_example' # str |  (optional)
sort_order = 'sort_order_example' # str |  (optional)

try:
    # List Users
    api_response = api_instance.list_users(q=q, after=after, limit=limit, filter=filter, search=search, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Finds a user that matches firstName, lastName, and email properties | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of users | [optional] 
 **limit** | **int**| Specifies the number of results returned | [optional] [default to 10]
 **filter** | **str**| Filters users with a supported expression for a subset of properties | [optional] 
 **search** | **str**| Searches for users with a supported filtering  expression for most properties | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_order** | **str**|  | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_user**
> User partial_update_user(body, user_id, strict=strict)



Fetch a user by `id`, `login`, or `login shortname` if the short name is unambiguous.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User | 
user_id = 'user_id_example' # str | 
strict = true # bool |  (optional)

try:
    api_response = api_instance.partial_update_user(body, user_id, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->partial_update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 
 **user_id** | **str**|  | 
 **strict** | **bool**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_user**
> UserActivationToken reactivate_user(user_id, send_email=send_email)

Reactivate User

Reactivates a user.  This operation can only be performed on users with a `PROVISIONED` status.  This operation restarts the activation workflow if for some reason the user activation was not completed when using the activationToken from [Activate User](#activate-user).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
send_email = false # bool | Sends an activation email to the user if true (optional) (default to false)

try:
    # Reactivate User
    api_response = api_instance.reactivate_user(user_id, send_email=send_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reactivate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**| Sends an activation email to the user if true | [optional] [default to false]

### Return type

[**UserActivationToken**](UserActivationToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_application_target_from_administrator_role_for_user**
> remove_application_target_from_administrator_role_for_user(user_id, role_id, app_name, application_id)

Remove App Instance Target to App Administrator Role given to a User

Remove App Instance Target to App Administrator Role given to a User

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 
application_id = 'application_id_example' # str | 

try:
    # Remove App Instance Target to App Administrator Role given to a User
    api_instance.remove_application_target_from_administrator_role_for_user(user_id, role_id, app_name, application_id)
except ApiException as e:
    print("Exception when calling UserApi->remove_application_target_from_administrator_role_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_application_target_from_application_administrator_role_for_user**
> remove_application_target_from_application_administrator_role_for_user(user_id, role_id, app_name)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
app_name = 'app_name_example' # str | 

try:
    api_instance.remove_application_target_from_application_administrator_role_for_user(user_id, role_id, app_name)
except ApiException as e:
    print("Exception when calling UserApi->remove_application_target_from_application_administrator_role_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **app_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_target_from_role**
> remove_group_target_from_role(user_id, role_id, group_id)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 
group_id = 'group_id_example' # str | 

try:
    api_instance.remove_group_target_from_role(user_id, role_id, group_id)
except ApiException as e:
    print("Exception when calling UserApi->remove_group_target_from_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_linked_object_for_user**
> remove_linked_object_for_user(user_id, relationship_name)



Delete linked objects for a user, relationshipName can be ONLY a primary relationship name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
relationship_name = 'relationship_name_example' # str | 

try:
    api_instance.remove_linked_object_for_user(user_id, relationship_name)
except ApiException as e:
    print("Exception when calling UserApi->remove_linked_object_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **relationship_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_from_user**
> remove_role_from_user(user_id, role_id)



Unassigns a role from a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
role_id = 'role_id_example' # str | 

try:
    api_instance.remove_role_from_user(user_id, role_id)
except ApiException as e:
    print("Exception when calling UserApi->remove_role_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **role_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_factors**
> reset_factors(user_id)

Reset Factors

This operation resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user's status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Reset Factors
    api_instance.reset_factors(user_id)
except ApiException as e:
    print("Exception when calling UserApi->reset_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> ResetPasswordToken reset_password(user_id, send_email)

Reset Password

Generates a one-time token (OTT) that can be used to reset a user's password.  The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
send_email = true # bool | 

try:
    # Reset Password
    api_response = api_instance.reset_password(user_id, send_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **send_email** | **bool**|  | 

### Return type

[**ResetPasswordToken**](ResetPasswordToken.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_grants_for_user_and_client**
> revoke_grants_for_user_and_client(user_id, client_id)



Revokes all grants for the specified user and client

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
client_id = 'client_id_example' # str | 

try:
    api_instance.revoke_grants_for_user_and_client(user_id, client_id)
except ApiException as e:
    print("Exception when calling UserApi->revoke_grants_for_user_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token_for_user_and_client**
> revoke_token_for_user_and_client(user_id, client_id, token_id)



Revokes the specified refresh token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
client_id = 'client_id_example' # str | 
token_id = 'token_id_example' # str | 

try:
    api_instance.revoke_token_for_user_and_client(user_id, client_id, token_id)
except ApiException as e:
    print("Exception when calling UserApi->revoke_token_for_user_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**|  | 
 **token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_tokens_for_user_and_client**
> revoke_tokens_for_user_and_client(user_id, client_id)



Revokes all refresh tokens issued for the specified User and Client.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
client_id = 'client_id_example' # str | 

try:
    api_instance.revoke_tokens_for_user_and_client(user_id, client_id)
except ApiException as e:
    print("Exception when calling UserApi->revoke_tokens_for_user_and_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_grant**
> revoke_user_grant(user_id, grant_id)



Revokes one grant for a specified user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 
grant_id = 'grant_id_example' # str | 

try:
    api_instance.revoke_user_grant(user_id, grant_id)
except ApiException as e:
    print("Exception when calling UserApi->revoke_user_grant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **grant_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_grants**
> revoke_user_grants(user_id)



Revokes all grants for a specified user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_instance.revoke_user_grants(user_id)
except ApiException as e:
    print("Exception when calling UserApi->revoke_user_grants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_linked_object_for_user**
> set_linked_object_for_user(associated_user_id, primary_relationship_name, primary_user_id)

Set Linked Object for User

Sets a linked object for a user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
associated_user_id = 'associated_user_id_example' # str | 
primary_relationship_name = 'primary_relationship_name_example' # str | 
primary_user_id = 'primary_user_id_example' # str | 

try:
    # Set Linked Object for User
    api_instance.set_linked_object_for_user(associated_user_id, primary_relationship_name, primary_user_id)
except ApiException as e:
    print("Exception when calling UserApi->set_linked_object_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **associated_user_id** | **str**|  | 
 **primary_relationship_name** | **str**|  | 
 **primary_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_user**
> suspend_user(user_id)

Suspend User

Suspends a user.  This operation can only be performed on users with an `ACTIVE` status.  The user will have a status of `SUSPENDED` when the process is complete.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Suspend User
    api_instance.suspend_user(user_id)
except ApiException as e:
    print("Exception when calling UserApi->suspend_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> unlock_user(user_id)

Unlock User

Unlocks a user with a `LOCKED_OUT` status and returns them to `ACTIVE` status.  Users will be able to login with their current password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Unlock User
    api_instance.unlock_user(user_id)
except ApiException as e:
    print("Exception when calling UserApi->unlock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuspend_user**
> unsuspend_user(user_id)

Unsuspend User

Unsuspends a user and returns them to the `ACTIVE` state.  This operation can only be performed on users that have a `SUSPENDED` status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Unsuspend User
    api_instance.unsuspend_user(user_id)
except ApiException as e:
    print("Exception when calling UserApi->unsuspend_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(body, user_id, strict=strict)

Update User

Update a user's profile and/or credentials using strict-update semantics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))
body = swagger_client.User() # User | 
user_id = 'user_id_example' # str | 
strict = true # bool |  (optional)

try:
    # Update User
    api_response = api_instance.update_user(body, user_id, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)|  | 
 **user_id** | **str**|  | 
 **strict** | **bool**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

