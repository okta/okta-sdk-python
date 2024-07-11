# openapi_client.CustomDomainApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_custom_domain**](CustomDomainApi.md#delete_custom_domain) | **DELETE** /api/v1/domains/{domainId} | Delete a Custom Domain
[**get_custom_domain**](CustomDomainApi.md#get_custom_domain) | **GET** /api/v1/domains/{domainId} | Retrieve a Custom Domain
[**list_custom_domains**](CustomDomainApi.md#list_custom_domains) | **GET** /api/v1/domains | List all Custom Domains
[**replace_custom_domain**](CustomDomainApi.md#replace_custom_domain) | **PUT** /api/v1/domains/{domainId} | Replace a Custom Domain&#39;s Brand
[**upsert_certificate**](CustomDomainApi.md#upsert_certificate) | **PUT** /api/v1/domains/{domainId}/certificate | Upsert the Custom Domain&#39;s Certificate
[**verify_domain**](CustomDomainApi.md#verify_domain) | **POST** /api/v1/domains/{domainId}/verify | Verify a Custom Domain


# **delete_custom_domain**
> delete_custom_domain(domain_id)

Delete a Custom Domain

Deletes a custom domain by `domainId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain

    try:
        # Delete a Custom Domain
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

Retrieve a Custom Domain

Retrieves a custom domain by `domainId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.domain_response import DomainResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain

    try:
        # Retrieve a Custom Domain
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

List all Custom Domains

Lists all verified custom domains for the org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.domain_list_response import DomainListResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomDomainApi(api_client)

    try:
        # List all Custom Domains
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

Replace a Custom Domain's Brand

Replaces a custom domain's brand

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.domain_response import DomainResponse
from openapi_client.models.update_domain import UpdateDomain
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain
    update_domain = openapi_client.UpdateDomain() # UpdateDomain | 

    try:
        # Replace a Custom Domain's Brand
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

Upsert the Custom Domain's Certificate

Upserts (creates or renews) the `MANUAL` certificate for the custom domain. If the `certificateSourceType` in the domain is `OKTA_MANAGED`, it becomes `MANUAL` and Okta no longer manages and renews certificates for this domain since a user-managed certificate has been provided.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.domain_certificate import DomainCertificate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain
    certificate = openapi_client.DomainCertificate() # DomainCertificate | 

    try:
        # Upsert the Custom Domain's Certificate
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

Verify a Custom Domain

Verifies the custom domain and validity of DNS records by `domainId`. Furthermore, if the `certificateSourceType` in the domain is `OKTA_MANAGED`, then an attempt is made to obtain and install a certificate. After a certificate is obtained and installed by Okta, Okta manages the certificate including certificate renewal.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.domain_response import DomainResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomDomainApi(api_client)
    domain_id = 'OmWNeywfTzElSLOBMZsL' # str | `id` of the Domain

    try:
        # Verify a Custom Domain
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

