# okta.IdentityProviderApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_identity_provider**](IdentityProviderApi.md#activate_identity_provider) | **POST** /api/v1/idps/{idpId}/lifecycle/activate | Activate an Identity Provider
[**clone_identity_provider_key**](IdentityProviderApi.md#clone_identity_provider_key) | **POST** /api/v1/idps/{idpId}/credentials/keys/{idpKeyId}/clone | Clone a Signing Credential Key
[**create_identity_provider**](IdentityProviderApi.md#create_identity_provider) | **POST** /api/v1/idps | Create an Identity Provider
[**create_identity_provider_key**](IdentityProviderApi.md#create_identity_provider_key) | **POST** /api/v1/idps/credentials/keys | Create an X.509 Certificate Public Key
[**deactivate_identity_provider**](IdentityProviderApi.md#deactivate_identity_provider) | **POST** /api/v1/idps/{idpId}/lifecycle/deactivate | Deactivate an Identity Provider
[**delete_identity_provider**](IdentityProviderApi.md#delete_identity_provider) | **DELETE** /api/v1/idps/{idpId} | Delete an Identity Provider
[**delete_identity_provider_key**](IdentityProviderApi.md#delete_identity_provider_key) | **DELETE** /api/v1/idps/credentials/keys/{idpKeyId} | Delete a Signing Credential Key
[**generate_csr_for_identity_provider**](IdentityProviderApi.md#generate_csr_for_identity_provider) | **POST** /api/v1/idps/{idpId}/credentials/csrs | Generate a Certificate Signing Request
[**generate_identity_provider_signing_key**](IdentityProviderApi.md#generate_identity_provider_signing_key) | **POST** /api/v1/idps/{idpId}/credentials/keys/generate | Generate a new Signing Credential Key
[**get_csr_for_identity_provider**](IdentityProviderApi.md#get_csr_for_identity_provider) | **GET** /api/v1/idps/{idpId}/credentials/csrs/{idpCsrId} | Retrieve a Certificate Signing Request
[**get_identity_provider**](IdentityProviderApi.md#get_identity_provider) | **GET** /api/v1/idps/{idpId} | Retrieve an Identity Provider
[**get_identity_provider_application_user**](IdentityProviderApi.md#get_identity_provider_application_user) | **GET** /api/v1/idps/{idpId}/users/{userId} | Retrieve a User
[**get_identity_provider_key**](IdentityProviderApi.md#get_identity_provider_key) | **GET** /api/v1/idps/credentials/keys/{idpKeyId} | Retrieve an Credential Key
[**get_identity_provider_signing_key**](IdentityProviderApi.md#get_identity_provider_signing_key) | **GET** /api/v1/idps/{idpId}/credentials/keys/{idpKeyId} | Retrieve a Signing Credential Key
[**link_user_to_identity_provider**](IdentityProviderApi.md#link_user_to_identity_provider) | **POST** /api/v1/idps/{idpId}/users/{userId} | Link a User to a Social IdP
[**list_csrs_for_identity_provider**](IdentityProviderApi.md#list_csrs_for_identity_provider) | **GET** /api/v1/idps/{idpId}/credentials/csrs | List all Certificate Signing Requests
[**list_identity_provider_application_users**](IdentityProviderApi.md#list_identity_provider_application_users) | **GET** /api/v1/idps/{idpId}/users | List all Users
[**list_identity_provider_keys**](IdentityProviderApi.md#list_identity_provider_keys) | **GET** /api/v1/idps/credentials/keys | List all Credential Keys
[**list_identity_provider_signing_keys**](IdentityProviderApi.md#list_identity_provider_signing_keys) | **GET** /api/v1/idps/{idpId}/credentials/keys | List all Signing Credential Keys
[**list_identity_providers**](IdentityProviderApi.md#list_identity_providers) | **GET** /api/v1/idps | List all Identity Providers
[**list_social_auth_tokens**](IdentityProviderApi.md#list_social_auth_tokens) | **GET** /api/v1/idps/{idpId}/users/{userId}/credentials/tokens | List all Tokens from a OIDC Identity Provider
[**publish_csr_for_identity_provider**](IdentityProviderApi.md#publish_csr_for_identity_provider) | **POST** /api/v1/idps/{idpId}/credentials/csrs/{idpCsrId}/lifecycle/publish | Publish a Certificate Signing Request
[**replace_identity_provider**](IdentityProviderApi.md#replace_identity_provider) | **PUT** /api/v1/idps/{idpId} | Replace an Identity Provider
[**revoke_csr_for_identity_provider**](IdentityProviderApi.md#revoke_csr_for_identity_provider) | **DELETE** /api/v1/idps/{idpId}/credentials/csrs/{idpCsrId} | Revoke a Certificate Signing Request
[**unlink_user_from_identity_provider**](IdentityProviderApi.md#unlink_user_from_identity_provider) | **DELETE** /api/v1/idps/{idpId}/users/{userId} | Unlink a User from IdP


# **activate_identity_provider**
> IdentityProvider activate_identity_provider(idp_id)

Activate an Identity Provider

Activates an inactive IdP

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # Activate an Identity Provider
        api_response = api_instance.activate_identity_provider(idp_id)
        print("The response of IdentityProviderApi->activate_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->activate_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **clone_identity_provider_key**
> JsonWebKey clone_identity_provider_key(idp_id, idp_key_id, target_idp_id)

Clone a Signing Credential Key

Clones a X.509 certificate for an IdP signing key credential from a source IdP to target IdP

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    idp_key_id = 'KmMo85SSsU7TZzOShcGb' # str | `id` of IdP Key
    target_idp_id = 'target_idp_id_example' # str | 

    try:
        # Clone a Signing Credential Key
        api_response = api_instance.clone_identity_provider_key(idp_id, idp_key_id, target_idp_id)
        print("The response of IdentityProviderApi->clone_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->clone_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_key_id** | **str**| &#x60;id&#x60; of IdP Key | 
 **target_idp_id** | **str**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_identity_provider**
> IdentityProvider create_identity_provider(identity_provider)

Create an Identity Provider

Creates a new identity provider integration

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
    api_instance = okta.IdentityProviderApi(api_client)
    identity_provider = okta.IdentityProvider() # IdentityProvider | 

    try:
        # Create an Identity Provider
        api_response = api_instance.create_identity_provider(identity_provider)
        print("The response of IdentityProviderApi->create_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider** | [**IdentityProvider**](IdentityProvider.md)|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **create_identity_provider_key**
> JsonWebKey create_identity_provider_key(json_web_key)

Create an X.509 Certificate Public Key

Creates a new X.509 certificate credential to the IdP key store.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    json_web_key = okta.JsonWebKey() # JsonWebKey | 

    try:
        # Create an X.509 Certificate Public Key
        api_response = api_instance.create_identity_provider_key(json_web_key)
        print("The response of IdentityProviderApi->create_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->create_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_web_key** | [**JsonWebKey**](JsonWebKey.md)|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

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

# **deactivate_identity_provider**
> IdentityProvider deactivate_identity_provider(idp_id)

Deactivate an Identity Provider

Deactivates an active IdP

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # Deactivate an Identity Provider
        api_response = api_instance.deactivate_identity_provider(idp_id)
        print("The response of IdentityProviderApi->deactivate_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->deactivate_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **delete_identity_provider**
> delete_identity_provider(idp_id)

Delete an Identity Provider

Deletes an identity provider integration by `idpId`

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # Delete an Identity Provider
        api_instance.delete_identity_provider(idp_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

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

# **delete_identity_provider_key**
> delete_identity_provider_key(idp_key_id)

Delete a Signing Credential Key

Deletes a specific IdP Key Credential by `kid` if it is not currently being used by an Active or Inactive IdP

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_key_id = 'KmMo85SSsU7TZzOShcGb' # str | `id` of IdP Key

    try:
        # Delete a Signing Credential Key
        api_instance.delete_identity_provider_key(idp_key_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->delete_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_key_id** | **str**| &#x60;id&#x60; of IdP Key | 

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

# **generate_csr_for_identity_provider**
> Csr generate_csr_for_identity_provider(idp_id, metadata)

Generate a Certificate Signing Request

Generates a new key pair and returns a Certificate Signing Request for it

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.csr import Csr
from okta.models.csr_metadata import CsrMetadata
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    metadata = okta.CsrMetadata() # CsrMetadata | 

    try:
        # Generate a Certificate Signing Request
        api_response = api_instance.generate_csr_for_identity_provider(idp_id, metadata)
        print("The response of IdentityProviderApi->generate_csr_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->generate_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **metadata** | [**CsrMetadata**](CsrMetadata.md)|  | 

### Return type

[**Csr**](Csr.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_identity_provider_signing_key**
> JsonWebKey generate_identity_provider_signing_key(idp_id, validity_years)

Generate a new Signing Credential Key

Generates a new X.509 certificate for an IdP signing key credential to be used for signing assertions sent to the IdP

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    validity_years = 56 # int | expiry of the IdP Key Credential

    try:
        # Generate a new Signing Credential Key
        api_response = api_instance.generate_identity_provider_signing_key(idp_id, validity_years)
        print("The response of IdentityProviderApi->generate_identity_provider_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->generate_identity_provider_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **validity_years** | **int**| expiry of the IdP Key Credential | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

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

# **get_csr_for_identity_provider**
> Csr get_csr_for_identity_provider(idp_id, idp_csr_id)

Retrieve a Certificate Signing Request

Retrieves a specific Certificate Signing Request model by id

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.csr import Csr
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    idp_csr_id = '1uEhyE65oV3H6KM9gYcN' # str | `id` of the IdP CSR

    try:
        # Retrieve a Certificate Signing Request
        api_response = api_instance.get_csr_for_identity_provider(idp_id, idp_csr_id)
        print("The response of IdentityProviderApi->get_csr_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_csr_id** | **str**| &#x60;id&#x60; of the IdP CSR | 

### Return type

[**Csr**](Csr.md)

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

# **get_identity_provider**
> IdentityProvider get_identity_provider(idp_id)

Retrieve an Identity Provider

Retrieves an identity provider integration by `idpId`

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # Retrieve an Identity Provider
        api_response = api_instance.get_identity_provider(idp_id)
        print("The response of IdentityProviderApi->get_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **get_identity_provider_application_user**
> IdentityProviderApplicationUser get_identity_provider_application_user(idp_id, user_id)

Retrieve a User

Retrieves a linked IdP user by ID

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    user_id = 'user_id_example' # str | 

    try:
        # Retrieve a User
        api_response = api_instance.get_identity_provider_application_user(idp_id, user_id)
        print("The response of IdentityProviderApi->get_identity_provider_application_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identity_provider_application_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**|  | 

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

# **get_identity_provider_key**
> JsonWebKey get_identity_provider_key(idp_key_id)

Retrieve an Credential Key

Retrieves a specific IdP Key Credential by `kid`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_key_id = 'KmMo85SSsU7TZzOShcGb' # str | `id` of IdP Key

    try:
        # Retrieve an Credential Key
        api_response = api_instance.get_identity_provider_key(idp_key_id)
        print("The response of IdentityProviderApi->get_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_key_id** | **str**| &#x60;id&#x60; of IdP Key | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

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

# **get_identity_provider_signing_key**
> JsonWebKey get_identity_provider_signing_key(idp_id, idp_key_id)

Retrieve a Signing Credential Key

Retrieves a specific IdP Key Credential by `kid`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    idp_key_id = 'KmMo85SSsU7TZzOShcGb' # str | `id` of IdP Key

    try:
        # Retrieve a Signing Credential Key
        api_response = api_instance.get_identity_provider_signing_key(idp_id, idp_key_id)
        print("The response of IdentityProviderApi->get_identity_provider_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->get_identity_provider_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_key_id** | **str**| &#x60;id&#x60; of IdP Key | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

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

Link a User to a Social IdP

Links an Okta user to an existing Social Identity Provider. This does not support the SAML2 Identity Provider Type

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    user_id = 'user_id_example' # str | 
    user_identity_provider_link_request = okta.UserIdentityProviderLinkRequest() # UserIdentityProviderLinkRequest | 

    try:
        # Link a User to a Social IdP
        api_response = api_instance.link_user_to_identity_provider(idp_id, user_id, user_identity_provider_link_request)
        print("The response of IdentityProviderApi->link_user_to_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->link_user_to_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**|  | 
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

# **list_csrs_for_identity_provider**
> List[Csr] list_csrs_for_identity_provider(idp_id)

List all Certificate Signing Requests

Lists all Certificate Signing Requests for an IdP

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.csr import Csr
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # List all Certificate Signing Requests
        api_response = api_instance.list_csrs_for_identity_provider(idp_id)
        print("The response of IdentityProviderApi->list_csrs_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_csrs_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

### Return type

[**List[Csr]**](Csr.md)

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

# **list_identity_provider_application_users**
> List[IdentityProviderApplicationUser] list_identity_provider_application_users(idp_id)

List all Users

Lists all users linked to the identity provider

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # List all Users
        api_response = api_instance.list_identity_provider_application_users(idp_id)
        print("The response of IdentityProviderApi->list_identity_provider_application_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_identity_provider_application_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

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

# **list_identity_provider_keys**
> List[JsonWebKey] list_identity_provider_keys(after=after, limit=limit)

List all Credential Keys

Lists all IdP key credentials

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of keys (optional)
    limit = 20 # int | Specifies the number of key results in a page (optional) (default to 20)

    try:
        # List all Credential Keys
        api_response = api_instance.list_identity_provider_keys(after=after, limit=limit)
        print("The response of IdentityProviderApi->list_identity_provider_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_identity_provider_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Specifies the pagination cursor for the next page of keys | [optional] 
 **limit** | **int**| Specifies the number of key results in a page | [optional] [default to 20]

### Return type

[**List[JsonWebKey]**](JsonWebKey.md)

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

# **list_identity_provider_signing_keys**
> List[JsonWebKey] list_identity_provider_signing_keys(idp_id)

List all Signing Credential Keys

Lists all signing key credentials for an IdP

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP

    try:
        # List all Signing Credential Keys
        api_response = api_instance.list_identity_provider_signing_keys(idp_id)
        print("The response of IdentityProviderApi->list_identity_provider_signing_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_identity_provider_signing_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

### Return type

[**List[JsonWebKey]**](JsonWebKey.md)

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

# **list_identity_providers**
> List[IdentityProvider] list_identity_providers(q=q, after=after, limit=limit, type=type)

List all Identity Providers

Lists all identity provider integrations with pagination. A subset of IdPs can be returned that match a supported filter expression or query.

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
    api_instance = okta.IdentityProviderApi(api_client)
    q = 'q_example' # str | Searches the name property of IdPs for matching value (optional)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of IdPs (optional)
    limit = 20 # int | Specifies the number of IdP results in a page (optional) (default to 20)
    type = 'type_example' # str | Filters IdPs by type (optional)

    try:
        # List all Identity Providers
        api_response = api_instance.list_identity_providers(q=q, after=after, limit=limit, type=type)
        print("The response of IdentityProviderApi->list_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Searches the name property of IdPs for matching value | [optional] 
 **after** | **str**| Specifies the pagination cursor for the next page of IdPs | [optional] 
 **limit** | **int**| Specifies the number of IdP results in a page | [optional] [default to 20]
 **type** | **str**| Filters IdPs by type | [optional] 

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_social_auth_tokens**
> List[SocialAuthToken] list_social_auth_tokens(idp_id, user_id)

List all Tokens from a OIDC Identity Provider

Lists the tokens minted by the Social Authentication Provider when the user authenticates with Okta via Social Auth

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    user_id = 'user_id_example' # str | 

    try:
        # List all Tokens from a OIDC Identity Provider
        api_response = api_instance.list_social_auth_tokens(idp_id, user_id)
        print("The response of IdentityProviderApi->list_social_auth_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->list_social_auth_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**|  | 

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

# **publish_csr_for_identity_provider**
> JsonWebKey publish_csr_for_identity_provider(idp_id, idp_csr_id, body)

Publish a Certificate Signing Request

Publishes a certificate signing request with a signed X.509 certificate and adds it into the signing key credentials for the IdP

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.json_web_key import JsonWebKey
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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    idp_csr_id = '1uEhyE65oV3H6KM9gYcN' # str | `id` of the IdP CSR
    body = None # bytearray | 

    try:
        # Publish a Certificate Signing Request
        api_response = api_instance.publish_csr_for_identity_provider(idp_id, idp_csr_id, body)
        print("The response of IdentityProviderApi->publish_csr_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->publish_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_csr_id** | **str**| &#x60;id&#x60; of the IdP CSR | 
 **body** | **bytearray**|  | 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-x509-ca-cert, application/pkix-cert, application/x-pem-file
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_identity_provider**
> IdentityProvider replace_identity_provider(idp_id, identity_provider)

Replace an Identity Provider

Replaces an identity provider integration by `idpId`

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    identity_provider = okta.IdentityProvider() # IdentityProvider | 

    try:
        # Replace an Identity Provider
        api_response = api_instance.replace_identity_provider(idp_id, identity_provider)
        print("The response of IdentityProviderApi->replace_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->replace_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **identity_provider** | [**IdentityProvider**](IdentityProvider.md)|  | 

### Return type

[**IdentityProvider**](IdentityProvider.md)

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

# **revoke_csr_for_identity_provider**
> revoke_csr_for_identity_provider(idp_id, idp_csr_id)

Revoke a Certificate Signing Request

Revokes a certificate signing request and deletes the key pair from the IdP

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    idp_csr_id = '1uEhyE65oV3H6KM9gYcN' # str | `id` of the IdP CSR

    try:
        # Revoke a Certificate Signing Request
        api_instance.revoke_csr_for_identity_provider(idp_id, idp_csr_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->revoke_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_csr_id** | **str**| &#x60;id&#x60; of the IdP CSR | 

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

# **unlink_user_from_identity_provider**
> unlink_user_from_identity_provider(idp_id, user_id)

Unlink a User from IdP

Unlinks the link between the Okta user and the IdP user

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
    api_instance = okta.IdentityProviderApi(api_client)
    idp_id = 'SVHoAOh0l8cPQkVX1LRl' # str | `id` of IdP
    user_id = 'user_id_example' # str | 

    try:
        # Unlink a User from IdP
        api_instance.unlink_user_from_identity_provider(idp_id, user_id)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->unlink_user_from_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **user_id** | **str**|  | 

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

