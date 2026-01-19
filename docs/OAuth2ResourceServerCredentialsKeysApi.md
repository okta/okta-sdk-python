# okta.OAuth2ResourceServerCredentialsKeysApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_o_auth2_resource_server_json_web_key**](OAuth2ResourceServerCredentialsKeysApi.md#activate_o_auth2_resource_server_json_web_key) | **POST** /api/v1/authorizationServers/{authServerId}/resourceservercredentials/keys/{keyId}/lifecycle/activate | Activate a Custom Authorization Server Public JSON Web Key
[**add_o_auth2_resource_server_json_web_key**](OAuth2ResourceServerCredentialsKeysApi.md#add_o_auth2_resource_server_json_web_key) | **POST** /api/v1/authorizationServers/{authServerId}/resourceservercredentials/keys | Add a JSON Web Key
[**deactivate_o_auth2_resource_server_json_web_key**](OAuth2ResourceServerCredentialsKeysApi.md#deactivate_o_auth2_resource_server_json_web_key) | **POST** /api/v1/authorizationServers/{authServerId}/resourceservercredentials/keys/{keyId}/lifecycle/deactivate | Deactivate a Custom Authorization Server Public JSON Web Key
[**delete_o_auth2_resource_server_json_web_key**](OAuth2ResourceServerCredentialsKeysApi.md#delete_o_auth2_resource_server_json_web_key) | **DELETE** /api/v1/authorizationServers/{authServerId}/resourceservercredentials/keys/{keyId} | Delete a Custom Authorization Server Public JSON Web Key
[**get_o_auth2_resource_server_json_web_key**](OAuth2ResourceServerCredentialsKeysApi.md#get_o_auth2_resource_server_json_web_key) | **GET** /api/v1/authorizationServers/{authServerId}/resourceservercredentials/keys/{keyId} | Retrieve a Custom Authorization Server Public JSON Web Key
[**list_o_auth2_resource_server_json_web_keys**](OAuth2ResourceServerCredentialsKeysApi.md#list_o_auth2_resource_server_json_web_keys) | **GET** /api/v1/authorizationServers/{authServerId}/resourceservercredentials/keys | List all Custom Authorization Server Public JSON Web Keys


# **activate_o_auth2_resource_server_json_web_key**
> OAuth2ResourceServerJsonWebKey activate_o_auth2_resource_server_json_web_key(auth_server_id, key_id)

Activate a Custom Authorization Server Public JSON Web Key

Activates a custom authorization server public JSON web key by key `id`. > **Note:** You can have only one active key at any given time for the authorization server. When you activate an inactive key, Okta automatically deactivates the current active key.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_resource_server_json_web_key import OAuth2ResourceServerJsonWebKey
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
    api_instance = okta.OAuth2ResourceServerCredentialsKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    key_id = 'apk2f4zrZbs8nUa7p0g4' # str | Unique `id` of the Custom Authorization Server JSON Web Key

    try:
        # Activate a Custom Authorization Server Public JSON Web Key
        api_response = api_instance.activate_o_auth2_resource_server_json_web_key(auth_server_id, key_id)
        print("The response of OAuth2ResourceServerCredentialsKeysApi->activate_o_auth2_resource_server_json_web_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ResourceServerCredentialsKeysApi->activate_o_auth2_resource_server_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the Custom Authorization Server JSON Web Key | 

### Return type

[**OAuth2ResourceServerJsonWebKey**](OAuth2ResourceServerJsonWebKey.md)

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

# **add_o_auth2_resource_server_json_web_key**
> OAuth2ResourceServerJsonWebKey add_o_auth2_resource_server_json_web_key(auth_server_id, o_auth2_resource_server_json_web_key_request_body)

Add a JSON Web Key

Adds a new JSON Web Key to the custom authorization server`s JSON web keys. > **Note:** This API doesn't allow you to add a key if the existing key doesn't have a `kid`. Use the [Replace an Authorization Server](/openapi/okta-management/management/tag/AuthorizationServer/#tag/AuthorizationServer/operation/replaceAuthorizationServer) operation to update the JWKS or [Delete a Custom Authorization Server Public JSON Web Key](/openapi/okta-management/management/tag/OAuth2ResourceServerCredentialsKeys/#tag/OAuth2ResourceServerCredentialsKeys/operation/deleteOAuth2ResourceServerJsonWebKey) and re-add the key with a `kid`. > **Note:** This API doesn't allow you to add a key with an ACTIVE status. You need to add an INACTIVE key first, and then ACTIVATE the key.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_resource_server_json_web_key import OAuth2ResourceServerJsonWebKey
from okta.models.o_auth2_resource_server_json_web_key_request_body import OAuth2ResourceServerJsonWebKeyRequestBody
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
    api_instance = okta.OAuth2ResourceServerCredentialsKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    o_auth2_resource_server_json_web_key_request_body = okta.OAuth2ResourceServerJsonWebKeyRequestBody() # OAuth2ResourceServerJsonWebKeyRequestBody | 

    try:
        # Add a JSON Web Key
        api_response = api_instance.add_o_auth2_resource_server_json_web_key(auth_server_id, o_auth2_resource_server_json_web_key_request_body)
        print("The response of OAuth2ResourceServerCredentialsKeysApi->add_o_auth2_resource_server_json_web_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ResourceServerCredentialsKeysApi->add_o_auth2_resource_server_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **o_auth2_resource_server_json_web_key_request_body** | [**OAuth2ResourceServerJsonWebKeyRequestBody**](OAuth2ResourceServerJsonWebKeyRequestBody.md)|  | 

### Return type

[**OAuth2ResourceServerJsonWebKey**](OAuth2ResourceServerJsonWebKey.md)

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

# **deactivate_o_auth2_resource_server_json_web_key**
> OAuth2ResourceServerJsonWebKey deactivate_o_auth2_resource_server_json_web_key(auth_server_id, key_id)

Deactivate a Custom Authorization Server Public JSON Web Key

Deactivates a custom authorization server public JSON web key by key `id`. > **Note:** Deactivating the active key isn't allowed if the authorization server has access token encryption enabled. You can activate another key, which makes the current key inactive.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_resource_server_json_web_key import OAuth2ResourceServerJsonWebKey
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
    api_instance = okta.OAuth2ResourceServerCredentialsKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    key_id = 'apk2f4zrZbs8nUa7p0g4' # str | Unique `id` of the Custom Authorization Server JSON Web Key

    try:
        # Deactivate a Custom Authorization Server Public JSON Web Key
        api_response = api_instance.deactivate_o_auth2_resource_server_json_web_key(auth_server_id, key_id)
        print("The response of OAuth2ResourceServerCredentialsKeysApi->deactivate_o_auth2_resource_server_json_web_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ResourceServerCredentialsKeysApi->deactivate_o_auth2_resource_server_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the Custom Authorization Server JSON Web Key | 

### Return type

[**OAuth2ResourceServerJsonWebKey**](OAuth2ResourceServerJsonWebKey.md)

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

# **delete_o_auth2_resource_server_json_web_key**
> delete_o_auth2_resource_server_json_web_key(auth_server_id, key_id)

Delete a Custom Authorization Server Public JSON Web Key

Deletes a custom authorization server public JSON web key by key `id`. You can only delete an inactive key.

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
    api_instance = okta.OAuth2ResourceServerCredentialsKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    key_id = 'apk2f4zrZbs8nUa7p0g4' # str | Unique `id` of the Custom Authorization Server JSON Web Key

    try:
        # Delete a Custom Authorization Server Public JSON Web Key
        api_instance.delete_o_auth2_resource_server_json_web_key(auth_server_id, key_id)
    except Exception as e:
        print("Exception when calling OAuth2ResourceServerCredentialsKeysApi->delete_o_auth2_resource_server_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the Custom Authorization Server JSON Web Key | 

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

# **get_o_auth2_resource_server_json_web_key**
> OAuth2ResourceServerJsonWebKey get_o_auth2_resource_server_json_web_key(auth_server_id, key_id)

Retrieve a Custom Authorization Server Public JSON Web Key

Retrieves a custom authorization server public JSON web key by key `id`

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
    api_instance = okta.OAuth2ResourceServerCredentialsKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    key_id = 'apk2f4zrZbs8nUa7p0g4' # str | Unique `id` of the Custom Authorization Server JSON Web Key

    try:
        # Retrieve a Custom Authorization Server Public JSON Web Key
        api_response = api_instance.get_o_auth2_resource_server_json_web_key(auth_server_id, key_id)
        print("The response of OAuth2ResourceServerCredentialsKeysApi->get_o_auth2_resource_server_json_web_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ResourceServerCredentialsKeysApi->get_o_auth2_resource_server_json_web_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **key_id** | **str**| Unique &#x60;id&#x60; of the Custom Authorization Server JSON Web Key | 

### Return type

[**OAuth2ResourceServerJsonWebKey**](OAuth2ResourceServerJsonWebKey.md)

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

# **list_o_auth2_resource_server_json_web_keys**
> List[OAuth2ResourceServerJsonWebKey] list_o_auth2_resource_server_json_web_keys(auth_server_id)

List all Custom Authorization Server Public JSON Web Keys

Lists all the public keys used by the custom authorization server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.o_auth2_resource_server_json_web_key import OAuth2ResourceServerJsonWebKey
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
    api_instance = okta.OAuth2ResourceServerCredentialsKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all Custom Authorization Server Public JSON Web Keys
        api_response = api_instance.list_o_auth2_resource_server_json_web_keys(auth_server_id)
        print("The response of OAuth2ResourceServerCredentialsKeysApi->list_o_auth2_resource_server_json_web_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2ResourceServerCredentialsKeysApi->list_o_auth2_resource_server_json_web_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[OAuth2ResourceServerJsonWebKey]**](OAuth2ResourceServerJsonWebKey.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

