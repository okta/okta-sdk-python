# okta.UserApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /api/v1/users | Create a user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/v1/users/{id} | Delete a user
[**get_user**](UserApi.md#get_user) | **GET** /api/v1/users/{id} | Retrieve a user
[**list_user_blocks**](UserApi.md#list_user_blocks) | **GET** /api/v1/users/{id}/blocks | List all user blocks
[**list_users**](UserApi.md#list_users) | **GET** /api/v1/users | List all users
[**replace_user**](UserApi.md#replace_user) | **PUT** /api/v1/users/{id} | Replace a user
[**update_user**](UserApi.md#update_user) | **POST** /api/v1/users/{id} | Update a user


# **create_user**
> User create_user(body, activate=activate, provider=provider, next_login=next_login)

Create a user

Creates a new user in your Okta org with or without credentials.<br> > **Legal Disclaimer** > > After a user is added to the Okta directory, they receive an activation email. As part of signing up for this service, > you agreed not to use Okta's service/product to spam and/or send unsolicited messages. > Please refrain from adding unrelated accounts to the directory as Okta is not responsible for, and disclaims any and all > liability associated with, the activation email's content. You, and you alone, bear responsibility for the emails sent to any recipients.  All responses return the created user. Activation of a user is an asynchronous operation. The system performs group reconciliation during activation and assigns the user to all apps via direct or indirect relationships (group memberships). * The user's `transitioningToStatus` property is `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation. * The user's `status` is `ACTIVE` when the activation process is complete.  The user is emailed a one-time activation token if activated without a password.  > **Note:** If the user is assigned to an app that is configured for provisioning, the activation process triggers downstream provisioning to the app.  It is possible for a user to sign in before these apps have been successfully provisioned for the user.  > **Important:** Do not generate or send a one-time activation token when activating users with an assigned password. Users should sign in with their assigned password.  For more information about the various scenarios of creating a user listed in the examples, see the [User creation scenarios](/openapi/okta-management/management/tag/User/#user-creation-scenarios) section.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.create_user_request import CreateUserRequest
from okta.models.user import User
from okta.models.user_next_login import UserNextLogin
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
    api_instance = okta.UserApi(api_client)
    body = okta.CreateUserRequest() # CreateUserRequest | 
    activate = True # bool | Executes an [activation lifecycle](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserLifecycle/#tag/UserLifecycle/operation/activateUser) operation when creating the user (optional) (default to True)
    provider = False # bool | Indicates whether to create a user with a specified authentication provider (optional) (default to False)
    next_login = okta.UserNextLogin() # UserNextLogin | With `activate=true`, if `nextLogin=changePassword`, a user is created, activated, and the password is set to `EXPIRED`. The user must change it the next time they sign in. (optional)

    try:
        # Create a user
        api_response = api_instance.create_user(body, activate=activate, provider=provider, next_login=next_login)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **activate** | **bool**| Executes an [activation lifecycle](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserLifecycle/#tag/UserLifecycle/operation/activateUser) operation when creating the user | [optional] [default to True]
 **provider** | **bool**| Indicates whether to create a user with a specified authentication provider | [optional] [default to False]
 **next_login** | [**UserNextLogin**](.md)| With &#x60;activate&#x3D;true&#x60;, if &#x60;nextLogin&#x3D;changePassword&#x60;, a user is created, activated, and the password is set to &#x60;EXPIRED&#x60;. The user must change it the next time they sign in. | [optional] 

### Return type

[**User**](User.md)

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

# **delete_user**
> delete_user(id, send_email=send_email, prefer=prefer)

Delete a user

Deletes a user permanently. This operation can only be performed on users that have a `DEPROVISIONED` status.  > **Warning:** This action can't be recovered!  This operation on a user that hasn't been deactivated causes that user to be deactivated. A second delete operation is required to delete the user.  > **Note:** You can also perform user deletion asynchronously. To invoke asynchronous user deletion, pass an HTTP header `Prefer: respond-async` with the request.  This header is also supported by user deactivation, which is performed if the delete endpoint is invoked on a user that hasn't been deactivated.

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
    api_instance = okta.UserApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    send_email = False # bool | Sends a deactivation email to the admin if `true` (optional) (default to False)
    prefer = 'prefer_example' # str |  (optional)

    try:
        # Delete a user
        api_instance.delete_user(id, send_email=send_email, prefer=prefer)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **send_email** | **bool**| Sends a deactivation email to the admin if &#x60;true&#x60; | [optional] [default to False]
 **prefer** | **str**|  | [optional] 

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

# **get_user**
> User get_user(id, content_type=content_type, expand=expand)

Retrieve a user

Retrieves a user from your Okta org.  You can substitute `me` for the `id` to fetch the current user linked to an API token or session cookie.  * The request returns the user linked to the API token that is specified in the Authorization header, not the user linked to the active session. Details of the admin user who granted the API token is returned.  * When the end user has an active Okta session, it is typically a CORS request from the browser. Therefore, it's possible to retrieve the current user without the Authorization header.  When fetching a user by `login` or `login shortname`, [URL encode](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding) the request parameter to ensure that special characters are escaped properly. Logins with a `/` character can only be fetched by `id` due to URL issues with escaping the `/` character. If you don't know a user's ID, you can use the [List all users](/openapi/okta-management/management/tag/User/#tag/User/operation/listUsers) endpoint to find it.  > **Note:** Some browsers block third-party cookies by default, which disrupts Okta functionality in certain flows. See [Mitigate the impact of third-party cookie deprecation](https://help.okta.com/okta_help.htm?type=oie&id=ext-third-party-cookies).

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
    api_instance = okta.UserApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    content_type = 'application/json; okta-response=omitCredentials,omitCredentialsLinks' # str | Specifies the media type of the resource. Optional `okta-response` value can be included for performance optimization.  Complex DelAuth configurations may degrade performance when fetching specific parts of the response, and passing this parameter can omit these parts, bypassing the bottleneck.  Enum values for `okta-response`:   * `omitCredentials`: Omits the credentials subobject from the response.   * `omitCredentialsLinks`: Omits the following HAL links from the response: Update password, Change recovery question, Start forgot password flow, Reset password, Reset factors, Unlock.   * `omitTransitioningToStatus`: Omits the `transitioningToStatus` field from the response. (optional)
    expand = 'blocks' # str | An optional parameter to include metadata in the `_embedded` attribute. Valid values: `blocks` or <x-lifecycle class=\"ea\"></x-lifecycle> `classification`. (optional)

    try:
        # Retrieve a user
        api_response = api_instance.get_user(id, content_type=content_type, expand=expand)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **content_type** | **str**| Specifies the media type of the resource. Optional &#x60;okta-response&#x60; value can be included for performance optimization.  Complex DelAuth configurations may degrade performance when fetching specific parts of the response, and passing this parameter can omit these parts, bypassing the bottleneck.  Enum values for &#x60;okta-response&#x60;:   * &#x60;omitCredentials&#x60;: Omits the credentials subobject from the response.   * &#x60;omitCredentialsLinks&#x60;: Omits the following HAL links from the response: Update password, Change recovery question, Start forgot password flow, Reset password, Reset factors, Unlock.   * &#x60;omitTransitioningToStatus&#x60;: Omits the &#x60;transitioningToStatus&#x60; field from the response. | [optional] 
 **expand** | **str**| An optional parameter to include metadata in the &#x60;_embedded&#x60; attribute. Valid values: &#x60;blocks&#x60; or &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; &#x60;classification&#x60;. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Etag - An HTTP entity tag (&#x60;ETag&#x60;) is an identifier for a specific version of a resource. See [Conditional Requests and Entity Tags](/#conditional-requests-and-entity-tags). <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_blocks**
> List[UserBlock] list_user_blocks(id)

List all user blocks

Lists information about how the user is blocked from accessing their account

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_block import UserBlock
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
    api_instance = okta.UserApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # List all user blocks
        api_response = api_instance.list_user_blocks(id)
        print("The response of UserApi->list_user_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

### Return type

[**List[UserBlock]**](UserBlock.md)

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

# **list_users**
> List[User] list_users(content_type=content_type, search=search, filter=filter, q=q, after=after, limit=limit, sort_by=sort_by, sort_order=sort_order, fields=fields, expand=expand)

List all users

Lists users in your org, with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria. Different results are returned depending on specified queries in the request.  > **Notes:** >  * This operation omits users that have a status of `DEPROVISIONED` in the response. To return all users, use a filter or search query instead. >  * The `search` parameter results are sourced from an eventually consistent datasource and may not reflect the latest information.

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
    api_instance = okta.UserApi(api_client)
    content_type = 'application/json; okta-response=omitCredentials,omitCredentialsLinks' # str | Specifies the media type of the resource. Optional `okta-response` value can be included for performance optimization.  Complex DelAuth configurations may degrade performance when fetching specific parts of the response, and passing this parameter can omit these parts, bypassing the bottleneck.  Enum values for `okta-response`:   * `omitCredentials`: Omits the credentials subobject from the response.   * `omitCredentialsLinks`: Omits the following HAL links from the response: Update password, Change recovery question, Start forgot password flow, Reset password, Reset factors, Unlock.   * `omitTransitioningToStatus`: Omits the `transitioningToStatus` field from the response. (optional)
    search = 'status%20eq%20%22STAGED%22' # str | Searches for users with a supported filtering expression for most properties. Okta recommends this query parameter because it provides the largest range of search options and optimal performance.  > **Note:** Using an overly complex or long search query can result in an error.  This operation supports [pagination](https://developer.okta.com/docs/api/#pagination). Use an ID lookup for records that you update to ensure your results contain the latest data. Returned users include those with the `DEPROVISIONED` status.  Property names in the search parameter are case sensitive, whereas operators (`eq`, `sw`, and so on) and string values are case insensitive. Unlike with user logins, diacritical marks are significant in search string values: a search for `isaac.brock` finds `Isaac.Brock`, but doesn't find a property whose value is `isáàc.bröck`.  This operation requires [URL encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). See [Special characters](https://developer.okta.com/docs/api/#special-characters).  This operation searches many properties:   * Any user profile attribute, including custom-defined attributes   * The top-level properties: `id`, `status`, `created`, `activated`, `statusChanged`, and `lastUpdated`   * The [user type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/#tag/UserType/operation/updateUserType) accessed as `type.id`   * Properties that have array values  > **Note:** <x-lifecycle class=\"ea\"></x-lifecycle> The ability to search by user classification is available as an [Early Access](https://developer.okta.com/docs/api/openapi/okta-management/guides/release-lifecycle/#early-access-ea) feature. The `classification.type` property cannot be used in conjunction with other search terms. You can search using `classification.type eq \"LITE\"` or `classification.type eq \"STANDARD\"`.  You can also use `sortBy` and `sortOrder` parameters. The `ne` (not equal) operator isn't supported, but you can obtain the same result by using `lt ... or ... gt`. For example, to see all users except those that have a status of `STAGED`, use `(status lt \"STAGED\" or status gt \"STAGED\")`.  You can search properties that are arrays. If any element matches the search term, the entire array (object) is returned. Okta follows the [SCIM Protocol Specification](https://tools.ietf.org/html/rfc7644#section-3.4.2.2) for searching arrays. You can search multiple arrays, multiple values in an array, as well as using the standard logical and filtering operators. See [Filter](https://developer.okta.com/docs/reference/core-okta-api/#filter).  Searches for users can be filtered by the following operators: `sw`, `eq`, and `co`. You can only use `co` with these select user profile attributes: `profile.firstName`, `profile.lastName`, `profile.email`, and `profile.login`. See [Operators](https://developer.okta.com/docs/api/#operators). (optional)
    filter = 'status%20eq%20%22LOCKED_OUT%22' # str | Filters users with a supported expression for a subset of properties.  > **Note:** Returned users include those with the `DEPROVISIONED` status.  This requires [URL encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). For example, `filter=lastUpdated gt \"2013-06-01T00:00:00.000Z\"` is encoded as `filter=lastUpdated%20gt%20%222013-06-01T00:00:00.000Z%22`. Filtering is case-sensitive for property names and query values, while operators are case-insensitive.  Filtering supports the following limited number of properties: `status`, `lastUpdated`, `id`, `profile.login`, `profile.email`, `profile.firstName`, and `profile.lastName`.  Additionally, filtering supports only the equal `eq` operator from the standard Okta API filtering semantics, except in the case of the `lastUpdated` property. This property can also use the inequality operators (`gt`, `ge`, `lt`, and `le`). For logical operators, only the logical operators `and` and `or` are supported. The `not` operator isn't supported. See [Filter](https://developer.okta.com/docs/api/#filter) and [Operators](https://developer.okta.com/docs/api/#operators). (optional)
    q = 'q_example' # str | Finds users who match the specified query. Use the `q` parameter for simple queries, such as a lookup of users by name when creating a people picker.  The value of `q` is matched against `firstName`, `lastName`, or `email`. This performs a `startsWith` match, but this is an implementation detail and can change without notice. You don't need to specify `firstName`, `lastName`, or `email`.  > **Notes:** > * Using the `q` parameter in a request omits users that have a status of `DEPROVISIONED`. To return all users, use a `filter` or `search` query instead. > * This doesn't support pagination, but you can use `limit`. > * This isn't designed for large data sets. For optimal performance, use the `search` parameter instead. (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 200 # int | Specifies the number of results returned. Defaults to 10 if `q` is provided.  You can use `limit` with `after` to define the cursor location in the data set and manage the user records per page. (optional) (default to 200)
    sort_by = 'sort_by_example' # str | Specifies the field to sort by (for search queries only). This can be any single property, for example `sortBy=profile.lastName`. Users with the same value for the `sortBy` property are ordered by `id`. Use with `sortOrder` to control the order of results. (optional)
    sort_order = 'asc' # str | Specifies sort order: `asc` or `desc` (for search queries only). This parameter is ignored if `sortBy` isn't present. (optional) (default to 'asc')
    fields = 'id,status,profile:(firstName,lastName,city)' # str | Specifies a select set of user properties to query. Any other properties will be filtered out of the returned users. This is often called field projections in APIs, which can reduce payload size, improve performance, and limit unneccessary data exposure.  Requested fields should be comma-separated. Comma-separate the fields and place sub-fields in the profile object inside a `profile:()` directive, for example `profile:(firstName, city)`. The `id` field is always included, regardless of whether it's specified in the `fields` parameter. (optional)
    expand = 'classification' # str | <x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>A parameter to include metadata in the `_embedded` property. Supported value: `classification`. (optional)

    try:
        # List all users
        api_response = api_instance.list_users(content_type=content_type, search=search, filter=filter, q=q, after=after, limit=limit, sort_by=sort_by, sort_order=sort_order, fields=fields, expand=expand)
        print("The response of UserApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specifies the media type of the resource. Optional &#x60;okta-response&#x60; value can be included for performance optimization.  Complex DelAuth configurations may degrade performance when fetching specific parts of the response, and passing this parameter can omit these parts, bypassing the bottleneck.  Enum values for &#x60;okta-response&#x60;:   * &#x60;omitCredentials&#x60;: Omits the credentials subobject from the response.   * &#x60;omitCredentialsLinks&#x60;: Omits the following HAL links from the response: Update password, Change recovery question, Start forgot password flow, Reset password, Reset factors, Unlock.   * &#x60;omitTransitioningToStatus&#x60;: Omits the &#x60;transitioningToStatus&#x60; field from the response. | [optional] 
 **search** | **str**| Searches for users with a supported filtering expression for most properties. Okta recommends this query parameter because it provides the largest range of search options and optimal performance.  &gt; **Note:** Using an overly complex or long search query can result in an error.  This operation supports [pagination](https://developer.okta.com/docs/api/#pagination). Use an ID lookup for records that you update to ensure your results contain the latest data. Returned users include those with the &#x60;DEPROVISIONED&#x60; status.  Property names in the search parameter are case sensitive, whereas operators (&#x60;eq&#x60;, &#x60;sw&#x60;, and so on) and string values are case insensitive. Unlike with user logins, diacritical marks are significant in search string values: a search for &#x60;isaac.brock&#x60; finds &#x60;Isaac.Brock&#x60;, but doesn&#39;t find a property whose value is &#x60;isáàc.bröck&#x60;.  This operation requires [URL encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). See [Special characters](https://developer.okta.com/docs/api/#special-characters).  This operation searches many properties:   * Any user profile attribute, including custom-defined attributes   * The top-level properties: &#x60;id&#x60;, &#x60;status&#x60;, &#x60;created&#x60;, &#x60;activated&#x60;, &#x60;statusChanged&#x60;, and &#x60;lastUpdated&#x60;   * The [user type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/#tag/UserType/operation/updateUserType) accessed as &#x60;type.id&#x60;   * Properties that have array values  &gt; **Note:** &lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt; The ability to search by user classification is available as an [Early Access](https://developer.okta.com/docs/api/openapi/okta-management/guides/release-lifecycle/#early-access-ea) feature. The &#x60;classification.type&#x60; property cannot be used in conjunction with other search terms. You can search using &#x60;classification.type eq \&quot;LITE\&quot;&#x60; or &#x60;classification.type eq \&quot;STANDARD\&quot;&#x60;.  You can also use &#x60;sortBy&#x60; and &#x60;sortOrder&#x60; parameters. The &#x60;ne&#x60; (not equal) operator isn&#39;t supported, but you can obtain the same result by using &#x60;lt ... or ... gt&#x60;. For example, to see all users except those that have a status of &#x60;STAGED&#x60;, use &#x60;(status lt \&quot;STAGED\&quot; or status gt \&quot;STAGED\&quot;)&#x60;.  You can search properties that are arrays. If any element matches the search term, the entire array (object) is returned. Okta follows the [SCIM Protocol Specification](https://tools.ietf.org/html/rfc7644#section-3.4.2.2) for searching arrays. You can search multiple arrays, multiple values in an array, as well as using the standard logical and filtering operators. See [Filter](https://developer.okta.com/docs/reference/core-okta-api/#filter).  Searches for users can be filtered by the following operators: &#x60;sw&#x60;, &#x60;eq&#x60;, and &#x60;co&#x60;. You can only use &#x60;co&#x60; with these select user profile attributes: &#x60;profile.firstName&#x60;, &#x60;profile.lastName&#x60;, &#x60;profile.email&#x60;, and &#x60;profile.login&#x60;. See [Operators](https://developer.okta.com/docs/api/#operators). | [optional] 
 **filter** | **str**| Filters users with a supported expression for a subset of properties.  &gt; **Note:** Returned users include those with the &#x60;DEPROVISIONED&#x60; status.  This requires [URL encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding). For example, &#x60;filter&#x3D;lastUpdated gt \&quot;2013-06-01T00:00:00.000Z\&quot;&#x60; is encoded as &#x60;filter&#x3D;lastUpdated%20gt%20%222013-06-01T00:00:00.000Z%22&#x60;. Filtering is case-sensitive for property names and query values, while operators are case-insensitive.  Filtering supports the following limited number of properties: &#x60;status&#x60;, &#x60;lastUpdated&#x60;, &#x60;id&#x60;, &#x60;profile.login&#x60;, &#x60;profile.email&#x60;, &#x60;profile.firstName&#x60;, and &#x60;profile.lastName&#x60;.  Additionally, filtering supports only the equal &#x60;eq&#x60; operator from the standard Okta API filtering semantics, except in the case of the &#x60;lastUpdated&#x60; property. This property can also use the inequality operators (&#x60;gt&#x60;, &#x60;ge&#x60;, &#x60;lt&#x60;, and &#x60;le&#x60;). For logical operators, only the logical operators &#x60;and&#x60; and &#x60;or&#x60; are supported. The &#x60;not&#x60; operator isn&#39;t supported. See [Filter](https://developer.okta.com/docs/api/#filter) and [Operators](https://developer.okta.com/docs/api/#operators). | [optional] 
 **q** | **str**| Finds users who match the specified query. Use the &#x60;q&#x60; parameter for simple queries, such as a lookup of users by name when creating a people picker.  The value of &#x60;q&#x60; is matched against &#x60;firstName&#x60;, &#x60;lastName&#x60;, or &#x60;email&#x60;. This performs a &#x60;startsWith&#x60; match, but this is an implementation detail and can change without notice. You don&#39;t need to specify &#x60;firstName&#x60;, &#x60;lastName&#x60;, or &#x60;email&#x60;.  &gt; **Notes:** &gt; * Using the &#x60;q&#x60; parameter in a request omits users that have a status of &#x60;DEPROVISIONED&#x60;. To return all users, use a &#x60;filter&#x60; or &#x60;search&#x60; query instead. &gt; * This doesn&#39;t support pagination, but you can use &#x60;limit&#x60;. &gt; * This isn&#39;t designed for large data sets. For optimal performance, use the &#x60;search&#x60; parameter instead. | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| Specifies the number of results returned. Defaults to 10 if &#x60;q&#x60; is provided.  You can use &#x60;limit&#x60; with &#x60;after&#x60; to define the cursor location in the data set and manage the user records per page. | [optional] [default to 200]
 **sort_by** | **str**| Specifies the field to sort by (for search queries only). This can be any single property, for example &#x60;sortBy&#x3D;profile.lastName&#x60;. Users with the same value for the &#x60;sortBy&#x60; property are ordered by &#x60;id&#x60;. Use with &#x60;sortOrder&#x60; to control the order of results. | [optional] 
 **sort_order** | **str**| Specifies sort order: &#x60;asc&#x60; or &#x60;desc&#x60; (for search queries only). This parameter is ignored if &#x60;sortBy&#x60; isn&#39;t present. | [optional] [default to &#39;asc&#39;]
 **fields** | **str**| Specifies a select set of user properties to query. Any other properties will be filtered out of the returned users. This is often called field projections in APIs, which can reduce payload size, improve performance, and limit unneccessary data exposure.  Requested fields should be comma-separated. Comma-separate the fields and place sub-fields in the profile object inside a &#x60;profile:()&#x60; directive, for example &#x60;profile:(firstName, city)&#x60;. The &#x60;id&#x60; field is always included, regardless of whether it&#39;s specified in the &#x60;fields&#x60; parameter. | [optional] 
 **expand** | **str**| &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;A parameter to include metadata in the &#x60;_embedded&#x60; property. Supported value: &#x60;classification&#x60;. | [optional] 

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_user**
> User replace_user(id, user, strict=strict, if_match=if_match)

Replace a user

Replaces a user's profile, credentials, or both using strict-update semantics.  All profile properties must be specified when updating a user's profile with a `PUT` method. Any property not specified in the request is deleted. > **Important:** Don't use a `PUT` method for partial updates.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.update_user_request import UpdateUserRequest
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
    api_instance = okta.UserApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    user = okta.UpdateUserRequest() # UpdateUserRequest | 
    strict = True # bool | If `true`, validates against minimum age and history password policy (optional)
    if_match = 'W/\"1234567890abcdef\"' # str | The ETag value of the user's expected current state. This becomes a conditional request used for concurrency control. See [Conditional Requests and Entity Tags](/#conditional-requests-and-entity-tags). (optional)

    try:
        # Replace a user
        api_response = api_instance.replace_user(id, user, strict=strict, if_match=if_match)
        print("The response of UserApi->replace_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->replace_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **user** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **strict** | **bool**| If &#x60;true&#x60;, validates against minimum age and history password policy | [optional] 
 **if_match** | **str**| The ETag value of the user&#39;s expected current state. This becomes a conditional request used for concurrency control. See [Conditional Requests and Entity Tags](/#conditional-requests-and-entity-tags). | [optional] 

### Return type

[**User**](User.md)

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

# **update_user**
> User update_user(id, user, strict=strict, if_match=if_match)

Update a user

Updates a user's profile or credentials with partial update semantics.  > **Important:** Use the `POST` method for partial updates. Unspecified properties are set to null with `PUT`.  `profile` and `credentials` can be updated independently or together with a single request. > **Note**: Currently, the user type of a user can only be changed via a full replacement PUT operation. If the request parameters of a partial update include the type element from the user object, the value must match the existing type of the user. Only admins are permitted to change the user type of a user; end users are not allowed to change their own user type.  > **Note**: To update a current user's profile with partial semantics, the `/api/v1/users/me` endpoint can be invoked. > > A user can only update profile properties for which the user has write access. Within the profile, if the user tries to update the primary or the secondary email IDs, verification emails are sent to those email IDs, and the fields are updated only upon verification.  If you are using this endpoint to set a password, it sets a password without validating existing user credentials. This is an administrative operation. For operations that validate credentials, refer to the [Reset password](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserCred/#tag/UserCred/operation/resetPassword), [Start forgot password flow](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserCred/#tag/UserCred/operation/forgotPassword), and [Update password](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserCred/#tag/UserCred/operation/changePassword) endpoints.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.update_user_request import UpdateUserRequest
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
    api_instance = okta.UserApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user
    user = okta.UpdateUserRequest() # UpdateUserRequest | 
    strict = True # bool | If true, validates against minimum age and history password policy (optional)
    if_match = 'W/\"1234567890abcdef\"' # str | The ETag value of the user's expected current state. This becomes a conditional request used for concurrency control. See [Conditional Requests and Entity Tags](/#conditional-requests-and-entity-tags). (optional)

    try:
        # Update a user
        api_response = api_instance.update_user(id, user, strict=strict, if_match=if_match)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 
 **user** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **strict** | **bool**| If true, validates against minimum age and history password policy | [optional] 
 **if_match** | **str**| The ETag value of the user&#39;s expected current state. This becomes a conditional request used for concurrency control. See [Conditional Requests and Entity Tags](/#conditional-requests-and-entity-tags). | [optional] 

### Return type

[**User**](User.md)

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

