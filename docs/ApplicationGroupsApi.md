# okta.ApplicationGroupsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_group_to_application**](ApplicationGroupsApi.md#assign_group_to_application) | **PUT** /api/v1/apps/{appId}/groups/{groupId} | Assign an application group
[**get_application_group_assignment**](ApplicationGroupsApi.md#get_application_group_assignment) | **GET** /api/v1/apps/{appId}/groups/{groupId} | Retrieve an application group
[**list_application_group_assignments**](ApplicationGroupsApi.md#list_application_group_assignments) | **GET** /api/v1/apps/{appId}/groups | List all application groups
[**unassign_application_from_group**](ApplicationGroupsApi.md#unassign_application_from_group) | **DELETE** /api/v1/apps/{appId}/groups/{groupId} | Unassign an application group
[**update_group_assignment_to_application**](ApplicationGroupsApi.md#update_group_assignment_to_application) | **PATCH** /api/v1/apps/{appId}/groups/{groupId} | Update an application group


# **assign_group_to_application**
> ApplicationGroupAssignment assign_group_to_application(app_id, group_id, application_group_assignment=application_group_assignment)

Assign an application group

Assigns a [Group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) to an app, which in turn assigns the app to each [User](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/) that belongs to the group. The resulting application user [scope](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/ApplicationUsers/#tag/ApplicationUsers/operation/listApplicationUsers!c=200&path=scope&t=response) is `GROUP` since the assignment was from the group membership.

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    application_group_assignment = okta.ApplicationGroupAssignment() # ApplicationGroupAssignment |  (optional)

    try:
        # Assign an application group
        api_response = api_instance.assign_group_to_application(app_id, group_id, application_group_assignment=application_group_assignment)
        print("The response of ApplicationGroupsApi->assign_group_to_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->assign_group_to_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
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

Retrieve an application group

Retrieves an app group assignment

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    expand = 'group' # str | An optional query parameter to return the corresponding assigned [group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) or the group assignment metadata details in the `_embedded` property. (optional)

    try:
        # Retrieve an application group
        api_response = api_instance.get_application_group_assignment(app_id, group_id, expand=expand)
        print("The response of ApplicationGroupsApi->get_application_group_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->get_application_group_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **expand** | **str**| An optional query parameter to return the corresponding assigned [group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) or the group assignment metadata details in the &#x60;_embedded&#x60; property. | [optional] 

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

List all application groups

Lists all app group assignments

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    q = 'test' # str | Specifies a filter for a list of assigned groups returned based on their names. The value of `q` is matched against the group `name`. This filter only supports the `startsWith` operation that matches the `q` string against the beginning of the [group name](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroups!c=200&path=profile/name&t=response). (optional)
    after = '16275000448691' # str | Specifies the pagination cursor for the `next` page of results. Treat this as an opaque value obtained through the next link relationship. See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)
    limit = 20 # int | Specifies the number of objects to return per page. If there are multiple pages of results, the Link header contains a `next` link that you need to use as an opaque value (follow it, don't parse it). See [Pagination](/#pagination). (optional) (default to 20)
    expand = 'group' # str | An optional query parameter to return the corresponding assigned [group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) or the group assignment metadata details in the `_embedded` property. (optional)

    try:
        # List all application groups
        api_response = api_instance.list_application_group_assignments(app_id, q=q, after=after, limit=limit, expand=expand)
        print("The response of ApplicationGroupsApi->list_application_group_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->list_application_group_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **q** | **str**| Specifies a filter for a list of assigned groups returned based on their names. The value of &#x60;q&#x60; is matched against the group &#x60;name&#x60;. This filter only supports the &#x60;startsWith&#x60; operation that matches the &#x60;q&#x60; string against the beginning of the [group name](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroups!c&#x3D;200&amp;path&#x3D;profile/name&amp;t&#x3D;response). | [optional] 
 **after** | **str**| Specifies the pagination cursor for the &#x60;next&#x60; page of results. Treat this as an opaque value obtained through the next link relationship. See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 
 **limit** | **int**| Specifies the number of objects to return per page. If there are multiple pages of results, the Link header contains a &#x60;next&#x60; link that you need to use as an opaque value (follow it, don&#39;t parse it). See [Pagination](/#pagination). | [optional] [default to 20]
 **expand** | **str**| An optional query parameter to return the corresponding assigned [group](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/) or the group assignment metadata details in the &#x60;_embedded&#x60; property. | [optional] 

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

Unassign an application group

Unassigns a Group from an app

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Unassign an application group
        api_instance.unassign_application_from_group(app_id, group_id)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->unassign_application_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
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

# **update_group_assignment_to_application**
> ApplicationGroupAssignment update_group_assignment_to_application(app_id, group_id, json_patch_operation=json_patch_operation)

Update an application group

Updates a group assignment to an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application_group_assignment import ApplicationGroupAssignment
from okta.models.json_patch_operation import JsonPatchOperation
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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    json_patch_operation = [okta.JsonPatchOperation()] # List[JsonPatchOperation] |  (optional)

    try:
        # Update an application group
        api_response = api_instance.update_group_assignment_to_application(app_id, group_id, json_patch_operation=json_patch_operation)
        print("The response of ApplicationGroupsApi->update_group_assignment_to_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->update_group_assignment_to_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)|  | [optional] 

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

