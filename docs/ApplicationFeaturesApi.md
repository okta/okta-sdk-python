# okta.ApplicationFeaturesApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature_for_application**](ApplicationFeaturesApi.md#get_feature_for_application) | **GET** /api/v1/apps/{appId}/features/{featureName} | Retrieve a feature
[**list_features_for_application**](ApplicationFeaturesApi.md#list_features_for_application) | **GET** /api/v1/apps/{appId}/features | List all features
[**update_feature_for_application**](ApplicationFeaturesApi.md#update_feature_for_application) | **PUT** /api/v1/apps/{appId}/features/{featureName} | Update a feature


# **get_feature_for_application**
> ApplicationFeature get_feature_for_application(app_id, feature_name)

Retrieve a feature

Retrieves a Feature object for an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_feature import ApplicationFeature
from okta.models.application_feature_type import ApplicationFeatureType
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
    api_instance = okta.ApplicationFeaturesApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    feature_name = okta.ApplicationFeatureType() # ApplicationFeatureType | Name of the Feature

    try:
        # Retrieve a feature
        api_response = api_instance.get_feature_for_application(app_id, feature_name)
        print("The response of ApplicationFeaturesApi->get_feature_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFeaturesApi->get_feature_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **feature_name** | [**ApplicationFeatureType**](.md)| Name of the Feature | 

### Return type

[**ApplicationFeature**](ApplicationFeature.md)

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

# **list_features_for_application**
> List[ApplicationFeature] list_features_for_application(app_id)

List all features

Lists all features for an app > **Note:** This request returns an error if provisioning isn't enabled for the app. > To set up provisioning, see [Update the default provisioning connection](/openapi/okta-management/management/tag/ApplicationConnections/#tag/ApplicationConnections/operation/updateDefaultProvisioningConnectionForApplication). 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_feature import ApplicationFeature
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
    api_instance = okta.ApplicationFeaturesApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # List all features
        api_response = api_instance.list_features_for_application(app_id)
        print("The response of ApplicationFeaturesApi->list_features_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFeaturesApi->list_features_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**List[ApplicationFeature]**](ApplicationFeature.md)

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

# **update_feature_for_application**
> ApplicationFeature update_feature_for_application(app_id, feature_name, update_feature_for_application_request)

Update a feature

Updates a Feature object for an app > **Note:** This endpoint supports partial updates. 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_feature import ApplicationFeature
from okta.models.application_feature_type import ApplicationFeatureType
from okta.models.update_feature_for_application_request import UpdateFeatureForApplicationRequest
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
    api_instance = okta.ApplicationFeaturesApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    feature_name = okta.ApplicationFeatureType() # ApplicationFeatureType | Name of the Feature
    update_feature_for_application_request = okta.UpdateFeatureForApplicationRequest() # UpdateFeatureForApplicationRequest | 

    try:
        # Update a feature
        api_response = api_instance.update_feature_for_application(app_id, feature_name, update_feature_for_application_request)
        print("The response of ApplicationFeaturesApi->update_feature_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFeaturesApi->update_feature_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **feature_name** | [**ApplicationFeatureType**](.md)| Name of the Feature | 
 **update_feature_for_application_request** | [**UpdateFeatureForApplicationRequest**](UpdateFeatureForApplicationRequest.md)|  | 

### Return type

[**ApplicationFeature**](ApplicationFeature.md)

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

