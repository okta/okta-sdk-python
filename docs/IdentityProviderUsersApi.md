# okta.IdentityProviderUsersApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_identity_provider_application_user**](IdentityProviderUsersApi.md#get_identity_provider_application_user) | **GET** /api/v1/idps/{idpId}/users/{userId} | Retrieve a user for IdP
[**link_user_to_identity_provider**](IdentityProviderUsersApi.md#link_user_to_identity_provider) | **POST** /api/v1/idps/{idpId}/users/{userId} | Link a user to IdP
[**list_identity_provider_application_users**](IdentityProviderUsersApi.md#list_identity_provider_application_users) | **GET** /api/v1/idps/{idpId}/users | List all users for IdP
[**list_social_auth_tokens**](IdentityProviderUsersApi.md#list_social_auth_tokens) | **GET** /api/v1/idps/{idpId}/users/{userId}/credentials/tokens | List all tokens from OIDC IdP
[**list_user_identity_providers**](IdentityProviderUsersApi.md#list_user_identity_providers) | **GET** /api/v1/users/{id}/idps | List all IdPs for user
[**unlink_user_from_identity_provider**](IdentityProviderUsersApi.md#unlink_user_from_identity_provider) | **DELETE** /api/v1/idps/{idpId}/users/{userId} | Unlink a user from IdP


# **get_identity_provider_application_user**
> IdentityProviderApplicationUser get_identity_provider_application_user(idp_id, user_id)

Retrieve a user for IdP

Retrieves a linked identity provider (IdP) user by ID

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_provider_application_user import IdentityProviderApplicationUser
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
    api_instance = okta.IdentityProviderUsersApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # Retrieve a user for IdP
        api_response = api_instance.get_identity_provider_application_user(idp_id, user_id)
        print("The response of IdentityProviderUsersApi->get_identity_provider_application_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderUsersApi->get_identity_provider_application_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**| ID of an existing Okta user | 

### Return type

[**IdentityProviderApplicationUser**](IdentityProviderApplicationUser.md)

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

# **link_user_to_identity_provider**
> IdentityProviderApplicationUser link_user_to_identity_provider(idp_id, user_id, user_identity_provider_link_request)

Link a user to IdP

Links an Okta user to an existing SAML or social identity provider (IdP).  The SAML IdP must have `honorPersistentNameId` set to `true` to use this API. The [Name Identifier Format](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/replaceIdentityProvider!path=protocol/0/settings&t=request) of the incoming assertion must be `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_provider_application_user import IdentityProviderApplicationUser
from okta.models.user_identity_provider_link_request import UserIdentityProviderLinkRequest
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
    api_instance = okta.IdentityProviderUsersApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    user_identity_provider_link_request = okta.UserIdentityProviderLinkRequest() # UserIdentityProviderLinkRequest | 

    try:
        # Link a user to IdP
        api_response = api_instance.link_user_to_identity_provider(idp_id, user_id, user_identity_provider_link_request)
        print("The response of IdentityProviderUsersApi->link_user_to_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderUsersApi->link_user_to_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**| ID of an existing Okta user | 
 **user_identity_provider_link_request** | [**UserIdentityProviderLinkRequest**](UserIdentityProviderLinkRequest.md)|  | 

### Return type

[**IdentityProviderApplicationUser**](IdentityProviderApplicationUser.md)

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

# **list_identity_provider_application_users**
> List[IdentityProviderApplicationUser] list_identity_provider_application_users(idp_id, q=q, after=after, limit=limit, expand=expand)

List all users for IdP

Lists all the users linked to an identity provider (IdP)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_provider_application_user import IdentityProviderApplicationUser
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
    api_instance = okta.IdentityProviderUsersApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    q = 'q_example' # str | Searches the records for matching value (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)
    expand = 'user' # str | Expand user data (optional)

    try:
        # List all users for IdP
        api_response = api_instance.list_identity_provider_application_users(idp_id, q=q, after=after, limit=limit, expand=expand)
        print("The response of IdentityProviderUsersApi->list_identity_provider_application_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderUsersApi->list_identity_provider_application_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **q** | **str**| Searches the records for matching value | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]
 **expand** | **str**| Expand user data | [optional] 

### Return type

[**List[IdentityProviderApplicationUser]**](IdentityProviderApplicationUser.md)

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

# **list_social_auth_tokens**
> List[SocialAuthToken] list_social_auth_tokens(idp_id, user_id)

List all tokens from OIDC IdP

Lists the tokens minted by the social authentication provider when the user authenticates with Okta via Social Auth.  Okta doesn't import all the user information from a social provider. If the app needs information that isn't imported, it can get the user token from this endpoint. Then the app can make an API call to the social provider with the token to request the additional information.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.social_auth_token import SocialAuthToken
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
    api_instance = okta.IdentityProviderUsersApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # List all tokens from OIDC IdP
        api_response = api_instance.list_social_auth_tokens(idp_id, user_id)
        print("The response of IdentityProviderUsersApi->list_social_auth_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderUsersApi->list_social_auth_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**| ID of an existing Okta user | 

### Return type

[**List[SocialAuthToken]**](SocialAuthToken.md)

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

# **list_user_identity_providers**
> List[IdentityProvider] list_user_identity_providers(id)

List all IdPs for user

Lists the identity providers (IdPs) associated with the user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.identity_provider import IdentityProvider
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
    api_instance = okta.IdentityProviderUsersApi(api_client)
    id = 'id_example' # str | An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user

    try:
        # List all IdPs for user
        api_response = api_instance.list_user_identity_providers(id)
        print("The response of IdentityProviderUsersApi->list_user_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderUsersApi->list_user_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An ID, login, or login shortname (as long as the shortname is unambiguous) of an existing Okta user | 

### Return type

[**List[IdentityProvider]**](IdentityProvider.md)

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

# **unlink_user_from_identity_provider**
> unlink_user_from_identity_provider(idp_id, user_id)

Unlink a user from IdP

Unlinks the Okta user and the identity provider (IdP) user. The next time the user federates into Okta through this IdP, they have to re-link their account according to the account link policy.

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
    api_instance = okta.IdentityProviderUsersApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # Unlink a user from IdP
        api_instance.unlink_user_from_identity_provider(idp_id, user_id)
    except Exception as e:
        print("Exception when calling IdentityProviderUsersApi->unlink_user_from_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
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

