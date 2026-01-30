# okta.TrustedOriginApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_trusted_origin**](TrustedOriginApi.md#activate_trusted_origin) | **POST** /api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate | Activate a trusted origin
[**create_trusted_origin**](TrustedOriginApi.md#create_trusted_origin) | **POST** /api/v1/trustedOrigins | Create a trusted origin
[**deactivate_trusted_origin**](TrustedOriginApi.md#deactivate_trusted_origin) | **POST** /api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate | Deactivate a trusted origin
[**delete_trusted_origin**](TrustedOriginApi.md#delete_trusted_origin) | **DELETE** /api/v1/trustedOrigins/{trustedOriginId} | Delete a trusted origin
[**get_trusted_origin**](TrustedOriginApi.md#get_trusted_origin) | **GET** /api/v1/trustedOrigins/{trustedOriginId} | Retrieve a trusted origin
[**list_trusted_origins**](TrustedOriginApi.md#list_trusted_origins) | **GET** /api/v1/trustedOrigins | List all trusted origins
[**replace_trusted_origin**](TrustedOriginApi.md#replace_trusted_origin) | **PUT** /api/v1/trustedOrigins/{trustedOriginId} | Replace a trusted origin


# **activate_trusted_origin**
> TrustedOrigin activate_trusted_origin(trusted_origin_id)

Activate a trusted origin

Activates a trusted origin. Sets the `status` to `ACTIVE`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.trusted_origin import TrustedOrigin
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
    api_instance = okta.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the trusted origin

    try:
        # Activate a trusted origin
        api_response = api_instance.activate_trusted_origin(trusted_origin_id)
        print("The response of TrustedOriginApi->activate_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->activate_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the trusted origin | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

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

# **create_trusted_origin**
> TrustedOrigin create_trusted_origin(trusted_origin)

Create a trusted origin

Creates a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.trusted_origin import TrustedOrigin
from okta.models.trusted_origin_write import TrustedOriginWrite
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
    api_instance = okta.TrustedOriginApi(api_client)
    trusted_origin = okta.TrustedOriginWrite() # TrustedOriginWrite | 

    try:
        # Create a trusted origin
        api_response = api_instance.create_trusted_origin(trusted_origin)
        print("The response of TrustedOriginApi->create_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->create_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin** | [**TrustedOriginWrite**](TrustedOriginWrite.md)|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

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

# **deactivate_trusted_origin**
> TrustedOrigin deactivate_trusted_origin(trusted_origin_id)

Deactivate a trusted origin

Deactivates a trusted origin. Sets the `status` to `INACTIVE`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.trusted_origin import TrustedOrigin
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
    api_instance = okta.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the trusted origin

    try:
        # Deactivate a trusted origin
        api_response = api_instance.deactivate_trusted_origin(trusted_origin_id)
        print("The response of TrustedOriginApi->deactivate_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->deactivate_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the trusted origin | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

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

# **delete_trusted_origin**
> delete_trusted_origin(trusted_origin_id)

Delete a trusted origin

Deletes a trusted origin

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
    api_instance = okta.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the trusted origin

    try:
        # Delete a trusted origin
        api_instance.delete_trusted_origin(trusted_origin_id)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->delete_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the trusted origin | 

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
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trusted_origin**
> TrustedOrigin get_trusted_origin(trusted_origin_id)

Retrieve a trusted origin

Retrieves a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.trusted_origin import TrustedOrigin
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
    api_instance = okta.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the trusted origin

    try:
        # Retrieve a trusted origin
        api_response = api_instance.get_trusted_origin(trusted_origin_id)
        print("The response of TrustedOriginApi->get_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->get_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the trusted origin | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

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

# **list_trusted_origins**
> List[TrustedOrigin] list_trusted_origins(q=q, filter=filter, after=after, limit=limit)

List all trusted origins

Lists all trusted origins

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.trusted_origin import TrustedOrigin
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
    api_instance = okta.TrustedOriginApi(api_client)
    q = 'q_example' # str | A search string that prefix matches against the `name` and `origin` (optional)
    filter = 'name eq \"Example trusted origin\"' # str | [Filter](https://developer.okta.com/docs/api/#filter) trusted origins with a supported expression for a subset of properties. You can filter on the following properties: `name`, `origin`, `status`, and `type` (type of scopes).  (optional)
    after = 'after_example' # str | After cursor provided by a prior request (optional)
    limit = 20 # int | Specifies the number of results (optional) (default to 20)

    try:
        # List all trusted origins
        api_response = api_instance.list_trusted_origins(q=q, filter=filter, after=after, limit=limit)
        print("The response of TrustedOriginApi->list_trusted_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->list_trusted_origins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| A search string that prefix matches against the &#x60;name&#x60; and &#x60;origin&#x60; | [optional] 
 **filter** | **str**| [Filter](https://developer.okta.com/docs/api/#filter) trusted origins with a supported expression for a subset of properties. You can filter on the following properties: &#x60;name&#x60;, &#x60;origin&#x60;, &#x60;status&#x60;, and &#x60;type&#x60; (type of scopes).  | [optional] 
 **after** | **str**| After cursor provided by a prior request | [optional] 
 **limit** | **int**| Specifies the number of results | [optional] [default to 20]

### Return type

[**List[TrustedOrigin]**](TrustedOrigin.md)

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

# **replace_trusted_origin**
> TrustedOrigin replace_trusted_origin(trusted_origin_id, trusted_origin)

Replace a trusted origin

Replaces a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.trusted_origin import TrustedOrigin
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
    api_instance = okta.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the trusted origin
    trusted_origin = okta.TrustedOrigin() # TrustedOrigin | 

    try:
        # Replace a trusted origin
        api_response = api_instance.replace_trusted_origin(trusted_origin_id, trusted_origin)
        print("The response of TrustedOriginApi->replace_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->replace_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the trusted origin | 
 **trusted_origin** | [**TrustedOrigin**](TrustedOrigin.md)|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

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

