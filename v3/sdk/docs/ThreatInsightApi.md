# openapi_client.ThreatInsightApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_configuration**](ThreatInsightApi.md#get_current_configuration) | **GET** /api/v1/threats/configuration | Retrieve the ThreatInsight Configuration
[**update_configuration**](ThreatInsightApi.md#update_configuration) | **POST** /api/v1/threats/configuration | Update the ThreatInsight Configuration


# **get_current_configuration**
> ThreatInsightConfiguration get_current_configuration()

Retrieve the ThreatInsight Configuration

Retrieves the ThreatInsight configuration for the org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.threat_insight_configuration import ThreatInsightConfiguration
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
    api_instance = openapi_client.ThreatInsightApi(api_client)

    try:
        # Retrieve the ThreatInsight Configuration
        api_response = api_instance.get_current_configuration()
        print("The response of ThreatInsightApi->get_current_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatInsightApi->get_current_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ThreatInsightConfiguration**](ThreatInsightConfiguration.md)

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

# **update_configuration**
> ThreatInsightConfiguration update_configuration(threat_insight_configuration)

Update the ThreatInsight Configuration

Updates the ThreatInsight configuration for the org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.threat_insight_configuration import ThreatInsightConfiguration
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
    api_instance = openapi_client.ThreatInsightApi(api_client)
    threat_insight_configuration = openapi_client.ThreatInsightConfiguration() # ThreatInsightConfiguration | 

    try:
        # Update the ThreatInsight Configuration
        api_response = api_instance.update_configuration(threat_insight_configuration)
        print("The response of ThreatInsightApi->update_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThreatInsightApi->update_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threat_insight_configuration** | [**ThreatInsightConfiguration**](ThreatInsightConfiguration.md)|  | 

### Return type

[**ThreatInsightConfiguration**](ThreatInsightConfiguration.md)

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

