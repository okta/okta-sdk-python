# okta.FeatureApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature**](FeatureApi.md#get_feature) | **GET** /api/v1/features/{featureId} | Retrieve a feature
[**list_feature_dependencies**](FeatureApi.md#list_feature_dependencies) | **GET** /api/v1/features/{featureId}/dependencies | List all dependencies
[**list_feature_dependents**](FeatureApi.md#list_feature_dependents) | **GET** /api/v1/features/{featureId}/dependents | List all dependents
[**list_features**](FeatureApi.md#list_features) | **GET** /api/v1/features | List all features
[**update_feature_lifecycle**](FeatureApi.md#update_feature_lifecycle) | **POST** /api/v1/features/{featureId}/{lifecycle} | Update a feature lifecycle


# **get_feature**
> Feature get_feature(feature_id)

Retrieve a feature

Retrieves a feature by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.feature import Feature
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
    api_instance = okta.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the feature

    try:
        # Retrieve a feature
        api_response = api_instance.get_feature(feature_id)
        print("The response of FeatureApi->get_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->get_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the feature | 

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

List all dependencies

Lists all feature dependencies for a specified feature.  A feature's dependencies are the features that it requires to be enabled in order for itself to be enabled.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.feature import Feature
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
    api_instance = okta.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the feature

    try:
        # List all dependencies
        api_response = api_instance.list_feature_dependencies(feature_id)
        print("The response of FeatureApi->list_feature_dependencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->list_feature_dependencies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the feature | 

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

List all dependents

Lists all feature dependents for the specified feature.  A feature's dependents are the features that need to be disabled in order for the feature itself to be disabled.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.feature import Feature
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
    api_instance = okta.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the feature

    try:
        # List all dependents
        api_response = api_instance.list_feature_dependents(feature_id)
        print("The response of FeatureApi->list_feature_dependents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->list_feature_dependents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the feature | 

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

List all features

Lists all self-service features for your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.feature import Feature
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
    api_instance = okta.FeatureApi(api_client)

    try:
        # List all features
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

Update a feature lifecycle

Updates a feature's lifecycle status. Use this endpoint to enable or disable a feature for your org.  Use the `mode=force` parameter to override dependency restrictions for a particular feature. Normally, you can't enable a feature if it has one or more dependencies that aren't enabled.  When you use the `mode=force` parameter while enabling a feature, Okta first tries to enable any disabled features that this feature may have as dependencies. If you don't pass the `mode=force` parameter and the feature has dependencies that need to be enabled before the feature is enabled, a 400 error is returned.  When you use the `mode=force` parameter while disabling a feature, Okta first tries to disable any enabled features that this feature may have as dependents. If you don't pass the `mode=force` parameter and the feature has dependents that need to be disabled before the feature is disabled, a 400 error is returned.  The following chart shows the different state transitions for a feature.  ![State transitions of a feature](../../../../../images/features/update-ssfeat-flowchart.png '#width=500px;')

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.feature import Feature
from okta.models.feature_lifecycle import FeatureLifecycle
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
    api_instance = okta.FeatureApi(api_client)
    feature_id = 'R5HjqNn1pEqWGy48E9jg' # str | `id` of the feature
    lifecycle = okta.FeatureLifecycle() # FeatureLifecycle | Whether to `ENABLE` or `DISABLE` the feature
    mode = 'mode_example' # str | Indicates if you want to force enable or disable a feature. Supported value is `force`. (optional)

    try:
        # Update a feature lifecycle
        api_response = api_instance.update_feature_lifecycle(feature_id, lifecycle, mode=mode)
        print("The response of FeatureApi->update_feature_lifecycle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeatureApi->update_feature_lifecycle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**| &#x60;id&#x60; of the feature | 
 **lifecycle** | [**FeatureLifecycle**](.md)| Whether to &#x60;ENABLE&#x60; or &#x60;DISABLE&#x60; the feature | 
 **mode** | **str**| Indicates if you want to force enable or disable a feature. Supported value is &#x60;force&#x60;. | [optional] 

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

