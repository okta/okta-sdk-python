# okta.DeviceIntegrationsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_device_integration**](DeviceIntegrationsApi.md#activate_device_integration) | **POST** /api/v1/device-integrations/{deviceIntegrationId}/lifecycle/activate | Activate a device integration
[**deactivate_device_integration**](DeviceIntegrationsApi.md#deactivate_device_integration) | **POST** /api/v1/device-integrations/{deviceIntegrationId}/lifecycle/deactivate | Deactivate a device integration
[**get_device_integration**](DeviceIntegrationsApi.md#get_device_integration) | **GET** /api/v1/device-integrations/{deviceIntegrationId} | Retrieve a device integration
[**list_device_integrations**](DeviceIntegrationsApi.md#list_device_integrations) | **GET** /api/v1/device-integrations | List all device integrations


# **activate_device_integration**
> DeviceIntegrations activate_device_integration(device_integration_id)

Activate a device integration

Activates a device integration and populates the related configurations by `deviceIntegrationId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_integrations import DeviceIntegrations
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
    api_instance = okta.DeviceIntegrationsApi(api_client)
    device_integration_id = 'device_integration_id_example' # str | The ID of the device integration

    try:
        # Activate a device integration
        api_response = api_instance.activate_device_integration(device_integration_id)
        print("The response of DeviceIntegrationsApi->activate_device_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceIntegrationsApi->activate_device_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_integration_id** | **str**| The ID of the device integration | 

### Return type

[**DeviceIntegrations**](DeviceIntegrations.md)

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

# **deactivate_device_integration**
> DeviceIntegrations deactivate_device_integration(device_integration_id)

Deactivate a device integration

Deactivates a device integration by `deviceIntegrationId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_integrations import DeviceIntegrations
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
    api_instance = okta.DeviceIntegrationsApi(api_client)
    device_integration_id = 'device_integration_id_example' # str | The ID of the device integration

    try:
        # Deactivate a device integration
        api_response = api_instance.deactivate_device_integration(device_integration_id)
        print("The response of DeviceIntegrationsApi->deactivate_device_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceIntegrationsApi->deactivate_device_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_integration_id** | **str**| The ID of the device integration | 

### Return type

[**DeviceIntegrations**](DeviceIntegrations.md)

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

# **get_device_integration**
> DeviceIntegrations get_device_integration(device_integration_id)

Retrieve a device integration

Retrieves a device integration by `deviceIntegrationId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_integrations import DeviceIntegrations
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
    api_instance = okta.DeviceIntegrationsApi(api_client)
    device_integration_id = 'device_integration_id_example' # str | The ID of the device integration

    try:
        # Retrieve a device integration
        api_response = api_instance.get_device_integration(device_integration_id)
        print("The response of DeviceIntegrationsApi->get_device_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceIntegrationsApi->get_device_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_integration_id** | **str**| The ID of the device integration | 

### Return type

[**DeviceIntegrations**](DeviceIntegrations.md)

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

# **list_device_integrations**
> List[DeviceIntegrations] list_device_integrations()

List all device integrations

Lists all device integrations for your org. Examples include Device Posture Provider, Windows Security Center, Chrome Device Trust, OSQuery, and Android Device Trust.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_integrations import DeviceIntegrations
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
    api_instance = okta.DeviceIntegrationsApi(api_client)

    try:
        # List all device integrations
        api_response = api_instance.list_device_integrations()
        print("The response of DeviceIntegrationsApi->list_device_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceIntegrationsApi->list_device_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DeviceIntegrations]**](DeviceIntegrations.md)

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

