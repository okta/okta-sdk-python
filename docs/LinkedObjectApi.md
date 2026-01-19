# okta.LinkedObjectApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_linked_object_definition**](LinkedObjectApi.md#create_linked_object_definition) | **POST** /api/v1/meta/schemas/user/linkedObjects | Create a linked object definition
[**delete_linked_object_definition**](LinkedObjectApi.md#delete_linked_object_definition) | **DELETE** /api/v1/meta/schemas/user/linkedObjects/{linkedObjectName} | Delete a linked object definition
[**get_linked_object_definition**](LinkedObjectApi.md#get_linked_object_definition) | **GET** /api/v1/meta/schemas/user/linkedObjects/{linkedObjectName} | Retrieve a linked object definition
[**list_linked_object_definitions**](LinkedObjectApi.md#list_linked_object_definitions) | **GET** /api/v1/meta/schemas/user/linkedObjects | List all linked object definitions


# **create_linked_object_definition**
> LinkedObject create_linked_object_definition(linked_object)

Create a linked object definition

Creates a Linked Object definition

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.linked_object import LinkedObject
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.LinkedObjectApi(api_client)
    linked_object = okta.LinkedObject() # LinkedObject | 

    try:
        # Create a linked object definition
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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_object_definition**
> delete_linked_object_definition(linked_object_name)

Delete a linked object definition

Deletes the Linked Object definition specified by either the `primary` or `associated` name. The entire definition is removed, regardless of which name that you specify.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.LinkedObjectApi(api_client)
    linked_object_name = 'linked_object_name_example' # str | Primary or Associated name

    try:
        # Delete a linked object definition
        api_instance.delete_linked_object_definition(linked_object_name)
    except Exception as e:
        print("Exception when calling LinkedObjectApi->delete_linked_object_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object_name** | **str**| Primary or Associated name | 

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

Retrieve a linked object definition

Retrieves a Linked Object definition

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.linked_object import LinkedObject
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.LinkedObjectApi(api_client)
    linked_object_name = 'linked_object_name_example' # str | Primary or Associated name

    try:
        # Retrieve a linked object definition
        api_response = api_instance.get_linked_object_definition(linked_object_name)
        print("The response of LinkedObjectApi->get_linked_object_definition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkedObjectApi->get_linked_object_definition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_object_name** | **str**| Primary or Associated name | 

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

List all linked object definitions

Lists all Linked Object definitions

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.linked_object import LinkedObject
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
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
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.LinkedObjectApi(api_client)

    try:
        # List all linked object definitions
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

