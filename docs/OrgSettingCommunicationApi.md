# okta.OrgSettingCommunicationApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_okta_communication_settings**](OrgSettingCommunicationApi.md#get_okta_communication_settings) | **GET** /api/v1/org/privacy/oktaCommunication | Retrieve the Okta communication settings
[**opt_in_users_to_okta_communication_emails**](OrgSettingCommunicationApi.md#opt_in_users_to_okta_communication_emails) | **POST** /api/v1/org/privacy/oktaCommunication/optIn | Opt in to Okta user communication emails
[**opt_out_users_from_okta_communication_emails**](OrgSettingCommunicationApi.md#opt_out_users_from_okta_communication_emails) | **POST** /api/v1/org/privacy/oktaCommunication/optOut | Opt out of Okta user communication emails


# **get_okta_communication_settings**
> OrgOktaCommunicationSetting get_okta_communication_settings()

Retrieve the Okta communication settings

Retrieves Okta Communication Settings of your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting
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
    api_instance = okta.OrgSettingCommunicationApi(api_client)

    try:
        # Retrieve the Okta communication settings
        api_response = api_instance.get_okta_communication_settings()
        print("The response of OrgSettingCommunicationApi->get_okta_communication_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingCommunicationApi->get_okta_communication_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

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

# **opt_in_users_to_okta_communication_emails**
> OrgOktaCommunicationSetting opt_in_users_to_okta_communication_emails()

Opt in to Okta user communication emails

Opts in all users of this org to Okta communication emails

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting
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
    api_instance = okta.OrgSettingCommunicationApi(api_client)

    try:
        # Opt in to Okta user communication emails
        api_response = api_instance.opt_in_users_to_okta_communication_emails()
        print("The response of OrgSettingCommunicationApi->opt_in_users_to_okta_communication_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingCommunicationApi->opt_in_users_to_okta_communication_emails: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

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

# **opt_out_users_from_okta_communication_emails**
> OrgOktaCommunicationSetting opt_out_users_from_okta_communication_emails()

Opt out of Okta user communication emails

Opts out all users of this org from Okta communication emails

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.org_okta_communication_setting import OrgOktaCommunicationSetting
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
    api_instance = okta.OrgSettingCommunicationApi(api_client)

    try:
        # Opt out of Okta user communication emails
        api_response = api_instance.opt_out_users_from_okta_communication_emails()
        print("The response of OrgSettingCommunicationApi->opt_out_users_from_okta_communication_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgSettingCommunicationApi->opt_out_users_from_okta_communication_emails: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgOktaCommunicationSetting**](OrgOktaCommunicationSetting.md)

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

