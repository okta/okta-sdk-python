# okta.LogStreamApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_log_stream**](LogStreamApi.md#activate_log_stream) | **POST** /api/v1/logStreams/{logStreamId}/lifecycle/activate | Activate a log stream
[**create_log_stream**](LogStreamApi.md#create_log_stream) | **POST** /api/v1/logStreams | Create a log stream
[**deactivate_log_stream**](LogStreamApi.md#deactivate_log_stream) | **POST** /api/v1/logStreams/{logStreamId}/lifecycle/deactivate | Deactivate a log stream
[**delete_log_stream**](LogStreamApi.md#delete_log_stream) | **DELETE** /api/v1/logStreams/{logStreamId} | Delete a log stream
[**get_log_stream**](LogStreamApi.md#get_log_stream) | **GET** /api/v1/logStreams/{logStreamId} | Retrieve a log stream
[**list_log_streams**](LogStreamApi.md#list_log_streams) | **GET** /api/v1/logStreams | List all log streams
[**replace_log_stream**](LogStreamApi.md#replace_log_stream) | **PUT** /api/v1/logStreams/{logStreamId} | Replace a log stream


# **activate_log_stream**
> LogStream activate_log_stream(log_stream_id)

Activate a log stream

Activates a log stream by `logStreamId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream import LogStream
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
    api_instance = okta.LogStreamApi(api_client)
    log_stream_id = '0oa1orzg0CHSgPcjZ0g4' # str | Unique identifier for the log stream

    try:
        # Activate a log stream
        api_response = api_instance.activate_log_stream(log_stream_id)
        print("The response of LogStreamApi->activate_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogStreamApi->activate_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| Unique identifier for the log stream | 

### Return type

[**LogStream**](LogStream.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_log_stream**
> LogStream create_log_stream(instance)

Create a log stream

Creates a new log stream object

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream import LogStream
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
    api_instance = okta.LogStreamApi(api_client)
    instance = okta.LogStream() # LogStream | 

    try:
        # Create a log stream
        api_response = api_instance.create_log_stream(instance)
        print("The response of LogStreamApi->create_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogStreamApi->create_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**LogStream**](LogStream.md)|  | 

### Return type

[**LogStream**](LogStream.md)

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

# **deactivate_log_stream**
> LogStream deactivate_log_stream(log_stream_id)

Deactivate a log stream

Deactivates a log stream by `logStreamId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream import LogStream
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
    api_instance = okta.LogStreamApi(api_client)
    log_stream_id = '0oa1orzg0CHSgPcjZ0g4' # str | Unique identifier for the log stream

    try:
        # Deactivate a log stream
        api_response = api_instance.deactivate_log_stream(log_stream_id)
        print("The response of LogStreamApi->deactivate_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogStreamApi->deactivate_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| Unique identifier for the log stream | 

### Return type

[**LogStream**](LogStream.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_log_stream**
> delete_log_stream(log_stream_id)

Delete a log stream

Deletes a log stream object from your org by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
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
    api_instance = okta.LogStreamApi(api_client)
    log_stream_id = '0oa1orzg0CHSgPcjZ0g4' # str | Unique identifier for the log stream

    try:
        # Delete a log stream
        api_instance.delete_log_stream(log_stream_id)
    except Exception as e:
        print("Exception when calling LogStreamApi->delete_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| Unique identifier for the log stream | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_stream**
> LogStream get_log_stream(log_stream_id)

Retrieve a log stream

Retrieves a log stream object by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream import LogStream
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
    api_instance = okta.LogStreamApi(api_client)
    log_stream_id = '0oa1orzg0CHSgPcjZ0g4' # str | Unique identifier for the log stream

    try:
        # Retrieve a log stream
        api_response = api_instance.get_log_stream(log_stream_id)
        print("The response of LogStreamApi->get_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogStreamApi->get_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| Unique identifier for the log stream | 

### Return type

[**LogStream**](LogStream.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_log_streams**
> List[LogStream] list_log_streams(after=after, limit=limit, filter=filter)

List all log streams

Lists all log stream objects in your org. You can request a paginated list or a subset of log streams that match a supported filter expression.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream import LogStream
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
    api_instance = okta.LogStreamApi(api_client)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    filter = 'type eq \"aws_eventbridge\"' # str | An expression that [filters](/#filter) the returned objects. You can only use the `eq` operator on either the `status` or `type` properties in the filter expression. (optional)

    try:
        # List all log streams
        api_response = api_instance.list_log_streams(after=after, limit=limit, filter=filter)
        print("The response of LogStreamApi->list_log_streams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogStreamApi->list_log_streams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **filter** | **str**| An expression that [filters](/#filter) the returned objects. You can only use the &#x60;eq&#x60; operator on either the &#x60;status&#x60; or &#x60;type&#x60; properties in the filter expression. | [optional] 

### Return type

[**List[LogStream]**](LogStream.md)

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

# **replace_log_stream**
> LogStream replace_log_stream(log_stream_id, instance)

Replace a log stream

Replaces the log stream object properties for a given ID.  This operation is typically used to update the configuration of a log stream. Depending on the type of log stream you want to update, certain properties can't be modified after the log stream is initially created. Use the [Retrieve the log stream schema for the schema type](/openapi/okta-management/management/tag/Schema/#tag/Schema/operation/getLogStreamSchema) request to determine which properties you can update for the specific log stream type. Log stream properties with the `\"writeOnce\" : true` attribute can't be updated after creation. You must still specify these `writeOnce` properties in the request body with the original values in the PUT request.  > **Note:** You don't have to specify properties that have both the `\"writeOnce\": true` and the `\"writeOnly\": true` attributes in the PUT request body. These property values are ignored even if you add them in the PUT request body.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream import LogStream
from okta.models.log_stream_put_schema import LogStreamPutSchema
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
    api_instance = okta.LogStreamApi(api_client)
    log_stream_id = '0oa1orzg0CHSgPcjZ0g4' # str | Unique identifier for the log stream
    instance = okta.LogStreamPutSchema() # LogStreamPutSchema | 

    try:
        # Replace a log stream
        api_response = api_instance.replace_log_stream(log_stream_id, instance)
        print("The response of LogStreamApi->replace_log_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogStreamApi->replace_log_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_id** | **str**| Unique identifier for the log stream | 
 **instance** | [**LogStreamPutSchema**](LogStreamPutSchema.md)|  | 

### Return type

[**LogStream**](LogStream.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

