# openapi_client.AttackProtectionApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_lockout_settings**](AttackProtectionApi.md#get_user_lockout_settings) | **GET** /attack-protection/api/v1/user-lockout-settings | Retrieve the User Lockout Settings
[**replace_user_lockout_settings**](AttackProtectionApi.md#replace_user_lockout_settings) | **PUT** /attack-protection/api/v1/user-lockout-settings | Replace the User Lockout Settings


# **get_user_lockout_settings**
> List[UserLockoutSettings] get_user_lockout_settings()

Retrieve the User Lockout Settings

Retrieves the User Lockout Settings for an org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_lockout_settings import UserLockoutSettings
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
    api_instance = openapi_client.AttackProtectionApi(api_client)

    try:
        # Retrieve the User Lockout Settings
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

# **replace_user_lockout_settings**
> UserLockoutSettings replace_user_lockout_settings(lockout_settings)

Replace the User Lockout Settings

Replaces the User Lockout Settings for an org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_lockout_settings import UserLockoutSettings
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
    api_instance = openapi_client.AttackProtectionApi(api_client)
    lockout_settings = openapi_client.UserLockoutSettings() # UserLockoutSettings | 

    try:
        # Replace the User Lockout Settings
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

