# okta.OktaPersonalSettingsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_personal_apps_export_block_list**](OktaPersonalSettingsApi.md#list_personal_apps_export_block_list) | **GET** /okta-personal-settings/api/v1/export-blocklists | List all blocked email domains
[**replace_blocked_email_domains**](OktaPersonalSettingsApi.md#replace_blocked_email_domains) | **PUT** /okta-personal-settings/api/v1/export-blocklists | Replace the blocked email domains
[**replace_okta_personal_admin_settings**](OktaPersonalSettingsApi.md#replace_okta_personal_admin_settings) | **PUT** /okta-personal-settings/api/v1/edit-feature | Replace the Okta Personal admin settings


# **list_personal_apps_export_block_list**
> PersonalAppsBlockList list_personal_apps_export_block_list()

List all blocked email domains

Lists all blocked email domains which are excluded from app migration

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.personal_apps_block_list import PersonalAppsBlockList
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
    api_instance = okta.OktaPersonalSettingsApi(api_client)

    try:
        # List all blocked email domains
        api_response = api_instance.list_personal_apps_export_block_list()
        print("The response of OktaPersonalSettingsApi->list_personal_apps_export_block_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OktaPersonalSettingsApi->list_personal_apps_export_block_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PersonalAppsBlockList**](PersonalAppsBlockList.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_blocked_email_domains**
> replace_blocked_email_domains(personal_apps_block_list)

Replace the blocked email domains

Replaces the list of blocked email domains which are excluded from app migration

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.personal_apps_block_list import PersonalAppsBlockList
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
    api_instance = okta.OktaPersonalSettingsApi(api_client)
    personal_apps_block_list = okta.PersonalAppsBlockList() # PersonalAppsBlockList | 

    try:
        # Replace the blocked email domains
        api_instance.replace_blocked_email_domains(personal_apps_block_list)
    except Exception as e:
        print("Exception when calling OktaPersonalSettingsApi->replace_blocked_email_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personal_apps_block_list** | [**PersonalAppsBlockList**](PersonalAppsBlockList.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_okta_personal_admin_settings**
> replace_okta_personal_admin_settings(okta_personal_admin_feature_settings)

Replace the Okta Personal admin settings

Replaces Okta Personal admin settings in a Workforce org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.okta_personal_admin_feature_settings import OktaPersonalAdminFeatureSettings
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
    api_instance = okta.OktaPersonalSettingsApi(api_client)
    okta_personal_admin_feature_settings = okta.OktaPersonalAdminFeatureSettings() # OktaPersonalAdminFeatureSettings | 

    try:
        # Replace the Okta Personal admin settings
        api_instance.replace_okta_personal_admin_settings(okta_personal_admin_feature_settings)
    except Exception as e:
        print("Exception when calling OktaPersonalSettingsApi->replace_okta_personal_admin_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_personal_admin_feature_settings** | [**OktaPersonalAdminFeatureSettings**](OktaPersonalAdminFeatureSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

