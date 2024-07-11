# openapi_client.UISchemaApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ui_schema**](UISchemaApi.md#create_ui_schema) | **POST** /api/v1/meta/uischemas | Create a UI Schema
[**delete_ui_schemas**](UISchemaApi.md#delete_ui_schemas) | **DELETE** /api/v1/meta/uischemas/{id} | Delete a UI Schema
[**get_ui_schema**](UISchemaApi.md#get_ui_schema) | **GET** /api/v1/meta/uischemas/{id} | Retrieve a UI Schema
[**list_ui_schemas**](UISchemaApi.md#list_ui_schemas) | **GET** /api/v1/meta/uischemas | List all UI Schemas
[**replace_ui_schemas**](UISchemaApi.md#replace_ui_schemas) | **PUT** /api/v1/meta/uischemas/{id} | Replace a UI Schema


# **create_ui_schema**
> UISchemasResponseObject create_ui_schema(uischemabody)

Create a UI Schema

Creates an input for an enrollment form

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.create_ui_schema import CreateUISchema
from openapi_client.models.ui_schemas_response_object import UISchemasResponseObject
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
    api_instance = openapi_client.UISchemaApi(api_client)
    uischemabody = openapi_client.CreateUISchema() # CreateUISchema | 

    try:
        # Create a UI Schema
        api_response = api_instance.create_ui_schema(uischemabody)
        print("The response of UISchemaApi->create_ui_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UISchemaApi->create_ui_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uischemabody** | [**CreateUISchema**](CreateUISchema.md)|  | 

### Return type

[**UISchemasResponseObject**](UISchemasResponseObject.md)

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

# **delete_ui_schemas**
> delete_ui_schemas(id)

Delete a UI Schema

Deletes a UI Schema by `id`

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
    api_instance = openapi_client.UISchemaApi(api_client)
    id = 'uis4a7liocgcRgcxZ0g7' # str | The unique ID of the UI Schema

    try:
        # Delete a UI Schema
        api_instance.delete_ui_schemas(id)
    except Exception as e:
        print("Exception when calling UISchemaApi->delete_ui_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the UI Schema | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ui_schema**
> UISchemasResponseObject get_ui_schema(id)

Retrieve a UI Schema

Retrieves a UI Schema by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.ui_schemas_response_object import UISchemasResponseObject
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
    api_instance = openapi_client.UISchemaApi(api_client)
    id = 'uis4a7liocgcRgcxZ0g7' # str | The unique ID of the UI Schema

    try:
        # Retrieve a UI Schema
        api_response = api_instance.get_ui_schema(id)
        print("The response of UISchemaApi->get_ui_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UISchemaApi->get_ui_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the UI Schema | 

### Return type

[**UISchemasResponseObject**](UISchemasResponseObject.md)

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

# **list_ui_schemas**
> List[UISchemasResponseObject] list_ui_schemas()

List all UI Schemas

Lists all UI Schemas in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.ui_schemas_response_object import UISchemasResponseObject
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
    api_instance = openapi_client.UISchemaApi(api_client)

    try:
        # List all UI Schemas
        api_response = api_instance.list_ui_schemas()
        print("The response of UISchemaApi->list_ui_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UISchemaApi->list_ui_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UISchemasResponseObject]**](UISchemasResponseObject.md)

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

# **replace_ui_schemas**
> UISchemasResponseObject replace_ui_schemas(id, update_ui_schema_body)

Replace a UI Schema

Replaces a UI Schema by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.ui_schemas_response_object import UISchemasResponseObject
from openapi_client.models.update_ui_schema import UpdateUISchema
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
    api_instance = openapi_client.UISchemaApi(api_client)
    id = 'uis4a7liocgcRgcxZ0g7' # str | The unique ID of the UI Schema
    update_ui_schema_body = openapi_client.UpdateUISchema() # UpdateUISchema | 

    try:
        # Replace a UI Schema
        api_response = api_instance.replace_ui_schemas(id, update_ui_schema_body)
        print("The response of UISchemaApi->replace_ui_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UISchemaApi->replace_ui_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique ID of the UI Schema | 
 **update_ui_schema_body** | [**UpdateUISchema**](UpdateUISchema.md)|  | 

### Return type

[**UISchemasResponseObject**](UISchemasResponseObject.md)

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

