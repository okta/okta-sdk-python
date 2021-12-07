# swagger_client.UserTypeApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_type**](UserTypeApi.md#create_user_type) | **POST** /api/v1/meta/types/user | 
[**delete_user_type**](UserTypeApi.md#delete_user_type) | **DELETE** /api/v1/meta/types/user/{typeId} | 
[**get_user_type**](UserTypeApi.md#get_user_type) | **GET** /api/v1/meta/types/user/{typeId} | 
[**list_user_types**](UserTypeApi.md#list_user_types) | **GET** /api/v1/meta/types/user | 
[**replace_user_type**](UserTypeApi.md#replace_user_type) | **PUT** /api/v1/meta/types/user/{typeId} | 
[**update_user_type**](UserTypeApi.md#update_user_type) | **POST** /api/v1/meta/types/user/{typeId} | 

# **create_user_type**
> UserType create_user_type(body)



Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10.

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
api_instance = swagger_client.UserTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserType() # UserType | 

try:
    api_response = api_instance.create_user_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTypeApi->create_user_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserType**](UserType.md)|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_type**
> delete_user_type(type_id)



Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users

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
api_instance = swagger_client.UserTypeApi(swagger_client.ApiClient(configuration))
type_id = 'type_id_example' # str | 

try:
    api_instance.delete_user_type(type_id)
except ApiException as e:
    print("Exception when calling UserTypeApi->delete_user_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_type**
> UserType get_user_type(type_id)



Fetches a User Type by ID. The special identifier `default` may be used to fetch the default User Type.

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
api_instance = swagger_client.UserTypeApi(swagger_client.ApiClient(configuration))
type_id = 'type_id_example' # str | 

try:
    api_response = api_instance.get_user_type(type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTypeApi->get_user_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_types**
> list[UserType] list_user_types()



Fetches all User Types in your org

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
api_instance = swagger_client.UserTypeApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_user_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTypeApi->list_user_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserType]**](UserType.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_user_type**
> UserType replace_user_type(body, type_id)



Replace an existing User Type

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
api_instance = swagger_client.UserTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserType() # UserType | 
type_id = 'type_id_example' # str | 

try:
    api_response = api_instance.replace_user_type(body, type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTypeApi->replace_user_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserType**](UserType.md)|  | 
 **type_id** | **str**|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_type**
> UserType update_user_type(body, type_id)



Updates an existing User Type

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
api_instance = swagger_client.UserTypeApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserType() # UserType | 
type_id = 'type_id_example' # str | 

try:
    api_response = api_instance.update_user_type(body, type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTypeApi->update_user_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserType**](UserType.md)|  | 
 **type_id** | **str**|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

