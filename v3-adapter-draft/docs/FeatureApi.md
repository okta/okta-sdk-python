# swagger_client.FeatureApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feature**](FeatureApi.md#get_feature) | **GET** /api/v1/features/{featureId} | 
[**list_feature_dependencies**](FeatureApi.md#list_feature_dependencies) | **GET** /api/v1/features/{featureId}/dependencies | 
[**list_feature_dependents**](FeatureApi.md#list_feature_dependents) | **GET** /api/v1/features/{featureId}/dependents | 
[**list_features**](FeatureApi.md#list_features) | **GET** /api/v1/features | 
[**update_feature_lifecycle**](FeatureApi.md#update_feature_lifecycle) | **POST** /api/v1/features/{featureId}/{lifecycle} | 

# **get_feature**
> Feature get_feature(feature_id)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FeatureApi(swagger_client.ApiClient(configuration))
feature_id = 'feature_id_example' # str | 

try:
    api_response = api_instance.get_feature(feature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->get_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 

### Return type

[**Feature**](Feature.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_feature_dependencies**
> list[Feature] list_feature_dependencies(feature_id)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FeatureApi(swagger_client.ApiClient(configuration))
feature_id = 'feature_id_example' # str | 

try:
    api_response = api_instance.list_feature_dependencies(feature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->list_feature_dependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 

### Return type

[**list[Feature]**](Feature.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_feature_dependents**
> list[Feature] list_feature_dependents(feature_id)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FeatureApi(swagger_client.ApiClient(configuration))
feature_id = 'feature_id_example' # str | 

try:
    api_response = api_instance.list_feature_dependents(feature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->list_feature_dependents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 

### Return type

[**list[Feature]**](Feature.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_features**
> list[Feature] list_features()



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FeatureApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_features()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->list_features: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Feature]**](Feature.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_feature_lifecycle**
> Feature update_feature_lifecycle(feature_id, lifecycle, mode=mode)



Success

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FeatureApi(swagger_client.ApiClient(configuration))
feature_id = 'feature_id_example' # str | 
lifecycle = 'lifecycle_example' # str | 
mode = 'mode_example' # str |  (optional)

try:
    api_response = api_instance.update_feature_lifecycle(feature_id, lifecycle, mode=mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeatureApi->update_feature_lifecycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 
 **lifecycle** | **str**|  | 
 **mode** | **str**|  | [optional] 

### Return type

[**Feature**](Feature.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

