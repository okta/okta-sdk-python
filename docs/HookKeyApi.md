# okta.HookKeyApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hook_key**](HookKeyApi.md#create_hook_key) | **POST** /api/v1/hook-keys | Create a key
[**delete_hook_key**](HookKeyApi.md#delete_hook_key) | **DELETE** /api/v1/hook-keys/{id} | Delete a key
[**get_hook_key**](HookKeyApi.md#get_hook_key) | **GET** /api/v1/hook-keys/{id} | Retrieve a key by ID
[**get_public_key**](HookKeyApi.md#get_public_key) | **GET** /api/v1/hook-keys/public/{keyId} | Retrieve a public key
[**list_hook_keys**](HookKeyApi.md#list_hook_keys) | **GET** /api/v1/hook-keys | List all keys
[**replace_hook_key**](HookKeyApi.md#replace_hook_key) | **PUT** /api/v1/hook-keys/{id} | Replace a key


# **create_hook_key**
> DetailedHookKeyInstance create_hook_key(key_request)

Create a key

Creates a key for use with other parts of the application, such as inline hooks  > **Note:**  Use the key name to access this key for inline hook operations.  The total number of keys that you can create in an Okta org is limited to 50.   The response is a [Key object](https://developer.okta.com/docs/reference/api/hook-keys/#key-object) that represents the  key that you create. The `id` property in the response serves as the unique ID for the key, which you can specify when  invoking other CRUD operations. The `keyId` provided in the response is the alias of the public key that you can use to get  details of the public key data in a separate call.  > **Note:** The keyId is the alias of the public key that you can use to retrieve the public key.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.detailed_hook_key_instance import DetailedHookKeyInstance
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

[**DetailedHookKeyInstance**](DetailedHookKeyInstance.md)

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
> delete_hook_key(id)

Delete a key

Deletes a key by `id`. After being deleted, the key is unrecoverable.  As a safety precaution, only keys that aren't being used are eligible for deletion. 

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
    id = 'XreKU5laGwBkjOTehusG' # str | ID of the Hook Key

    try:
        # Delete a key
        api_instance.delete_hook_key(id)
    except Exception as e:
        print("Exception when calling HookKeyApi->delete_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Hook Key | 

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
> HookKey get_hook_key(id)

Retrieve a key by ID

Retrieves the public portion of the Key object using the `id` parameter  >**Note:** The `?expand=publickey` query parameter optionally returns the full object including the details of the public key in the response body's `_embedded` property.

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
    id = 'XreKU5laGwBkjOTehusG' # str | ID of the Hook Key

    try:
        # Retrieve a key by ID
        api_response = api_instance.get_hook_key(id)
        print("The response of HookKeyApi->get_hook_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->get_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Hook Key | 

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
> Embedded get_public_key(key_id)

Retrieve a public key

Retrieves a public key by `keyId`  >**Note:** keyId is the alias of the public key.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.embedded import Embedded
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
    key_id = 'FcH2P9Eg7wr0o8N2FuV0' # str | id\" of the Public Key

    try:
        # Retrieve a public key
        api_response = api_instance.get_public_key(key_id)
        print("The response of HookKeyApi->get_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->get_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| id\&quot; of the Public Key | 

### Return type

[**Embedded**](Embedded.md)

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
> DetailedHookKeyInstance replace_hook_key(id, key_request)

Replace a key

Replaces a key by `id`  This request replaces existing properties after passing validation.  > **Note:** The only parameter that you can update is the name of the key, which must be unique at all times.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.detailed_hook_key_instance import DetailedHookKeyInstance
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
    id = 'XreKU5laGwBkjOTehusG' # str | ID of the Hook Key
    key_request = okta.KeyRequest() # KeyRequest | 

    try:
        # Replace a key
        api_response = api_instance.replace_hook_key(id, key_request)
        print("The response of HookKeyApi->replace_hook_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HookKeyApi->replace_hook_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Hook Key | 
 **key_request** | [**KeyRequest**](KeyRequest.md)|  | 

### Return type

[**DetailedHookKeyInstance**](DetailedHookKeyInstance.md)

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

