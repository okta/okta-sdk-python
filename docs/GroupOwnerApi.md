# okta.GroupOwnerApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_group_owner**](GroupOwnerApi.md#assign_group_owner) | **POST** /api/v1/groups/{groupId}/owners | Assign a group owner
[**delete_group_owner**](GroupOwnerApi.md#delete_group_owner) | **DELETE** /api/v1/groups/{groupId}/owners/{ownerId} | Delete a group owner
[**list_group_owners**](GroupOwnerApi.md#list_group_owners) | **GET** /api/v1/groups/{groupId}/owners | List all group owners


# **assign_group_owner**
> GroupOwner assign_group_owner(group_id, assign_group_owner_request_body)

Assign a group owner

Assigns a group owner

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.assign_group_owner_request_body import AssignGroupOwnerRequestBody
from okta.models.group_owner import GroupOwner
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
    api_instance = okta.GroupOwnerApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    assign_group_owner_request_body = okta.AssignGroupOwnerRequestBody() # AssignGroupOwnerRequestBody | 

    try:
        # Assign a group owner
        api_response = api_instance.assign_group_owner(group_id, assign_group_owner_request_body)
        print("The response of GroupOwnerApi->assign_group_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupOwnerApi->assign_group_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **assign_group_owner_request_body** | [**AssignGroupOwnerRequestBody**](AssignGroupOwnerRequestBody.md)|  | 

### Return type

[**GroupOwner**](GroupOwner.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_owner**
> delete_group_owner(group_id, owner_id)

Delete a group owner

Deletes a group owner from a specific group

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
    api_instance = okta.GroupOwnerApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    owner_id = '00u1emaK22TWRYd3TtG' # str | The `id` of the group owner

    try:
        # Delete a group owner
        api_instance.delete_group_owner(group_id, owner_id)
    except Exception as e:
        print("Exception when calling GroupOwnerApi->delete_group_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **owner_id** | **str**| The &#x60;id&#x60; of the group owner | 

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

# **list_group_owners**
> List[GroupOwner] list_group_owners(group_id, search=search, after=after, limit=limit)

List all group owners

Lists all owners for a specific group

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group_owner import GroupOwner
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
    api_instance = okta.GroupOwnerApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    search = 'search_example' # str | SCIM filter expression for group owners. Allows you to filter owners by type. (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of owners (optional)
    limit = 1000 # int | Specifies the number of owner results in a page (optional) (default to 1000)

    try:
        # List all group owners
        api_response = api_instance.list_group_owners(group_id, search=search, after=after, limit=limit)
        print("The response of GroupOwnerApi->list_group_owners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupOwnerApi->list_group_owners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **search** | **str**| SCIM filter expression for group owners. Allows you to filter owners by type. | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of owners | [optional] 
 **limit** | **int**| Specifies the number of owner results in a page | [optional] [default to 1000]

### Return type

[**List[GroupOwner]**](GroupOwner.md)

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

