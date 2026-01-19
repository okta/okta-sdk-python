# okta.AuthorizationServerKeysApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authorization_server_key**](AuthorizationServerKeysApi.md#get_authorization_server_key) | **GET** /api/v1/authorizationServers/{authServerId}/credentials/keys/{keyId} | Retrieve an authorization server key
[**list_authorization_server_keys**](AuthorizationServerKeysApi.md#list_authorization_server_keys) | **GET** /api/v1/authorizationServers/{authServerId}/credentials/keys | List all credential keys
[**rotate_authorization_server_keys**](AuthorizationServerKeysApi.md#rotate_authorization_server_keys) | **POST** /api/v1/authorizationServers/{authServerId}/credentials/lifecycle/keyRotate | Rotate all credential keys


# **get_authorization_server_key**
> AuthorizationServerJsonWebKey get_authorization_server_key(auth_server_id, key_id)

Retrieve an authorization server key

Retrieves an Authorization Server Key specified by the `keyId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_json_web_key import AuthorizationServerJsonWebKey
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
    api_instance = okta.AuthorizationServerKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    key_id = 'P7jXpG-LG2ObNgY9C0Mn2uf4InCQTmRZMDCZoVNxdrk' # str | `id` of the certificate key

    try:
        # Retrieve an authorization server key
        api_response = api_instance.get_authorization_server_key(auth_server_id, key_id)
        print("The response of AuthorizationServerKeysApi->get_authorization_server_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerKeysApi->get_authorization_server_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **key_id** | **str**| &#x60;id&#x60; of the certificate key | 

### Return type

[**AuthorizationServerJsonWebKey**](AuthorizationServerJsonWebKey.md)

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

# **list_authorization_server_keys**
> List[AuthorizationServerJsonWebKey] list_authorization_server_keys(auth_server_id)

List all credential keys

Lists all of the current, future, and expired Keys used by the Custom Authorization Server

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_json_web_key import AuthorizationServerJsonWebKey
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
    api_instance = okta.AuthorizationServerKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server

    try:
        # List all credential keys
        api_response = api_instance.list_authorization_server_keys(auth_server_id)
        print("The response of AuthorizationServerKeysApi->list_authorization_server_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerKeysApi->list_authorization_server_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 

### Return type

[**List[AuthorizationServerJsonWebKey]**](AuthorizationServerJsonWebKey.md)

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

# **rotate_authorization_server_keys**
> List[AuthorizationServerJsonWebKey] rotate_authorization_server_keys(auth_server_id, use)

Rotate all credential keys

Rotates the current Keys for a Custom Authorization Server. If you rotate Keys, the `ACTIVE` Key becomes the `EXPIRED` Key, the `NEXT` Key becomes the `ACTIVE` Key, and the Custom Authorization Server immediately begins using the new active Key to sign tokens.  > **Note:** Okta rotates your Keys automatically in `AUTO` mode. You can rotate Keys yourself in either mode. If Keys are rotated manually, you should invalidate any intermediate cache. and fetch the Keys again using the Keys endpoint.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.authorization_server_json_web_key import AuthorizationServerJsonWebKey
from okta.models.jwk_use import JwkUse
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
    api_instance = okta.AuthorizationServerKeysApi(api_client)
    auth_server_id = 'GeGRTEr7f3yu2n7grw22' # str | `id` of the Authorization Server
    use = okta.JwkUse() # JwkUse | 

    try:
        # Rotate all credential keys
        api_response = api_instance.rotate_authorization_server_keys(auth_server_id, use)
        print("The response of AuthorizationServerKeysApi->rotate_authorization_server_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationServerKeysApi->rotate_authorization_server_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_server_id** | **str**| &#x60;id&#x60; of the Authorization Server | 
 **use** | [**JwkUse**](JwkUse.md)|  | 

### Return type

[**List[AuthorizationServerJsonWebKey]**](AuthorizationServerJsonWebKey.md)

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

