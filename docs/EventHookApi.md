# okta.EventHookApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_event_hook**](EventHookApi.md#activate_event_hook) | **POST** /api/v1/eventHooks/{eventHookId}/lifecycle/activate | Activate an event hook
[**create_event_hook**](EventHookApi.md#create_event_hook) | **POST** /api/v1/eventHooks | Create an event hook
[**deactivate_event_hook**](EventHookApi.md#deactivate_event_hook) | **POST** /api/v1/eventHooks/{eventHookId}/lifecycle/deactivate | Deactivate an event hook
[**delete_event_hook**](EventHookApi.md#delete_event_hook) | **DELETE** /api/v1/eventHooks/{eventHookId} | Delete an event hook
[**get_event_hook**](EventHookApi.md#get_event_hook) | **GET** /api/v1/eventHooks/{eventHookId} | Retrieve an event hook
[**list_event_hooks**](EventHookApi.md#list_event_hooks) | **GET** /api/v1/eventHooks | List all event hooks
[**replace_event_hook**](EventHookApi.md#replace_event_hook) | **PUT** /api/v1/eventHooks/{eventHookId} | Replace an event hook
[**verify_event_hook**](EventHookApi.md#verify_event_hook) | **POST** /api/v1/eventHooks/{eventHookId}/lifecycle/verify | Verify an event hook


# **activate_event_hook**
> EventHook activate_event_hook(event_hook_id)

Activate an event hook

Activates the event hook that matches the provided `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)
    event_hook_id = 'who8vt36qfNpCGz9H1e6' # str | `id` of the Event Hook

    try:
        # Activate an event hook
        api_response = api_instance.activate_event_hook(event_hook_id)
        print("The response of EventHookApi->activate_event_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->activate_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**| &#x60;id&#x60; of the Event Hook | 

### Return type

[**EventHook**](EventHook.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_hook**
> EventHook create_event_hook(event_hook)

Create an event hook

Creates a new event hook for your organization in `ACTIVE` status. You pass an event hook object in the JSON payload of your request. That object represents the set of required information about the event hook you're registering, including:   * The URI of your external service   * The [events](https://developer.okta.com/docs/reference/api/event-types/) in Okta you want to subscribe to   * An optional event hook filter that can reduce the number of event hook calls. This is a self-service Early Access (EA) feature.     See [Create an event hook filter](https://developer.okta.com/docs/concepts/event-hooks/#create-an-event-hook-filter).      Additionally, you can specify a secret API key for Okta to pass to your external service endpoint for security verification. Note that the API key you set here is unrelated to the Okta API token you must supply when making calls to Okta APIs. Optionally, you can specify extra headers that Okta passes to your external service with each call. Your external service must use a valid HTTPS endpoint.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)
    event_hook = okta.EventHook() # EventHook | 

    try:
        # Create an event hook
        api_response = api_instance.create_event_hook(event_hook)
        print("The response of EventHookApi->create_event_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->create_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook** | [**EventHook**](EventHook.md)|  | 

### Return type

[**EventHook**](EventHook.md)

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

# **deactivate_event_hook**
> EventHook deactivate_event_hook(event_hook_id)

Deactivate an event hook

Deactivates the event hook that matches the provided `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)
    event_hook_id = 'who8vt36qfNpCGz9H1e6' # str | `id` of the Event Hook

    try:
        # Deactivate an event hook
        api_response = api_instance.deactivate_event_hook(event_hook_id)
        print("The response of EventHookApi->deactivate_event_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->deactivate_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**| &#x60;id&#x60; of the Event Hook | 

### Return type

[**EventHook**](EventHook.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_hook**
> delete_event_hook(event_hook_id)

Delete an event hook

Deletes the event hook that matches the provided `id`. After deletion, the event hook is unrecoverable. As a safety precaution, you can only delete event hooks with a status of `INACTIVE`.

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
    api_instance = okta.EventHookApi(api_client)
    event_hook_id = 'who8vt36qfNpCGz9H1e6' # str | `id` of the Event Hook

    try:
        # Delete an event hook
        api_instance.delete_event_hook(event_hook_id)
    except Exception as e:
        print("Exception when calling EventHookApi->delete_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**| &#x60;id&#x60; of the Event Hook | 

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

# **get_event_hook**
> EventHook get_event_hook(event_hook_id)

Retrieve an event hook

Retrieves an event hook

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)
    event_hook_id = 'who8vt36qfNpCGz9H1e6' # str | `id` of the Event Hook

    try:
        # Retrieve an event hook
        api_response = api_instance.get_event_hook(event_hook_id)
        print("The response of EventHookApi->get_event_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->get_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**| &#x60;id&#x60; of the Event Hook | 

### Return type

[**EventHook**](EventHook.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_hooks**
> List[EventHook] list_event_hooks()

List all event hooks

Lists all event hooks

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)

    try:
        # List all event hooks
        api_response = api_instance.list_event_hooks()
        print("The response of EventHookApi->list_event_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->list_event_hooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EventHook]**](EventHook.md)

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

# **replace_event_hook**
> EventHook replace_event_hook(event_hook_id, event_hook)

Replace an event hook

Replaces an event hook. Okta validates the new properties before replacing the existing values. Some event hook properties are immutable and can't be updated. Refer to the parameter description in the request body schema.  >**Note:** Updating the `channel` property requires you to verify the hook again.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)
    event_hook_id = 'who8vt36qfNpCGz9H1e6' # str | `id` of the Event Hook
    event_hook = okta.EventHook() # EventHook | 

    try:
        # Replace an event hook
        api_response = api_instance.replace_event_hook(event_hook_id, event_hook)
        print("The response of EventHookApi->replace_event_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->replace_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**| &#x60;id&#x60; of the Event Hook | 
 **event_hook** | [**EventHook**](EventHook.md)|  | 

### Return type

[**EventHook**](EventHook.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_event_hook**
> EventHook verify_event_hook(event_hook_id)

Verify an event hook

Verifies that the event hook matches the provided `eventHookId`. To verify ownership, your endpoint must send information back to Okta in JSON format. See [Event hooks](https://developer.okta.com/docs/concepts/event-hooks/#one-time-verification-request).  Only `ACTIVE` and `VERIFIED` event hooks can receive events from Okta.  If a response is not received within 3 seconds, the outbound request times out. One retry is attempted after a timeout or error response. If a successful response still isn't received, this operation returns a 400 error with more information about the failure.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.event_hook import EventHook
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
    api_instance = okta.EventHookApi(api_client)
    event_hook_id = 'who8vt36qfNpCGz9H1e6' # str | `id` of the Event Hook

    try:
        # Verify an event hook
        api_response = api_instance.verify_event_hook(event_hook_id)
        print("The response of EventHookApi->verify_event_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventHookApi->verify_event_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**| &#x60;id&#x60; of the Event Hook | 

### Return type

[**EventHook**](EventHook.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

