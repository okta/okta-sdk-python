# okta.PrincipalRateLimitApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_principal_rate_limit_entity**](PrincipalRateLimitApi.md#create_principal_rate_limit_entity) | **POST** /api/v1/principal-rate-limits | Create a principal rate limit
[**get_principal_rate_limit_entity**](PrincipalRateLimitApi.md#get_principal_rate_limit_entity) | **GET** /api/v1/principal-rate-limits/{principalRateLimitId} | Retrieve a principal rate limit
[**list_principal_rate_limit_entities**](PrincipalRateLimitApi.md#list_principal_rate_limit_entities) | **GET** /api/v1/principal-rate-limits | List all principal rate limits
[**replace_principal_rate_limit_entity**](PrincipalRateLimitApi.md#replace_principal_rate_limit_entity) | **PUT** /api/v1/principal-rate-limits/{principalRateLimitId} | Replace a principal rate limit


# **create_principal_rate_limit_entity**
> PrincipalRateLimitEntity create_principal_rate_limit_entity(entity)

Create a principal rate limit

Creates a new principal rate limit entity. Okta only allows one principal rate limit entity per org and principal.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.principal_rate_limit_entity import PrincipalRateLimitEntity
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
    api_instance = okta.PrincipalRateLimitApi(api_client)
    entity = okta.PrincipalRateLimitEntity() # PrincipalRateLimitEntity | 

    try:
        # Create a principal rate limit
        api_response = api_instance.create_principal_rate_limit_entity(entity)
        print("The response of PrincipalRateLimitApi->create_principal_rate_limit_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->create_principal_rate_limit_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | [**PrincipalRateLimitEntity**](PrincipalRateLimitEntity.md)|  | 

### Return type

[**PrincipalRateLimitEntity**](PrincipalRateLimitEntity.md)

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

# **get_principal_rate_limit_entity**
> PrincipalRateLimitEntity get_principal_rate_limit_entity(principal_rate_limit_id)

Retrieve a principal rate limit

Retrieves a principal rate limit entity by `principalRateLimitId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.principal_rate_limit_entity import PrincipalRateLimitEntity
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
    api_instance = okta.PrincipalRateLimitApi(api_client)
    principal_rate_limit_id = '0oacamvryxiyMqgiY1d7' # str | ID of the principal rate limit

    try:
        # Retrieve a principal rate limit
        api_response = api_instance.get_principal_rate_limit_entity(principal_rate_limit_id)
        print("The response of PrincipalRateLimitApi->get_principal_rate_limit_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->get_principal_rate_limit_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_rate_limit_id** | **str**| ID of the principal rate limit | 

### Return type

[**PrincipalRateLimitEntity**](PrincipalRateLimitEntity.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_principal_rate_limit_entities**
> List[PrincipalRateLimitEntity] list_principal_rate_limit_entities(filter, after=after, limit=limit)

List all principal rate limits

Lists all Principal Rate Limit entities considering the provided parameters

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.principal_rate_limit_entity import PrincipalRateLimitEntity
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
    api_instance = okta.PrincipalRateLimitApi(api_client)
    filter = 'filter_example' # str | Filters the list of principal rate limit entities by the provided principal type (`principalType`). For example, `filter=principalType eq \"SSWS_TOKEN\"` or `filter=principalType eq \"OAUTH_CLIENT\"`.
    after = 'after_example' # str | The cursor to use for pagination. It's an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination). (optional)
    limit = 20 # int | Specifies the number of items to return in a single response page. (optional) (default to 20)

    try:
        # List all principal rate limits
        api_response = api_instance.list_principal_rate_limit_entities(filter, after=after, limit=limit)
        print("The response of PrincipalRateLimitApi->list_principal_rate_limit_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->list_principal_rate_limit_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the list of principal rate limit entities by the provided principal type (&#x60;principalType&#x60;). For example, &#x60;filter&#x3D;principalType eq \&quot;SSWS_TOKEN\&quot;&#x60; or &#x60;filter&#x3D;principalType eq \&quot;OAUTH_CLIENT\&quot;&#x60;. | 
 **after** | **str**| The cursor to use for pagination. It&#39;s an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination). | [optional] 
 **limit** | **int**| Specifies the number of items to return in a single response page. | [optional] [default to 20]

### Return type

[**List[PrincipalRateLimitEntity]**](PrincipalRateLimitEntity.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_principal_rate_limit_entity**
> PrincipalRateLimitEntity replace_principal_rate_limit_entity(principal_rate_limit_id, entity)

Replace a principal rate limit

Replaces a principal rate limit entity by `principalRateLimitId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.principal_rate_limit_entity import PrincipalRateLimitEntity
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
    api_instance = okta.PrincipalRateLimitApi(api_client)
    principal_rate_limit_id = '0oacamvryxiyMqgiY1d7' # str | ID of the principal rate limit
    entity = okta.PrincipalRateLimitEntity() # PrincipalRateLimitEntity | 

    try:
        # Replace a principal rate limit
        api_response = api_instance.replace_principal_rate_limit_entity(principal_rate_limit_id, entity)
        print("The response of PrincipalRateLimitApi->replace_principal_rate_limit_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->replace_principal_rate_limit_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_rate_limit_id** | **str**| ID of the principal rate limit | 
 **entity** | [**PrincipalRateLimitEntity**](PrincipalRateLimitEntity.md)|  | 

### Return type

[**PrincipalRateLimitEntity**](PrincipalRateLimitEntity.md)

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

