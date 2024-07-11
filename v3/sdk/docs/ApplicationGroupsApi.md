# okta.ApplicationGroupsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_group_to_application**](ApplicationGroupsApi.md#assign_group_to_application) | **PUT** /api/v1/apps/{appId}/groups/{groupId} | Assign a Group
[**get_application_group_assignment**](ApplicationGroupsApi.md#get_application_group_assignment) | **GET** /api/v1/apps/{appId}/groups/{groupId} | Retrieve an Assigned Group
[**list_application_group_assignments**](ApplicationGroupsApi.md#list_application_group_assignments) | **GET** /api/v1/apps/{appId}/groups | List all Assigned Groups
[**unassign_application_from_group**](ApplicationGroupsApi.md#unassign_application_from_group) | **DELETE** /api/v1/apps/{appId}/groups/{groupId} | Unassign a Group


# **assign_group_to_application**
> ApplicationGroupAssignment assign_group_to_application(app_id, group_id, application_group_assignment=application_group_assignment)

Assign a Group

Assigns a group to an application

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_group_assignment import ApplicationGroupAssignment
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
    api_instance = okta.ApplicationGroupsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    application_group_assignment = okta.ApplicationGroupAssignment() # ApplicationGroupAssignment |  (optional)

    try:
        # Assign a Group
        api_response = api_instance.assign_group_to_application(app_id, group_id, application_group_assignment=application_group_assignment)
        print("The response of ApplicationGroupsApi->assign_group_to_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->assign_group_to_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **application_group_assignment** | [**ApplicationGroupAssignment**](ApplicationGroupAssignment.md)|  | [optional] 

### Return type

[**ApplicationGroupAssignment**](ApplicationGroupAssignment.md)

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

# **get_application_group_assignment**
> ApplicationGroupAssignment get_application_group_assignment(app_id, group_id, expand=expand)

Retrieve an Assigned Group

Retrieves an application group assignment

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_group_assignment import ApplicationGroupAssignment
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
    api_instance = okta.ApplicationGroupsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    expand = 'expand_example' # str |  (optional)

    try:
        # Retrieve an Assigned Group
        api_response = api_instance.get_application_group_assignment(app_id, group_id, expand=expand)
        print("The response of ApplicationGroupsApi->get_application_group_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->get_application_group_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **expand** | **str**|  | [optional] 

### Return type

[**ApplicationGroupAssignment**](ApplicationGroupAssignment.md)

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

# **list_application_group_assignments**
> List[ApplicationGroupAssignment] list_application_group_assignments(app_id, q=q, after=after, limit=limit, expand=expand)

List all Assigned Groups

Lists all group assignments for an application

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_group_assignment import ApplicationGroupAssignment
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
    api_instance = okta.ApplicationGroupsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    q = 'q_example' # str |  (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of assignments (optional)
    limit = -1 # int | Specifies the number of results for a page (optional) (default to -1)
    expand = 'expand_example' # str |  (optional)

    try:
        # List all Assigned Groups
        api_response = api_instance.list_application_group_assignments(app_id, q=q, after=after, limit=limit, expand=expand)
        print("The response of ApplicationGroupsApi->list_application_group_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->list_application_group_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **q** | **str**|  | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of assignments | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to -1]
 **expand** | **str**|  | [optional] 

### Return type

[**List[ApplicationGroupAssignment]**](ApplicationGroupAssignment.md)

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

# **unassign_application_from_group**
> unassign_application_from_group(app_id, group_id)

Unassign a Group

Unassigns a group from an application

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
    api_instance = okta.ApplicationGroupsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Unassign a Group
        api_instance.unassign_application_from_group(app_id, group_id)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->unassign_application_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 

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

