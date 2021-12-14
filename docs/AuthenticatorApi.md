# swagger_client.AuthenticatorApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_authenticator**](AuthenticatorApi.md#activate_authenticator) | **POST** /api/v1/authenticators/{authenticatorId}/lifecycle/activate | Activate Authenticator
[**deactivate_authenticator**](AuthenticatorApi.md#deactivate_authenticator) | **POST** /api/v1/authenticators/{authenticatorId}/lifecycle/deactivate | Deactivate Authenticator
[**get_authenticator**](AuthenticatorApi.md#get_authenticator) | **GET** /api/v1/authenticators/{authenticatorId} | Get Authenticator
[**list_authenticators**](AuthenticatorApi.md#list_authenticators) | **GET** /api/v1/authenticators | List Authenticators

# **activate_authenticator**
> activate_authenticator(authenticator_id)

Activate Authenticator

Activates an authenticator by `authenticatorId`.

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
api_instance = swagger_client.AuthenticatorApi(swagger_client.ApiClient(configuration))
authenticator_id = 'authenticator_id_example' # str | 

try:
    # Activate Authenticator
    api_instance.activate_authenticator(authenticator_id)
except ApiException as e:
    print("Exception when calling AuthenticatorApi->activate_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_authenticator**
> deactivate_authenticator(authenticator_id)

Deactivate Authenticator

Deactivates an authenticator by `authenticatorId`.

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
api_instance = swagger_client.AuthenticatorApi(swagger_client.ApiClient(configuration))
authenticator_id = 'authenticator_id_example' # str | 

try:
    # Deactivate Authenticator
    api_instance.deactivate_authenticator(authenticator_id)
except ApiException as e:
    print("Exception when calling AuthenticatorApi->deactivate_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authenticator**
> Authenticator get_authenticator(authenticator_id)

Get Authenticator

Fetches an authenticator from your Okta organization by `authenticatorId`.

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
api_instance = swagger_client.AuthenticatorApi(swagger_client.ApiClient(configuration))
authenticator_id = 'authenticator_id_example' # str | 

try:
    # Get Authenticator
    api_response = api_instance.get_authenticator(authenticator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticatorApi->get_authenticator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_id** | **str**|  | 

### Return type

[**Authenticator**](Authenticator.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authenticators**
> list[Authenticator] list_authenticators()

List Authenticators

Enumerates authenticators in your organization.

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
api_instance = swagger_client.AuthenticatorApi(swagger_client.ApiClient(configuration))

try:
    # List Authenticators
    api_response = api_instance.list_authenticators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticatorApi->list_authenticators: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Authenticator]**](Authenticator.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

