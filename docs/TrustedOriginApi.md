# swagger_client.TrustedOriginApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_origin**](TrustedOriginApi.md#activate_origin) | **POST** /api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate | 
[**create_origin**](TrustedOriginApi.md#create_origin) | **POST** /api/v1/trustedOrigins | 
[**deactivate_origin**](TrustedOriginApi.md#deactivate_origin) | **POST** /api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate | 
[**delete_origin**](TrustedOriginApi.md#delete_origin) | **DELETE** /api/v1/trustedOrigins/{trustedOriginId} | 
[**get_origin**](TrustedOriginApi.md#get_origin) | **GET** /api/v1/trustedOrigins/{trustedOriginId} | 
[**list_origins**](TrustedOriginApi.md#list_origins) | **GET** /api/v1/trustedOrigins | 
[**update_origin**](TrustedOriginApi.md#update_origin) | **PUT** /api/v1/trustedOrigins/{trustedOriginId} | 

# **activate_origin**
> TrustedOrigin activate_origin(trusted_origin_id)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
trusted_origin_id = 'trusted_origin_id_example' # str | 

try:
    api_response = api_instance.activate_origin(trusted_origin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->activate_origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_origin**
> TrustedOrigin create_origin(body)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrustedOrigin() # TrustedOrigin | 

try:
    api_response = api_instance.create_origin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->create_origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustedOrigin**](TrustedOrigin.md)|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_origin**
> TrustedOrigin deactivate_origin(trusted_origin_id)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
trusted_origin_id = 'trusted_origin_id_example' # str | 

try:
    api_response = api_instance.deactivate_origin(trusted_origin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->deactivate_origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_origin**
> delete_origin(trusted_origin_id)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
trusted_origin_id = 'trusted_origin_id_example' # str | 

try:
    api_instance.delete_origin(trusted_origin_id)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->delete_origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_origin**
> TrustedOrigin get_origin(trusted_origin_id)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
trusted_origin_id = 'trusted_origin_id_example' # str | 

try:
    api_response = api_instance.get_origin(trusted_origin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->get_origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusted_origin_id** | **str**|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_origins**
> list[TrustedOrigin] list_origins(q=q, filter=filter, after=after, limit=limit)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str |  (optional)
filter = 'filter_example' # str |  (optional)
after = 'after_example' # str |  (optional)
limit = -1 # int |  (optional) (default to -1)

try:
    api_response = api_instance.list_origins(q=q, filter=filter, after=after, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->list_origins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]

### Return type

[**list[TrustedOrigin]**](TrustedOrigin.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_origin**
> TrustedOrigin update_origin(body, trusted_origin_id)



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
api_instance = swagger_client.TrustedOriginApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrustedOrigin() # TrustedOrigin | 
trusted_origin_id = 'trusted_origin_id_example' # str | 

try:
    api_response = api_instance.update_origin(body, trusted_origin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrustedOriginApi->update_origin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrustedOrigin**](TrustedOrigin.md)|  | 
 **trusted_origin_id** | **str**|  | 

### Return type

[**TrustedOrigin**](TrustedOrigin.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

