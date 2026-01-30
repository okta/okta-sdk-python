# okta.ApplicationTokensApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_o_auth2_token_for_application**](ApplicationTokensApi.md#get_o_auth2_token_for_application) | **GET** /api/v1/apps/{appId}/tokens/{tokenId} | Retrieve an application token
[**list_o_auth2_tokens_for_application**](ApplicationTokensApi.md#list_o_auth2_tokens_for_application) | **GET** /api/v1/apps/{appId}/tokens | List all application refresh tokens
[**revoke_o_auth2_token_for_application**](ApplicationTokensApi.md#revoke_o_auth2_token_for_application) | **DELETE** /api/v1/apps/{appId}/tokens/{tokenId} | Revoke an application token
[**revoke_o_auth2_tokens_for_application**](ApplicationTokensApi.md#revoke_o_auth2_tokens_for_application) | **DELETE** /api/v1/apps/{appId}/tokens | Revoke all application tokens


# **get_o_auth2_token_for_application**
> OAuth2RefreshToken get_o_auth2_token_for_application(app_id, token_id, expand=expand)

Retrieve an application token

Retrieves a refresh token for the specified app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken
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
    api_instance = okta.ApplicationTokensApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token
    expand = 'scope' # str | An optional parameter to return scope details in the `_embedded` property. Valid value: `scope` (optional)

    try:
        # Retrieve an application token
        api_response = api_instance.get_o_auth2_token_for_application(app_id, token_id, expand=expand)
        print("The response of ApplicationTokensApi->get_o_auth2_token_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->get_o_auth2_token_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 
 **expand** | **str**| An optional parameter to return scope details in the &#x60;_embedded&#x60; property. Valid value: &#x60;scope&#x60; | [optional] 

### Return type

[**OAuth2RefreshToken**](OAuth2RefreshToken.md)

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

# **list_o_auth2_tokens_for_application**
> List[OAuth2RefreshToken] list_o_auth2_tokens_for_application(app_id, expand=expand, after=after, limit=limit)

List all application refresh tokens

Lists all refresh tokens for an app  > **Note:** The results are [paginated](/#pagination) according to the `limit` parameter. > If there are multiple pages of results, the Link header contains a `next` link that you need to use as an opaque value (follow it, don't parse it). 

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_refresh_token import OAuth2RefreshToken
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
    api_instance = okta.ApplicationTokensApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    expand = 'scope' # str | An optional parameter to return scope details in the `_embedded` property. Valid value: `scope` (optional)
    after = '16275000448691' # str | Specifies the pagination cursor for the next page of results. Treat this as an opaque value obtained through the next link relationship. See [Pagination](/#pagination). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all application refresh tokens
        api_response = api_instance.list_o_auth2_tokens_for_application(app_id, expand=expand, after=after, limit=limit)
        print("The response of ApplicationTokensApi->list_o_auth2_tokens_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->list_o_auth2_tokens_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **expand** | **str**| An optional parameter to return scope details in the &#x60;_embedded&#x60; property. Valid value: &#x60;scope&#x60; | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of results. Treat this as an opaque value obtained through the next link relationship. See [Pagination](/#pagination). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**List[OAuth2RefreshToken]**](OAuth2RefreshToken.md)

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

# **revoke_o_auth2_token_for_application**
> revoke_o_auth2_token_for_application(app_id, token_id)

Revoke an application token

Revokes the specified token for the specified app

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
    api_instance = okta.ApplicationTokensApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token

    try:
        # Revoke an application token
        api_instance.revoke_o_auth2_token_for_application(app_id, token_id)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->revoke_o_auth2_token_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 

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

# **revoke_o_auth2_tokens_for_application**
> revoke_o_auth2_tokens_for_application(app_id)

Revoke all application tokens

Revokes all OAuth 2.0 refresh tokens for the specified app. Any access tokens issued with these refresh tokens are also revoked, but access tokens issued without a refresh token aren't affected.

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
    api_instance = okta.ApplicationTokensApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # Revoke all application tokens
        api_instance.revoke_o_auth2_tokens_for_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->revoke_o_auth2_tokens_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

