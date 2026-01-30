# okta.IdentityProviderKeysApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity_provider_key**](IdentityProviderKeysApi.md#create_identity_provider_key) | **POST** /api/v1/idps/credentials/keys | Create an IdP key credential
[**delete_identity_provider_key**](IdentityProviderKeysApi.md#delete_identity_provider_key) | **DELETE** /api/v1/idps/credentials/keys/{kid} | Delete an IdP key credential
[**get_identity_provider_key**](IdentityProviderKeysApi.md#get_identity_provider_key) | **GET** /api/v1/idps/credentials/keys/{kid} | Retrieve an IdP key credential
[**list_identity_provider_keys**](IdentityProviderKeysApi.md#list_identity_provider_keys) | **GET** /api/v1/idps/credentials/keys | List all IdP key credentials
[**replace_identity_provider_key**](IdentityProviderKeysApi.md#replace_identity_provider_key) | **PUT** /api/v1/idps/credentials/keys/{kid} | Replace an IdP key credential


# **create_identity_provider_key**
> IdPKeyCredential create_identity_provider_key(json_web_key)

Create an IdP key credential

Creates a new X.509 certificate credential in the identity provider (IdP) key store > **Note:** RSA-based certificates are supported for all IdP types. Okta currently supports EC-based certificates only for the `X509` IdP type. For EC-based certificates we support only P-256, P-384, and P-521 curves.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.id_p_certificate_credential import IdPCertificateCredential
from okta.models.id_p_key_credential import IdPKeyCredential
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
    api_instance = okta.IdentityProviderKeysApi(api_client)
    json_web_key = okta.IdPCertificateCredential() # IdPCertificateCredential | 

    try:
        # Create an IdP key credential
        api_response = api_instance.create_identity_provider_key(json_web_key)
        print("The response of IdentityProviderKeysApi->create_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderKeysApi->create_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_web_key** | [**IdPCertificateCredential**](IdPCertificateCredential.md)|  | 

### Return type

[**IdPKeyCredential**](IdPKeyCredential.md)

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

# **delete_identity_provider_key**
> delete_identity_provider_key(kid)

Delete an IdP key credential

Deletes a specific identity provider (IdP) key credential by `kid` if it isn't currently being used by an active or inactive IdP

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
    api_instance = okta.IdentityProviderKeysApi(api_client)
    kid = 'KmMo85SSsU7TZzOShcGb' # str | Unique `id` of the IdP key credential

    try:
        # Delete an IdP key credential
        api_instance.delete_identity_provider_key(kid)
    except Exception as e:
        print("Exception when calling IdentityProviderKeysApi->delete_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| Unique &#x60;id&#x60; of the IdP key credential | 

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

# **get_identity_provider_key**
> IdPKeyCredential get_identity_provider_key(kid)

Retrieve an IdP key credential

Retrieves a specific identity provider (IdP) key credential by `kid`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.id_p_key_credential import IdPKeyCredential
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
    api_instance = okta.IdentityProviderKeysApi(api_client)
    kid = 'KmMo85SSsU7TZzOShcGb' # str | Unique `id` of the IdP key credential

    try:
        # Retrieve an IdP key credential
        api_response = api_instance.get_identity_provider_key(kid)
        print("The response of IdentityProviderKeysApi->get_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderKeysApi->get_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| Unique &#x60;id&#x60; of the IdP key credential | 

### Return type

[**IdPKeyCredential**](IdPKeyCredential.md)

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

# **list_identity_provider_keys**
> List[IdPKeyCredential] list_identity_provider_keys(after=after, limit=limit)

List all IdP key credentials

Lists all identity provider (IdP) key credentials

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.id_p_key_credential import IdPKeyCredential
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
    api_instance = okta.IdentityProviderKeysApi(api_client)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)
    limit = 20 # int | A limit on the number of objects to return (optional) (default to 20)

    try:
        # List all IdP key credentials
        api_response = api_instance.list_identity_provider_keys(after=after, limit=limit)
        print("The response of IdentityProviderKeysApi->list_identity_provider_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderKeysApi->list_identity_provider_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 
 **limit** | **int**| A limit on the number of objects to return | [optional] [default to 20]

### Return type

[**List[IdPKeyCredential]**](IdPKeyCredential.md)

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

# **replace_identity_provider_key**
> IdPKeyCredential replace_identity_provider_key(kid, id_p_key_credential)

Replace an IdP key credential

Replaces an identity provider (IdP) key credential by `kid`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.id_p_key_credential import IdPKeyCredential
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
    api_instance = okta.IdentityProviderKeysApi(api_client)
    kid = 'KmMo85SSsU7TZzOShcGb' # str | Unique `id` of the IdP key credential
    id_p_key_credential = okta.IdPKeyCredential() # IdPKeyCredential | Updated IdP key credential

    try:
        # Replace an IdP key credential
        api_response = api_instance.replace_identity_provider_key(kid, id_p_key_credential)
        print("The response of IdentityProviderKeysApi->replace_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderKeysApi->replace_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| Unique &#x60;id&#x60; of the IdP key credential | 
 **id_p_key_credential** | [**IdPKeyCredential**](IdPKeyCredential.md)| Updated IdP key credential | 

### Return type

[**IdPKeyCredential**](IdPKeyCredential.md)

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

