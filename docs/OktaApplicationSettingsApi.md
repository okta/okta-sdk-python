# okta.OktaApplicationSettingsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_first_party_app_settings**](OktaApplicationSettingsApi.md#get_first_party_app_settings) | **GET** /api/v1/first-party-app-settings/{appName} | Retrieve the Okta application settings
[**replace_first_party_app_settings**](OktaApplicationSettingsApi.md#replace_first_party_app_settings) | **PUT** /api/v1/first-party-app-settings/{appName} | Replace the Okta application settings


# **get_first_party_app_settings**
> AdminConsoleSettings get_first_party_app_settings(app_name)

Retrieve the Okta application settings

Retrieves the settings for an Okta app (also known as an Okta first-party app)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.admin_console_settings import AdminConsoleSettings
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
    api_instance = okta.OktaApplicationSettingsApi(api_client)
    app_name = 'admin-console' # str | The key name for the Okta app.<br> Supported apps:   * Okta Admin Console (`admin-console`) 

    try:
        # Retrieve the Okta application settings
        api_response = api_instance.get_first_party_app_settings(app_name)
        print("The response of OktaApplicationSettingsApi->get_first_party_app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OktaApplicationSettingsApi->get_first_party_app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The key name for the Okta app.&lt;br&gt; Supported apps:   * Okta Admin Console (&#x60;admin-console&#x60;)  | 

### Return type

[**AdminConsoleSettings**](AdminConsoleSettings.md)

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

# **replace_first_party_app_settings**
> AdminConsoleSettings replace_first_party_app_settings(app_name, admin_console_settings)

Replace the Okta application settings

Replaces the settings for an Okta app (also known as an Okta first-party app)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.admin_console_settings import AdminConsoleSettings
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
    api_instance = okta.OktaApplicationSettingsApi(api_client)
    app_name = 'admin-console' # str | The key name for the Okta app.<br> Supported apps:   * Okta Admin Console (`admin-console`) 
    admin_console_settings = okta.AdminConsoleSettings() # AdminConsoleSettings | 

    try:
        # Replace the Okta application settings
        api_response = api_instance.replace_first_party_app_settings(app_name, admin_console_settings)
        print("The response of OktaApplicationSettingsApi->replace_first_party_app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OktaApplicationSettingsApi->replace_first_party_app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| The key name for the Okta app.&lt;br&gt; Supported apps:   * Okta Admin Console (&#x60;admin-console&#x60;)  | 
 **admin_console_settings** | [**AdminConsoleSettings**](AdminConsoleSettings.md)|  | 

### Return type

[**AdminConsoleSettings**](AdminConsoleSettings.md)

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

