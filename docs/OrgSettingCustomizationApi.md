# okta.OrgSettingCustomizationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_preferences**](OrgSettingCustomizationApi.md#get_org_preferences) | **GET** /api/v1/org/preferences | Retrieve the org preferences
[**set_org_hide_okta_ui_footer**](OrgSettingCustomizationApi.md#set_org_hide_okta_ui_footer) | **POST** /api/v1/org/preferences/hideEndUserFooter | Set the hide dashboard footer preference
[**set_org_show_okta_ui_footer**](OrgSettingCustomizationApi.md#set_org_show_okta_ui_footer) | **POST** /api/v1/org/preferences/showEndUserFooter | Set the show dashboard footer preference


# **get_org_preferences**
> OrgPreferences get_org_preferences()

Retrieve the org preferences

Retrieves preferences of your Okta org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_preferences import OrgPreferences
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
    api_instance = okta.OrgSettingCustomizationApi(api_client)

    try:
        # Retrieve the org preferences
        api_response = api_instance.get_org_preferences()
        print("The response of OrgSettingCustomizationApi->get_org_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingCustomizationApi->get_org_preferences: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

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

# **set_org_hide_okta_ui_footer**
> OrgPreferences set_org_hide_okta_ui_footer()

Set the hide dashboard footer preference

Sets the preference to hide the Okta End-User Dashboard footer for all end users of your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_preferences import OrgPreferences
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
    api_instance = okta.OrgSettingCustomizationApi(api_client)

    try:
        # Set the hide dashboard footer preference
        api_response = api_instance.set_org_hide_okta_ui_footer()
        print("The response of OrgSettingCustomizationApi->set_org_hide_okta_ui_footer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingCustomizationApi->set_org_hide_okta_ui_footer: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

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

# **set_org_show_okta_ui_footer**
> OrgPreferences set_org_show_okta_ui_footer()

Set the show dashboard footer preference

Sets the preference to show the Okta UI footer for all end users of your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_preferences import OrgPreferences
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
    api_instance = okta.OrgSettingCustomizationApi(api_client)

    try:
        # Set the show dashboard footer preference
        api_response = api_instance.set_org_show_okta_ui_footer()
        print("The response of OrgSettingCustomizationApi->set_org_show_okta_ui_footer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingCustomizationApi->set_org_show_okta_ui_footer: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgPreferences**](OrgPreferences.md)

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

