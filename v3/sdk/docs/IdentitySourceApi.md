# openapi_client.IdentitySourceApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_source_session**](IdentitySourceApi.md#create_identity_source_session) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions | Create an Identity Source Session
[**delete_identity_source_session**](IdentitySourceApi.md#delete_identity_source_session) | **DELETE** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId} | Delete an Identity Source Session
[**get_identity_source_session**](IdentitySourceApi.md#get_identity_source_session) | **GET** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId} | Retrieve an Identity Source Session
[**list_identity_source_sessions**](IdentitySourceApi.md#list_identity_source_sessions) | **GET** /api/v1/identity-sources/{identitySourceId}/sessions | List all Identity Source Sessions
[**start_import_from_identity_source**](IdentitySourceApi.md#start_import_from_identity_source) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/start-import | Start the import from the Identity Source
[**upload_identity_source_data_for_delete**](IdentitySourceApi.md#upload_identity_source_data_for_delete) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-delete | Upload the data to be deleted in Okta
[**upload_identity_source_data_for_upsert**](IdentitySourceApi.md#upload_identity_source_data_for_upsert) | **POST** /api/v1/identity-sources/{identitySourceId}/sessions/{sessionId}/bulk-upsert | Upload the data to be upserted in Okta


# **create_identity_source_session**
> List[IdentitySourceSession] create_identity_source_session(identity_source_id)

Create an Identity Source Session

Creates an identity source session for the given identity source instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.identity_source_session import IdentitySourceSession
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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 

    try:
        # Create an Identity Source Session
        api_response = api_instance.create_identity_source_session(identity_source_id)
        print("The response of IdentitySourceApi->create_identity_source_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->create_identity_source_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 

### Return type

[**List[IdentitySourceSession]**](IdentitySourceSession.md)

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

# **delete_identity_source_session**
> delete_identity_source_session(identity_source_id, session_id)

Delete an Identity Source Session

Deletes an identity source session for a given `identitySourceId` and `sessionId`

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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Delete an Identity Source Session
        api_instance.delete_identity_source_session(identity_source_id, session_id)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->delete_identity_source_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 
 **session_id** | **str**|  | 

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

# **get_identity_source_session**
> IdentitySourceSession get_identity_source_session(identity_source_id, session_id)

Retrieve an Identity Source Session

Retrieves an identity source session for a given identity source id and session id

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.identity_source_session import IdentitySourceSession
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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Retrieve an Identity Source Session
        api_response = api_instance.get_identity_source_session(identity_source_id, session_id)
        print("The response of IdentitySourceApi->get_identity_source_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->get_identity_source_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

[**IdentitySourceSession**](IdentitySourceSession.md)

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

# **list_identity_source_sessions**
> List[IdentitySourceSession] list_identity_source_sessions(identity_source_id)

List all Identity Source Sessions

Lists all identity source sessions for the given identity source instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.identity_source_session import IdentitySourceSession
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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 

    try:
        # List all Identity Source Sessions
        api_response = api_instance.list_identity_source_sessions(identity_source_id)
        print("The response of IdentitySourceApi->list_identity_source_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->list_identity_source_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 

### Return type

[**List[IdentitySourceSession]**](IdentitySourceSession.md)

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

# **start_import_from_identity_source**
> List[IdentitySourceSession] start_import_from_identity_source(identity_source_id, session_id)

Start the import from the Identity Source

Starts the import from the identity source described by the uploaded bulk operations

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.identity_source_session import IdentitySourceSession
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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Start the import from the Identity Source
        api_response = api_instance.start_import_from_identity_source(identity_source_id, session_id)
        print("The response of IdentitySourceApi->start_import_from_identity_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->start_import_from_identity_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

[**List[IdentitySourceSession]**](IdentitySourceSession.md)

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

# **upload_identity_source_data_for_delete**
> upload_identity_source_data_for_delete(identity_source_id, session_id, bulk_delete_request_body=bulk_delete_request_body)

Upload the data to be deleted in Okta

Uploads entities that need to be deleted in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.bulk_delete_request_body import BulkDeleteRequestBody
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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 
    session_id = 'session_id_example' # str | 
    bulk_delete_request_body = openapi_client.BulkDeleteRequestBody() # BulkDeleteRequestBody |  (optional)

    try:
        # Upload the data to be deleted in Okta
        api_instance.upload_identity_source_data_for_delete(identity_source_id, session_id, bulk_delete_request_body=bulk_delete_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_data_for_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 
 **session_id** | **str**|  | 
 **bulk_delete_request_body** | [**BulkDeleteRequestBody**](BulkDeleteRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_identity_source_data_for_upsert**
> upload_identity_source_data_for_upsert(identity_source_id, session_id, bulk_upsert_request_body=bulk_upsert_request_body)

Upload the data to be upserted in Okta

Uploads entities that need to be upserted in Okta from the identity source for the given session

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.bulk_upsert_request_body import BulkUpsertRequestBody
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
    api_instance = openapi_client.IdentitySourceApi(api_client)
    identity_source_id = 'identity_source_id_example' # str | 
    session_id = 'session_id_example' # str | 
    bulk_upsert_request_body = openapi_client.BulkUpsertRequestBody() # BulkUpsertRequestBody |  (optional)

    try:
        # Upload the data to be upserted in Okta
        api_instance.upload_identity_source_data_for_upsert(identity_source_id, session_id, bulk_upsert_request_body=bulk_upsert_request_body)
    except Exception as e:
        print("Exception when calling IdentitySourceApi->upload_identity_source_data_for_upsert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_source_id** | **str**|  | 
 **session_id** | **str**|  | 
 **bulk_upsert_request_body** | [**BulkUpsertRequestBody**](BulkUpsertRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

