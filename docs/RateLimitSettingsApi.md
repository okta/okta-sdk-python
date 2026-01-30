# okta.RateLimitSettingsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate_limit_settings_admin_notifications**](RateLimitSettingsApi.md#get_rate_limit_settings_admin_notifications) | **GET** /api/v1/rate-limit-settings/admin-notifications | Retrieve the rate limit admin notification settings
[**get_rate_limit_settings_per_client**](RateLimitSettingsApi.md#get_rate_limit_settings_per_client) | **GET** /api/v1/rate-limit-settings/per-client | Retrieve the per-client rate limit settings
[**get_rate_limit_settings_warning_threshold**](RateLimitSettingsApi.md#get_rate_limit_settings_warning_threshold) | **GET** /api/v1/rate-limit-settings/warning-threshold | Retrieve the rate limit warning threshold percentage
[**replace_rate_limit_settings_admin_notifications**](RateLimitSettingsApi.md#replace_rate_limit_settings_admin_notifications) | **PUT** /api/v1/rate-limit-settings/admin-notifications | Replace the rate limit admin notification settings
[**replace_rate_limit_settings_per_client**](RateLimitSettingsApi.md#replace_rate_limit_settings_per_client) | **PUT** /api/v1/rate-limit-settings/per-client | Replace the per-client rate limit settings
[**replace_rate_limit_settings_warning_threshold**](RateLimitSettingsApi.md#replace_rate_limit_settings_warning_threshold) | **PUT** /api/v1/rate-limit-settings/warning-threshold | Replace the rate limit warning threshold percentage


# **get_rate_limit_settings_admin_notifications**
> RateLimitAdminNotifications get_rate_limit_settings_admin_notifications()

Retrieve the rate limit admin notification settings

Retrieves the currently configured Rate Limit Admin Notification Settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.rate_limit_admin_notifications import RateLimitAdminNotifications
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
    api_instance = okta.RateLimitSettingsApi(api_client)

    try:
        # Retrieve the rate limit admin notification settings
        api_response = api_instance.get_rate_limit_settings_admin_notifications()
        print("The response of RateLimitSettingsApi->get_rate_limit_settings_admin_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitSettingsApi->get_rate_limit_settings_admin_notifications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RateLimitAdminNotifications**](RateLimitAdminNotifications.md)

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

# **get_rate_limit_settings_per_client**
> PerClientRateLimitSettings get_rate_limit_settings_per_client()

Retrieve the per-client rate limit settings

Retrieves the currently configured Per-Client Rate Limit Settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.per_client_rate_limit_settings import PerClientRateLimitSettings
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
    api_instance = okta.RateLimitSettingsApi(api_client)

    try:
        # Retrieve the per-client rate limit settings
        api_response = api_instance.get_rate_limit_settings_per_client()
        print("The response of RateLimitSettingsApi->get_rate_limit_settings_per_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitSettingsApi->get_rate_limit_settings_per_client: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PerClientRateLimitSettings**](PerClientRateLimitSettings.md)

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

# **get_rate_limit_settings_warning_threshold**
> RateLimitWarningThresholdResponse get_rate_limit_settings_warning_threshold()

Retrieve the rate limit warning threshold percentage

Retrieves the currently configured threshold for warning notifications when the API's rate limit is exceeded

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.rate_limit_warning_threshold_response import RateLimitWarningThresholdResponse
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
    api_instance = okta.RateLimitSettingsApi(api_client)

    try:
        # Retrieve the rate limit warning threshold percentage
        api_response = api_instance.get_rate_limit_settings_warning_threshold()
        print("The response of RateLimitSettingsApi->get_rate_limit_settings_warning_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitSettingsApi->get_rate_limit_settings_warning_threshold: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RateLimitWarningThresholdResponse**](RateLimitWarningThresholdResponse.md)

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

# **replace_rate_limit_settings_admin_notifications**
> RateLimitAdminNotifications replace_rate_limit_settings_admin_notifications(rate_limit_admin_notifications)

Replace the rate limit admin notification settings

Replaces the Rate Limit Admin Notification Settings and returns the configured properties

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.rate_limit_admin_notifications import RateLimitAdminNotifications
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
    api_instance = okta.RateLimitSettingsApi(api_client)
    rate_limit_admin_notifications = okta.RateLimitAdminNotifications() # RateLimitAdminNotifications | 

    try:
        # Replace the rate limit admin notification settings
        api_response = api_instance.replace_rate_limit_settings_admin_notifications(rate_limit_admin_notifications)
        print("The response of RateLimitSettingsApi->replace_rate_limit_settings_admin_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitSettingsApi->replace_rate_limit_settings_admin_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limit_admin_notifications** | [**RateLimitAdminNotifications**](RateLimitAdminNotifications.md)|  | 

### Return type

[**RateLimitAdminNotifications**](RateLimitAdminNotifications.md)

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

# **replace_rate_limit_settings_per_client**
> PerClientRateLimitSettings replace_rate_limit_settings_per_client(per_client_rate_limit_settings)

Replace the per-client rate limit settings

Replaces the Per-Client Rate Limit Settings and returns the configured properties

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.per_client_rate_limit_settings import PerClientRateLimitSettings
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
    api_instance = okta.RateLimitSettingsApi(api_client)
    per_client_rate_limit_settings = okta.PerClientRateLimitSettings() # PerClientRateLimitSettings | 

    try:
        # Replace the per-client rate limit settings
        api_response = api_instance.replace_rate_limit_settings_per_client(per_client_rate_limit_settings)
        print("The response of RateLimitSettingsApi->replace_rate_limit_settings_per_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitSettingsApi->replace_rate_limit_settings_per_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_client_rate_limit_settings** | [**PerClientRateLimitSettings**](PerClientRateLimitSettings.md)|  | 

### Return type

[**PerClientRateLimitSettings**](PerClientRateLimitSettings.md)

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

# **replace_rate_limit_settings_warning_threshold**
> RateLimitWarningThresholdResponse replace_rate_limit_settings_warning_threshold(rate_limit_warning_threshold=rate_limit_warning_threshold)

Replace the rate limit warning threshold percentage

Replaces the Rate Limit Warning Threshold Percentage and returns the configured property

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.rate_limit_warning_threshold_request import RateLimitWarningThresholdRequest
from okta.models.rate_limit_warning_threshold_response import RateLimitWarningThresholdResponse
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
    api_instance = okta.RateLimitSettingsApi(api_client)
    rate_limit_warning_threshold = okta.RateLimitWarningThresholdRequest() # RateLimitWarningThresholdRequest |  (optional)

    try:
        # Replace the rate limit warning threshold percentage
        api_response = api_instance.replace_rate_limit_settings_warning_threshold(rate_limit_warning_threshold=rate_limit_warning_threshold)
        print("The response of RateLimitSettingsApi->replace_rate_limit_settings_warning_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitSettingsApi->replace_rate_limit_settings_warning_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limit_warning_threshold** | [**RateLimitWarningThresholdRequest**](RateLimitWarningThresholdRequest.md)|  | [optional] 

### Return type

[**RateLimitWarningThresholdResponse**](RateLimitWarningThresholdResponse.md)

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

