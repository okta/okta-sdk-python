# okta.EmailDomainApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_domain**](EmailDomainApi.md#create_email_domain) | **POST** /api/v1/email-domains | Create an email domain
[**delete_email_domain**](EmailDomainApi.md#delete_email_domain) | **DELETE** /api/v1/email-domains/{emailDomainId} | Delete an email domain
[**get_email_domain**](EmailDomainApi.md#get_email_domain) | **GET** /api/v1/email-domains/{emailDomainId} | Retrieve an email domain
[**list_email_domains**](EmailDomainApi.md#list_email_domains) | **GET** /api/v1/email-domains | List all email domains
[**replace_email_domain**](EmailDomainApi.md#replace_email_domain) | **PUT** /api/v1/email-domains/{emailDomainId} | Replace an email domain
[**verify_email_domain**](EmailDomainApi.md#verify_email_domain) | **POST** /api/v1/email-domains/{emailDomainId}/verify | Verify an email domain


# **create_email_domain**
> EmailDomainResponse create_email_domain(email_domain, expand=expand)

Create an email domain

Creates an Email Domain in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_domain import EmailDomain
from okta.models.email_domain_response import EmailDomainResponse
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
    api_instance = okta.EmailDomainApi(api_client)
    email_domain = okta.EmailDomain() # EmailDomain | 
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Create an email domain
        api_response = api_instance.create_email_domain(email_domain, expand=expand)
        print("The response of EmailDomainApi->create_email_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailDomainApi->create_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_domain** | [**EmailDomain**](EmailDomain.md)|  | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**EmailDomainResponse**](EmailDomainResponse.md)

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_domain**
> delete_email_domain(email_domain_id, expand=expand)

Delete an email domain

Deletes an Email Domain by `emailDomainId`

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
    api_instance = okta.EmailDomainApi(api_client)
    email_domain_id = 'email_domain_id_example' # str | 
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Delete an email domain
        api_instance.delete_email_domain(email_domain_id, expand=expand)
    except Exception as e:
        print("Exception when calling EmailDomainApi->delete_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_domain_id** | **str**|  | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

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
**400** | Unable to delete custom email domain due to mail provider specific restrictions |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_domain**
> EmailDomainResponseWithEmbedded get_email_domain(email_domain_id, expand=expand)

Retrieve an email domain

Retrieves an Email Domain by `emailDomainId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_domain_response_with_embedded import EmailDomainResponseWithEmbedded
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
    api_instance = okta.EmailDomainApi(api_client)
    email_domain_id = 'email_domain_id_example' # str | 
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Retrieve an email domain
        api_response = api_instance.get_email_domain(email_domain_id, expand=expand)
        print("The response of EmailDomainApi->get_email_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailDomainApi->get_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_domain_id** | **str**|  | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**EmailDomainResponseWithEmbedded**](EmailDomainResponseWithEmbedded.md)

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

# **list_email_domains**
> List[EmailDomainResponseWithEmbedded] list_email_domains(expand=expand)

List all email domains

Lists all the Email Domains in your org

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_domain_response_with_embedded import EmailDomainResponseWithEmbedded
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
    api_instance = okta.EmailDomainApi(api_client)
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # List all email domains
        api_response = api_instance.list_email_domains(expand=expand)
        print("The response of EmailDomainApi->list_email_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailDomainApi->list_email_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**List[EmailDomainResponseWithEmbedded]**](EmailDomainResponseWithEmbedded.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_email_domain**
> EmailDomainResponse replace_email_domain(email_domain_id, update_email_domain, expand=expand)

Replace an email domain

Replaces associated username and sender display name by `emailDomainId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_domain_response import EmailDomainResponse
from okta.models.update_email_domain import UpdateEmailDomain
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
    api_instance = okta.EmailDomainApi(api_client)
    email_domain_id = 'email_domain_id_example' # str | 
    update_email_domain = okta.UpdateEmailDomain() # UpdateEmailDomain | 
    expand = ['expand_example'] # List[str] | Specifies additional metadata to be included in the response (optional)

    try:
        # Replace an email domain
        api_response = api_instance.replace_email_domain(email_domain_id, update_email_domain, expand=expand)
        print("The response of EmailDomainApi->replace_email_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailDomainApi->replace_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_domain_id** | **str**|  | 
 **update_email_domain** | [**UpdateEmailDomain**](UpdateEmailDomain.md)|  | 
 **expand** | [**List[str]**](str.md)| Specifies additional metadata to be included in the response | [optional] 

### Return type

[**EmailDomainResponse**](EmailDomainResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_domain**
> EmailDomainResponse verify_email_domain(email_domain_id)

Verify an email domain

Verifies an Email Domain by `emailDomainId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.email_domain_response import EmailDomainResponse
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
    api_instance = okta.EmailDomainApi(api_client)
    email_domain_id = 'email_domain_id_example' # str | 

    try:
        # Verify an email domain
        api_response = api_instance.verify_email_domain(email_domain_id)
        print("The response of EmailDomainApi->verify_email_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailDomainApi->verify_email_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_domain_id** | **str**|  | 

### Return type

[**EmailDomainResponse**](EmailDomainResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Email domain could not be verified by mail provider |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

