# okta.GroupApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupApi.md#add_group) | **POST** /api/v1/groups | Add a group
[**assign_user_to_group**](GroupApi.md#assign_user_to_group) | **PUT** /api/v1/groups/{groupId}/users/{userId} | Assign a user to a group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /api/v1/groups/{groupId} | Delete a group
[**get_group**](GroupApi.md#get_group) | **GET** /api/v1/groups/{groupId} | Retrieve a group
[**list_assigned_applications_for_group**](GroupApi.md#list_assigned_applications_for_group) | **GET** /api/v1/groups/{groupId}/apps | List all assigned apps
[**list_group_users**](GroupApi.md#list_group_users) | **GET** /api/v1/groups/{groupId}/users | List all member users
[**list_groups**](GroupApi.md#list_groups) | **GET** /api/v1/groups | List all groups
[**replace_group**](GroupApi.md#replace_group) | **PUT** /api/v1/groups/{groupId} | Replace a group
[**unassign_user_from_group**](GroupApi.md#unassign_user_from_group) | **DELETE** /api/v1/groups/{groupId}/users/{userId} | Unassign a user from a group


# **add_group**
> Group add_group(group)

Add a group

Adds a new group with the `OKTA_GROUP` type to your org. > **Note:** App import operations are responsible for syncing groups with `APP_GROUP` type such as Active Directory groups. See [About groups](https://help.okta.com/okta_help.htm?id=Directory_Groups) in the help documentation.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.add_group_request import AddGroupRequest
from okta.models.group import Group
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
    api_instance = okta.GroupApi(api_client)
    group = okta.AddGroupRequest() # AddGroupRequest | 

    try:
        # Add a group
        api_response = api_instance.add_group(group)
        print("The response of GroupApi->add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**AddGroupRequest**](AddGroupRequest.md)|  | 

### Return type

[**Group**](Group.md)

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

# **assign_user_to_group**
> assign_user_to_group(group_id, user_id)

Assign a user to a group

Assigns a user to a group with the `OKTA_GROUP` type. > **Note:** You only can modify memberships for groups of the `OKTA_GROUP` type. App imports are responsible for managing group memberships for groups of the `APP_GROUP` type, such as Active Directory groups.

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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # Assign a user to a group
        api_instance.assign_user_to_group(group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupApi->assign_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **user_id** | **str**| ID of an existing Okta user | 

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

# **delete_group**
> delete_group(group_id)

Delete a group

Deletes a group of the `OKTA_GROUP` or `APP_GROUP` type from your org. > **Note:** You can't remove groups of type `APP_GROUP` if they are used in a group push mapping.

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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Delete a group
        api_instance.delete_group(group_id)
    except Exception as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_group**
> Group get_group(group_id)

Retrieve a group

Retrieves a specific group by `id` from your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group import Group
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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group

    try:
        # Retrieve a group
        api_response = api_instance.get_group(group_id)
        print("The response of GroupApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 

### Return type

[**Group**](Group.md)

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

# **list_assigned_applications_for_group**
> List[Application] list_assigned_applications_for_group(group_id, after=after, limit=limit)

List all assigned apps

Lists all apps that are assigned to a group. See [Application Groups API](/openapi/okta-management/management/tag/ApplicationGroups/).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.application import Application
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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    after = 'after_example' # str | Specifies the pagination cursor for the next page of apps (optional)
    limit = 20 # int | Specifies the number of app results for a page (optional) (default to 20)

    try:
        # List all assigned apps
        api_response = api_instance.list_assigned_applications_for_group(group_id, after=after, limit=limit)
        print("The response of GroupApi->list_assigned_applications_for_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_assigned_applications_for_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **after** | **str**| Specifies the pagination cursor for the next page of apps | [optional] 
 **limit** | **int**| Specifies the number of app results for a page | [optional] [default to 20]

### Return type

[**List[Application]**](Application.md)

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

# **list_group_users**
> List[User] list_group_users(group_id, after=after, limit=limit)

List all member users

Lists all users that are a member of a group. The default user limit is set to a very high number due to historical reasons that are no longer valid for most orgs. This will change in a future version of this API. The recommended page limit is now `limit=200`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user import User
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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 1000 # int | Specifies the number of user results in a page (optional) (default to 1000)

    try:
        # List all member users
        api_response = api_instance.list_group_users(group_id, after=after, limit=limit)
        print("The response of GroupApi->list_group_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_group_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| Specifies the number of user results in a page | [optional] [default to 1000]

### Return type

[**List[User]**](User.md)

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

# **list_groups**
> List[Group] list_groups(search=search, filter=filter, q=q, after=after, limit=limit, expand=expand, sort_by=sort_by, sort_order=sort_order)

List all groups

Lists all groups with pagination support.  > **Note:** To list all groups belonging to a member, use the [List all groups endpoint in the User Resources API](/openapi/okta-management/management/tag/UserResources/#tag/UserResources/operation/listUserGroups).  The number of groups returned depends on the specified [`limit`](/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroups!in=query&path=limit&t=request), if you have a search, filter, and/or query parameter set, and if that parameter is not null. We recommend using a limit less than or equal to 200.  A subset of groups can be returned that match a supported filter expression, query, or search criteria.  > **Note:** The `search` parameter results are sourced from an eventually consistent datasource and may not reflect the latest information.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.group import Group
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
    api_instance = okta.GroupApi(api_client)
    search = 'type%20eq%20%22APP_GROUP%22' # str | Searches for groups with a supported [filtering](https://developer.okta.com/docs/api/#filter) expression for all properties except for `_embedded`, `_links`, and `objectClass`. Okta recommends this query parameter because it provides the largest range of search options and optimal performance.  This operation supports [pagination](https://developer.okta.com/docs/api/#pagination).  Using search requires [URL encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding), for example, `search=type eq \"OKTA_GROUP\"` is encoded as `search=type+eq+%22OKTA_GROUP%22`.  This operation searches many properties:  * Any group profile attribute, including imported app group profile attributes. * The top-level properties: `id`, `created`, `lastMembershipUpdated`, `lastUpdated`, and `type`. * The [source](/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroups!c=200&path=_links/source&t=response) of groups with type of `APP_GROUP`, accessed as `source.id`.  You can also use the `sortBy` and `sortOrder` parameters.  Searches for groups can be filtered by the following operators: `sw`, `eq`, and `co`. You can only use `co` with these select profile attributes: `profile.name` and `profile.description`. See [Operators](https://developer.okta.com/docs/api/#operators). (optional)
    filter = 'id%20eq%20%2200g1emaKYZTWRYYRRTSK%22' # str | Filter expression for groups. See [Filter](https://developer.okta.com/docs/api/#filter).  Filtering supports the following limited number of properties: `id`, `type`, `lastUpdated`, and `lastMembershipUpdated`.  > **Note:** All filters must be [URL encoded](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). For example, `filter=lastUpdated gt \"2013-06-01T00:00:00.000Z\"` is encoded as `filter=lastUpdated%20gt%20%222013-06-01T00:00:00.000Z%22`.  See [Special characters](https://developer.okta.com/docs/api/#special-characters). (optional)
    q = 'West&limit=10' # str | Finds a group that matches the `name` property. > **Note:** Paging and searching are currently mutually exclusive. You can't page a query. The default limit for a query is 300 results. Query is intended for an auto-complete picker use case where users refine their search string to constrain the results. (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of groups. The `after` cursor should be treated as an opaque value and obtained through the next link relation. See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)
    limit = 56 # int | Specifies the number of group results in a page.  Okta recommends using a specific value other than the default or maximum. If your request times out, retry your request with a smaller `limit` and [page the results](https://developer.okta.com/docs/api/#pagination).  The Okta default `Everyone` group isn't returned for users with a group admin role. (optional)
    expand = 'expand_example' # str | If specified, additional metadata is included in the response. Possible values are `stats` and `app`. This additional metadata is listed in the [`_embedded`](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/#tag/Group/operation/addGroup!c=200&path=_embedded&t=response) property of the response.  > **Note:** You can use the `stats` value to return the number of users within a group. This is listed as the `_embedded.stats.usersCount` value in the response. See this [Knowledge Base article](https://support.okta.com/help/s/article/Is-there-an-API-that-returns-the-number-of-users-in-a-group?language=en_US) for more information and an example. (optional)
    sort_by = 'lastUpdated' # str | Specifies the field to sort by (for search queries only). `sortBy` can be any single property, for example `sortBy=profile.name`. Groups with the same value for the `sortBy` property are ordered by `id`'. Use with `sortOrder` to control the order of results. (optional)
    sort_order = 'asc' # str | Specifies sort order: `asc` or `desc` (for search queries only). This parameter is ignored if `sortBy` isn't present. (optional) (default to 'asc')

    try:
        # List all groups
        api_response = api_instance.list_groups(search=search, filter=filter, q=q, after=after, limit=limit, expand=expand, sort_by=sort_by, sort_order=sort_order)
        print("The response of GroupApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Searches for groups with a supported [filtering](https://developer.okta.com/docs/api/#filter) expression for all properties except for &#x60;_embedded&#x60;, &#x60;_links&#x60;, and &#x60;objectClass&#x60;. Okta recommends this query parameter because it provides the largest range of search options and optimal performance.  This operation supports [pagination](https://developer.okta.com/docs/api/#pagination).  Using search requires [URL encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding), for example, &#x60;search&#x3D;type eq \&quot;OKTA_GROUP\&quot;&#x60; is encoded as &#x60;search&#x3D;type+eq+%22OKTA_GROUP%22&#x60;.  This operation searches many properties:  * Any group profile attribute, including imported app group profile attributes. * The top-level properties: &#x60;id&#x60;, &#x60;created&#x60;, &#x60;lastMembershipUpdated&#x60;, &#x60;lastUpdated&#x60;, and &#x60;type&#x60;. * The [source](/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroups!c&#x3D;200&amp;path&#x3D;_links/source&amp;t&#x3D;response) of groups with type of &#x60;APP_GROUP&#x60;, accessed as &#x60;source.id&#x60;.  You can also use the &#x60;sortBy&#x60; and &#x60;sortOrder&#x60; parameters.  Searches for groups can be filtered by the following operators: &#x60;sw&#x60;, &#x60;eq&#x60;, and &#x60;co&#x60;. You can only use &#x60;co&#x60; with these select profile attributes: &#x60;profile.name&#x60; and &#x60;profile.description&#x60;. See [Operators](https://developer.okta.com/docs/api/#operators). | [optional] 
 **filter** | **str**| Filter expression for groups. See [Filter](https://developer.okta.com/docs/api/#filter).  Filtering supports the following limited number of properties: &#x60;id&#x60;, &#x60;type&#x60;, &#x60;lastUpdated&#x60;, and &#x60;lastMembershipUpdated&#x60;.  &gt; **Note:** All filters must be [URL encoded](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). For example, &#x60;filter&#x3D;lastUpdated gt \&quot;2013-06-01T00:00:00.000Z\&quot;&#x60; is encoded as &#x60;filter&#x3D;lastUpdated%20gt%20%222013-06-01T00:00:00.000Z%22&#x60;.  See [Special characters](https://developer.okta.com/docs/api/#special-characters). | [optional] 
 **q** | **str**| Finds a group that matches the &#x60;name&#x60; property. &gt; **Note:** Paging and searching are currently mutually exclusive. You can&#39;t page a query. The default limit for a query is 300 results. Query is intended for an auto-complete picker use case where users refine their search string to constrain the results. | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of groups. The &#x60;after&#x60; cursor should be treated as an opaque value and obtained through the next link relation. See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 
 **limit** | **int**| Specifies the number of group results in a page.  Okta recommends using a specific value other than the default or maximum. If your request times out, retry your request with a smaller &#x60;limit&#x60; and [page the results](https://developer.okta.com/docs/api/#pagination).  The Okta default &#x60;Everyone&#x60; group isn&#39;t returned for users with a group admin role. | [optional] 
 **expand** | **str**| If specified, additional metadata is included in the response. Possible values are &#x60;stats&#x60; and &#x60;app&#x60;. This additional metadata is listed in the [&#x60;_embedded&#x60;](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/#tag/Group/operation/addGroup!c&#x3D;200&amp;path&#x3D;_embedded&amp;t&#x3D;response) property of the response.  &gt; **Note:** You can use the &#x60;stats&#x60; value to return the number of users within a group. This is listed as the &#x60;_embedded.stats.usersCount&#x60; value in the response. See this [Knowledge Base article](https://support.okta.com/help/s/article/Is-there-an-API-that-returns-the-number-of-users-in-a-group?language&#x3D;en_US) for more information and an example. | [optional] 
 **sort_by** | **str**| Specifies the field to sort by (for search queries only). &#x60;sortBy&#x60; can be any single property, for example &#x60;sortBy&#x3D;profile.name&#x60;. Groups with the same value for the &#x60;sortBy&#x60; property are ordered by &#x60;id&#x60;&#39;. Use with &#x60;sortOrder&#x60; to control the order of results. | [optional] 
 **sort_order** | **str**| Specifies sort order: &#x60;asc&#x60; or &#x60;desc&#x60; (for search queries only). This parameter is ignored if &#x60;sortBy&#x60; isn&#39;t present. | [optional] [default to &#39;asc&#39;]

### Return type

[**List[Group]**](Group.md)

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

# **replace_group**
> Group replace_group(group_id, group)

Replace a group

Replaces the profile for a group of `OKTA_GROUP` type from your org. > **Note :** You only can modify profiles for groups of the `OKTA_GROUP` type. > > App imports are responsible for updating profiles for groups of the `APP_GROUP` type, such as Active Directory groups.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.add_group_request import AddGroupRequest
from okta.models.group import Group
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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    group = okta.AddGroupRequest() # AddGroupRequest | 

    try:
        # Replace a group
        api_response = api_instance.replace_group(group_id, group)
        print("The response of GroupApi->replace_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->replace_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **group** | [**AddGroupRequest**](AddGroupRequest.md)|  | 

### Return type

[**Group**](Group.md)

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

# **unassign_user_from_group**
> unassign_user_from_group(group_id, user_id)

Unassign a user from a group

Unassigns a user from a group with the `OKTA_GROUP` type. > **Note:** You only can modify memberships for groups of the `OKTA_GROUP` type. > > App imports are responsible for managing group memberships for groups of the `APP_GROUP` type, such as Active Directory groups.

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
    api_instance = okta.GroupApi(api_client)
    group_id = '00g1emaKYZTWRYYRRTSK' # str | The `id` of the group
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # Unassign a user from a group
        api_instance.unassign_user_from_group(group_id, user_id)
    except Exception as e:
        print("Exception when calling GroupApi->unassign_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &#x60;id&#x60; of the group | 
 **user_id** | **str**| ID of an existing Okta user | 

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

