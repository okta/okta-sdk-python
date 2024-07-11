# okta.PushProviderApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_push_provider**](PushProviderApi.md#create_push_provider) | **POST** /api/v1/push-providers | Create a Push Provider
[**delete_push_provider**](PushProviderApi.md#delete_push_provider) | **DELETE** /api/v1/push-providers/{pushProviderId} | Delete a Push Provider
[**get_push_provider**](PushProviderApi.md#get_push_provider) | **GET** /api/v1/push-providers/{pushProviderId} | Retrieve a Push Provider
[**list_push_providers**](PushProviderApi.md#list_push_providers) | **GET** /api/v1/push-providers | List all Push Providers
[**replace_push_provider**](PushProviderApi.md#replace_push_provider) | **PUT** /api/v1/push-providers/{pushProviderId} | Replace a Push Provider


# **create_push_provider**
> PushProvider create_push_provider(push_provider)

Create a Push Provider

Creates a new push provider

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.push_provider import PushProvider
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
    api_instance = okta.PushProviderApi(api_client)
    push_provider = okta.PushProvider() # PushProvider | 

    try:
        # Create a Push Provider
        api_response = api_instance.create_push_provider(push_provider)
        print("The response of PushProviderApi->create_push_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushProviderApi->create_push_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_provider** | [**PushProvider**](PushProvider.md)|  | 

### Return type

[**PushProvider**](PushProvider.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_push_provider**
> delete_push_provider(push_provider_id)

Delete a Push Provider

Deletes a push provider by `pushProviderId`. If the push provider is currently being used in the org by a custom authenticator, the delete will not be allowed.

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
    api_instance = okta.PushProviderApi(api_client)
    push_provider_id = 'push_provider_id_example' # str | Id of the push provider

    try:
        # Delete a Push Provider
        api_instance.delete_push_provider(push_provider_id)
    except Exception as e:
        print("Exception when calling PushProviderApi->delete_push_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_provider_id** | **str**| Id of the push provider | 

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_provider**
> PushProvider get_push_provider(push_provider_id)

Retrieve a Push Provider

Retrieves a push provider by `pushProviderId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.push_provider import PushProvider
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
    api_instance = okta.PushProviderApi(api_client)
    push_provider_id = 'push_provider_id_example' # str | Id of the push provider

    try:
        # Retrieve a Push Provider
        api_response = api_instance.get_push_provider(push_provider_id)
        print("The response of PushProviderApi->get_push_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushProviderApi->get_push_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_provider_id** | **str**| Id of the push provider | 

### Return type

[**PushProvider**](PushProvider.md)

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

# **list_push_providers**
> List[PushProvider] list_push_providers(type=type)

List all Push Providers

Lists all push providers

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.provider_type import ProviderType
from okta.models.push_provider import PushProvider
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
    api_instance = okta.PushProviderApi(api_client)
    type = okta.ProviderType() # ProviderType | Filters push providers by `providerType` (optional)

    try:
        # List all Push Providers
        api_response = api_instance.list_push_providers(type=type)
        print("The response of PushProviderApi->list_push_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushProviderApi->list_push_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ProviderType**](.md)| Filters push providers by &#x60;providerType&#x60; | [optional] 

### Return type

[**List[PushProvider]**](PushProvider.md)

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

# **replace_push_provider**
> PushProvider replace_push_provider(push_provider_id, push_provider)

Replace a Push Provider

Replaces a push provider by `pushProviderId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.push_provider import PushProvider
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
    api_instance = okta.PushProviderApi(api_client)
    push_provider_id = 'push_provider_id_example' # str | Id of the push provider
    push_provider = okta.PushProvider() # PushProvider | 

    try:
        # Replace a Push Provider
        api_response = api_instance.replace_push_provider(push_provider_id, push_provider)
        print("The response of PushProviderApi->replace_push_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushProviderApi->replace_push_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_provider_id** | **str**| Id of the push provider | 
 **push_provider** | [**PushProvider**](PushProvider.md)|  | 

### Return type

[**PushProvider**](PushProvider.md)

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

