# openapi_client.SchemaApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_ui_schema**](SchemaApi.md#get_app_ui_schema) | **GET** /api/v1/meta/layouts/apps/{appName}/sections/{section}/{operation} | Retrieve the UI schema for a section
[**get_app_ui_schema_links**](SchemaApi.md#get_app_ui_schema_links) | **GET** /api/v1/meta/layouts/apps/{appName} | Retrieve the links for UI schemas for an Application
[**get_application_user_schema**](SchemaApi.md#get_application_user_schema) | **GET** /api/v1/meta/schemas/apps/{appId}/default | Retrieve the default Application User Schema for an Application
[**get_group_schema**](SchemaApi.md#get_group_schema) | **GET** /api/v1/meta/schemas/group/default | Retrieve the default Group Schema
[**get_log_stream_schema**](SchemaApi.md#get_log_stream_schema) | **GET** /api/v1/meta/schemas/logStream/{logStreamType} | Retrieve the Log Stream Schema for the schema type
[**get_user_schema**](SchemaApi.md#get_user_schema) | **GET** /api/v1/meta/schemas/user/{schemaId} | Retrieve a User Schema
[**list_log_stream_schemas**](SchemaApi.md#list_log_stream_schemas) | **GET** /api/v1/meta/schemas/logStream | List the Log Stream Schemas
[**update_application_user_profile**](SchemaApi.md#update_application_user_profile) | **POST** /api/v1/meta/schemas/apps/{appId}/default | Update the default Application User Schema for an Application
[**update_group_schema**](SchemaApi.md#update_group_schema) | **POST** /api/v1/meta/schemas/group/default | Update the default Group Schema
[**update_user_profile**](SchemaApi.md#update_user_profile) | **POST** /api/v1/meta/schemas/user/{schemaId} | Update a User Schema


# **get_app_ui_schema**
> ApplicationLayout get_app_ui_schema(app_name, section, operation)

Retrieve the UI schema for a section

Retrieves the UI schema for an Application given `appName`, `section` and `operation`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.application_layout import ApplicationLayout
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
    api_instance = openapi_client.SchemaApi(api_client)
    app_name = 'oidc_client' # str | 
    section = 'section_example' # str | 
    operation = 'operation_example' # str | 

    try:
        # Retrieve the UI schema for a section
        api_response = api_instance.get_app_ui_schema(app_name, section, operation)
        print("The response of SchemaApi->get_app_ui_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_app_ui_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | 
 **section** | **str**|  | 
 **operation** | **str**|  | 

### Return type

[**ApplicationLayout**](ApplicationLayout.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_ui_schema_links**
> ApplicationLayouts get_app_ui_schema_links(app_name)

Retrieve the links for UI schemas for an Application

Retrieves the links for UI schemas for an Application given `appName`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.application_layouts import ApplicationLayouts
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
    api_instance = openapi_client.SchemaApi(api_client)
    app_name = 'oidc_client' # str | 

    try:
        # Retrieve the links for UI schemas for an Application
        api_response = api_instance.get_app_ui_schema_links(app_name)
        print("The response of SchemaApi->get_app_ui_schema_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_app_ui_schema_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | 

### Return type

[**ApplicationLayouts**](ApplicationLayouts.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_user_schema**
> UserSchema get_application_user_schema(app_id)

Retrieve the default Application User Schema for an Application

Retrieves the Schema for an App User

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_schema import UserSchema
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
    api_instance = openapi_client.SchemaApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Retrieve the default Application User Schema for an Application
        api_response = api_instance.get_application_user_schema(app_id)
        print("The response of SchemaApi->get_application_user_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_application_user_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_schema**
> GroupSchema get_group_schema()

Retrieve the default Group Schema

Retrieves the group schema

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_schema import GroupSchema
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
    api_instance = openapi_client.SchemaApi(api_client)

    try:
        # Retrieve the default Group Schema
        api_response = api_instance.get_group_schema()
        print("The response of SchemaApi->get_group_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_group_schema: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GroupSchema**](GroupSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_stream_schema**
> LogStreamSchema get_log_stream_schema(log_stream_type)

Retrieve the Log Stream Schema for the schema type

Retrieves the schema for a Log Stream type. The `logStreamType` element in the URL specifies the Log Stream type, which is either `aws_eventbridge` or `splunk_cloud_logstreaming`. Use the `aws_eventbridge` literal to retrieve the AWS EventBridge type schema, and use the `splunk_cloud_logstreaming` literal retrieve the Splunk Cloud type schema.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.log_stream_schema import LogStreamSchema
from openapi_client.models.log_stream_type import LogStreamType
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
    api_instance = openapi_client.SchemaApi(api_client)
    log_stream_type = openapi_client.LogStreamType() # LogStreamType | 

    try:
        # Retrieve the Log Stream Schema for the schema type
        api_response = api_instance.get_log_stream_schema(log_stream_type)
        print("The response of SchemaApi->get_log_stream_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_log_stream_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_stream_type** | [**LogStreamType**](.md)|  | 

### Return type

[**LogStreamSchema**](LogStreamSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_schema**
> UserSchema get_user_schema(schema_id)

Retrieve a User Schema

Retrieves the schema for a Schema Id

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_schema import UserSchema
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
    api_instance = openapi_client.SchemaApi(api_client)
    schema_id = 'schema_id_example' # str | 

    try:
        # Retrieve a User Schema
        api_response = api_instance.get_user_schema(schema_id)
        print("The response of SchemaApi->get_user_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_user_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**|  | 

### Return type

[**UserSchema**](UserSchema.md)

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

# **list_log_stream_schemas**
> List[LogStreamSchema] list_log_stream_schemas()

List the Log Stream Schemas

Lists the schema for all log stream types visible for this org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.log_stream_schema import LogStreamSchema
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
    api_instance = openapi_client.SchemaApi(api_client)

    try:
        # List the Log Stream Schemas
        api_response = api_instance.list_log_stream_schemas()
        print("The response of SchemaApi->list_log_stream_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->list_log_stream_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LogStreamSchema]**](LogStreamSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_user_profile**
> UserSchema update_application_user_profile(app_id, body=body)

Update the default Application User Schema for an Application

Partially updates on the User Profile properties of the Application User Schema

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_schema import UserSchema
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
    api_instance = openapi_client.SchemaApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    body = openapi_client.UserSchema() # UserSchema |  (optional)

    try:
        # Update the default Application User Schema for an Application
        api_response = api_instance.update_application_user_profile(app_id, body=body)
        print("The response of SchemaApi->update_application_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->update_application_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **body** | [**UserSchema**](UserSchema.md)|  | [optional] 

### Return type

[**UserSchema**](UserSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_schema**
> GroupSchema update_group_schema(group_schema=group_schema)

Update the default Group Schema

Updates the default group schema. This updates, adds, or removes one or more custom Group Profile properties in the schema.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.group_schema import GroupSchema
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
    api_instance = openapi_client.SchemaApi(api_client)
    group_schema = openapi_client.GroupSchema() # GroupSchema |  (optional)

    try:
        # Update the default Group Schema
        api_response = api_instance.update_group_schema(group_schema=group_schema)
        print("The response of SchemaApi->update_group_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->update_group_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_schema** | [**GroupSchema**](GroupSchema.md)|  | [optional] 

### Return type

[**GroupSchema**](GroupSchema.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> UserSchema update_user_profile(schema_id, user_schema)

Update a User Schema

Partially updates on the User Profile properties of the user schema

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.user_schema import UserSchema
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
    api_instance = openapi_client.SchemaApi(api_client)
    schema_id = 'schema_id_example' # str | 
    user_schema = openapi_client.UserSchema() # UserSchema | 

    try:
        # Update a User Schema
        api_response = api_instance.update_user_profile(schema_id, user_schema)
        print("The response of SchemaApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**|  | 
 **user_schema** | [**UserSchema**](UserSchema.md)|  | 

### Return type

[**UserSchema**](UserSchema.md)

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

