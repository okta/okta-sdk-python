# okta.AgentPoolsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_agent_pools_update**](AgentPoolsApi.md#activate_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId}/activate | Activate an agent pool update
[**create_agent_pools_update**](AgentPoolsApi.md#create_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates | Create an agent pool update
[**deactivate_agent_pools_update**](AgentPoolsApi.md#deactivate_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId}/deactivate | Deactivate an agent pool update
[**delete_agent_pools_update**](AgentPoolsApi.md#delete_agent_pools_update) | **DELETE** /api/v1/agentPools/{poolId}/updates/{updateId} | Delete an agent pool update
[**get_agent_pools_update_instance**](AgentPoolsApi.md#get_agent_pools_update_instance) | **GET** /api/v1/agentPools/{poolId}/updates/{updateId} | Retrieve an agent pool update by ID
[**get_agent_pools_update_settings**](AgentPoolsApi.md#get_agent_pools_update_settings) | **GET** /api/v1/agentPools/{poolId}/updates/settings | Retrieve an agent pool update&#39;s settings
[**list_agent_pools**](AgentPoolsApi.md#list_agent_pools) | **GET** /api/v1/agentPools | List all agent pools
[**list_agent_pools_updates**](AgentPoolsApi.md#list_agent_pools_updates) | **GET** /api/v1/agentPools/{poolId}/updates | List all agent pool updates
[**pause_agent_pools_update**](AgentPoolsApi.md#pause_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId}/pause | Pause an agent pool update
[**resume_agent_pools_update**](AgentPoolsApi.md#resume_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId}/resume | Resume an agent pool update
[**retry_agent_pools_update**](AgentPoolsApi.md#retry_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId}/retry | Retry an agent pool update
[**stop_agent_pools_update**](AgentPoolsApi.md#stop_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId}/stop | Stop an agent pool update
[**update_agent_pools_update**](AgentPoolsApi.md#update_agent_pools_update) | **POST** /api/v1/agentPools/{poolId}/updates/{updateId} | Update an agent pool update by ID
[**update_agent_pools_update_settings**](AgentPoolsApi.md#update_agent_pools_update_settings) | **POST** /api/v1/agentPools/{poolId}/updates/settings | Update an agent pool update settings


# **activate_agent_pools_update**
> AgentPoolUpdate activate_agent_pools_update(pool_id, update_id)

Activate an agent pool update

Activates a scheduled agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Activate an agent pool update
        api_response = api_instance.activate_agent_pools_update(pool_id, update_id)
        print("The response of AgentPoolsApi->activate_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->activate_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Activated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_pools_update**
> AgentPoolUpdate create_agent_pools_update(pool_id, agent_pool_update)

Create an agent pool update

Creates an agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    agent_pool_update = okta.AgentPoolUpdate() # AgentPoolUpdate | 

    try:
        # Create an agent pool update
        api_response = api_instance.create_agent_pools_update(pool_id, agent_pool_update)
        print("The response of AgentPoolsApi->create_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->create_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **agent_pool_update** | [**AgentPoolUpdate**](AgentPoolUpdate.md)|  | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

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

# **deactivate_agent_pools_update**
> AgentPoolUpdate deactivate_agent_pools_update(pool_id, update_id)

Deactivate an agent pool update

Deactivates scheduled agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Deactivate an agent pool update
        api_response = api_instance.deactivate_agent_pools_update(pool_id, update_id)
        print("The response of AgentPoolsApi->deactivate_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->deactivate_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deactivated |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_pools_update**
> delete_agent_pools_update(pool_id, update_id)

Delete an agent pool update

Deletes agent pool update

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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Delete an agent pool update
        api_instance.delete_agent_pools_update(pool_id, update_id)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->delete_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

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
**204** | Deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_pools_update_instance**
> AgentPoolUpdate get_agent_pools_update_instance(pool_id, update_id)

Retrieve an agent pool update by ID

Retrieves an agent pool update by its `updateId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Retrieve an agent pool update by ID
        api_response = api_instance.get_agent_pools_update_instance(pool_id, update_id)
        print("The response of AgentPoolsApi->get_agent_pools_update_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->get_agent_pools_update_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

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

# **get_agent_pools_update_settings**
> AgentPoolUpdateSetting get_agent_pools_update_settings(pool_id)

Retrieve an agent pool update's settings

Retrieves the current state of the agent pool update instance settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update_setting import AgentPoolUpdateSetting
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to

    try:
        # Retrieve an agent pool update's settings
        api_response = api_instance.get_agent_pools_update_settings(pool_id)
        print("The response of AgentPoolsApi->get_agent_pools_update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->get_agent_pools_update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 

### Return type

[**AgentPoolUpdateSetting**](AgentPoolUpdateSetting.md)

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

# **list_agent_pools**
> List[AgentPool] list_agent_pools(limit_per_pool_type=limit_per_pool_type, pool_type=pool_type, after=after)

List all agent pools

Lists all agent pools with pagination support

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool import AgentPool
from okta.models.agent_type import AgentType
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
    api_instance = okta.AgentPoolsApi(api_client)
    limit_per_pool_type = 5 # int | Maximum number of agent pools returned (optional) (default to 5)
    pool_type = okta.AgentType() # AgentType | Agent type to search for (optional)
    after = 'after_example' # str | The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the `Link` response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). (optional)

    try:
        # List all agent pools
        api_response = api_instance.list_agent_pools(limit_per_pool_type=limit_per_pool_type, pool_type=pool_type, after=after)
        print("The response of AgentPoolsApi->list_agent_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->list_agent_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_per_pool_type** | **int**| Maximum number of agent pools returned | [optional] [default to 5]
 **pool_type** | [**AgentType**](.md)| Agent type to search for | [optional] 
 **after** | **str**| The cursor to use for pagination. It is an opaque string that specifies your current location in the list and is obtained from the &#x60;Link&#x60; response header. See [Pagination](https://developer.okta.com/docs/api/#pagination) and [Link header](https://developer.okta.com/docs/api/#link-header). | [optional] 

### Return type

[**List[AgentPool]**](AgentPool.md)

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

# **list_agent_pools_updates**
> List[AgentPoolUpdate] list_agent_pools_updates(pool_id, scheduled=scheduled)

List all agent pool updates

Lists all agent pool updates

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    scheduled = True # bool | Return only scheduled or ad-hoc updates. If this parameter isn't provided, Okta returns the entire list of updates. (optional)

    try:
        # List all agent pool updates
        api_response = api_instance.list_agent_pools_updates(pool_id, scheduled=scheduled)
        print("The response of AgentPoolsApi->list_agent_pools_updates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->list_agent_pools_updates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **scheduled** | **bool**| Return only scheduled or ad-hoc updates. If this parameter isn&#39;t provided, Okta returns the entire list of updates. | [optional] 

### Return type

[**List[AgentPoolUpdate]**](AgentPoolUpdate.md)

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

# **pause_agent_pools_update**
> AgentPoolUpdate pause_agent_pools_update(pool_id, update_id)

Pause an agent pool update

Pauses a running or queued agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Pause an agent pool update
        api_response = api_instance.pause_agent_pools_update(pool_id, update_id)
        print("The response of AgentPoolsApi->pause_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->pause_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Paused |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_agent_pools_update**
> AgentPoolUpdate resume_agent_pools_update(pool_id, update_id)

Resume an agent pool update

Resumes a running or queued agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Resume an agent pool update
        api_response = api_instance.resume_agent_pools_update(pool_id, update_id)
        print("The response of AgentPoolsApi->resume_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->resume_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resumed |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_agent_pools_update**
> AgentPoolUpdate retry_agent_pools_update(pool_id, update_id)

Retry an agent pool update

Retries an agent pool update if the update is unsuccessful or communication with Okta was interrupted during an agent auto-update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Retry an agent pool update
        api_response = api_instance.retry_agent_pools_update(pool_id, update_id)
        print("The response of AgentPoolsApi->retry_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->retry_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Retried |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_agent_pools_update**
> AgentPoolUpdate stop_agent_pools_update(pool_id, update_id)

Stop an agent pool update

Stops an agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update

    try:
        # Stop an agent pool update
        api_response = api_instance.stop_agent_pools_update(pool_id, update_id)
        print("The response of AgentPoolsApi->stop_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->stop_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Stopped |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_pools_update**
> AgentPoolUpdate update_agent_pools_update(pool_id, update_id, agent_pool_update)

Update an agent pool update by ID

Updates an agent pool update instance and returns the latest agent pool update

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update import AgentPoolUpdate
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    update_id = 'update_id_example' # str | ID of the update
    agent_pool_update = okta.AgentPoolUpdate() # AgentPoolUpdate | 

    try:
        # Update an agent pool update by ID
        api_response = api_instance.update_agent_pools_update(pool_id, update_id, agent_pool_update)
        print("The response of AgentPoolsApi->update_agent_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->update_agent_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **update_id** | **str**| ID of the update | 
 **agent_pool_update** | [**AgentPoolUpdate**](AgentPoolUpdate.md)|  | 

### Return type

[**AgentPoolUpdate**](AgentPoolUpdate.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_pools_update_settings**
> AgentPoolUpdateSetting update_agent_pools_update_settings(pool_id, agent_pool_update_setting)

Update an agent pool update settings

Updates an agent pool update instance settings

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.agent_pool_update_setting import AgentPoolUpdateSetting
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
    api_instance = okta.AgentPoolsApi(api_client)
    pool_id = 'pool_id_example' # str | ID of the agent pool for which the settings apply to
    agent_pool_update_setting = okta.AgentPoolUpdateSetting() # AgentPoolUpdateSetting | 

    try:
        # Update an agent pool update settings
        api_response = api_instance.update_agent_pools_update_settings(pool_id, agent_pool_update_setting)
        print("The response of AgentPoolsApi->update_agent_pools_update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentPoolsApi->update_agent_pools_update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| ID of the agent pool for which the settings apply to | 
 **agent_pool_update_setting** | [**AgentPoolUpdateSetting**](AgentPoolUpdateSetting.md)|  | 

### Return type

[**AgentPoolUpdateSetting**](AgentPoolUpdateSetting.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

