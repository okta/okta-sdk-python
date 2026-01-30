# okta.SystemLogApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_log_events**](SystemLogApi.md#list_log_events) | **GET** /api/v1/logs | List all System Log events


# **list_log_events**
> List[LogEvent] list_log_events(since=since, until=until, after=after, filter=filter, q=q, limit=limit, sort_order=sort_order)

List all System Log events

Lists all System Log events  See [System Log query](https://developer.okta.com/docs/reference/system-log-query/) for further details and examples, and [System Log filters and search](https://help.okta.com/okta_help.htm?type=oie&id=csh-syslog-filters) for common use cases.  By default, 100 System Log events are returned. If there are more events, see the [header link](https://developer.okta.com/docs/api/#link-header) for the `next` link, or increase the number of returned objects using the `limit` parameter.  >**Note:** The value of the `clientSecret` property in the System Log is secured by a hashing function, and isn't the value used during authentication.

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
    since = '7 days prior to until' # str | Filters the lower time bound of the log events `published` property for bounded queries or persistence time for polling queries (optional) (default to '7 days prior to until')
    until = 'current time' # str | Filters the upper time bound of the log events `published` property for bounded queries or persistence time for polling queries. (optional) (default to 'current time')
    after = 'after_example' # str | Retrieves the next page of results. Okta returns a link in the HTTP Header (`rel=next`) that includes the after query parameter (optional)
    filter = 'filter_example' # str | Filter expression that filters the results. All operators except [ ] are supported. See [Filter](https://developer.okta.com/docs/api/#filter) and [Operators](https://developer.okta.com/docs/api/#operators). (optional)
    q = 'q_example' # str | Filters log events results by one or more case insensitive keywords. (optional)
    limit = 100 # int | Sets the number of results that are returned in the response (optional) (default to 100)
    sort_order = ASCENDING # str | The order of the returned events that are sorted by the `published` property (optional) (default to ASCENDING)

    try:
        # List all System Log events
        api_response = api_instance.list_log_events(since=since, until=until, after=after, filter=filter, q=q, limit=limit, sort_order=sort_order)
        print("The response of SystemLogApi->list_log_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemLogApi->list_log_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| Filters the lower time bound of the log events &#x60;published&#x60; property for bounded queries or persistence time for polling queries | [optional] [default to &#39;7 days prior to until&#39;]
 **until** | **str**| Filters the upper time bound of the log events &#x60;published&#x60; property for bounded queries or persistence time for polling queries. | [optional] [default to &#39;current time&#39;]
 **after** | **str**| Retrieves the next page of results. Okta returns a link in the HTTP Header (&#x60;rel&#x3D;next&#x60;) that includes the after query parameter | [optional] 
 **filter** | **str**| Filter expression that filters the results. All operators except [ ] are supported. See [Filter](https://developer.okta.com/docs/api/#filter) and [Operators](https://developer.okta.com/docs/api/#operators). | [optional] 
 **q** | **str**| Filters log events results by one or more case insensitive keywords. | [optional] 
 **limit** | **int**| Sets the number of results that are returned in the response | [optional] [default to 100]
 **sort_order** | **str**| The order of the returned events that are sorted by the &#x60;published&#x60; property | [optional] [default to ASCENDING]

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

