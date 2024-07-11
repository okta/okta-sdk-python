# okta.SystemLogApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_log_events**](SystemLogApi.md#list_log_events) | **GET** /api/v1/logs | List all System Log Events


# **list_log_events**
> List[LogEvent] list_log_events(since=since, until=until, filter=filter, q=q, limit=limit, sort_order=sort_order, after=after)

List all System Log Events

Lists all system log events. The Okta System Log API provides read access to your organization’s system log. This API provides more functionality than the Events API

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_event import LogEvent
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
    api_instance = okta.SystemLogApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    filter = 'filter_example' # str |  (optional)
    q = 'q_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    sort_order = 'ASCENDING' # str |  (optional) (default to 'ASCENDING')
    after = 'after_example' # str |  (optional)

    try:
        # List all System Log Events
        api_response = api_instance.list_log_events(since=since, until=until, filter=filter, q=q, limit=limit, sort_order=sort_order, after=after)
        print("The response of SystemLogApi->list_log_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->list_log_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **sort_order** | **str**|  | [optional] [default to &#39;ASCENDING&#39;]
 **after** | **str**|  | [optional] 

### Return type

[**List[LogEvent]**](LogEvent.md)

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

