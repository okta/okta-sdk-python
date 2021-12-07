# swagger_client.ThreatInsightApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_configuration**](ThreatInsightApi.md#get_current_configuration) | **GET** /api/v1/threats/configuration | 
[**update_configuration**](ThreatInsightApi.md#update_configuration) | **POST** /api/v1/threats/configuration | 

# **get_current_configuration**
> ThreatInsightConfiguration get_current_configuration()



Gets current ThreatInsight configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThreatInsightApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_current_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatInsightApi->get_current_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ThreatInsightConfiguration**](ThreatInsightConfiguration.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> ThreatInsightConfiguration update_configuration(body)



Updates ThreatInsight configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ThreatInsightApi(swagger_client.ApiClient(configuration))
body = swagger_client.ThreatInsightConfiguration() # ThreatInsightConfiguration | 

try:
    api_response = api_instance.update_configuration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThreatInsightApi->update_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ThreatInsightConfiguration**](ThreatInsightConfiguration.md)|  | 

### Return type

[**ThreatInsightConfiguration**](ThreatInsightConfiguration.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

