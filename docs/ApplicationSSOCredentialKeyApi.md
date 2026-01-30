# okta.ApplicationSSOCredentialKeyApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_application_key**](ApplicationSSOCredentialKeyApi.md#clone_application_key) | **POST** /api/v1/apps/{appId}/credentials/keys/{keyId}/clone | Clone a key credential
[**generate_application_key**](ApplicationSSOCredentialKeyApi.md#generate_application_key) | **POST** /api/v1/apps/{appId}/credentials/keys/generate | Generate a key credential
[**generate_csr_for_application**](ApplicationSSOCredentialKeyApi.md#generate_csr_for_application) | **POST** /api/v1/apps/{appId}/credentials/csrs | Generate a certificate signing request
[**get_application_key**](ApplicationSSOCredentialKeyApi.md#get_application_key) | **GET** /api/v1/apps/{appId}/credentials/keys/{keyId} | Retrieve a key credential
[**get_csr_for_application**](ApplicationSSOCredentialKeyApi.md#get_csr_for_application) | **GET** /api/v1/apps/{appId}/credentials/csrs/{csrId} | Retrieve a certificate signing request
[**list_application_keys**](ApplicationSSOCredentialKeyApi.md#list_application_keys) | **GET** /api/v1/apps/{appId}/credentials/keys | List all key credentials
[**list_csrs_for_application**](ApplicationSSOCredentialKeyApi.md#list_csrs_for_application) | **GET** /api/v1/apps/{appId}/credentials/csrs | List all certificate signing requests
[**publish_csr_from_application**](ApplicationSSOCredentialKeyApi.md#publish_csr_from_application) | **POST** /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle/publish | Publish a certificate signing request
[**revoke_csr_from_application**](ApplicationSSOCredentialKeyApi.md#revoke_csr_from_application) | **DELETE** /api/v1/apps/{appId}/credentials/csrs/{csrId} | Revoke a certificate signing request


# **clone_application_key**
> JsonWebKey clone_application_key(app_id, key_id, target_aid)

Clone a key credential

Clones an X.509 certificate for an Application Key Credential from a source app to a target app.  For step-by-step instructions to clone a credential, see [Share application key credentials for IdPs across apps](https://developer.okta.com/docs/guides/sharing-cert/main/). > **Note:** Sharing certificates isn't a recommended security practice.

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    key_id = 'sjP9eiETijYz110VkhHN' # str | ID of the Key Credential for the application
    target_aid = '0ouuytCAJSSDELFTUIDS' # str | Unique key of the target Application

    try:
        # Clone a key credential
        api_response = api_instance.clone_application_key(app_id, key_id, target_aid)
        print("The response of ApplicationSSOCredentialKeyApi->clone_application_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->clone_application_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **key_id** | **str**| ID of the Key Credential for the application | 
 **target_aid** | **str**| Unique key of the target Application | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_application_key**
> JsonWebKey generate_application_key(app_id, validity_years)

Generate a key credential

Generates a new X.509 certificate for an app key credential > **Note:** To update an Application with the newly generated key credential, use the [Replace an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/replaceApplication) request with the new [credentials.signing.kid](/openapi/okta-management/management/tag/Application/#tag/Application/operation/replaceApplication!path=4/credentials/signing/kid&t=request) value in the request body. You can provide just the [Signing Credential object](/openapi/okta-management/management/tag/Application/#tag/Application/operation/replaceApplication!path=4/credentials/signing&t=request) instead of the entire [Application Credential object](/openapi/okta-management/management/tag/Application/#tag/Application/operation/replaceApplication!path=4/credentials&t=request).

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    validity_years = 5 # int | Expiry years of the Application Key Credential

    try:
        # Generate a key credential
        api_response = api_instance.generate_application_key(app_id, validity_years)
        print("The response of ApplicationSSOCredentialKeyApi->generate_application_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->generate_application_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **validity_years** | **int**| Expiry years of the Application Key Credential | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_csr_for_application**
> str generate_csr_for_application(app_id, metadata)

Generate a certificate signing request

Generates a new key pair and returns the Certificate Signing Request(CSR) for it. The information in a CSR is used by the Certificate Authority (CA) to verify and create your certificate. It also contains the public key that is included in your certificate.  Returns CSR in `pkcs#10` format if the `Accept` media type is `application/pkcs10` or a CSR object if the `Accept` media type is `application/json`. > **Note:** The key pair isn't listed in the Key Credentials for the app until it's published.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    metadata = okta.CsrMetadata() # CsrMetadata | 

    try:
        # Generate a certificate signing request
        api_response = api_instance.generate_csr_for_application(app_id, metadata)
        print("The response of ApplicationSSOCredentialKeyApi->generate_csr_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->generate_csr_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **metadata** | [**CsrMetadata**](CsrMetadata.md)|  | 

### Return type

**str**

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pkcs10, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Content-Type - The Content-Type of the response <br>  * Content-Transfer-Encoding - Encoding of the response <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_key**
> JsonWebKey get_application_key(app_id, key_id)

Retrieve a key credential

Retrieves a specific Application Key Credential by `kid`

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    key_id = 'sjP9eiETijYz110VkhHN' # str | ID of the Key Credential for the application

    try:
        # Retrieve a key credential
        api_response = api_instance.get_application_key(app_id, key_id)
        print("The response of ApplicationSSOCredentialKeyApi->get_application_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->get_application_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **key_id** | **str**| ID of the Key Credential for the application | 

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

# **get_csr_for_application**
> Csr get_csr_for_application(app_id, csr_id)

Retrieve a certificate signing request

Retrieves a Certificate Signing Request (CSR) for the app by `csrId`.  Returns a Base64-encoded CSR in DER format if the `Accept` media type is `application/pkcs10` or a CSR object if the `Accept` media type is `application/json`.

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    csr_id = 'fd7x1h7uTcZFx22rU1f7' # str | `id` of the CSR

    try:
        # Retrieve a certificate signing request
        api_response = api_instance.get_csr_for_application(app_id, csr_id)
        print("The response of ApplicationSSOCredentialKeyApi->get_csr_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->get_csr_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **csr_id** | **str**| &#x60;id&#x60; of the CSR | 

### Return type

[**Csr**](Csr.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/pkcs10

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Type - The Content-Type of the response <br>  * Content-Transfer-Encoding - Encoding of the response <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_keys**
> List[JsonWebKey] list_application_keys(app_id)

List all key credentials

Lists all key credentials for an app

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # List all key credentials
        api_response = api_instance.list_application_keys(app_id)
        print("The response of ApplicationSSOCredentialKeyApi->list_application_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->list_application_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

# **list_csrs_for_application**
> List[Csr] list_csrs_for_application(app_id)

List all certificate signing requests

Lists all Certificate Signing Requests for an application

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID

    try:
        # List all certificate signing requests
        api_response = api_instance.list_csrs_for_application(app_id)
        print("The response of ApplicationSSOCredentialKeyApi->list_csrs_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->list_csrs_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 

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

# **publish_csr_from_application**
> JsonWebKey publish_csr_from_application(app_id, csr_id, body)

Publish a certificate signing request

Publishes a Certificate Signing Request (CSR) for the app with a signed X.509 certificate and adds it into the Application Key Credentials. > **Note:** Publishing a certificate completes the lifecycle of the CSR and it's no longer accessible.

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    csr_id = 'fd7x1h7uTcZFx22rU1f7' # str | `id` of the CSR
    body = None # bytearray | 

    try:
        # Publish a certificate signing request
        api_response = api_instance.publish_csr_from_application(app_id, csr_id, body)
        print("The response of ApplicationSSOCredentialKeyApi->publish_csr_from_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->publish_csr_from_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **csr_id** | **str**| &#x60;id&#x60; of the CSR | 
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

# **revoke_csr_from_application**
> revoke_csr_from_application(app_id, csr_id)

Revoke a certificate signing request

Revokes a Certificate Signing Request and deletes the key pair from the app

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
    api_instance = okta.ApplicationSSOCredentialKeyApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | Application ID
    csr_id = 'fd7x1h7uTcZFx22rU1f7' # str | `id` of the CSR

    try:
        # Revoke a certificate signing request
        api_instance.revoke_csr_from_application(app_id, csr_id)
    except Exception as e:
        print("Exception when calling ApplicationSSOCredentialKeyApi->revoke_csr_from_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID | 
 **csr_id** | **str**| &#x60;id&#x60; of the CSR | 

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

