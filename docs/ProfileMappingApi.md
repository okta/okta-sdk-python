# swagger_client.ProfileMappingApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile_mapping**](ProfileMappingApi.md#get_profile_mapping) | **GET** /api/v1/mappings/{mappingId} | Get Profile Mapping
[**list_profile_mappings**](ProfileMappingApi.md#list_profile_mappings) | **GET** /api/v1/mappings | 
[**update_profile_mapping**](ProfileMappingApi.md#update_profile_mapping) | **POST** /api/v1/mappings/{mappingId} | Update Profile Mapping

# **get_profile_mapping**
> ProfileMapping get_profile_mapping(mapping_id)

Get Profile Mapping

Fetches a single Profile Mapping referenced by its ID.

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
api_instance = swagger_client.ProfileMappingApi(swagger_client.ApiClient(configuration))
mapping_id = 'mapping_id_example' # str | 

try:
    # Get Profile Mapping
    api_response = api_instance.get_profile_mapping(mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileMappingApi->get_profile_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**|  | 

### Return type

[**ProfileMapping**](ProfileMapping.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profile_mappings**
> list[ProfileMapping] list_profile_mappings(after=after, limit=limit, source_id=source_id, target_id=target_id)



Enumerates Profile Mappings in your organization with pagination.

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
api_instance = swagger_client.ProfileMappingApi(swagger_client.ApiClient(configuration))
after = 'after_example' # str |  (optional)
limit = -1 # int |  (optional) (default to -1)
source_id = 'source_id_example' # str |  (optional)
target_id = '' # str |  (optional)

try:
    api_response = api_instance.list_profile_mappings(after=after, limit=limit, source_id=source_id, target_id=target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileMappingApi->list_profile_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]
 **source_id** | **str**|  | [optional] 
 **target_id** | **str**|  | [optional] 

### Return type

[**list[ProfileMapping]**](ProfileMapping.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_mapping**
> ProfileMapping update_profile_mapping(body, mapping_id)

Update Profile Mapping

Updates an existing Profile Mapping by adding, updating, or removing one or many Property Mappings.

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
api_instance = swagger_client.ProfileMappingApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProfileMapping() # ProfileMapping | 
mapping_id = 'mapping_id_example' # str | 

try:
    # Update Profile Mapping
    api_response = api_instance.update_profile_mapping(body, mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileMappingApi->update_profile_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProfileMapping**](ProfileMapping.md)|  | 
 **mapping_id** | **str**|  | 

### Return type

[**ProfileMapping**](ProfileMapping.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

