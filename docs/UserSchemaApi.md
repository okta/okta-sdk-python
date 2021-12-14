# swagger_client.UserSchemaApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_user_schema**](UserSchemaApi.md#get_application_user_schema) | **GET** /api/v1/meta/schemas/apps/{appInstanceId}/default | Fetches the Schema for an App User
[**get_user_schema**](UserSchemaApi.md#get_user_schema) | **GET** /api/v1/meta/schemas/user/{schemaId} | Fetches the schema for a Schema Id.
[**update_application_user_profile**](UserSchemaApi.md#update_application_user_profile) | **POST** /api/v1/meta/schemas/apps/{appInstanceId}/default | Partial updates on the User Profile properties of the Application User Schema.
[**update_user_profile**](UserSchemaApi.md#update_user_profile) | **POST** /api/v1/meta/schemas/user/{schemaId} | 

# **get_application_user_schema**
> UserSchema get_application_user_schema(app_instance_id)

Fetches the Schema for an App User

Fetches the Schema for an App User

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
api_instance = swagger_client.UserSchemaApi(swagger_client.ApiClient(configuration))
app_instance_id = 'app_instance_id_example' # str | 

try:
    # Fetches the Schema for an App User
    api_response = api_instance.get_application_user_schema(app_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSchemaApi->get_application_user_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **str**|  | 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_schema**
> UserSchema get_user_schema(schema_id)

Fetches the schema for a Schema Id.

Fetches the schema for a Schema Id.

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
api_instance = swagger_client.UserSchemaApi(swagger_client.ApiClient(configuration))
schema_id = 'schema_id_example' # str | 

try:
    # Fetches the schema for a Schema Id.
    api_response = api_instance.get_user_schema(schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSchemaApi->get_user_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**|  | 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_user_profile**
> UserSchema update_application_user_profile(app_instance_id, body=body)

Partial updates on the User Profile properties of the Application User Schema.

Partial updates on the User Profile properties of the Application User Schema.

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
api_instance = swagger_client.UserSchemaApi(swagger_client.ApiClient(configuration))
app_instance_id = 'app_instance_id_example' # str | 
body = swagger_client.UserSchema() # UserSchema |  (optional)

try:
    # Partial updates on the User Profile properties of the Application User Schema.
    api_response = api_instance.update_application_user_profile(app_instance_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSchemaApi->update_application_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_instance_id** | **str**|  | 
 **body** | [**UserSchema**](UserSchema.md)|  | [optional] 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> UserSchema update_user_profile(body, schema_id)



Partial updates on the User Profile properties of the user schema.

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
api_instance = swagger_client.UserSchemaApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserSchema() # UserSchema | 
schema_id = 'schema_id_example' # str | 

try:
    api_response = api_instance.update_user_profile(body, schema_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSchemaApi->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSchema**](UserSchema.md)|  | 
 **schema_id** | **str**|  | 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

