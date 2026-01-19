# okta.CustomDomainApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_domain**](CustomDomainApi.md#create_custom_domain) | **POST** /api/v1/domains | Create a custom domain
[**delete_custom_domain**](CustomDomainApi.md#delete_custom_domain) | **DELETE** /api/v1/domains/{domainId} | Delete a custom domain
[**get_custom_domain**](CustomDomainApi.md#get_custom_domain) | **GET** /api/v1/domains/{domainId} | Retrieve a custom domain
[**list_custom_domains**](CustomDomainApi.md#list_custom_domains) | **GET** /api/v1/domains | List all custom domains
[**replace_custom_domain**](CustomDomainApi.md#replace_custom_domain) | **PUT** /api/v1/domains/{domainId} | Replace a custom domain&#39;s brand
[**upsert_certificate**](CustomDomainApi.md#upsert_certificate) | **PUT** /api/v1/domains/{domainId}/certificate | Upsert the custom domain&#39;s certificate
[**verify_domain**](CustomDomainApi.md#verify_domain) | **POST** /api/v1/domains/{domainId}/verify | Verify a custom domain


# **create_custom_domain**
> DomainResponse create_custom_domain(domain)

Create a custom domain

Creates your custom domain

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.domain_request import DomainRequest
from okta.models.domain_response import DomainResponse
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
    api_instance = okta.CustomDomainApi(api_client)
    domain = okta.DomainRequest() # DomainRequest | 

    try:
        # Create a custom domain
        api_response = api_instance.create_custom_domain(domain)
        print("The response of CustomDomainApi->create_custom_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainApi->create_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**DomainRequest**](DomainRequest.md)|  | 

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **delete_custom_domain**
> delete_custom_domain(domain_id)

Delete a custom domain

Deletes a custom domain by `domainId`

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
    api_instance = okta.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain

    try:
        # Delete a custom domain
        api_instance.delete_custom_domain(domain_id)
    except Exception as e:
        print("Exception when calling CustomDomainApi->delete_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| &#x60;id&#x60; of the Domain | 

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

# **get_custom_domain**
> DomainResponse get_custom_domain(domain_id)

Retrieve a custom domain

Retrieves a custom domain by `domainId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.domain_response import DomainResponse
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
    api_instance = okta.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain

    try:
        # Retrieve a custom domain
        api_response = api_instance.get_custom_domain(domain_id)
        print("The response of CustomDomainApi->get_custom_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainApi->get_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| &#x60;id&#x60; of the Domain | 

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **list_custom_domains**
> DomainListResponse list_custom_domains()

List all custom domains

Lists all verified custom domains for the org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.domain_list_response import DomainListResponse
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
    api_instance = okta.CustomDomainApi(api_client)

    try:
        # List all custom domains
        api_response = api_instance.list_custom_domains()
        print("The response of CustomDomainApi->list_custom_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainApi->list_custom_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainListResponse**](DomainListResponse.md)

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

# **replace_custom_domain**
> DomainResponse replace_custom_domain(domain_id, update_domain)

Replace a custom domain's brand

Replaces a custom domain's brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.domain_response import DomainResponse
from okta.models.update_domain import UpdateDomain
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
    api_instance = okta.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain
    update_domain = okta.UpdateDomain() # UpdateDomain | 

    try:
        # Replace a custom domain's brand
        api_response = api_instance.replace_custom_domain(domain_id, update_domain)
        print("The response of CustomDomainApi->replace_custom_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainApi->replace_custom_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| &#x60;id&#x60; of the Domain | 
 **update_domain** | [**UpdateDomain**](UpdateDomain.md)|  | 

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **upsert_certificate**
> upsert_certificate(domain_id, certificate)

Upsert the custom domain's certificate

Upserts (creates or renews) the `MANUAL` certificate for the custom domain  > **Notes:** > * If the existing `certificateSourceType` is `OKTA_MANAGED`, this operation changes the source type to `MANUAL`. Okta no longer manages and renews certificates for this domain after you provide a user-managed certificate. > * Okta supports TLS certificates and private keys that are PEM-encoded and 2048, 3072, or 4096 bits. See the [Custom domain guide](https://developer.okta.com/docs/guides/custom-url-domain/main/) for more details.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.domain_certificate import DomainCertificate
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
    api_instance = okta.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain
    certificate = okta.DomainCertificate() # DomainCertificate | 

    try:
        # Upsert the custom domain's certificate
        api_instance.upsert_certificate(domain_id, certificate)
    except Exception as e:
        print("Exception when calling CustomDomainApi->upsert_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| &#x60;id&#x60; of the Domain | 
 **certificate** | [**DomainCertificate**](DomainCertificate.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_domain**
> DomainResponse verify_domain(domain_id)

Verify a custom domain

Verifies the custom domain and validity of DNS records by `domainId`. Verify your custom domain to confirm that you own or control the domain and that you have properly configured the required DNS records. Furthermore, if the `certificateSourceType` in the domain is `OKTA_MANAGED`, then an attempt is made to obtain and install a certificate. After a certificate is obtained and installed by Okta, Okta manages the certificate including certificate renewal.  Verify your custom domain after you've [created it](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/CustomDomain/#tag/CustomDomain/operation/createCustomDomain) and after you've added your TXT and CNAME records to your domain provider. Okta doesn't verify your domain automatically. You must use the API to verify your custom domain if you change your DNS records or if you encounter issues with domain validation.  > **Note:** DNS record changes can take time to propagate. If you recently updated your DNS records, you may need to wait before verifying your custom domain. If you encounter issues with domain verification, double-check your DNS records and ensure that they're correctly configured. See [Update your DNS TXT](https://developer.okta.com/docs/guides/custom-url-domain/main/#update-your-dns-txt) for more information about verifying your custom domain.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.domain_response import DomainResponse
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
    api_instance = okta.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain

    try:
        # Verify a custom domain
        api_response = api_instance.verify_domain(domain_id)
        print("The response of CustomDomainApi->verify_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomDomainApi->verify_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| &#x60;id&#x60; of the Domain | 

### Return type

[**DomainResponse**](DomainResponse.md)

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

