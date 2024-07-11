# okta.InlineHookApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_inline_hook**](InlineHookApi.md#activate_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/lifecycle/activate | Activate an Inline Hook
[**create_inline_hook**](InlineHookApi.md#create_inline_hook) | **POST** /api/v1/inlineHooks | Create an Inline Hook
[**deactivate_inline_hook**](InlineHookApi.md#deactivate_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/lifecycle/deactivate | Deactivate an Inline Hook
[**delete_inline_hook**](InlineHookApi.md#delete_inline_hook) | **DELETE** /api/v1/inlineHooks/{inlineHookId} | Delete an Inline Hook
[**execute_inline_hook**](InlineHookApi.md#execute_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/execute | Execute an Inline Hook
[**get_inline_hook**](InlineHookApi.md#get_inline_hook) | **GET** /api/v1/inlineHooks/{inlineHookId} | Retrieve an Inline Hook
[**list_inline_hooks**](InlineHookApi.md#list_inline_hooks) | **GET** /api/v1/inlineHooks | List all Inline Hooks
[**replace_inline_hook**](InlineHookApi.md#replace_inline_hook) | **PUT** /api/v1/inlineHooks/{inlineHookId} | Replace an Inline Hook


# **activate_inline_hook**
> InlineHook activate_inline_hook(inline_hook_id)

Activate an Inline Hook

Activates the inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the Inline Hook

    try:
        # Activate an Inline Hook
        api_response = api_instance.activate_inline_hook(inline_hook_id)
        print("The response of InlineHookApi->activate_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->activate_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the Inline Hook | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **create_inline_hook**
> InlineHook create_inline_hook(inline_hook)

Create an Inline Hook

Creates an inline hook

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook = okta.InlineHook() # InlineHook | 

    try:
        # Create an Inline Hook
        api_response = api_instance.create_inline_hook(inline_hook)
        print("The response of InlineHookApi->create_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->create_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook** | [**InlineHook**](InlineHook.md)|  | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **deactivate_inline_hook**
> InlineHook deactivate_inline_hook(inline_hook_id)

Deactivate an Inline Hook

Deactivates the inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the Inline Hook

    try:
        # Deactivate an Inline Hook
        api_response = api_instance.deactivate_inline_hook(inline_hook_id)
        print("The response of InlineHookApi->deactivate_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->deactivate_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the Inline Hook | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **delete_inline_hook**
> delete_inline_hook(inline_hook_id)

Delete an Inline Hook

Deletes an inline hook by `inlineHookId`. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion.

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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the Inline Hook

    try:
        # Delete an Inline Hook
        api_instance.delete_inline_hook(inline_hook_id)
    except Exception as e:
        print("Exception when calling InlineHookApi->delete_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the Inline Hook | 

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

# **execute_inline_hook**
> InlineHookResponse execute_inline_hook(inline_hook_id, payload_data)

Execute an Inline Hook

Executes the inline hook by `inlineHookId` using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook_response import InlineHookResponse
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the Inline Hook
    payload_data = None # object | 

    try:
        # Execute an Inline Hook
        api_response = api_instance.execute_inline_hook(inline_hook_id, payload_data)
        print("The response of InlineHookApi->execute_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->execute_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the Inline Hook | 
 **payload_data** | **object**|  | 

### Return type

[**InlineHookResponse**](InlineHookResponse.md)

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

# **get_inline_hook**
> InlineHook get_inline_hook(inline_hook_id)

Retrieve an Inline Hook

Retrieves an inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the Inline Hook

    try:
        # Retrieve an Inline Hook
        api_response = api_instance.get_inline_hook(inline_hook_id)
        print("The response of InlineHookApi->get_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->get_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the Inline Hook | 

### Return type

[**InlineHook**](InlineHook.md)

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

# **list_inline_hooks**
> List[InlineHook] list_inline_hooks(type=type)

List all Inline Hooks

Lists all inline hooks

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    type = 'type_example' # str |  (optional)

    try:
        # List all Inline Hooks
        api_response = api_instance.list_inline_hooks(type=type)
        print("The response of InlineHookApi->list_inline_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->list_inline_hooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 

### Return type

[**List[InlineHook]**](InlineHook.md)

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

# **replace_inline_hook**
> InlineHook replace_inline_hook(inline_hook_id, inline_hook)

Replace an Inline Hook

Replaces an inline hook by `inlineHookId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.inline_hook import InlineHook
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
    api_instance = okta.InlineHookApi(api_client)
    inline_hook_id = 'Y7Rzrd4g4xj6WdKzrBHH' # str | `id` of the Inline Hook
    inline_hook = okta.InlineHook() # InlineHook | 

    try:
        # Replace an Inline Hook
        api_response = api_instance.replace_inline_hook(inline_hook_id, inline_hook)
        print("The response of InlineHookApi->replace_inline_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InlineHookApi->replace_inline_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**| &#x60;id&#x60; of the Inline Hook | 
 **inline_hook** | [**InlineHook**](InlineHook.md)|  | 

### Return type

[**InlineHook**](InlineHook.md)

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

