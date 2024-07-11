# okta.PrincipalRateLimitApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_principal_rate_limit_entity**](PrincipalRateLimitApi.md#create_principal_rate_limit_entity) | **POST** /api/v1/principal-rate-limits | Create a Principal Rate Limit
[**get_principal_rate_limit_entity**](PrincipalRateLimitApi.md#get_principal_rate_limit_entity) | **GET** /api/v1/principal-rate-limits/{principalRateLimitId} | Retrieve a Principal Rate Limit
[**list_principal_rate_limit_entities**](PrincipalRateLimitApi.md#list_principal_rate_limit_entities) | **GET** /api/v1/principal-rate-limits | List all Principal Rate Limits
[**replace_principal_rate_limit_entity**](PrincipalRateLimitApi.md#replace_principal_rate_limit_entity) | **PUT** /api/v1/principal-rate-limits/{principalRateLimitId} | Replace a Principal Rate Limit


# **create_principal_rate_limit_entity**
> PrincipalRateLimitEntity create_principal_rate_limit_entity(entity)

Create a Principal Rate Limit

Creates a new Principal Rate Limit entity. In the current release, we only allow one Principal Rate Limit entity per org and principal.

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
        # Create a Principal Rate Limit
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

Retrieve a Principal Rate Limit

Retrieves a Principal Rate Limit entity by `principalRateLimitId`

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
    principal_rate_limit_id = 'abcd1234' # str | id of the Principal Rate Limit

    try:
        # Retrieve a Principal Rate Limit
        api_response = api_instance.get_principal_rate_limit_entity(principal_rate_limit_id)
        print("The response of PrincipalRateLimitApi->get_principal_rate_limit_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->get_principal_rate_limit_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_rate_limit_id** | **str**| id of the Principal Rate Limit | 

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
> List[PrincipalRateLimitEntity] list_principal_rate_limit_entities(filter=filter, after=after, limit=limit)

List all Principal Rate Limits

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
    filter = 'filter_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List all Principal Rate Limits
        api_response = api_instance.list_principal_rate_limit_entities(filter=filter, after=after, limit=limit)
        print("The response of PrincipalRateLimitApi->list_principal_rate_limit_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->list_principal_rate_limit_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

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

Replace a Principal Rate Limit

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
    principal_rate_limit_id = 'abcd1234' # str | id of the Principal Rate Limit
    entity = okta.PrincipalRateLimitEntity() # PrincipalRateLimitEntity | 

    try:
        # Replace a Principal Rate Limit
        api_response = api_instance.replace_principal_rate_limit_entity(principal_rate_limit_id, entity)
        print("The response of PrincipalRateLimitApi->replace_principal_rate_limit_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrincipalRateLimitApi->replace_principal_rate_limit_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **principal_rate_limit_id** | **str**| id of the Principal Rate Limit | 
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

