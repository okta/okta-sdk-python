# swagger_client.CAPTCHAApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_captcha_instance**](CAPTCHAApi.md#create_captcha_instance) | **POST** /api/v1/captchas | Create new CAPTCHA instance
[**delete_captcha_instance**](CAPTCHAApi.md#delete_captcha_instance) | **DELETE** /api/v1/captchas/{captchaId} | Delete CAPTCHA Instance
[**get_captcha_instance**](CAPTCHAApi.md#get_captcha_instance) | **GET** /api/v1/captchas/{captchaId} | Get CAPTCHA Instance
[**list_captcha_instances**](CAPTCHAApi.md#list_captcha_instances) | **GET** /api/v1/captchas | List CAPTCHA instances
[**partial_update_captcha_instance**](CAPTCHAApi.md#partial_update_captcha_instance) | **POST** /api/v1/captchas/{captchaId} | Partial Update CAPTCHA instance
[**update_captcha_instance**](CAPTCHAApi.md#update_captcha_instance) | **PUT** /api/v1/captchas/{captchaId} | Update CAPTCHA instance

# **create_captcha_instance**
> CAPTCHAInstance create_captcha_instance(body=body)

Create new CAPTCHA instance

Adds a new CAPTCHA instance to your organization. In current release, we only allow one CAPTCHA instance per org.

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
api_instance = swagger_client.CAPTCHAApi(swagger_client.ApiClient(configuration))
body = swagger_client.CAPTCHAInstance() # CAPTCHAInstance |  (optional)

try:
    # Create new CAPTCHA instance
    api_response = api_instance.create_captcha_instance(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CAPTCHAApi->create_captcha_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CAPTCHAInstance**](CAPTCHAInstance.md)|  | [optional] 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_captcha_instance**
> delete_captcha_instance(captcha_id)

Delete CAPTCHA Instance

Delete a CAPTCHA instance by `id`.

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
api_instance = swagger_client.CAPTCHAApi(swagger_client.ApiClient(configuration))
captcha_id = 'captcha_id_example' # str | id of the CAPTCHA

try:
    # Delete CAPTCHA Instance
    api_instance.delete_captcha_instance(captcha_id)
except ApiException as e:
    print("Exception when calling CAPTCHAApi->delete_captcha_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_id** | **str**| id of the CAPTCHA | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_captcha_instance**
> CAPTCHAInstance get_captcha_instance(captcha_id)

Get CAPTCHA Instance

Fetches a CAPTCHA instance by `id`.

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
api_instance = swagger_client.CAPTCHAApi(swagger_client.ApiClient(configuration))
captcha_id = 'captcha_id_example' # str | id of the CAPTCHA

try:
    # Get CAPTCHA Instance
    api_response = api_instance.get_captcha_instance(captcha_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CAPTCHAApi->get_captcha_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **captcha_id** | **str**| id of the CAPTCHA | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_captcha_instances**
> list[CAPTCHAInstance] list_captcha_instances()

List CAPTCHA instances

Enumerates CAPTCHA instances in your organization with pagination. A subset of CAPTCHA instances can be returned that match a supported filter expression or query.

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
api_instance = swagger_client.CAPTCHAApi(swagger_client.ApiClient(configuration))

try:
    # List CAPTCHA instances
    api_response = api_instance.list_captcha_instances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CAPTCHAApi->list_captcha_instances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CAPTCHAInstance]**](CAPTCHAInstance.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_captcha_instance**
> CAPTCHAInstance partial_update_captcha_instance(body, captcha_id)

Partial Update CAPTCHA instance

Partially update a CAPTCHA instance by `id`.

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
api_instance = swagger_client.CAPTCHAApi(swagger_client.ApiClient(configuration))
body = swagger_client.CAPTCHAInstance() # CAPTCHAInstance | 
captcha_id = 'captcha_id_example' # str | id of the CAPTCHA

try:
    # Partial Update CAPTCHA instance
    api_response = api_instance.partial_update_captcha_instance(body, captcha_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CAPTCHAApi->partial_update_captcha_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CAPTCHAInstance**](CAPTCHAInstance.md)|  | 
 **captcha_id** | **str**| id of the CAPTCHA | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_captcha_instance**
> CAPTCHAInstance update_captcha_instance(body, captcha_id)

Update CAPTCHA instance

Update a CAPTCHA instance by `id`.

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
api_instance = swagger_client.CAPTCHAApi(swagger_client.ApiClient(configuration))
body = swagger_client.CAPTCHAInstance() # CAPTCHAInstance | 
captcha_id = 'captcha_id_example' # str | id of the CAPTCHA

try:
    # Update CAPTCHA instance
    api_response = api_instance.update_captcha_instance(body, captcha_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CAPTCHAApi->update_captcha_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CAPTCHAInstance**](CAPTCHAInstance.md)|  | 
 **captcha_id** | **str**| id of the CAPTCHA | 

### Return type

[**CAPTCHAInstance**](CAPTCHAInstance.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

