# okta.AttackProtectionApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authenticator_settings**](AttackProtectionApi.md#get_authenticator_settings) | **GET** /attack-protection/api/v1/authenticator-settings | Retrieve the authenticator settings
[**get_user_lockout_settings**](AttackProtectionApi.md#get_user_lockout_settings) | **GET** /attack-protection/api/v1/user-lockout-settings | Retrieve the user lockout settings
[**replace_authenticator_settings**](AttackProtectionApi.md#replace_authenticator_settings) | **PUT** /attack-protection/api/v1/authenticator-settings | Replace the authenticator settings
[**replace_user_lockout_settings**](AttackProtectionApi.md#replace_user_lockout_settings) | **PUT** /attack-protection/api/v1/user-lockout-settings | Replace the user lockout settings


# **get_authenticator_settings**
> List[AttackProtectionAuthenticatorSettings] get_authenticator_settings()

Retrieve the authenticator settings

Retrieves the Authenticator Settings for an org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.attack_protection_authenticator_settings import AttackProtectionAuthenticatorSettings
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
    api_instance = okta.AttackProtectionApi(api_client)

    try:
        # Retrieve the authenticator settings
        api_response = api_instance.get_authenticator_settings()
        print("The response of AttackProtectionApi->get_authenticator_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttackProtectionApi->get_authenticator_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AttackProtectionAuthenticatorSettings]**](AttackProtectionAuthenticatorSettings.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_lockout_settings**
> List[UserLockoutSettings] get_user_lockout_settings()

Retrieve the user lockout settings

Retrieves the User Lockout Settings for an org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_lockout_settings import UserLockoutSettings
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
    api_instance = okta.AttackProtectionApi(api_client)

    try:
        # Retrieve the user lockout settings
        api_response = api_instance.get_user_lockout_settings()
        print("The response of AttackProtectionApi->get_user_lockout_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttackProtectionApi->get_user_lockout_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserLockoutSettings]**](UserLockoutSettings.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_authenticator_settings**
> AttackProtectionAuthenticatorSettings replace_authenticator_settings(authenticator_settings)

Replace the authenticator settings

Replaces the Authenticator Settings for an org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.attack_protection_authenticator_settings import AttackProtectionAuthenticatorSettings
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
    api_instance = okta.AttackProtectionApi(api_client)
    authenticator_settings = okta.AttackProtectionAuthenticatorSettings() # AttackProtectionAuthenticatorSettings | 

    try:
        # Replace the authenticator settings
        api_response = api_instance.replace_authenticator_settings(authenticator_settings)
        print("The response of AttackProtectionApi->replace_authenticator_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttackProtectionApi->replace_authenticator_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_settings** | [**AttackProtectionAuthenticatorSettings**](AttackProtectionAuthenticatorSettings.md)|  | 

### Return type

[**AttackProtectionAuthenticatorSettings**](AttackProtectionAuthenticatorSettings.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_user_lockout_settings**
> UserLockoutSettings replace_user_lockout_settings(lockout_settings)

Replace the user lockout settings

Replaces the User Lockout Settings for an org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_lockout_settings import UserLockoutSettings
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
    api_instance = okta.AttackProtectionApi(api_client)
    lockout_settings = okta.UserLockoutSettings() # UserLockoutSettings | 

    try:
        # Replace the user lockout settings
        api_response = api_instance.replace_user_lockout_settings(lockout_settings)
        print("The response of AttackProtectionApi->replace_user_lockout_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttackProtectionApi->replace_user_lockout_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lockout_settings** | [**UserLockoutSettings**](UserLockoutSettings.md)|  | 

### Return type

[**UserLockoutSettings**](UserLockoutSettings.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

