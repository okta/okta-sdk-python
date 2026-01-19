# okta.GroupPushMappingApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_push_mapping**](GroupPushMappingApi.md#create_group_push_mapping) | **POST** /api/v1/apps/{appId}/group-push/mappings | Create a group push mapping
[**delete_group_push_mapping**](GroupPushMappingApi.md#delete_group_push_mapping) | **DELETE** /api/v1/apps/{appId}/group-push/mappings/{mappingId} | Delete a group push mapping
[**get_group_push_mapping**](GroupPushMappingApi.md#get_group_push_mapping) | **GET** /api/v1/apps/{appId}/group-push/mappings/{mappingId} | Retrieve a group push mapping
[**list_group_push_mappings**](GroupPushMappingApi.md#list_group_push_mappings) | **GET** /api/v1/apps/{appId}/group-push/mappings | List all group push mappings
[**update_group_push_mapping**](GroupPushMappingApi.md#update_group_push_mapping) | **PATCH** /api/v1/apps/{appId}/group-push/mappings/{mappingId} | Update a group push mapping


# **create_group_push_mapping**
> GroupPushMapping create_group_push_mapping(app_id, body)

Create a group push mapping

Creates or links a group push mapping.  **Note:** Either `targetGroupId` or `targetGroupName` must be provided, but not both. If `targetGroupId` is provided, it links to an existing group. If `targetGroupName` is provided, it creates a new group.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_group_push_mapping_request import CreateGroupPushMappingRequest
from okta.models.group_push_mapping import GroupPushMapping
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
    api_instance = okta.GroupPushMappingApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    body = okta.CreateGroupPushMappingRequest() # CreateGroupPushMappingRequest | 

    try:
        # Create a group push mapping
        api_response = api_instance.create_group_push_mapping(app_id, body)
        print("The response of GroupPushMappingApi->create_group_push_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupPushMappingApi->create_group_push_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **body** | [**CreateGroupPushMappingRequest**](CreateGroupPushMappingRequest.md)|  | 

### Return type

[**GroupPushMapping**](GroupPushMapping.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_push_mapping**
> delete_group_push_mapping(app_id, mapping_id, delete_target_group)

Delete a group push mapping

Deletes a specific group push mapping. The group push mapping must be in an `INACTIVE` state.

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
    api_instance = okta.GroupPushMappingApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    mapping_id = 'gPm00000000000000000' # str | Group push mapping ID
    delete_target_group = False # bool | If set to `true`, the target group is also deleted. If set to `false`, the target group isn't deleted. (default to False)

    try:
        # Delete a group push mapping
        api_instance.delete_group_push_mapping(app_id, mapping_id, delete_target_group)
    except Exception as e:
        print("Exception when calling GroupPushMappingApi->delete_group_push_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **mapping_id** | **str**| Group push mapping ID | 
 **delete_target_group** | **bool**| If set to &#x60;true&#x60;, the target group is also deleted. If set to &#x60;false&#x60;, the target group isn&#39;t deleted. | [default to False]

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_push_mapping**
> GroupPushMapping get_group_push_mapping(app_id, mapping_id)

Retrieve a group push mapping

Retrieves a group push mapping by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_push_mapping import GroupPushMapping
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
    api_instance = okta.GroupPushMappingApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    mapping_id = 'gPm00000000000000000' # str | Group push mapping ID

    try:
        # Retrieve a group push mapping
        api_response = api_instance.get_group_push_mapping(app_id, mapping_id)
        print("The response of GroupPushMappingApi->get_group_push_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupPushMappingApi->get_group_push_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **mapping_id** | **str**| Group push mapping ID | 

### Return type

[**GroupPushMapping**](GroupPushMapping.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_push_mappings**
> List[GroupPushMapping] list_group_push_mappings(app_id, after=after, limit=limit, last_updated=last_updated, source_group_id=source_group_id, status=status)

List all group push mappings

Lists all group push mappings with pagination support

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_push_mapping import GroupPushMapping
from okta.models.group_push_mapping_status import GroupPushMappingStatus
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
    api_instance = okta.GroupPushMappingApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    after = 'after_example' # str | Specifies the pagination cursor for the next page of mappings (optional)
    limit = 100 # int | Specifies the number of results returned (optional) (default to 100)
    last_updated = '2025-01-01T00:00:00Z' # str | Filters group push mappings by last updated date. The `lastUpdated` parameter supports the following format: `YYYY-MM-DDTHH:mm:ssZ`. This filters mappings updated on or after the specified date and time in UTC.  If you don't specify a value, all group push mappings are returned. (optional)
    source_group_id = '00g00000000000000000' # str | Filters group push mappings by source group ID. If you don't specify a value, all group push mappings are returned. (optional)
    status = okta.GroupPushMappingStatus() # GroupPushMappingStatus | Filters group push mappings by status. If you don't specify a value, all group push mappings are returned. (optional)

    try:
        # List all group push mappings
        api_response = api_instance.list_group_push_mappings(app_id, after=after, limit=limit, last_updated=last_updated, source_group_id=source_group_id, status=status)
        print("The response of GroupPushMappingApi->list_group_push_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupPushMappingApi->list_group_push_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **after** | **str**| Specifies the pagination cursor for the next page of mappings | [optional] 
 **limit** | **int**| Specifies the number of results returned | [optional] [default to 100]
 **last_updated** | **str**| Filters group push mappings by last updated date. The &#x60;lastUpdated&#x60; parameter supports the following format: &#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;. This filters mappings updated on or after the specified date and time in UTC.  If you don&#39;t specify a value, all group push mappings are returned. | [optional] 
 **source_group_id** | **str**| Filters group push mappings by source group ID. If you don&#39;t specify a value, all group push mappings are returned. | [optional] 
 **status** | [**GroupPushMappingStatus**](.md)| Filters group push mappings by status. If you don&#39;t specify a value, all group push mappings are returned. | [optional] 

### Return type

[**List[GroupPushMapping]**](GroupPushMapping.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_push_mapping**
> GroupPushMapping update_group_push_mapping(app_id, mapping_id, body)

Update a group push mapping

Updates the status of a group push mapping

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_push_mapping import GroupPushMapping
from okta.models.update_group_push_mapping_request import UpdateGroupPushMappingRequest
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
    api_instance = okta.GroupPushMappingApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    mapping_id = 'gPm00000000000000000' # str | Group push mapping ID
    body = okta.UpdateGroupPushMappingRequest() # UpdateGroupPushMappingRequest | 

    try:
        # Update a group push mapping
        api_response = api_instance.update_group_push_mapping(app_id, mapping_id, body)
        print("The response of GroupPushMappingApi->update_group_push_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupPushMappingApi->update_group_push_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **mapping_id** | **str**| Group push mapping ID | 
 **body** | [**UpdateGroupPushMappingRequest**](UpdateGroupPushMappingRequest.md)|  | 

### Return type

[**GroupPushMapping**](GroupPushMapping.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

