# okta.ApiServiceIntegrationsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_api_service_integration_instance_secret**](ApiServiceIntegrationsApi.md#activate_api_service_integration_instance_secret) | **POST** /integrations/api/v1/api-services/{apiServiceId}/credentials/secrets/{secretId}/lifecycle/activate | Activate an API service integration instance secret
[**create_api_service_integration_instance**](ApiServiceIntegrationsApi.md#create_api_service_integration_instance) | **POST** /integrations/api/v1/api-services | Create an API service integration instance
[**create_api_service_integration_instance_secret**](ApiServiceIntegrationsApi.md#create_api_service_integration_instance_secret) | **POST** /integrations/api/v1/api-services/{apiServiceId}/credentials/secrets | Create an API service integration instance secret
[**deactivate_api_service_integration_instance_secret**](ApiServiceIntegrationsApi.md#deactivate_api_service_integration_instance_secret) | **POST** /integrations/api/v1/api-services/{apiServiceId}/credentials/secrets/{secretId}/lifecycle/deactivate | Deactivate an API service integration instance secret
[**delete_api_service_integration_instance**](ApiServiceIntegrationsApi.md#delete_api_service_integration_instance) | **DELETE** /integrations/api/v1/api-services/{apiServiceId} | Delete an API service integration instance
[**delete_api_service_integration_instance_secret**](ApiServiceIntegrationsApi.md#delete_api_service_integration_instance_secret) | **DELETE** /integrations/api/v1/api-services/{apiServiceId}/credentials/secrets/{secretId} | Delete an API service integration instance secret
[**get_api_service_integration_instance**](ApiServiceIntegrationsApi.md#get_api_service_integration_instance) | **GET** /integrations/api/v1/api-services/{apiServiceId} | Retrieve an API service integration instance
[**list_api_service_integration_instance_secrets**](ApiServiceIntegrationsApi.md#list_api_service_integration_instance_secrets) | **GET** /integrations/api/v1/api-services/{apiServiceId}/credentials/secrets | List all API service integration instance secrets
[**list_api_service_integration_instances**](ApiServiceIntegrationsApi.md#list_api_service_integration_instances) | **GET** /integrations/api/v1/api-services | List all API service integration instances


# **activate_api_service_integration_instance_secret**
> APIServiceIntegrationInstanceSecret activate_api_service_integration_instance_secret(api_service_id, secret_id)

Activate an API service integration instance secret

Activates an API Service Integration instance Secret by `secretId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.api_service_integration_instance_secret import APIServiceIntegrationInstanceSecret
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | `id` of the API Service Integration instance Secret

    try:
        # Activate an API service integration instance secret
        api_response = api_instance.activate_api_service_integration_instance_secret(api_service_id, secret_id)
        print("The response of ApiServiceIntegrationsApi->activate_api_service_integration_instance_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->activate_api_service_integration_instance_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 
 **secret_id** | **str**| &#x60;id&#x60; of the API Service Integration instance Secret | 

### Return type

[**APIServiceIntegrationInstanceSecret**](APIServiceIntegrationInstanceSecret.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_service_integration_instance**
> PostAPIServiceIntegrationInstance create_api_service_integration_instance(post_api_service_integration_instance_request)

Create an API service integration instance

Creates and authorizes an API Service Integration instance

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.post_api_service_integration_instance import PostAPIServiceIntegrationInstance
from okta.models.post_api_service_integration_instance_request import PostAPIServiceIntegrationInstanceRequest
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    post_api_service_integration_instance_request = okta.PostAPIServiceIntegrationInstanceRequest() # PostAPIServiceIntegrationInstanceRequest | 

    try:
        # Create an API service integration instance
        api_response = api_instance.create_api_service_integration_instance(post_api_service_integration_instance_request)
        print("The response of ApiServiceIntegrationsApi->create_api_service_integration_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->create_api_service_integration_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_api_service_integration_instance_request** | [**PostAPIServiceIntegrationInstanceRequest**](PostAPIServiceIntegrationInstanceRequest.md)|  | 

### Return type

[**PostAPIServiceIntegrationInstance**](PostAPIServiceIntegrationInstance.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_api_service_integration_instance_secret**
> APIServiceIntegrationInstanceSecret create_api_service_integration_instance_secret(api_service_id)

Create an API service integration instance secret

Creates an API Service Integration instance Secret object with a new active client secret. You can create up to two Secret objects. An error is returned if you attempt to create more than two Secret objects.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.api_service_integration_instance_secret import APIServiceIntegrationInstanceSecret
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance

    try:
        # Create an API service integration instance secret
        api_response = api_instance.create_api_service_integration_instance_secret(api_service_id)
        print("The response of ApiServiceIntegrationsApi->create_api_service_integration_instance_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->create_api_service_integration_instance_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 

### Return type

[**APIServiceIntegrationInstanceSecret**](APIServiceIntegrationInstanceSecret.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_api_service_integration_instance_secret**
> APIServiceIntegrationInstanceSecret deactivate_api_service_integration_instance_secret(api_service_id, secret_id)

Deactivate an API service integration instance secret

Deactivates an API Service Integration instance Secret by `secretId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.api_service_integration_instance_secret import APIServiceIntegrationInstanceSecret
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | `id` of the API Service Integration instance Secret

    try:
        # Deactivate an API service integration instance secret
        api_response = api_instance.deactivate_api_service_integration_instance_secret(api_service_id, secret_id)
        print("The response of ApiServiceIntegrationsApi->deactivate_api_service_integration_instance_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->deactivate_api_service_integration_instance_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 
 **secret_id** | **str**| &#x60;id&#x60; of the API Service Integration instance Secret | 

### Return type

[**APIServiceIntegrationInstanceSecret**](APIServiceIntegrationInstanceSecret.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_service_integration_instance**
> delete_api_service_integration_instance(api_service_id)

Delete an API service integration instance

Deletes an API Service Integration instance by `id`. This operation also revokes access to scopes that were previously granted to this API Service Integration instance.

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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance

    try:
        # Delete an API service integration instance
        api_instance.delete_api_service_integration_instance(api_service_id)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->delete_api_service_integration_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_service_integration_instance_secret**
> delete_api_service_integration_instance_secret(api_service_id, secret_id)

Delete an API service integration instance secret

Deletes an API Service Integration instance Secret by `secretId`. You can only delete an inactive Secret.

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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance
    secret_id = 'ocs2f4zrZbs8nUa7p0g4' # str | `id` of the API Service Integration instance Secret

    try:
        # Delete an API service integration instance secret
        api_instance.delete_api_service_integration_instance_secret(api_service_id, secret_id)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->delete_api_service_integration_instance_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 
 **secret_id** | **str**| &#x60;id&#x60; of the API Service Integration instance Secret | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_service_integration_instance**
> APIServiceIntegrationInstance get_api_service_integration_instance(api_service_id)

Retrieve an API service integration instance

Retrieves an API Service Integration instance by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.api_service_integration_instance import APIServiceIntegrationInstance
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance

    try:
        # Retrieve an API service integration instance
        api_response = api_instance.get_api_service_integration_instance(api_service_id)
        print("The response of ApiServiceIntegrationsApi->get_api_service_integration_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->get_api_service_integration_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 

### Return type

[**APIServiceIntegrationInstance**](APIServiceIntegrationInstance.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_service_integration_instance_secrets**
> List[APIServiceIntegrationInstanceSecret] list_api_service_integration_instance_secrets(api_service_id)

List all API service integration instance secrets

Lists all client secrets for an API Service Integration instance by `apiServiceId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.api_service_integration_instance_secret import APIServiceIntegrationInstanceSecret
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    api_service_id = '000lr2rLjZ6NsGn1P0g3' # str | `id` of the API Service Integration instance

    try:
        # List all API service integration instance secrets
        api_response = api_instance.list_api_service_integration_instance_secrets(api_service_id)
        print("The response of ApiServiceIntegrationsApi->list_api_service_integration_instance_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->list_api_service_integration_instance_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_service_id** | **str**| &#x60;id&#x60; of the API Service Integration instance | 

### Return type

[**List[APIServiceIntegrationInstanceSecret]**](APIServiceIntegrationInstanceSecret.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_service_integration_instances**
> List[APIServiceIntegrationInstance] list_api_service_integration_instances(after=after)

List all API service integration instances

Lists all API Service Integration instances with a pagination option

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.api_service_integration_instance import APIServiceIntegrationInstance
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
    api_instance = okta.ApiServiceIntegrationsApi(api_client)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)

    try:
        # List all API service integration instances
        api_response = api_instance.list_api_service_integration_instances(after=after)
        print("The response of ApiServiceIntegrationsApi->list_api_service_integration_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiServiceIntegrationsApi->list_api_service_integration_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 

### Return type

[**List[APIServiceIntegrationInstance]**](APIServiceIntegrationInstance.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

