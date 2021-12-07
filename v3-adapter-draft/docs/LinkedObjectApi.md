# swagger_client.LinkedObjectApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_linked_object_definition**](LinkedObjectApi.md#add_linked_object_definition) | **POST** /api/v1/meta/schemas/user/linkedObjects | 
[**delete_linked_object_definition**](LinkedObjectApi.md#delete_linked_object_definition) | **DELETE** /api/v1/meta/schemas/user/linkedObjects/{linkedObjectName} | 
[**get_linked_object_definition**](LinkedObjectApi.md#get_linked_object_definition) | **GET** /api/v1/meta/schemas/user/linkedObjects/{linkedObjectName} | 
[**list_linked_object_definitions**](LinkedObjectApi.md#list_linked_object_definitions) | **GET** /api/v1/meta/schemas/user/linkedObjects | 

# **add_linked_object_definition**
> LinkedObject add_linked_object_definition(body)



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
api_instance = swagger_client.LinkedObjectApi(swagger_client.ApiClient(configuration))
body = swagger_client.LinkedObject() # LinkedObject | 

try:
    api_response = api_instance.add_linked_object_definition(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedObjectApi->add_linked_object_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LinkedObject**](LinkedObject.md)|  | 

### Return type

[**LinkedObject**](LinkedObject.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_object_definition**
> delete_linked_object_definition(linked_object_name)



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
api_instance = swagger_client.LinkedObjectApi(swagger_client.ApiClient(configuration))
linked_object_name = 'linked_object_name_example' # str | 

try:
    api_instance.delete_linked_object_definition(linked_object_name)
except ApiException as e:
    print("Exception when calling LinkedObjectApi->delete_linked_object_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_object_definition**
> LinkedObject get_linked_object_definition(linked_object_name)



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
api_instance = swagger_client.LinkedObjectApi(swagger_client.ApiClient(configuration))
linked_object_name = 'linked_object_name_example' # str | 

try:
    api_response = api_instance.get_linked_object_definition(linked_object_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedObjectApi->get_linked_object_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object_name** | **str**|  | 

### Return type

[**LinkedObject**](LinkedObject.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_linked_object_definitions**
> list[LinkedObject] list_linked_object_definitions()



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
api_instance = swagger_client.LinkedObjectApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_linked_object_definitions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedObjectApi->list_linked_object_definitions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LinkedObject]**](LinkedObject.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

