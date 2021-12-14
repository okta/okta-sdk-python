# swagger_client.InlineHookApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_inline_hook**](InlineHookApi.md#activate_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/lifecycle/activate | 
[**create_inline_hook**](InlineHookApi.md#create_inline_hook) | **POST** /api/v1/inlineHooks | 
[**deactivate_inline_hook**](InlineHookApi.md#deactivate_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/lifecycle/deactivate | 
[**delete_inline_hook**](InlineHookApi.md#delete_inline_hook) | **DELETE** /api/v1/inlineHooks/{inlineHookId} | 
[**execute_inline_hook**](InlineHookApi.md#execute_inline_hook) | **POST** /api/v1/inlineHooks/{inlineHookId}/execute | 
[**get_inline_hook**](InlineHookApi.md#get_inline_hook) | **GET** /api/v1/inlineHooks/{inlineHookId} | 
[**list_inline_hooks**](InlineHookApi.md#list_inline_hooks) | **GET** /api/v1/inlineHooks | 
[**update_inline_hook**](InlineHookApi.md#update_inline_hook) | **PUT** /api/v1/inlineHooks/{inlineHookId} | 

# **activate_inline_hook**
> InlineHook activate_inline_hook(inline_hook_id)



Activates the Inline Hook matching the provided id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InlineHookApi()
inline_hook_id = 'inline_hook_id_example' # str | 

try:
    api_response = api_instance.activate_inline_hook(inline_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->activate_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**|  | 

### Return type

[**InlineHook**](InlineHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inline_hook**
> InlineHook create_inline_hook(body)



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
api_instance = swagger_client.InlineHookApi(swagger_client.ApiClient(configuration))
body = swagger_client.InlineHook() # InlineHook | 

try:
    api_response = api_instance.create_inline_hook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->create_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineHook**](InlineHook.md)|  | 

### Return type

[**InlineHook**](InlineHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_inline_hook**
> InlineHook deactivate_inline_hook(inline_hook_id)



Deactivates the Inline Hook matching the provided id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InlineHookApi()
inline_hook_id = 'inline_hook_id_example' # str | 

try:
    api_response = api_instance.deactivate_inline_hook(inline_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->deactivate_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**|  | 

### Return type

[**InlineHook**](InlineHook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inline_hook**
> delete_inline_hook(inline_hook_id)



Deletes the Inline Hook matching the provided id. Once deleted, the Inline Hook is unrecoverable. As a safety precaution, only Inline Hooks with a status of INACTIVE are eligible for deletion.

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
api_instance = swagger_client.InlineHookApi(swagger_client.ApiClient(configuration))
inline_hook_id = 'inline_hook_id_example' # str | 

try:
    api_instance.delete_inline_hook(inline_hook_id)
except ApiException as e:
    print("Exception when calling InlineHookApi->delete_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_inline_hook**
> InlineHookResponse execute_inline_hook(body, inline_hook_id)



Executes the Inline Hook matching the provided inlineHookId using the request body as the input. This will send the provided data through the Channel and return a response if it matches the correct data contract. This execution endpoint should only be used for testing purposes.

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
api_instance = swagger_client.InlineHookApi(swagger_client.ApiClient(configuration))
body = swagger_client.InlineHookPayload() # InlineHookPayload | 
inline_hook_id = 'inline_hook_id_example' # str | 

try:
    api_response = api_instance.execute_inline_hook(body, inline_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->execute_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineHookPayload**](InlineHookPayload.md)|  | 
 **inline_hook_id** | **str**|  | 

### Return type

[**InlineHookResponse**](InlineHookResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inline_hook**
> InlineHook get_inline_hook(inline_hook_id)



Gets an inline hook by ID

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
api_instance = swagger_client.InlineHookApi(swagger_client.ApiClient(configuration))
inline_hook_id = 'inline_hook_id_example' # str | 

try:
    api_response = api_instance.get_inline_hook(inline_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->get_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_hook_id** | **str**|  | 

### Return type

[**InlineHook**](InlineHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inline_hooks**
> list[InlineHook] list_inline_hooks(type=type)



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
api_instance = swagger_client.InlineHookApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str |  (optional)

try:
    api_response = api_instance.list_inline_hooks(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->list_inline_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 

### Return type

[**list[InlineHook]**](InlineHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inline_hook**
> InlineHook update_inline_hook(body, inline_hook_id)



Updates an inline hook by ID

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
api_instance = swagger_client.InlineHookApi(swagger_client.ApiClient(configuration))
body = swagger_client.InlineHook() # InlineHook | 
inline_hook_id = 'inline_hook_id_example' # str | 

try:
    api_response = api_instance.update_inline_hook(body, inline_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InlineHookApi->update_inline_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineHook**](InlineHook.md)|  | 
 **inline_hook_id** | **str**|  | 

### Return type

[**InlineHook**](InlineHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

