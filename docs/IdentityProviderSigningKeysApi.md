# okta.IdentityProviderSigningKeysApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_identity_provider_key**](IdentityProviderSigningKeysApi.md#clone_identity_provider_key) | **POST** /api/v1/idps/{idpId}/credentials/keys/{kid}/clone | Clone a signing key credential for IdP
[**generate_csr_for_identity_provider**](IdentityProviderSigningKeysApi.md#generate_csr_for_identity_provider) | **POST** /api/v1/idps/{idpId}/credentials/csrs | Generate a certificate signing request
[**generate_identity_provider_signing_key**](IdentityProviderSigningKeysApi.md#generate_identity_provider_signing_key) | **POST** /api/v1/idps/{idpId}/credentials/keys/generate | Generate a new signing key credential for IdP
[**get_csr_for_identity_provider**](IdentityProviderSigningKeysApi.md#get_csr_for_identity_provider) | **GET** /api/v1/idps/{idpId}/credentials/csrs/{idpCsrId} | Retrieve a certificate signing request
[**get_identity_provider_signing_key**](IdentityProviderSigningKeysApi.md#get_identity_provider_signing_key) | **GET** /api/v1/idps/{idpId}/credentials/keys/{kid} | Retrieve a signing key credential for IdP
[**list_active_identity_provider_signing_key**](IdentityProviderSigningKeysApi.md#list_active_identity_provider_signing_key) | **GET** /api/v1/idps/{idpId}/credentials/keys/active | List the active signing key credential for IdP
[**list_csrs_for_identity_provider**](IdentityProviderSigningKeysApi.md#list_csrs_for_identity_provider) | **GET** /api/v1/idps/{idpId}/credentials/csrs | List all certificate signing requests
[**list_identity_provider_signing_keys**](IdentityProviderSigningKeysApi.md#list_identity_provider_signing_keys) | **GET** /api/v1/idps/{idpId}/credentials/keys | List all signing key credentials for IdP
[**publish_csr_for_identity_provider**](IdentityProviderSigningKeysApi.md#publish_csr_for_identity_provider) | **POST** /api/v1/idps/{idpId}/credentials/csrs/{idpCsrId}/lifecycle/publish | Publish a certificate signing request
[**revoke_csr_for_identity_provider**](IdentityProviderSigningKeysApi.md#revoke_csr_for_identity_provider) | **DELETE** /api/v1/idps/{idpId}/credentials/csrs/{idpCsrId} | Revoke a certificate signing request


# **clone_identity_provider_key**
> IdPKeyCredential clone_identity_provider_key(idp_id, kid, target_idp_id)

Clone a signing key credential for IdP

Clones an X.509 certificate for an identity provider (IdP) signing key credential from a source IdP to target IdP > **Caution:** Sharing certificates isn't a recommended security practice.  > **Note:** If the key is already present in the list of key credentials for the target IdP, you receive a 400 error response.

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    kid = 'KmMo85SSsU7TZzOShcGb' # str | Unique `id` of the IdP key credential
    target_idp_id = 'target_idp_id_example' # str | `id` of the target IdP

    try:
        # Clone a signing key credential for IdP
        api_response = api_instance.clone_identity_provider_key(idp_id, kid, target_idp_id)
        print("The response of IdentityProviderSigningKeysApi->clone_identity_provider_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->clone_identity_provider_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **kid** | **str**| Unique &#x60;id&#x60; of the IdP key credential | 
 **target_idp_id** | **str**| &#x60;id&#x60; of the target IdP | 

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
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr_for_identity_provider**
> IdPCsr generate_csr_for_identity_provider(idp_id, metadata)

Generate a certificate signing request

Generates a new key pair and returns a certificate signing request (CSR) for it > **Note:** The private key isn't listed in the [signing key credentials for the identity provider (IdP)](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProviderSigningKeys/#tag/IdentityProviderSigningKeys/operation/listIdentityProviderSigningKeys) until it's published.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.csr_metadata import CsrMetadata
from okta.models.id_p_csr import IdPCsr
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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    metadata = okta.CsrMetadata() # CsrMetadata | 

    try:
        # Generate a certificate signing request
        api_response = api_instance.generate_csr_for_identity_provider(idp_id, metadata)
        print("The response of IdentityProviderSigningKeysApi->generate_csr_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->generate_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **metadata** | [**CsrMetadata**](CsrMetadata.md)|  | 

### Return type

[**IdPCsr**](IdPCsr.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/pkcs10

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
> IdPKeyCredential generate_identity_provider_signing_key(idp_id, validity_years)

Generate a new signing key credential for IdP

Generates a new X.509 certificate for an identity provider (IdP) signing key credential to be used for signing assertions sent to the IdP. IdP signing keys are read-only. > **Note:** To update an IdP with the newly generated key credential, [update your IdP](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/replaceIdentityProvider) using the returned key's `kid` in the [signing credential](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/replaceIdentityProvider!path=protocol/0/credentials/signing/kid&t=request).

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    validity_years = 56 # int | expiry of the IdP key credential

    try:
        # Generate a new signing key credential for IdP
        api_response = api_instance.generate_identity_provider_signing_key(idp_id, validity_years)
        print("The response of IdentityProviderSigningKeysApi->generate_identity_provider_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->generate_identity_provider_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **validity_years** | **int**| expiry of the IdP key credential | 

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

# **get_csr_for_identity_provider**
> IdPCsr get_csr_for_identity_provider(idp_id, idp_csr_id)

Retrieve a certificate signing request

Retrieves a specific certificate signing request (CSR) by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.id_p_csr import IdPCsr
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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    idp_csr_id = '1uEhyE65oV3H6KM9gYcN' # str | `id` of the IdP CSR

    try:
        # Retrieve a certificate signing request
        api_response = api_instance.get_csr_for_identity_provider(idp_id, idp_csr_id)
        print("The response of IdentityProviderSigningKeysApi->get_csr_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->get_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_csr_id** | **str**| &#x60;id&#x60; of the IdP CSR | 

### Return type

[**IdPCsr**](IdPCsr.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pkcs10

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_provider_signing_key**
> IdPKeyCredential get_identity_provider_signing_key(idp_id, kid)

Retrieve a signing key credential for IdP

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    kid = 'KmMo85SSsU7TZzOShcGb' # str | Unique `id` of the IdP key credential

    try:
        # Retrieve a signing key credential for IdP
        api_response = api_instance.get_identity_provider_signing_key(idp_id, kid)
        print("The response of IdentityProviderSigningKeysApi->get_identity_provider_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->get_identity_provider_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
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

# **list_active_identity_provider_signing_key**
> List[IdPKeyCredential] list_active_identity_provider_signing_key(idp_id)

List the active signing key credential for IdP

Lists the active signing key credential for an identity provider (IdP)

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP

    try:
        # List the active signing key credential for IdP
        api_response = api_instance.list_active_identity_provider_signing_key(idp_id)
        print("The response of IdentityProviderSigningKeysApi->list_active_identity_provider_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->list_active_identity_provider_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

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
**204** | No Content |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_csrs_for_identity_provider**
> List[IdPCsr] list_csrs_for_identity_provider(idp_id)

List all certificate signing requests

Lists all certificate signing requests (CSRs) for an identity provider (IdP)

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.id_p_csr import IdPCsr
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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP

    try:
        # List all certificate signing requests
        api_response = api_instance.list_csrs_for_identity_provider(idp_id)
        print("The response of IdentityProviderSigningKeysApi->list_csrs_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->list_csrs_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

### Return type

[**List[IdPCsr]**](IdPCsr.md)

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

# **list_identity_provider_signing_keys**
> List[IdPKeyCredential] list_identity_provider_signing_keys(idp_id)

List all signing key credentials for IdP

Lists all signing key credentials for an identity provider (IdP)

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP

    try:
        # List all signing key credentials for IdP
        api_response = api_instance.list_identity_provider_signing_keys(idp_id)
        print("The response of IdentityProviderSigningKeysApi->list_identity_provider_signing_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->list_identity_provider_signing_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_csr_for_identity_provider**
> IdPKeyCredential publish_csr_for_identity_provider(idp_id, idp_csr_id, body)

Publish a certificate signing request

Publishes the certificate signing request (CSR) with a signed X.509 certificate and adds it into the signing key credentials for the identity provider (IdP) > **Notes:** > * Publishing a certificate completes the lifecycle of the CSR, and it's no longer accessible. > * If the validity period of the certificate is less than 90 days, a 400 error response is returned.

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    idp_csr_id = '1uEhyE65oV3H6KM9gYcN' # str | `id` of the IdP CSR
    body = None # bytearray | 

    try:
        # Publish a certificate signing request
        api_response = api_instance.publish_csr_for_identity_provider(idp_id, idp_csr_id, body)
        print("The response of IdentityProviderSigningKeysApi->publish_csr_for_identity_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->publish_csr_for_identity_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp_id** | **str**| &#x60;id&#x60; of IdP | 
 **idp_csr_id** | **str**| &#x60;id&#x60; of the IdP CSR | 
 **body** | **bytearray**|  | 

### Return type

[**IdPKeyCredential**](IdPKeyCredential.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/pkix-cert, application/x-x509-ca-cert, application/x-pem-file
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

# **revoke_csr_for_identity_provider**
> revoke_csr_for_identity_provider(idp_id, idp_csr_id)

Revoke a certificate signing request

Revokes a certificate signing request (CSR) and deletes the key pair from the identity provider (IdP)

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
    api_instance = okta.IdentityProviderSigningKeysApi(api_client)
    idp_id = '0oa62bfdjnK55Z5x80h7' # str | `id` of IdP
    idp_csr_id = '1uEhyE65oV3H6KM9gYcN' # str | `id` of the IdP CSR

    try:
        # Revoke a certificate signing request
        api_instance.revoke_csr_for_identity_provider(idp_id, idp_csr_id)
    except Exception as e:
        print("Exception when calling IdentityProviderSigningKeysApi->revoke_csr_for_identity_provider: %s\n" % e)
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

