# openapi_client.TrustedOriginApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_trusted_origin**](TrustedOriginApi.md#activate_trusted_origin) | **POST** /api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate | Activate a Trusted Origin
[**create_trusted_origin**](TrustedOriginApi.md#create_trusted_origin) | **POST** /api/v1/trustedOrigins | Create a Trusted Origin
[**deactivate_trusted_origin**](TrustedOriginApi.md#deactivate_trusted_origin) | **POST** /api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate | Deactivate a Trusted Origin
[**delete_trusted_origin**](TrustedOriginApi.md#delete_trusted_origin) | **DELETE** /api/v1/trustedOrigins/{trustedOriginId} | Delete a Trusted Origin
[**get_trusted_origin**](TrustedOriginApi.md#get_trusted_origin) | **GET** /api/v1/trustedOrigins/{trustedOriginId} | Retrieve a Trusted Origin
[**list_trusted_origins**](TrustedOriginApi.md#list_trusted_origins) | **GET** /api/v1/trustedOrigins | List all Trusted Origins
[**replace_trusted_origin**](TrustedOriginApi.md#replace_trusted_origin) | **PUT** /api/v1/trustedOrigins/{trustedOriginId} | Replace a Trusted Origin


# **activate_trusted_origin**
> TrustedOrigin activate_trusted_origin(trusted_origin_id)

Activate a Trusted Origin

Activates a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.trusted_origin import TrustedOrigin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the Trusted Origin

    try:
        # Activate a Trusted Origin
        api_response = api_instance.activate_trusted_origin(trusted_origin_id)
        print("The response of TrustedOriginApi->activate_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->activate_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the Trusted Origin | 

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

Create a Trusted Origin

Creates a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.trusted_origin import TrustedOrigin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    trusted_origin = openapi_client.TrustedOrigin() # TrustedOrigin | 

    try:
        # Create a Trusted Origin
        api_response = api_instance.create_trusted_origin(trusted_origin)
        print("The response of TrustedOriginApi->create_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->create_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_trusted_origin**
> TrustedOrigin deactivate_trusted_origin(trusted_origin_id)

Deactivate a Trusted Origin

Deactivates a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.trusted_origin import TrustedOrigin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the Trusted Origin

    try:
        # Deactivate a Trusted Origin
        api_response = api_instance.deactivate_trusted_origin(trusted_origin_id)
        print("The response of TrustedOriginApi->deactivate_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->deactivate_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the Trusted Origin | 

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

Delete a Trusted Origin

Deletes a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the Trusted Origin

    try:
        # Delete a Trusted Origin
        api_instance.delete_trusted_origin(trusted_origin_id)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->delete_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the Trusted Origin | 

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

Retrieve a Trusted Origin

Retrieves a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.trusted_origin import TrustedOrigin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the Trusted Origin

    try:
        # Retrieve a Trusted Origin
        api_response = api_instance.get_trusted_origin(trusted_origin_id)
        print("The response of TrustedOriginApi->get_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->get_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the Trusted Origin | 

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

List all Trusted Origins

Lists all trusted origins

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.trusted_origin import TrustedOrigin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    q = 'q_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = -1 # int |  (optional) (default to -1)

    try:
        # List all Trusted Origins
        api_response = api_instance.list_trusted_origins(q=q, filter=filter, after=after, limit=limit)
        print("The response of TrustedOriginApi->list_trusted_origins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->list_trusted_origins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

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

Replace a Trusted Origin

Replaces a trusted origin

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.trusted_origin import TrustedOrigin
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TrustedOriginApi(api_client)
    trusted_origin_id = '7j2PkU1nyNIDe26ZNufR' # str | `id` of the Trusted Origin
    trusted_origin = openapi_client.TrustedOrigin() # TrustedOrigin | 

    try:
        # Replace a Trusted Origin
        api_response = api_instance.replace_trusted_origin(trusted_origin_id, trusted_origin)
        print("The response of TrustedOriginApi->replace_trusted_origin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedOriginApi->replace_trusted_origin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**| &#x60;id&#x60; of the Trusted Origin | 
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

