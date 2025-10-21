# okta.ApplicationCredentialsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_application_key**](ApplicationCredentialsApi.md#clone_application_key) | **POST** /api/v1/apps/{appId}/credentials/keys/{keyId}/clone | Clone a Key Credential
[**generate_application_key**](ApplicationCredentialsApi.md#generate_application_key) | **POST** /api/v1/apps/{appId}/credentials/keys/generate | Generate a Key Credential
[**generate_csr_for_application**](ApplicationCredentialsApi.md#generate_csr_for_application) | **POST** /api/v1/apps/{appId}/credentials/csrs | Generate a Certificate Signing Request
[**get_application_key**](ApplicationCredentialsApi.md#get_application_key) | **GET** /api/v1/apps/{appId}/credentials/keys/{keyId} | Retrieve a Key Credential
[**get_csr_for_application**](ApplicationCredentialsApi.md#get_csr_for_application) | **GET** /api/v1/apps/{appId}/credentials/csrs/{csrId} | Retrieve a Certificate Signing Request
[**list_application_keys**](ApplicationCredentialsApi.md#list_application_keys) | **GET** /api/v1/apps/{appId}/credentials/keys | List all Key Credentials
[**list_csrs_for_application**](ApplicationCredentialsApi.md#list_csrs_for_application) | **GET** /api/v1/apps/{appId}/credentials/csrs | List all Certificate Signing Requests
[**publish_csr_from_application**](ApplicationCredentialsApi.md#publish_csr_from_application) | **POST** /api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle/publish | Publish a Certificate Signing Request
[**revoke_csr_from_application**](ApplicationCredentialsApi.md#revoke_csr_from_application) | **DELETE** /api/v1/apps/{appId}/credentials/csrs/{csrId} | Revoke a Certificate Signing Request


# **clone_application_key**
> JsonWebKey clone_application_key(app_id, key_id, target_aid)

Clone a Key Credential

Clones a X.509 certificate for an application key credential from a source application to target application.

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    key_id = 'sjP9eiETijYz110VkhHN' # str | ID of the Key Credential for the application
    target_aid = 'target_aid_example' # str | Unique key of the target Application

    try:
        # Clone a Key Credential
        api_response = api_instance.clone_application_key(app_id, key_id, target_aid)
        print("The response of ApplicationCredentialsApi->clone_application_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->clone_application_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_application_key**
> JsonWebKey generate_application_key(app_id, validity_years=validity_years)

Generate a Key Credential

Generates a new X.509 certificate for an application key credential

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    validity_years = 56 # int |  (optional)

    try:
        # Generate a Key Credential
        api_response = api_instance.generate_application_key(app_id, validity_years=validity_years)
        print("The response of ApplicationCredentialsApi->generate_application_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->generate_application_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **validity_years** | **int**|  | [optional] 

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

# **generate_csr_for_application**
> Csr generate_csr_for_application(app_id, metadata)

Generate a Certificate Signing Request

Generates a new key pair and returns the Certificate Signing Request for it

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    metadata = okta.CsrMetadata() # CsrMetadata | 

    try:
        # Generate a Certificate Signing Request
        api_response = api_instance.generate_csr_for_application(app_id, metadata)
        print("The response of ApplicationCredentialsApi->generate_csr_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->generate_csr_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
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

# **get_application_key**
> JsonWebKey get_application_key(app_id, key_id)

Retrieve a Key Credential

Retrieves a specific application key credential by kid

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    key_id = 'sjP9eiETijYz110VkhHN' # str | ID of the Key Credential for the application

    try:
        # Retrieve a Key Credential
        api_response = api_instance.get_application_key(app_id, key_id)
        print("The response of ApplicationCredentialsApi->get_application_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->get_application_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
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

Retrieve a Certificate Signing Request

Retrieves a certificate signing request for the app by `id`

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    csr_id = 'fd7x1h7uTcZFx22rU1f7' # str | `id` of the CSR

    try:
        # Retrieve a Certificate Signing Request
        api_response = api_instance.get_csr_for_application(app_id, csr_id)
        print("The response of ApplicationCredentialsApi->get_csr_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->get_csr_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **csr_id** | **str**| &#x60;id&#x60; of the CSR | 

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

# **list_application_keys**
> List[JsonWebKey] list_application_keys(app_id)

List all Key Credentials

Lists all key credentials for an application

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # List all Key Credentials
        api_response = api_instance.list_application_keys(app_id)
        print("The response of ApplicationCredentialsApi->list_application_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->list_application_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

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

List all Certificate Signing Requests

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # List all Certificate Signing Requests
        api_response = api_instance.list_csrs_for_application(app_id)
        print("The response of ApplicationCredentialsApi->list_csrs_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->list_csrs_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

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

Publish a Certificate Signing Request

Publishes a certificate signing request for the app with a signed X.509 certificate and adds it into the application key credentials

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    csr_id = 'fd7x1h7uTcZFx22rU1f7' # str | `id` of the CSR
    body = None # bytearray | 

    try:
        # Publish a Certificate Signing Request
        api_response = api_instance.publish_csr_from_application(app_id, csr_id, body)
        print("The response of ApplicationCredentialsApi->publish_csr_from_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->publish_csr_from_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
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

Revoke a Certificate Signing Request

Revokes a certificate signing request and deletes the key pair from the application

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
    api_instance = okta.ApplicationCredentialsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    csr_id = 'fd7x1h7uTcZFx22rU1f7' # str | `id` of the CSR

    try:
        # Revoke a Certificate Signing Request
        api_instance.revoke_csr_from_application(app_id, csr_id)
    except Exception as e:
        print("Exception when calling ApplicationCredentialsApi->revoke_csr_from_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
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

