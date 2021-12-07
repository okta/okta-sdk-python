# swagger_client.LogApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logs**](LogApi.md#get_logs) | **GET** /api/v1/logs | Fetch a list of events from your Okta organization system log.

# **get_logs**
> list[LogEvent] get_logs(since=since, until=until, filter=filter, q=q, limit=limit, sort_order=sort_order, after=after)

Fetch a list of events from your Okta organization system log.

The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

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
api_instance = swagger_client.LogApi(swagger_client.ApiClient(configuration))
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
filter = 'filter_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 100 # int |  (optional) (default to 100)
sort_order = 'ASCENDING' # str |  (optional) (default to ASCENDING)
after = 'after_example' # str |  (optional)

try:
    # Fetch a list of events from your Okta organization system log.
    api_response = api_instance.get_logs(since=since, until=until, filter=filter, q=q, limit=limit, sort_order=sort_order, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **sort_order** | **str**|  | [optional] [default to ASCENDING]
 **after** | **str**|  | [optional] 

### Return type

[**list[LogEvent]**](LogEvent.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

