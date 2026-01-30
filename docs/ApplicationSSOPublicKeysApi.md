# okta.ApplicationSSOPublicKeysApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_o_auth2_client_json_web_key**](ApplicationSSOPublicKeysApi.md#activate_o_auth2_client_json_web_key) | **POST** /api/v1/apps/{appId}/credentials/jwks/{keyId}/lifecycle/activate | Activate an OAuth 2.0 client JSON Web Key
[**activate_o_auth2_client_secret**](ApplicationSSOPublicKeysApi.md#activate_o_auth2_client_secret) | **POST** /api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/activate | Activate an OAuth 2.0 client secret
[**add_jwk**](ApplicationSSOPublicKeysApi.md#add_jwk) | **POST** /api/v1/apps/{appId}/credentials/jwks | Add a JSON Web Key
[**create_o_auth2_client_secret**](ApplicationSSOPublicKeysApi.md#create_o_auth2_client_secret) | **POST** /api/v1/apps/{appId}/credentials/secrets | Create an OAuth 2.0 client secret
[**deactivate_o_auth2_client_json_web_key**](ApplicationSSOPublicKeysApi.md#deactivate_o_auth2_client_json_web_key) | **POST** /api/v1/apps/{appId}/credentials/jwks/{keyId}/lifecycle/deactivate | Deactivate an OAuth 2.0 client JSON Web Key
[**deactivate_o_auth2_client_secret**](ApplicationSSOPublicKeysApi.md#deactivate_o_auth2_client_secret) | **POST** /api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/deactivate | Deactivate an OAuth 2.0 client secret
[**delete_o_auth2_client_secret**](ApplicationSSOPublicKeysApi.md#delete_o_auth2_client_secret) | **DELETE** /api/v1/apps/{appId}/credentials/secrets/{secretId} | Delete an OAuth 2.0 client secret
[**deletejwk**](ApplicationSSOPublicKeysApi.md#deletejwk) | **DELETE** /api/v1/apps/{appId}/credentials/jwks/{keyId} | Delete an OAuth 2.0 client JSON Web Key
[**get_jwk**](ApplicationSSOPublicKeysApi.md#get_jwk) | **GET** /api/v1/apps/{appId}/credentials/jwks/{keyId} | Retrieve an OAuth 2.0 client JSON Web Key
[**get_o_auth2_client_secret**](ApplicationSSOPublicKeysApi.md#get_o_auth2_client_secret) | **GET** /api/v1/apps/{appId}/credentials/secrets/{secretId} | Retrieve an OAuth 2.0 client secret
[**list_jwk**](ApplicationSSOPublicKeysApi.md#list_jwk) | **GET** /api/v1/apps/{appId}/credentials/jwks | List all the OAuth 2.0 client JSON Web Keys
[**list_o_auth2_client_secrets**](ApplicationSSOPublicKeysApi.md#list_o_auth2_client_secrets) | **GET** /api/v1/apps/{appId}/credentials/secrets | List all OAuth 2.0 client secrets


# **activate_o_auth2_client_json_web_key**
> ListJwk200ResponseInner activate_o_auth2_client_json_web_key(app_id, key_id)

Activate an OAuth 2.0 client JSON Web Key

Activates an OAuth 2.0 Client JSON Web Key by `keyId` > **Note:** You can have only one active encryption key at any given time for app. When you activate an inactive key, the current active key is automatically deactivated.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.list_jwk200_response_inner import ListJwk200ResponseInner
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    key_id = 'pks2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client JSON Web Key

    try:
        # Activate an OAuth 2.0 client JSON Web Key
        api_response = api_instance.activate_o_auth2_client_json_web_key(app_id, key_id)
        print("The response of ApplicationSSOPublicKeysApi->activate_o_auth2_client_json_web_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->activate_o_auth2_client_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client JSON Web Key | 

### Return type

[**ListJwk200ResponseInner**](ListJwk200ResponseInner.md)

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

# **activate_o_auth2_client_secret**
> OAuth2ClientSecret activate_o_auth2_client_secret(app_id, secret_id)

Activate an OAuth 2.0 client secret

Activates an OAuth 2.0 Client Secret by `secretId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client_secret import OAuth2ClientSecret
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client Secret

    try:
        # Activate an OAuth 2.0 client secret
        api_response = api_instance.activate_o_auth2_client_secret(app_id, secret_id)
        print("The response of ApplicationSSOPublicKeysApi->activate_o_auth2_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->activate_o_auth2_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **secret_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client Secret | 

### Return type

[**OAuth2ClientSecret**](OAuth2ClientSecret.md)

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

# **add_jwk**
> ListJwk200ResponseInner add_jwk(app_id, add_jwk_request)

Add a JSON Web Key

Adds a new JSON Web Key to the client`s JSON Web Keys. > **Note:** This API doesn't allow you to add a key if the existing key doesn't have a `kid`. This is also consistent with how the [Dynamic Client Registration](/openapi/okta-oauth/oauth/tag/Client/) or [Applications](/openapi/okta-management/management/tag/Application/) APIs behave, as they don't allow the creation of multiple keys without `kids`. Use the [Replace an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/replaceApplication) or the [Replace a Client Application](/openapi/okta-oauth/oauth/tag/Client/#tag/Client/operation/replaceClient) operation to update the JWKS or [Delete an OAuth 2.0 Client JSON Web Key](/openapi/okta-management/management/tag/ApplicationSSOPublicKeys/#tag/ApplicationSSOPublicKeys/operation/deletejwk) and re-add the key with a `kid`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.add_jwk_request import AddJwkRequest
from okta.models.list_jwk200_response_inner import ListJwk200ResponseInner
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    add_jwk_request = okta.AddJwkRequest() # AddJwkRequest | 

    try:
        # Add a JSON Web Key
        api_response = api_instance.add_jwk(app_id, add_jwk_request)
        print("The response of ApplicationSSOPublicKeysApi->add_jwk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->add_jwk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **add_jwk_request** | [**AddJwkRequest**](AddJwkRequest.md)|  | 

### Return type

[**ListJwk200ResponseInner**](ListJwk200ResponseInner.md)

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

# **create_o_auth2_client_secret**
> OAuth2ClientSecret create_o_auth2_client_secret(app_id, o_auth2_client_secret_request_body=o_auth2_client_secret_request_body)

Create an OAuth 2.0 client secret

Creates an OAuth 2.0 Client Secret object with a new active client secret. You can create up to two Secret objects. An error is returned if you attempt to create more than two Secret objects. > **Note:** This API lets you bring your own secret. If [token_endpoint_auth_method](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication!path=4/credentials/oauthClient/token_endpoint_auth_method&t=request) of the app is `client_secret_jwt`, then the minimum length of `client_secret` is 32 characters. If no secret is specified in the request, Okta adds a new system-generated secret.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client_secret import OAuth2ClientSecret
from okta.models.o_auth2_client_secret_request_body import OAuth2ClientSecretRequestBody
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    o_auth2_client_secret_request_body = okta.OAuth2ClientSecretRequestBody() # OAuth2ClientSecretRequestBody |  (optional)

    try:
        # Create an OAuth 2.0 client secret
        api_response = api_instance.create_o_auth2_client_secret(app_id, o_auth2_client_secret_request_body=o_auth2_client_secret_request_body)
        print("The response of ApplicationSSOPublicKeysApi->create_o_auth2_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->create_o_auth2_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **o_auth2_client_secret_request_body** | [**OAuth2ClientSecretRequestBody**](OAuth2ClientSecretRequestBody.md)|  | [optional] 

### Return type

[**OAuth2ClientSecret**](OAuth2ClientSecret.md)

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

# **deactivate_o_auth2_client_json_web_key**
> OAuth2ClientJsonSigningKeyResponse deactivate_o_auth2_client_json_web_key(app_id, key_id)

Deactivate an OAuth 2.0 client JSON Web Key

Deactivates an OAuth 2.0 Client JSON Web Key by `keyId`. > **Note:** You can only deactivate signing keys. Deactivating the active encryption key isn't allowed if the client has ID token encryption enabled. You can activate another encryption key, which makes the current key inactive.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client_json_signing_key_response import OAuth2ClientJsonSigningKeyResponse
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    key_id = 'pks2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client JSON Web Key

    try:
        # Deactivate an OAuth 2.0 client JSON Web Key
        api_response = api_instance.deactivate_o_auth2_client_json_web_key(app_id, key_id)
        print("The response of ApplicationSSOPublicKeysApi->deactivate_o_auth2_client_json_web_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->deactivate_o_auth2_client_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client JSON Web Key | 

### Return type

[**OAuth2ClientJsonSigningKeyResponse**](OAuth2ClientJsonSigningKeyResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_o_auth2_client_secret**
> OAuth2ClientSecret deactivate_o_auth2_client_secret(app_id, secret_id)

Deactivate an OAuth 2.0 client secret

Deactivates an OAuth 2.0 Client Secret by `secretId`. You can't deactivate a secret if it's the only secret of the client.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client_secret import OAuth2ClientSecret
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client Secret

    try:
        # Deactivate an OAuth 2.0 client secret
        api_response = api_instance.deactivate_o_auth2_client_secret(app_id, secret_id)
        print("The response of ApplicationSSOPublicKeysApi->deactivate_o_auth2_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->deactivate_o_auth2_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **secret_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client Secret | 

### Return type

[**OAuth2ClientSecret**](OAuth2ClientSecret.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth2_client_secret**
> delete_o_auth2_client_secret(app_id, secret_id)

Delete an OAuth 2.0 client secret

Deletes an OAuth 2.0 Client Secret by `secretId`. You can only delete an inactive Secret.

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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client Secret

    try:
        # Delete an OAuth 2.0 client secret
        api_instance.delete_o_auth2_client_secret(app_id, secret_id)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->delete_o_auth2_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **secret_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client Secret | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletejwk**
> deletejwk(app_id, key_id)

Delete an OAuth 2.0 client JSON Web Key

Deletes an OAuth 2.0 Client JSON Web Key by `keyId`. You can only delete an inactive key.

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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    key_id = 'pks2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client JSON Web Key

    try:
        # Delete an OAuth 2.0 client JSON Web Key
        api_instance.deletejwk(app_id, key_id)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->deletejwk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client JSON Web Key | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwk**
> GetJwk200Response get_jwk(app_id, key_id)

Retrieve an OAuth 2.0 client JSON Web Key

Retrieves an OAuth 2.0 Client JSON Web Key by `keyId`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.get_jwk200_response import GetJwk200Response
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    key_id = 'pks2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client JSON Web Key

    try:
        # Retrieve an OAuth 2.0 client JSON Web Key
        api_response = api_instance.get_jwk(app_id, key_id)
        print("The response of ApplicationSSOPublicKeysApi->get_jwk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->get_jwk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client JSON Web Key | 

### Return type

[**GetJwk200Response**](GetJwk200Response.md)

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

# **get_o_auth2_client_secret**
> OAuth2ClientSecret get_o_auth2_client_secret(app_id, secret_id)

Retrieve an OAuth 2.0 client secret

Retrieves an OAuth 2.0 Client Secret by `secretId`

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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | Unique `id` of the OAuth 2.0 Client Secret

    try:
        # Retrieve an OAuth 2.0 client secret
        api_response = api_instance.get_o_auth2_client_secret(app_id, secret_id)
        print("The response of ApplicationSSOPublicKeysApi->get_o_auth2_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->get_o_auth2_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **secret_id** | **str**| Unique &#x60;id&#x60; of the OAuth 2.0 Client Secret | 

### Return type

[**OAuth2ClientSecret**](OAuth2ClientSecret.md)

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

# **list_jwk**
> List[ListJwk200ResponseInner] list_jwk(app_id)

List all the OAuth 2.0 client JSON Web Keys

Lists all JSON Web Keys for an OAuth 2.0 client app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.list_jwk200_response_inner import ListJwk200ResponseInner
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # List all the OAuth 2.0 client JSON Web Keys
        api_response = api_instance.list_jwk(app_id)
        print("The response of ApplicationSSOPublicKeysApi->list_jwk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->list_jwk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**List[ListJwk200ResponseInner]**](ListJwk200ResponseInner.md)

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

# **list_o_auth2_client_secrets**
> List[OAuth2ClientSecret] list_o_auth2_client_secrets(app_id)

List all OAuth 2.0 client secrets

Lists all client secrets for an OAuth 2.0 client app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_client_secret import OAuth2ClientSecret
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
    api_instance = okta.ApplicationSSOPublicKeysApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # List all OAuth 2.0 client secrets
        api_response = api_instance.list_o_auth2_client_secrets(app_id)
        print("The response of ApplicationSSOPublicKeysApi->list_o_auth2_client_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOPublicKeysApi->list_o_auth2_client_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

### Return type

[**List[OAuth2ClientSecret]**](OAuth2ClientSecret.md)

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

