# okta.RealmAssignmentApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_realm_assignment**](RealmAssignmentApi.md#activate_realm_assignment) | **POST** /api/v1/realm-assignments/{assignmentId}/lifecycle/activate | Activate a realm assignment
[**create_realm_assignment**](RealmAssignmentApi.md#create_realm_assignment) | **POST** /api/v1/realm-assignments | Create a realm assignment
[**deactivate_realm_assignment**](RealmAssignmentApi.md#deactivate_realm_assignment) | **POST** /api/v1/realm-assignments/{assignmentId}/lifecycle/deactivate | Deactivate a realm assignment
[**delete_realm_assignment**](RealmAssignmentApi.md#delete_realm_assignment) | **DELETE** /api/v1/realm-assignments/{assignmentId} | Delete a realm assignment
[**execute_realm_assignment**](RealmAssignmentApi.md#execute_realm_assignment) | **POST** /api/v1/realm-assignments/operations | Execute a realm assignment
[**get_realm_assignment**](RealmAssignmentApi.md#get_realm_assignment) | **GET** /api/v1/realm-assignments/{assignmentId} | Retrieve a realm assignment
[**list_realm_assignment_operations**](RealmAssignmentApi.md#list_realm_assignment_operations) | **GET** /api/v1/realm-assignments/operations | List all realm assignment operations
[**list_realm_assignments**](RealmAssignmentApi.md#list_realm_assignments) | **GET** /api/v1/realm-assignments | List all realm assignments
[**replace_realm_assignment**](RealmAssignmentApi.md#replace_realm_assignment) | **PUT** /api/v1/realm-assignments/{assignmentId} | Replace a realm assignment


# **activate_realm_assignment**
> activate_realm_assignment(assignment_id)

Activate a realm assignment

Activates a realm assignment

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
    api_instance = okta.RealmAssignmentApi(api_client)
    assignment_id = 'rul2jy7jLUlnO3ng00g4' # str | ID of the realm assignment

    try:
        # Activate a realm assignment
        api_instance.activate_realm_assignment(assignment_id)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->activate_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| ID of the realm assignment | 

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

# **create_realm_assignment**
> RealmAssignment create_realm_assignment(body)

Create a realm assignment

Creates a new realm assignment

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_realm_assignment_request import CreateRealmAssignmentRequest
from okta.models.realm_assignment import RealmAssignment
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
    api_instance = okta.RealmAssignmentApi(api_client)
    body = okta.CreateRealmAssignmentRequest() # CreateRealmAssignmentRequest | 

    try:
        # Create a realm assignment
        api_response = api_instance.create_realm_assignment(body)
        print("The response of RealmAssignmentApi->create_realm_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->create_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRealmAssignmentRequest**](CreateRealmAssignmentRequest.md)|  | 

### Return type

[**RealmAssignment**](RealmAssignment.md)

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

# **deactivate_realm_assignment**
> deactivate_realm_assignment(assignment_id)

Deactivate a realm assignment

Deactivates a realm assignment

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
    api_instance = okta.RealmAssignmentApi(api_client)
    assignment_id = 'rul2jy7jLUlnO3ng00g4' # str | ID of the realm assignment

    try:
        # Deactivate a realm assignment
        api_instance.deactivate_realm_assignment(assignment_id)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->deactivate_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| ID of the realm assignment | 

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

# **delete_realm_assignment**
> delete_realm_assignment(assignment_id)

Delete a realm assignment

Deletes a realm assignment

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
    api_instance = okta.RealmAssignmentApi(api_client)
    assignment_id = 'rul2jy7jLUlnO3ng00g4' # str | ID of the realm assignment

    try:
        # Delete a realm assignment
        api_instance.delete_realm_assignment(assignment_id)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->delete_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| ID of the realm assignment | 

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

# **execute_realm_assignment**
> RealmAssignmentOperationResponse execute_realm_assignment(body)

Execute a realm assignment

Executes a realm assignment

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.operation_request import OperationRequest
from okta.models.realm_assignment_operation_response import RealmAssignmentOperationResponse
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
    api_instance = okta.RealmAssignmentApi(api_client)
    body = {"assignmentId":"0pr1b7rxZj2ibQzfP0g5"} # OperationRequest | 

    try:
        # Execute a realm assignment
        api_response = api_instance.execute_realm_assignment(body)
        print("The response of RealmAssignmentApi->execute_realm_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->execute_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)|  | 

### Return type

[**RealmAssignmentOperationResponse**](RealmAssignmentOperationResponse.md)

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

# **get_realm_assignment**
> RealmAssignment get_realm_assignment(assignment_id)

Retrieve a realm assignment

Retrieves a realm assignment

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.realm_assignment import RealmAssignment
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
    api_instance = okta.RealmAssignmentApi(api_client)
    assignment_id = 'rul2jy7jLUlnO3ng00g4' # str | ID of the realm assignment

    try:
        # Retrieve a realm assignment
        api_response = api_instance.get_realm_assignment(assignment_id)
        print("The response of RealmAssignmentApi->get_realm_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->get_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| ID of the realm assignment | 

### Return type

[**RealmAssignment**](RealmAssignment.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **list_realm_assignment_operations**
> List[RealmAssignmentOperationResponse] list_realm_assignment_operations(limit=limit, after=after)

List all realm assignment operations

Lists all realm assignment operations. The upper limit is 200 and operations are sorted in descending order from most recent to oldest by ID.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.realm_assignment_operation_response import RealmAssignmentOperationResponse
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
    api_instance = okta.RealmAssignmentApi(api_client)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)

    try:
        # List all realm assignment operations
        api_response = api_instance.list_realm_assignment_operations(limit=limit, after=after)
        print("The response of RealmAssignmentApi->list_realm_assignment_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->list_realm_assignment_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 

### Return type

[**List[RealmAssignmentOperationResponse]**](RealmAssignmentOperationResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_realm_assignments**
> List[RealmAssignment] list_realm_assignments(limit=limit, after=after)

List all realm assignments

Lists all realm assignments

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.realm_assignment import RealmAssignment
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
    api_instance = okta.RealmAssignmentApi(api_client)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    after = 'after_example' # str | The cursor used for pagination. It represents the priority of the last realm assignment returned in the previous fetch operation. (optional)

    try:
        # List all realm assignments
        api_response = api_instance.list_realm_assignments(limit=limit, after=after)
        print("The response of RealmAssignmentApi->list_realm_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->list_realm_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **after** | **str**| The cursor used for pagination. It represents the priority of the last realm assignment returned in the previous fetch operation. | [optional] 

### Return type

[**List[RealmAssignment]**](RealmAssignment.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_realm_assignment**
> RealmAssignment replace_realm_assignment(assignment_id, body)

Replace a realm assignment

Replaces a realm assignment

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.realm_assignment import RealmAssignment
from okta.models.update_realm_assignment_request import UpdateRealmAssignmentRequest
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
    api_instance = okta.RealmAssignmentApi(api_client)
    assignment_id = 'rul2jy7jLUlnO3ng00g4' # str | ID of the realm assignment
    body = okta.UpdateRealmAssignmentRequest() # UpdateRealmAssignmentRequest | 

    try:
        # Replace a realm assignment
        api_response = api_instance.replace_realm_assignment(assignment_id, body)
        print("The response of RealmAssignmentApi->replace_realm_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RealmAssignmentApi->replace_realm_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**| ID of the realm assignment | 
 **body** | [**UpdateRealmAssignmentRequest**](UpdateRealmAssignmentRequest.md)|  | 

### Return type

[**RealmAssignment**](RealmAssignment.md)

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

