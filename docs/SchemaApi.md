# okta.SchemaApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_user_schema**](SchemaApi.md#get_application_user_schema) | **GET** /api/v1/meta/schemas/apps/{appId}/default | Retrieve the default app user schema for an app
[**get_group_schema**](SchemaApi.md#get_group_schema) | **GET** /api/v1/meta/schemas/group/default | Retrieve the default group schema
[**get_log_stream_schema**](SchemaApi.md#get_log_stream_schema) | **GET** /api/v1/meta/schemas/logStream/{logStreamType} | Retrieve the log stream schema for the schema type
[**get_user_schema**](SchemaApi.md#get_user_schema) | **GET** /api/v1/meta/schemas/user/{schemaId} | Retrieve a user schema
[**list_log_stream_schemas**](SchemaApi.md#list_log_stream_schemas) | **GET** /api/v1/meta/schemas/logStream | List the log stream schemas
[**update_application_user_profile**](SchemaApi.md#update_application_user_profile) | **POST** /api/v1/meta/schemas/apps/{appId}/default | Update the app user profile schema for an app
[**update_group_schema**](SchemaApi.md#update_group_schema) | **POST** /api/v1/meta/schemas/group/default | Update the group profile schema
[**update_user_profile**](SchemaApi.md#update_user_profile) | **POST** /api/v1/meta/schemas/user/{schemaId} | Update a user schema


# **get_application_user_schema**
> UserSchema get_application_user_schema(app_id)

Retrieve the default app user schema for an app

Retrieves the default schema for an app user.  The [User Types](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/) feature does not extend to apps. All users assigned to a given app use the same app user schema. Therefore, unlike the user schema operations, the app user schema operations all specify `default` and don't accept a schema ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_schema import UserSchema
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
    api_instance = okta.SchemaApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Retrieve the default app user schema for an app
        api_response = api_instance.get_application_user_schema(app_id)
        print("The response of SchemaApi->get_application_user_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_application_user_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

Retrieve the default group schema

Retrieves the group schema  The [User Types](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/) feature does not extend to groups. All groups use the same group schema. Unlike user schema operations, group schema operations all specify `default` and don't accept a schema ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_schema import GroupSchema
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
    api_instance = okta.SchemaApi(api_client)

    try:
        # Retrieve the default group schema
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

Retrieve the log stream schema for the schema type

Retrieves the schema for a log stream type. The `logStreamType` element in the URL specifies the log stream type, which is either `aws_eventbridge` or `splunk_cloud_logstreaming`. Use the `aws_eventbridge` literal to retrieve the AWS EventBridge type schema, and use the `splunk_cloud_logstreaming` literal retrieve the Splunk Cloud type schema.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream_schema import LogStreamSchema
from okta.models.log_stream_type import LogStreamType
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
    api_instance = okta.SchemaApi(api_client)
    log_stream_type = okta.LogStreamType() # LogStreamType | 

    try:
        # Retrieve the log stream schema for the schema type
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

Retrieve a user schema

Retrieves the schema for a user type

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_schema import UserSchema
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
    api_instance = okta.SchemaApi(api_client)
    schema_id = 'schema_id_example' # str | Schema ID. You can also use `default` to refer to the default user type schema.

    try:
        # Retrieve a user schema
        api_response = api_instance.get_user_schema(schema_id)
        print("The response of SchemaApi->get_user_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->get_user_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema ID. You can also use &#x60;default&#x60; to refer to the default user type schema. | 

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

List the log stream schemas

Lists the schema for all log stream types visible for this org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.log_stream_schema import LogStreamSchema
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
    api_instance = okta.SchemaApi(api_client)

    try:
        # List the log stream schemas
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

Update the app user profile schema for an app

Updates the app user schema. This updates, adds, or removes one or more custom profile properties or the nullability of a base property in the app user schema for an app. Changing a base property's nullability (for example, the value of its `required` field) is allowed only if it is nullable in the default predefined schema for the app.  > **Note:** You must set properties explicitly to `null` to remove them from the schema; otherwise, `POST` is interpreted as a partial update.  The [User Types](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/) feature does not extend to apps. All users assigned to a given app use the same app user schema. Therefore, unlike the user schema operations, the app user schema operations all specify `default` and don't accept a schema ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_schema import UserSchema
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
    api_instance = okta.SchemaApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    body = okta.UserSchema() # UserSchema |  (optional)

    try:
        # Update the app user profile schema for an app
        api_response = api_instance.update_application_user_profile(app_id, body=body)
        print("The response of SchemaApi->update_application_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->update_application_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
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

Update the group profile schema

Updates the group profile schema. This updates, adds, or removes one or more custom profile properties in a group schema. Currently Okta does not support changing base group profile properties.  > **Note:** You must set properties explicitly to `null` to remove them from the schema; otherwise, `POST` is interpreted as a partial update.  The [User Types](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/) feature does not extend to groups. All groups use the same group schema. Unlike user schema operations, group schema operations all specify `default` and don't accept a schema ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_schema import GroupSchema
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
    api_instance = okta.SchemaApi(api_client)
    group_schema = okta.GroupSchema() # GroupSchema |  (optional)

    try:
        # Update the group profile schema
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

Update a user schema

Updates a user schema. Use this request to update, add, or remove one or more profile properties in a user schema. If you specify `default` for the `schemaId`, updates will apply to the default user type.  Unlike custom user profile properties, limited changes are allowed to base user profile properties (permissions, nullability of the `firstName` and `lastName` properties, or pattern for `login`). You can't remove a property from the default schema if it's being referenced as a [`matchAttribute`](/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path=policy/subject/matchAttribute&t=request) in `SAML2` IdPs. Currently, all validation of SAML assertions are only performed against the default user type.  > **Note:** You must set properties explicitly to `null` to remove them from the schema; otherwise, `POST` is interpreted as a partial update.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_schema import UserSchema
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
    api_instance = okta.SchemaApi(api_client)
    schema_id = 'schema_id_example' # str | Schema ID. You can also use `default` to refer to the default user type schema.
    user_schema = okta.UserSchema() # UserSchema | 

    try:
        # Update a user schema
        api_response = api_instance.update_user_profile(schema_id, user_schema)
        print("The response of SchemaApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema ID. You can also use &#x60;default&#x60; to refer to the default user type schema. | 
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

