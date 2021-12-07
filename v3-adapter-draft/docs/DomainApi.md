# swagger_client.DomainApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate**](DomainApi.md#create_certificate) | **PUT** /api/v1/domains/{domainId}/certificate | Create Certificate
[**create_domain**](DomainApi.md#create_domain) | **POST** /api/v1/domains | Create Domain
[**delete_domain**](DomainApi.md#delete_domain) | **DELETE** /api/v1/domains/{domainId} | Delete Domain
[**get_domain**](DomainApi.md#get_domain) | **GET** /api/v1/domains/{domainId} | Get Domain
[**list_domains**](DomainApi.md#list_domains) | **GET** /api/v1/domains | List Domains
[**verify_domain**](DomainApi.md#verify_domain) | **POST** /api/v1/domains/{domainId}/verify | Verify Domain

# **create_certificate**
> create_certificate(body, domain_id)

Create Certificate

Creates the Certificate for the Domain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainCertificate() # DomainCertificate | 
domain_id = 'domain_id_example' # str | 

try:
    # Create Certificate
    api_instance.create_certificate(body, domain_id)
except ApiException as e:
    print("Exception when calling DomainApi->create_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainCertificate**](DomainCertificate.md)|  | 
 **domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain**
> DomainResponse create_domain(body)

Create Domain

Creates your domain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
body = swagger_client.Domain() # Domain | 

try:
    # Create Domain
    api_response = api_instance.create_domain(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Domain**](Domain.md)|  | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> delete_domain(domain_id)

Delete Domain

Deletes a Domain by `id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 

try:
    # Delete Domain
    api_instance.delete_domain(domain_id)
except ApiException as e:
    print("Exception when calling DomainApi->delete_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> DomainResponse get_domain(domain_id)

Get Domain

Fetches a Domain by `id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 

try:
    # Get Domain
    api_response = api_instance.get_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> DomainListResponse list_domains()

List Domains

List all verified custom Domains for the org.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))

try:
    # List Domains
    api_response = api_instance.list_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->list_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DomainListResponse**](DomainListResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_domain**
> DomainResponse verify_domain(domain_id)

Verify Domain

Verifies the Domain by `id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DomainApi(swagger_client.ApiClient(configuration))
domain_id = 'domain_id_example' # str | 

try:
    # Verify Domain
    api_response = api_instance.verify_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->verify_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

