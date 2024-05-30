# openapi_client.FeatureApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature**](FeatureApi.md#get_feature) | **GET** /api/v1/features/{featureId} | Retrieve a Feature
[**list_feature_dependencies**](FeatureApi.md#list_feature_dependencies) | **GET** /api/v1/features/{featureId}/dependencies | List all Dependencies
[**list_feature_dependents**](FeatureApi.md#list_feature_dependents) | **GET** /api/v1/features/{featureId}/dependents | List all Dependents
[**list_features**](FeatureApi.md#list_features) | **GET** /api/v1/features | List all Features
[**update_feature_lifecycle**](FeatureApi.md#update_feature_lifecycle) | **POST** /api/v1/features/{featureId}/{lifecycle} | Update a Feature Lifecycle


# **get_feature**
> Feature get_feature(feature_id)

Retrieve a Feature

Retrieves a feature

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.feature import Feature
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
    api_instance = openapi_client.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the Feature

    try:
        # Retrieve a Feature
        api_response = api_instance.get_feature(feature_id)
        print("The response of FeatureApi->get_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->get_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the Feature | 

### Return type

[**Feature**](Feature.md)

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

# **list_feature_dependencies**
> List[Feature] list_feature_dependencies(feature_id)

List all Dependencies

Lists all dependencies

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.feature import Feature
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
    api_instance = openapi_client.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the Feature

    try:
        # List all Dependencies
        api_response = api_instance.list_feature_dependencies(feature_id)
        print("The response of FeatureApi->list_feature_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->list_feature_dependencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the Feature | 

### Return type

[**List[Feature]**](Feature.md)

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

# **list_feature_dependents**
> List[Feature] list_feature_dependents(feature_id)

List all Dependents

Lists all dependents

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.feature import Feature
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
    api_instance = openapi_client.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the Feature

    try:
        # List all Dependents
        api_response = api_instance.list_feature_dependents(feature_id)
        print("The response of FeatureApi->list_feature_dependents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->list_feature_dependents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the Feature | 

### Return type

[**List[Feature]**](Feature.md)

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

# **list_features**
> List[Feature] list_features()

List all Features

Lists all features

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.feature import Feature
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
    api_instance = openapi_client.FeatureApi(api_client)

    try:
        # List all Features
        api_response = api_instance.list_features()
        print("The response of FeatureApi->list_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->list_features: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Feature]**](Feature.md)

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

# **update_feature_lifecycle**
> Feature update_feature_lifecycle(feature_id, lifecycle, mode=mode)

Update a Feature Lifecycle

Updates a feature lifecycle

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.feature import Feature
from openapi_client.models.feature_lifecycle import FeatureLifecycle
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
    api_instance = openapi_client.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the Feature
    lifecycle = openapi_client.FeatureLifecycle() # FeatureLifecycle | Whether to `enable` or `disable` the feature
    mode = 'mode_example' # str |  (optional)

    try:
        # Update a Feature Lifecycle
        api_response = api_instance.update_feature_lifecycle(feature_id, lifecycle, mode=mode)
        print("The response of FeatureApi->update_feature_lifecycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->update_feature_lifecycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the Feature | 
 **lifecycle** | [**FeatureLifecycle**](.md)| Whether to &#x60;enable&#x60; or &#x60;disable&#x60; the feature | 
 **mode** | **str**|  | [optional] 

### Return type

[**Feature**](Feature.md)

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

