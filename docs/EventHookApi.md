# swagger_client.EventHookApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_event_hook**](EventHookApi.md#activate_event_hook) | **POST** /api/v1/eventHooks/{eventHookId}/lifecycle/activate | 
[**create_event_hook**](EventHookApi.md#create_event_hook) | **POST** /api/v1/eventHooks | 
[**deactivate_event_hook**](EventHookApi.md#deactivate_event_hook) | **POST** /api/v1/eventHooks/{eventHookId}/lifecycle/deactivate | 
[**delete_event_hook**](EventHookApi.md#delete_event_hook) | **DELETE** /api/v1/eventHooks/{eventHookId} | 
[**get_event_hook**](EventHookApi.md#get_event_hook) | **GET** /api/v1/eventHooks/{eventHookId} | 
[**list_event_hooks**](EventHookApi.md#list_event_hooks) | **GET** /api/v1/eventHooks | 
[**update_event_hook**](EventHookApi.md#update_event_hook) | **PUT** /api/v1/eventHooks/{eventHookId} | 
[**verify_event_hook**](EventHookApi.md#verify_event_hook) | **POST** /api/v1/eventHooks/{eventHookId}/lifecycle/verify | 

# **activate_event_hook**
> EventHook activate_event_hook(event_hook_id)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
event_hook_id = 'event_hook_id_example' # str | 

try:
    api_response = api_instance.activate_event_hook(event_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->activate_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**|  | 

### Return type

[**EventHook**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_hook**
> EventHook create_event_hook(body)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
body = swagger_client.EventHook() # EventHook | 

try:
    api_response = api_instance.create_event_hook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->create_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventHook**](EventHook.md)|  | 

### Return type

[**EventHook**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_event_hook**
> EventHook deactivate_event_hook(event_hook_id)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
event_hook_id = 'event_hook_id_example' # str | 

try:
    api_response = api_instance.deactivate_event_hook(event_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->deactivate_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**|  | 

### Return type

[**EventHook**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_hook**
> delete_event_hook(event_hook_id)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
event_hook_id = 'event_hook_id_example' # str | 

try:
    api_instance.delete_event_hook(event_hook_id)
except ApiException as e:
    print("Exception when calling EventHookApi->delete_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_hook**
> EventHook get_event_hook(event_hook_id)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
event_hook_id = 'event_hook_id_example' # str | 

try:
    api_response = api_instance.get_event_hook(event_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->get_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**|  | 

### Return type

[**EventHook**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_hooks**
> list[EventHook] list_event_hooks()



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_event_hooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->list_event_hooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventHook]**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_hook**
> EventHook update_event_hook(body, event_hook_id)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
body = swagger_client.EventHook() # EventHook | 
event_hook_id = 'event_hook_id_example' # str | 

try:
    api_response = api_instance.update_event_hook(body, event_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->update_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventHook**](EventHook.md)|  | 
 **event_hook_id** | **str**|  | 

### Return type

[**EventHook**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_event_hook**
> EventHook verify_event_hook(event_hook_id)



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
api_instance = swagger_client.EventHookApi(swagger_client.ApiClient(configuration))
event_hook_id = 'event_hook_id_example' # str | 

try:
    api_response = api_instance.verify_event_hook(event_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventHookApi->verify_event_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_hook_id** | **str**|  | 

### Return type

[**EventHook**](EventHook.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

