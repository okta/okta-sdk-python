# openapi_client.LinkedObjectApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_linked_object_definition**](LinkedObjectApi.md#create_linked_object_definition) | **POST** /api/v1/meta/schemas/user/linkedObjects | Create a Linked Object Definition
[**delete_linked_object_definition**](LinkedObjectApi.md#delete_linked_object_definition) | **DELETE** /api/v1/meta/schemas/user/linkedObjects/{linkedObjectName} | Delete a Linked Object Definition
[**get_linked_object_definition**](LinkedObjectApi.md#get_linked_object_definition) | **GET** /api/v1/meta/schemas/user/linkedObjects/{linkedObjectName} | Retrieve a Linked Object Definition
[**list_linked_object_definitions**](LinkedObjectApi.md#list_linked_object_definitions) | **GET** /api/v1/meta/schemas/user/linkedObjects | List all Linked Object Definitions


# **create_linked_object_definition**
> LinkedObject create_linked_object_definition(linked_object)

Create a Linked Object Definition

Creates a linked object definition

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.linked_object import LinkedObject
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
    api_instance = openapi_client.LinkedObjectApi(api_client)
    linked_object = openapi_client.LinkedObject() # LinkedObject | 

    try:
        # Create a Linked Object Definition
        api_response = api_instance.create_linked_object_definition(linked_object)
        print("The response of LinkedObjectApi->create_linked_object_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkedObjectApi->create_linked_object_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object** | [**LinkedObject**](LinkedObject.md)|  | 

### Return type

[**LinkedObject**](LinkedObject.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_object_definition**
> delete_linked_object_definition(linked_object_name)

Delete a Linked Object Definition

Deletes a linked object definition

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
    api_instance = openapi_client.LinkedObjectApi(api_client)
    linked_object_name = 'linked_object_name_example' # str | 

    try:
        # Delete a Linked Object Definition
        api_instance.delete_linked_object_definition(linked_object_name)
    except Exception as e:
        print("Exception when calling LinkedObjectApi->delete_linked_object_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object_name** | **str**|  | 

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

# **get_linked_object_definition**
> LinkedObject get_linked_object_definition(linked_object_name)

Retrieve a Linked Object Definition

Retrieves a linked object definition

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.linked_object import LinkedObject
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
    api_instance = openapi_client.LinkedObjectApi(api_client)
    linked_object_name = 'linked_object_name_example' # str | 

    try:
        # Retrieve a Linked Object Definition
        api_response = api_instance.get_linked_object_definition(linked_object_name)
        print("The response of LinkedObjectApi->get_linked_object_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkedObjectApi->get_linked_object_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object_name** | **str**|  | 

### Return type

[**LinkedObject**](LinkedObject.md)

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

# **list_linked_object_definitions**
> List[LinkedObject] list_linked_object_definitions()

List all Linked Object Definitions

Lists all linked object definitions

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.linked_object import LinkedObject
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
    api_instance = openapi_client.LinkedObjectApi(api_client)

    try:
        # List all Linked Object Definitions
        api_response = api_instance.list_linked_object_definitions()
        print("The response of LinkedObjectApi->list_linked_object_definitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkedObjectApi->list_linked_object_definitions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LinkedObject]**](LinkedObject.md)

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

