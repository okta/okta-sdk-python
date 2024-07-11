# okta.HookKeyApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hook_key**](HookKeyApi.md#create_hook_key) | **POST** /api/v1/hook-keys | Create a key
[**delete_hook_key**](HookKeyApi.md#delete_hook_key) | **DELETE** /api/v1/hook-keys/{hookKeyId} | Delete a key
[**get_hook_key**](HookKeyApi.md#get_hook_key) | **GET** /api/v1/hook-keys/{hookKeyId} | Retrieve a key
[**get_public_key**](HookKeyApi.md#get_public_key) | **GET** /api/v1/hook-keys/public/{publicKeyId} | Retrieve a public key
[**list_hook_keys**](HookKeyApi.md#list_hook_keys) | **GET** /api/v1/hook-keys | List all keys
[**replace_hook_key**](HookKeyApi.md#replace_hook_key) | **PUT** /api/v1/hook-keys/{hookKeyId} | Replace a key


# **create_hook_key**
> HookKey create_hook_key(key_request)

Create a key

Creates a key for use with other parts of the application, such as inline hooks  Use the key name to access this key for inline hook operations.  The total number of keys that you can create in an Okta org is limited to 50. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.hook_key import HookKey
from okta.models.key_request import KeyRequest
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
    api_instance = okta.HookKeyApi(api_client)
    key_request = okta.KeyRequest() # KeyRequest | 

    try:
        # Create a key
        api_response = api_instance.create_hook_key(key_request)
        print("The response of HookKeyApi->create_hook_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->create_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_request** | [**KeyRequest**](KeyRequest.md)|  | 

### Return type

[**HookKey**](HookKey.md)

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

# **delete_hook_key**
> delete_hook_key(hook_key_id)

Delete a key

Deletes a key by `hookKeyId`. After being deleted, the key is unrecoverable.  As a safety precaution, only keys that aren't being used are eligible for deletion. 

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
    api_instance = okta.HookKeyApi(api_client)
    hook_key_id = 'XreKU5laGwBkjOTehusG' # str | `id` of the Hook Key

    try:
        # Delete a key
        api_instance.delete_hook_key(hook_key_id)
    except Exception as e:
        print("Exception when calling HookKeyApi->delete_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_key_id** | **str**| &#x60;id&#x60; of the Hook Key | 

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

# **get_hook_key**
> HookKey get_hook_key(hook_key_id)

Retrieve a key

Retrieves a key by `hookKeyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.hook_key import HookKey
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
    api_instance = okta.HookKeyApi(api_client)
    hook_key_id = 'XreKU5laGwBkjOTehusG' # str | `id` of the Hook Key

    try:
        # Retrieve a key
        api_response = api_instance.get_hook_key(hook_key_id)
        print("The response of HookKeyApi->get_hook_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->get_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_key_id** | **str**| &#x60;id&#x60; of the Hook Key | 

### Return type

[**HookKey**](HookKey.md)

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

# **get_public_key**
> JsonWebKey get_public_key(public_key_id)

Retrieve a public key

Retrieves a public key by `keyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.HookKeyApi(api_client)
    public_key_id = 'FcH2P9Eg7wr0o8N2FuV0' # str | `id` of the Public Key

    try:
        # Retrieve a public key
        api_response = api_instance.get_public_key(public_key_id)
        print("The response of HookKeyApi->get_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->get_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_key_id** | **str**| &#x60;id&#x60; of the Public Key | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

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

# **list_hook_keys**
> List[HookKey] list_hook_keys()

List all keys

Lists all keys

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.hook_key import HookKey
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
    api_instance = okta.HookKeyApi(api_client)

    try:
        # List all keys
        api_response = api_instance.list_hook_keys()
        print("The response of HookKeyApi->list_hook_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->list_hook_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[HookKey]**](HookKey.md)

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

# **replace_hook_key**
> HookKey replace_hook_key(hook_key_id, key_request)

Replace a key

Replaces a key by `hookKeyId`  This request replaces existing properties after passing validation.  Note: The only parameter that you can update is the name of the key, which must be unique at all times. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.hook_key import HookKey
from okta.models.key_request import KeyRequest
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
    api_instance = okta.HookKeyApi(api_client)
    hook_key_id = 'XreKU5laGwBkjOTehusG' # str | `id` of the Hook Key
    key_request = okta.KeyRequest() # KeyRequest | 

    try:
        # Replace a key
        api_response = api_instance.replace_hook_key(hook_key_id, key_request)
        print("The response of HookKeyApi->replace_hook_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->replace_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_key_id** | **str**| &#x60;id&#x60; of the Hook Key | 
 **key_request** | [**KeyRequest**](KeyRequest.md)|  | 

### Return type

[**HookKey**](HookKey.md)

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

