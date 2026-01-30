# okta.UserLinkedObjectApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_linked_object_value_for_primary**](UserLinkedObjectApi.md#assign_linked_object_value_for_primary) | **PUT** /api/v1/users/{userIdOrLogin}/linkedObjects/{primaryRelationshipName}/{primaryUserId} | Assign a linked object value for primary
[**delete_linked_object_for_user**](UserLinkedObjectApi.md#delete_linked_object_for_user) | **DELETE** /api/v1/users/{userIdOrLogin}/linkedObjects/{relationshipName} | Delete a linked object value
[**list_linked_objects_for_user**](UserLinkedObjectApi.md#list_linked_objects_for_user) | **GET** /api/v1/users/{userIdOrLogin}/linkedObjects/{relationshipName} | List the primary or all of the associated linked object values


# **assign_linked_object_value_for_primary**
> assign_linked_object_value_for_primary(user_id_or_login, primary_relationship_name, primary_user_id)

Assign a linked object value for primary

Assigns the first user as the `associated` and the second user as the `primary` for the specified relationship.  If the first user is already associated with a different `primary` for this relationship, the previous link is removed. A linked object relationship can specify only one primary user for an associated user.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserLinkedObjectApi(api_client)
    user_id_or_login = '00u5zex6ztMbOZhF50h7' # str | If for the `self` link, this is the ID of the user for whom you want to get the primary user ID. If for the `associated` relation, this is the user ID or login value of the user assigned the associated relationship.  This can be `me` to represent the current session user.
    primary_relationship_name = 'manager' # str | Name of the `primary` relationship being assigned
    primary_user_id = 'primary_user_id_example' # str | User ID to be assigned to the `primary` relationship for the `associated` user

    try:
        # Assign a linked object value for primary
        api_instance.assign_linked_object_value_for_primary(user_id_or_login, primary_relationship_name, primary_user_id)
    except Exception as e:
        print("Exception when calling UserLinkedObjectApi->assign_linked_object_value_for_primary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_login** | **str**| If for the &#x60;self&#x60; link, this is the ID of the user for whom you want to get the primary user ID. If for the &#x60;associated&#x60; relation, this is the user ID or login value of the user assigned the associated relationship.  This can be &#x60;me&#x60; to represent the current session user. | 
 **primary_relationship_name** | **str**| Name of the &#x60;primary&#x60; relationship being assigned | 
 **primary_user_id** | **str**| User ID to be assigned to the &#x60;primary&#x60; relationship for the &#x60;associated&#x60; user | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_object_for_user**
> delete_linked_object_for_user(user_id_or_login, relationship_name)

Delete a linked object value

Deletes any existing relationship between the `associated` and `primary` user. For the `associated` user, this is specified by the ID. The `primary` name specifies the relationship.  The operation is successful if the relationship is deleted. The operation is also successful if the specified user isn't in the `associated` relationship for any instance of the specified `primary` and thus, no relationship is found.

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
    api_instance = okta.UserLinkedObjectApi(api_client)
    user_id_or_login = '00u5zex6ztMbOZhF50h7' # str | If for the `self` link, this is the ID of the user for whom you want to get the primary user ID. If for the `associated` relation, this is the user ID or login value of the user assigned the associated relationship.  This can be `me` to represent the current session user.
    relationship_name = 'manager' # str | Name of the `primary` or `associated` relationship being queried

    try:
        # Delete a linked object value
        api_instance.delete_linked_object_for_user(user_id_or_login, relationship_name)
    except Exception as e:
        print("Exception when calling UserLinkedObjectApi->delete_linked_object_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_login** | **str**| If for the &#x60;self&#x60; link, this is the ID of the user for whom you want to get the primary user ID. If for the &#x60;associated&#x60; relation, this is the user ID or login value of the user assigned the associated relationship.  This can be &#x60;me&#x60; to represent the current session user. | 
 **relationship_name** | **str**| Name of the &#x60;primary&#x60; or &#x60;associated&#x60; relationship being queried | 

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

# **list_linked_objects_for_user**
> List[ResponseLinks] list_linked_objects_for_user(user_id_or_login, relationship_name)

List the primary or all of the associated linked object values

Lists either the `self` link for the primary user or all associated users in the relationship specified by `relationshipName`. If the specified user isn't associated in any relationship, an empty array is returned.  Use `me` instead of `id` to specify the current session user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.response_links import ResponseLinks
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
    api_instance = okta.UserLinkedObjectApi(api_client)
    user_id_or_login = '00u5zex6ztMbOZhF50h7' # str | If for the `self` link, this is the ID of the user for whom you want to get the primary user ID. If for the `associated` relation, this is the user ID or login value of the user assigned the associated relationship.  This can be `me` to represent the current session user.
    relationship_name = 'manager' # str | Name of the `primary` or `associated` relationship being queried

    try:
        # List the primary or all of the associated linked object values
        api_response = api_instance.list_linked_objects_for_user(user_id_or_login, relationship_name)
        print("The response of UserLinkedObjectApi->list_linked_objects_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserLinkedObjectApi->list_linked_objects_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_or_login** | **str**| If for the &#x60;self&#x60; link, this is the ID of the user for whom you want to get the primary user ID. If for the &#x60;associated&#x60; relation, this is the user ID or login value of the user assigned the associated relationship.  This can be &#x60;me&#x60; to represent the current session user. | 
 **relationship_name** | **str**| Name of the &#x60;primary&#x60; or &#x60;associated&#x60; relationship being queried | 

### Return type

[**List[ResponseLinks]**](ResponseLinks.md)

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

