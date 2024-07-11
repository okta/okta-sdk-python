# openapi_client.UserTypeApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_type**](UserTypeApi.md#create_user_type) | **POST** /api/v1/meta/types/user | Create a User Type
[**delete_user_type**](UserTypeApi.md#delete_user_type) | **DELETE** /api/v1/meta/types/user/{typeId} | Delete a User Type
[**get_user_type**](UserTypeApi.md#get_user_type) | **GET** /api/v1/meta/types/user/{typeId} | Retrieve a User Type
[**list_user_types**](UserTypeApi.md#list_user_types) | **GET** /api/v1/meta/types/user | List all User Types
[**replace_user_type**](UserTypeApi.md#replace_user_type) | **PUT** /api/v1/meta/types/user/{typeId} | Replace a User Type
[**update_user_type**](UserTypeApi.md#update_user_type) | **POST** /api/v1/meta/types/user/{typeId} | Update a User Type


# **create_user_type**
> UserType create_user_type(user_type)

Create a User Type

Creates a new User Type. Okta automatically creates a `default` User Type for your org. You may add up to nine additional User Types. > **Note**: New User Types are based on the current default schema template. Modifications to this schema do not automatically propagate to previously created User Types.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_type import UserType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserTypeApi(api_client)
    user_type = openapi_client.UserType() # UserType | 

    try:
        # Create a User Type
        api_response = api_instance.create_user_type(user_type)
        print("The response of UserTypeApi->create_user_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->create_user_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | [**UserType**](UserType.md)|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_type**
> delete_user_type(type_id)

Delete a User Type

Deletes a User Type permanently. > **Note**: You can't delete the default User Type or a User Type that is currently assigned to users.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserTypeApi(api_client)
    type_id = 'type_id_example' # str | 

    try:
        # Delete a User Type
        api_instance.delete_user_type(type_id)
    except Exception as e:
        print("Exception when calling UserTypeApi->delete_user_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_type**
> UserType get_user_type(type_id)

Retrieve a User Type

Retrieves a User Type by ID. Use `default` to fetch the default User Type.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_type import UserType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserTypeApi(api_client)
    type_id = 'type_id_example' # str | 

    try:
        # Retrieve a User Type
        api_response = api_instance.get_user_type(type_id)
        print("The response of UserTypeApi->get_user_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->get_user_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_types**
> List[UserType] list_user_types()

List all User Types

Lists all User Types in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_type import UserType
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserTypeApi(api_client)

    try:
        # List all User Types
        api_response = api_instance.list_user_types()
        print("The response of UserTypeApi->list_user_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->list_user_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserType]**](UserType.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_user_type**
> UserType replace_user_type(type_id, user_type=user_type)

Replace a User Type

Replaces an existing User Type. > **Note**: The `name` of an existing User Type can't be changed, but must be part of the request body. You can only replace the `displayName` and `description` elements.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_type import UserType
from openapi_client.models.user_type_put_request import UserTypePutRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserTypeApi(api_client)
    type_id = 'type_id_example' # str | 
    user_type = openapi_client.UserTypePutRequest() # UserTypePutRequest |  (optional)

    try:
        # Replace a User Type
        api_response = api_instance.replace_user_type(type_id, user_type=user_type)
        print("The response of UserTypeApi->replace_user_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->replace_user_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 
 **user_type** | [**UserTypePutRequest**](UserTypePutRequest.md)|  | [optional] 

### Return type

[**UserType**](UserType.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_type**
> UserType update_user_type(type_id, user_type)

Update a User Type

Updates an existing User Type. > **Note**: You can only update the `displayName` and `description` elements. The `name` of an existing User Type can't be changed.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_type import UserType
from openapi_client.models.user_type_post_request import UserTypePostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserTypeApi(api_client)
    type_id = 'type_id_example' # str | 
    user_type = openapi_client.UserTypePostRequest() # UserTypePostRequest | 

    try:
        # Update a User Type
        api_response = api_instance.update_user_type(type_id, user_type)
        print("The response of UserTypeApi->update_user_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->update_user_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 
 **user_type** | [**UserTypePostRequest**](UserTypePostRequest.md)|  | 

### Return type

[**UserType**](UserType.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

