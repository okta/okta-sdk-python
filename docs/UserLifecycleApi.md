# okta.UserLifecycleApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UserLifecycleApi.md#activate_user) | **POST** /api/v1/users/{id}/lifecycle/activate | Activate a user
[**deactivate_user**](UserLifecycleApi.md#deactivate_user) | **POST** /api/v1/users/{id}/lifecycle/deactivate | Deactivate a user
[**reactivate_user**](UserLifecycleApi.md#reactivate_user) | **POST** /api/v1/users/{id}/lifecycle/reactivate | Reactivate a user
[**reset_factors**](UserLifecycleApi.md#reset_factors) | **POST** /api/v1/users/{id}/lifecycle/reset_factors | Reset the factors
[**suspend_user**](UserLifecycleApi.md#suspend_user) | **POST** /api/v1/users/{id}/lifecycle/suspend | Suspend a user
[**unlock_user**](UserLifecycleApi.md#unlock_user) | **POST** /api/v1/users/{id}/lifecycle/unlock | Unlock a user
[**unsuspend_user**](UserLifecycleApi.md#unsuspend_user) | **POST** /api/v1/users/{id}/lifecycle/unsuspend | Unsuspend a user


# **activate_user**
> UserActivationToken activate_user(id, send_email=send_email)

Activate a user

Activates a user.  Perform this operation only on users with a `STAGED` or `DEPROVISIONED` status. Activation of a user is an asynchronous operation. * The user has the `transitioningToStatus` property with an `ACTIVE` value during activation. This indicates that the user hasn't completed the asynchronous operation. * The user has an `ACTIVE` status when the activation process completes.  Users who don't have a password must complete the welcome flow by visiting the activation link to complete the transition to `ACTIVE` status.  > **Note:** If you want to send a branded user activation email, change the subdomain of your request to the custom domain that's associated with the brand. > For example, change `subdomain.okta.com` to `custom.domain.one`. See [Multibrand and custom domains](https://developer.okta.com/docs/concepts/brands/#multibrand-and-custom-domains).  > **Note:** If you have optional password enabled, visiting the activation link is optional for users who aren't required to enroll a password. > See [Create user with optional password](/openapi/okta-management/management/tag/User/#create-user-with-optional-password).  > **Legal disclaimer** > After a user is added to the Okta directory, they receive an activation email. As part of signing up for this service, > you agreed not to use Okta's service/product to spam and/or send unsolicited messages. > Please refrain from adding unrelated accounts to the directory as Okta is not responsible for, and disclaims any and all > liability associated with, the activation email's content. You, and you alone, bear responsibility for the emails sent to any recipients.

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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    send_email = True # bool | Sends an activation email to the user if `true` (optional) (default to True)

    try:
        # Activate a user
        api_response = api_instance.activate_user(id, send_email=send_email)
        print("The response of UserLifecycleApi->activate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->activate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **send_email** | **bool**| Sends an activation email to the user if &#x60;true&#x60; | [optional] [default to True]

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

# **deactivate_user**
> Success deactivate_user(id, send_email=send_email, prefer=prefer)

Deactivate a user

Deactivates a user.  Perform this operation only on users that do not have a `DEPROVISIONED` status. * The user's `transitioningToStatus` property is `DEPROVISIONED` during deactivation to indicate that the user hasn't completed the asynchronous operation. * The user's status is `DEPROVISIONED` when the deactivation process is complete.  > **Important:** Deactivating a user is a **destructive** operation. The user is deprovisioned from all assigned apps, which might destroy their data such as email or files. **This action cannot be recovered!**  You can also perform user deactivation asynchronously. To invoke asynchronous user deactivation, pass an HTTP header `Prefer: respond-async` with the request.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    send_email = False # bool | Sends a deactivation email to the admin if `true` (optional) (default to False)
    prefer = 'prefer_example' # str | Request asynchronous processing (optional)

    try:
        # Deactivate a user
        api_response = api_instance.deactivate_user(id, send_email=send_email, prefer=prefer)
        print("The response of UserLifecycleApi->deactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->deactivate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **send_email** | **bool**| Sends a deactivation email to the admin if &#x60;true&#x60; | [optional] [default to False]
 **prefer** | **str**| Request asynchronous processing | [optional] 

### Return type

[**Success**](Success.md)

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

# **reactivate_user**
> UserActivationToken reactivate_user(id, send_email=send_email)

Reactivate a user

Reactivates a user.  Perform this operation only on users with a `PROVISIONED` or `RECOVERY` [status](/openapi/okta-management/management/tag/User/#tag/User/operation/listUsers!c=200&path=status&t=response). This operation restarts the activation workflow if for some reason the user activation wasn't completed when using the `activationToken` from [Activate User](/openapi/okta-management/management/tag/UserLifecycle/#tag/UserLifecycle/operation/activateUser).  Users that don't have a password must complete the flow by completing the [Reset password](/openapi/okta-management/management/tag/UserCred/#tag/UserCred/operation/resetPassword) flow and MFA enrollment steps to transition the user to `ACTIVE` status.  If `sendEmail` is `false`, returns an activation link for the user to set up their account. The activation token can be used to create a custom activation link.

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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    send_email = False # bool | Sends an activation email to the user if `true` (optional) (default to False)

    try:
        # Reactivate a user
        api_response = api_instance.reactivate_user(id, send_email=send_email)
        print("The response of UserLifecycleApi->reactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->reactivate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **send_email** | **bool**| Sends an activation email to the user if &#x60;true&#x60; | [optional] [default to False]

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

# **reset_factors**
> Success reset_factors(id)

Reset the factors

Resets all factors for the specified user. All MFA factor enrollments return to the unenrolled state. The user's status remains `ACTIVE`. This link is present only if the user is currently enrolled in one or more MFA factors.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # Reset the factors
        api_response = api_instance.reset_factors(id)
        print("The response of UserLifecycleApi->reset_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->reset_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

### Return type

[**Success**](Success.md)

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

# **suspend_user**
> Success suspend_user(id)

Suspend a user

Suspends a user. Perform this operation only on users with an `ACTIVE` status. The user has a `SUSPENDED` status when the process completes.  Suspended users can't sign in to Okta. They can only be unsuspended or deactivated. Their group and app assignments are retained.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # Suspend a user
        api_response = api_instance.suspend_user(id)
        print("The response of UserLifecycleApi->suspend_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->suspend_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

### Return type

[**Success**](Success.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> Success unlock_user(id)

Unlock a user

Unlocks a user with a `LOCKED_OUT` status or unlocks a user with an `ACTIVE` status that's blocked from unknown devices. Unlocked users have an `ACTIVE` status and can sign in with their current password. > **Note:** This operation works with Okta-sourced users. It doesn't support directory-sourced accounts such as Active Directory.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # Unlock a user
        api_response = api_instance.unlock_user(id)
        print("The response of UserLifecycleApi->unlock_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->unlock_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

### Return type

[**Success**](Success.md)

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
> Success unsuspend_user(id)

Unsuspend a user

Unsuspends a user and returns them to the `ACTIVE` state. This operation can only be performed on users that have a `SUSPENDED` status.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.success import Success
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
    api_instance = okta.UserLifecycleApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # Unsuspend a user
        api_response = api_instance.unsuspend_user(id)
        print("The response of UserLifecycleApi->unsuspend_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLifecycleApi->unsuspend_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

### Return type

[**Success**](Success.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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

