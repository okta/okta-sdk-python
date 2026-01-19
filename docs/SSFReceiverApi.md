# okta.SSFReceiverApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_security_events_provider_instance**](SSFReceiverApi.md#activate_security_events_provider_instance) | **POST** /api/v1/security-events-providers/{securityEventProviderId}/lifecycle/activate | Activate a security events provider
[**create_security_events_provider_instance**](SSFReceiverApi.md#create_security_events_provider_instance) | **POST** /api/v1/security-events-providers | Create a security events provider
[**deactivate_security_events_provider_instance**](SSFReceiverApi.md#deactivate_security_events_provider_instance) | **POST** /api/v1/security-events-providers/{securityEventProviderId}/lifecycle/deactivate | Deactivate a security events provider
[**delete_security_events_provider_instance**](SSFReceiverApi.md#delete_security_events_provider_instance) | **DELETE** /api/v1/security-events-providers/{securityEventProviderId} | Delete a security events provider
[**get_security_events_provider_instance**](SSFReceiverApi.md#get_security_events_provider_instance) | **GET** /api/v1/security-events-providers/{securityEventProviderId} | Retrieve the security events provider
[**list_security_events_provider_instances**](SSFReceiverApi.md#list_security_events_provider_instances) | **GET** /api/v1/security-events-providers | List all security events providers
[**replace_security_events_provider_instance**](SSFReceiverApi.md#replace_security_events_provider_instance) | **PUT** /api/v1/security-events-providers/{securityEventProviderId} | Replace a security events provider


# **activate_security_events_provider_instance**
> SecurityEventsProviderResponse activate_security_events_provider_instance(security_event_provider_id)

Activate a security events provider

Activates a Security Events Provider instance by setting its status to `ACTIVE`. This operation resumes the flow of events from the Security Events Provider to Okta.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.security_events_provider_response import SecurityEventsProviderResponse
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
    api_instance = okta.SSFReceiverApi(api_client)
    security_event_provider_id = 'sse1qg25RpusjUP6m0g5' # str | `id` of the Security Events Provider instance

    try:
        # Activate a security events provider
        api_response = api_instance.activate_security_events_provider_instance(security_event_provider_id)
        print("The response of SSFReceiverApi->activate_security_events_provider_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->activate_security_events_provider_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_event_provider_id** | **str**| &#x60;id&#x60; of the Security Events Provider instance | 

### Return type

[**SecurityEventsProviderResponse**](SecurityEventsProviderResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_events_provider_instance**
> SecurityEventsProviderResponse create_security_events_provider_instance(instance)

Create a security events provider

Creates a Security Events Provider instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.security_events_provider_request import SecurityEventsProviderRequest
from okta.models.security_events_provider_response import SecurityEventsProviderResponse
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
    api_instance = okta.SSFReceiverApi(api_client)
    instance = okta.SecurityEventsProviderRequest() # SecurityEventsProviderRequest | 

    try:
        # Create a security events provider
        api_response = api_instance.create_security_events_provider_instance(instance)
        print("The response of SSFReceiverApi->create_security_events_provider_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->create_security_events_provider_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance** | [**SecurityEventsProviderRequest**](SecurityEventsProviderRequest.md)|  | 

### Return type

[**SecurityEventsProviderResponse**](SecurityEventsProviderResponse.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_security_events_provider_instance**
> SecurityEventsProviderResponse deactivate_security_events_provider_instance(security_event_provider_id)

Deactivate a security events provider

Deactivates a Security Events Provider instance by setting its status to `INACTIVE`. This operation stops the flow of events from the Security Events Provider to Okta.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.security_events_provider_response import SecurityEventsProviderResponse
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
    api_instance = okta.SSFReceiverApi(api_client)
    security_event_provider_id = 'sse1qg25RpusjUP6m0g5' # str | `id` of the Security Events Provider instance

    try:
        # Deactivate a security events provider
        api_response = api_instance.deactivate_security_events_provider_instance(security_event_provider_id)
        print("The response of SSFReceiverApi->deactivate_security_events_provider_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->deactivate_security_events_provider_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_event_provider_id** | **str**| &#x60;id&#x60; of the Security Events Provider instance | 

### Return type

[**SecurityEventsProviderResponse**](SecurityEventsProviderResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_security_events_provider_instance**
> delete_security_events_provider_instance(security_event_provider_id)

Delete a security events provider

Deletes a Security Events Provider instance specified by `id`

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
    api_instance = okta.SSFReceiverApi(api_client)
    security_event_provider_id = 'sse1qg25RpusjUP6m0g5' # str | `id` of the Security Events Provider instance

    try:
        # Delete a security events provider
        api_instance.delete_security_events_provider_instance(security_event_provider_id)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->delete_security_events_provider_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_event_provider_id** | **str**| &#x60;id&#x60; of the Security Events Provider instance | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_events_provider_instance**
> SecurityEventsProviderResponse get_security_events_provider_instance(security_event_provider_id)

Retrieve the security events provider

Retrieves the Security Events Provider instance specified by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.security_events_provider_response import SecurityEventsProviderResponse
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
    api_instance = okta.SSFReceiverApi(api_client)
    security_event_provider_id = 'sse1qg25RpusjUP6m0g5' # str | `id` of the Security Events Provider instance

    try:
        # Retrieve the security events provider
        api_response = api_instance.get_security_events_provider_instance(security_event_provider_id)
        print("The response of SSFReceiverApi->get_security_events_provider_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->get_security_events_provider_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_event_provider_id** | **str**| &#x60;id&#x60; of the Security Events Provider instance | 

### Return type

[**SecurityEventsProviderResponse**](SecurityEventsProviderResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_security_events_provider_instances**
> List[SecurityEventsProviderResponse] list_security_events_provider_instances()

List all security events providers

Lists all Security Events Provider instances

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.security_events_provider_response import SecurityEventsProviderResponse
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
    api_instance = okta.SSFReceiverApi(api_client)

    try:
        # List all security events providers
        api_response = api_instance.list_security_events_provider_instances()
        print("The response of SSFReceiverApi->list_security_events_provider_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->list_security_events_provider_instances: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SecurityEventsProviderResponse]**](SecurityEventsProviderResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_security_events_provider_instance**
> SecurityEventsProviderResponse replace_security_events_provider_instance(security_event_provider_id, instance)

Replace a security events provider

Replaces a Security Events Provider instance specified by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.security_events_provider_request import SecurityEventsProviderRequest
from okta.models.security_events_provider_response import SecurityEventsProviderResponse
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
    api_instance = okta.SSFReceiverApi(api_client)
    security_event_provider_id = 'sse1qg25RpusjUP6m0g5' # str | `id` of the Security Events Provider instance
    instance = okta.SecurityEventsProviderRequest() # SecurityEventsProviderRequest | 

    try:
        # Replace a security events provider
        api_response = api_instance.replace_security_events_provider_instance(security_event_provider_id, instance)
        print("The response of SSFReceiverApi->replace_security_events_provider_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSFReceiverApi->replace_security_events_provider_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_event_provider_id** | **str**| &#x60;id&#x60; of the Security Events Provider instance | 
 **instance** | [**SecurityEventsProviderRequest**](SecurityEventsProviderRequest.md)|  | 

### Return type

[**SecurityEventsProviderResponse**](SecurityEventsProviderResponse.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

