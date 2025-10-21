# okta.ApplicationTokensApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_o_auth2_token_for_application**](ApplicationTokensApi.md#get_o_auth2_token_for_application) | **GET** /api/v1/apps/{appId}/tokens/{tokenId} | Retrieve an OAuth 2.0 Token
[**list_o_auth2_tokens_for_application**](ApplicationTokensApi.md#list_o_auth2_tokens_for_application) | **GET** /api/v1/apps/{appId}/tokens | List all OAuth 2.0 Tokens
[**revoke_o_auth2_token_for_application**](ApplicationTokensApi.md#revoke_o_auth2_token_for_application) | **DELETE** /api/v1/apps/{appId}/tokens/{tokenId} | Revoke an OAuth 2.0 Token
[**revoke_o_auth2_tokens_for_application**](ApplicationTokensApi.md#revoke_o_auth2_tokens_for_application) | **DELETE** /api/v1/apps/{appId}/tokens | Revoke all OAuth 2.0 Tokens


# **get_o_auth2_token_for_application**
> OAuth2Token get_o_auth2_token_for_application(app_id, token_id, expand=expand)

Retrieve an OAuth 2.0 Token

Retrieves a token for the specified application

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_token import OAuth2Token
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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token
    expand = 'expand_example' # str |  (optional)

    try:
        # Retrieve an OAuth 2.0 Token
        api_response = api_instance.get_o_auth2_token_for_application(app_id, token_id, expand=expand)
        print("The response of ApplicationTokensApi->get_o_auth2_token_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->get_o_auth2_token_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **token_id** | **str**| &#x60;id&#x60; of Token | 
 **expand** | **str**|  | [optional] 

### Return type

[**OAuth2Token**](OAuth2Token.md)

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
> List[OAuth2Token] list_o_auth2_tokens_for_application(app_id, expand=expand, after=after, limit=limit)

List all OAuth 2.0 Tokens

Lists all tokens for the application

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_token import OAuth2Token
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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    expand = 'expand_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all OAuth 2.0 Tokens
        api_response = api_instance.list_o_auth2_tokens_for_application(app_id, expand=expand, after=after, limit=limit)
        print("The response of ApplicationTokensApi->list_o_auth2_tokens_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->list_o_auth2_tokens_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **expand** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**List[OAuth2Token]**](OAuth2Token.md)

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

Revoke an OAuth 2.0 Token

Revokes the specified token for the specified application

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    token_id = 'sHHSth53yJAyNSTQKDJZ' # str | `id` of Token

    try:
        # Revoke an OAuth 2.0 Token
        api_instance.revoke_o_auth2_token_for_application(app_id, token_id)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->revoke_o_auth2_token_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
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

Revoke all OAuth 2.0 Tokens

Revokes all tokens for the specified application

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
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Revoke all OAuth 2.0 Tokens
        api_instance.revoke_o_auth2_tokens_for_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationTokensApi->revoke_o_auth2_tokens_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

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

