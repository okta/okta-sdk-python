# okta.UserCredApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](UserCredApi.md#change_password) | **POST** /api/v1/users/{userId}/credentials/change_password | Update password
[**change_recovery_question**](UserCredApi.md#change_recovery_question) | **POST** /api/v1/users/{userId}/credentials/change_recovery_question | Update recovery question
[**expire_password**](UserCredApi.md#expire_password) | **POST** /api/v1/users/{id}/lifecycle/expire_password | Expire the password
[**expire_password_with_temp_password**](UserCredApi.md#expire_password_with_temp_password) | **POST** /api/v1/users/{id}/lifecycle/expire_password_with_temp_password | Expire the password with a temporary password
[**forgot_password**](UserCredApi.md#forgot_password) | **POST** /api/v1/users/{userId}/credentials/forgot_password | Start forgot password flow
[**forgot_password_set_new_password**](UserCredApi.md#forgot_password_set_new_password) | **POST** /api/v1/users/{userId}/credentials/forgot_password_recovery_question | Reset password with recovery question
[**reset_password**](UserCredApi.md#reset_password) | **POST** /api/v1/users/{id}/lifecycle/reset_password | Reset a password


# **change_password**
> UserCredentials change_password(user_id, change_password_request, strict=strict)

Update password

Updates a user's password by validating the user's current password.  This operation provides an option to delete all the sessions of the specified user. However, if the request is made in the context of a session owned by the specified user, that session isn't cleared.  You can only perform this operation on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid [password credential](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/#tag/User/operation/createUser!path=credentials/password&t=request).  The user transitions to `ACTIVE` status when successfully invoked in `RECOVERY` status.  > **Note:** The Okta account management policy doesn't support the `/users/{userId}/credentials/change_password` endpoint. See [Configure an Okta account management policy](https://developer.okta.com/docs/guides/okta-account-management-policy/main/).

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
    api_instance = okta.UserCredApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    change_password_request = okta.ChangePasswordRequest() # ChangePasswordRequest | 
    strict = False # bool | If true, validates against the password minimum age policy (optional) (default to False)

    try:
        # Update password
        api_response = api_instance.change_password(user_id, change_password_request, strict=strict)
        print("The response of UserCredApi->change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)|  | 
 **strict** | **bool**| If true, validates against the password minimum age policy | [optional] [default to False]

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

Update recovery question

Updates a user's recovery question and answer credential by validating the user's current password. You can only perform this operation on users in `STAGED`, `ACTIVE`, or `RECOVERY` status that have a valid [password credential](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/#tag/User/operation/createUser!path=credentials/password&t=request).

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
    api_instance = okta.UserCredApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    user_credentials = okta.UserCredentials() # UserCredentials | 

    try:
        # Update recovery question
        api_response = api_instance.change_recovery_question(user_id, user_credentials)
        print("The response of UserCredApi->change_recovery_question:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->change_recovery_question: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **expire_password**
> User expire_password(id)

Expire the password

Expires the password. This operation transitions the user status to `PASSWORD_EXPIRED` so that the user must change their password the next time that they sign in. <br> If you have integrated Okta with your on-premises Active Directory (AD), then setting a user's password as expired in Okta also expires the password in AD. When the user tries to sign in to Okta, delegated authentication finds the password-expired status in AD, and the user is presented with the password-expired page where they can change their password.  > **Note:** The Okta account management policy doesn't support the `/users/{id}/lifecycle/expire_password` endpoint. See [Configure an Okta account management policy](https://developer.okta.com/docs/guides/okta-account-management-policy/main/).

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
    api_instance = okta.UserCredApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # Expire the password
        api_response = api_instance.expire_password(id)
        print("The response of UserCredApi->expire_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->expire_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

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

# **expire_password_with_temp_password**
> User expire_password_with_temp_password(id, revoke_sessions=revoke_sessions)

Expire the password with a temporary password

Expires the password and resets the user's password to a temporary password. This operation transitions the user status to `PASSWORD_EXPIRED` so that the user must change their password the next time that they sign in. The user's password is reset to a temporary password that's returned, and then the user's password is expired. If `revokeSessions` is included in the request with a value of `true`, the user's current outstanding sessions are revoked and require re-authentication. <br> If you have integrated Okta with your on-premises Active Directory (AD), then setting a user's password as expired in Okta also expires the password in AD. When the user tries to sign in to Okta, delegated authentication finds the password-expired status in AD, and the user is presented with the password-expired page where they can change their password.

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
    api_instance = okta.UserCredApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    revoke_sessions = False # bool | Revokes the user's existing sessions if `true` (optional) (default to False)

    try:
        # Expire the password with a temporary password
        api_response = api_instance.expire_password_with_temp_password(id, revoke_sessions=revoke_sessions)
        print("The response of UserCredApi->expire_password_with_temp_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->expire_password_with_temp_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **revoke_sessions** | **bool**| Revokes the user&#39;s existing sessions if &#x60;true&#x60; | [optional] [default to False]

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

# **forgot_password**
> ForgotPasswordResponse forgot_password(user_id, send_email=send_email)

Start forgot password flow

Starts the forgot password flow.  Generates a one-time token (OTT) that you can use to reset a user's password.  The user must validate their security question's answer when visiting the reset link. Perform this operation only on users with an `ACTIVE` status and a valid [recovery question credential](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/#tag/User/operation/createUser!path=credentials/recovery_question&t=request).  > **Note:** If you have migrated to Identity Engine, you can allow users to recover passwords with any enrolled MFA authenticator. See [Self-service account recovery](https://help.okta.com/oie/en-us/content/topics/identity-engine/authenticators/configure-sspr.htm?cshid=ext-config-sspr).  If an email address is associated with multiple users, keep in mind the following to ensure a successful password recovery lookup:   * Okta no longer includes deactivated users in the lookup.   * The lookup searches sign-in IDs first, then primary email addresses, and then secondary email addresses.  If `sendEmail` is `false`, returns a link for the user to reset their password. This operation doesn't affect the status of the user.

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
    api_instance = okta.UserCredApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    send_email = True # bool | Sends a forgot password email to the user if `true` (optional) (default to True)

    try:
        # Start forgot password flow
        api_response = api_instance.forgot_password(user_id, send_email=send_email)
        print("The response of UserCredApi->forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->forgot_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **send_email** | **bool**| Sends a forgot password email to the user if &#x60;true&#x60; | [optional] [default to True]

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
**200** | Reset URL |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgot_password_set_new_password**
> UserCredentials forgot_password_set_new_password(user_id, user_credentials, send_email=send_email)

Reset password with recovery question

Resets the user's password to the specified password if the provided answer to the recovery question is correct. You must include the recovery question answer with the submission.

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
    api_instance = okta.UserCredApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    user_credentials = okta.UserCredentials() # UserCredentials | 
    send_email = True # bool |  (optional) (default to True)

    try:
        # Reset password with recovery question
        api_response = api_instance.forgot_password_set_new_password(user_id, user_credentials, send_email=send_email)
        print("The response of UserCredApi->forgot_password_set_new_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->forgot_password_set_new_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
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

# **reset_password**
> ResetPasswordToken reset_password(id, send_email, revoke_sessions=revoke_sessions)

Reset a password

Resets a password. Generates a one-time token (OTT) that you can use to reset a user's password. You can automatically email the OTT link to the user or return the OTT to the API caller and distribute using a custom flow.  This operation transitions the user to the `RECOVERY` status. The user is then not able to sign in or initiate a forgot password flow until they complete the reset flow.  This operation provides an option to delete all the user's sessions. However, if the request is made in the context of a session owned by the specified user, that session isn't cleared. > **Note:** You can also use this API to convert a user with the Okta credential provider to use a federated provider. After this conversion, the user can't directly sign in with a password. > To convert a federated user back to an Okta user, use the default API call.  If an email address is associated with multiple users, keep in mind the following to ensure a successful password recovery lookup:   * Okta no longer includes deactivated users in the lookup.   * The lookup searches sign-in IDs first, then primary email addresses, and then secondary email addresses.   If `sendEmail` is `false`, returns a link for the user to reset their password.

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
    api_instance = okta.UserCredApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    send_email = True # bool | 
    revoke_sessions = False # bool | Revokes all user sessions, except for the current session, if set to `true` (optional) (default to False)

    try:
        # Reset a password
        api_response = api_instance.reset_password(id, send_email, revoke_sessions=revoke_sessions)
        print("The response of UserCredApi->reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserCredApi->reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **send_email** | **bool**|  | 
 **revoke_sessions** | **bool**| Revokes all user sessions, except for the current session, if set to &#x60;true&#x60; | [optional] [default to False]

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

