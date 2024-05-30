# openapi_client.ApplicationConnectionsApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#activate_default_provisioning_connection_for_application) | **POST** /api/v1/apps/{appId}/connections/default/lifecycle/activate | Activate the default Provisioning Connection
[**deactivate_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#deactivate_default_provisioning_connection_for_application) | **POST** /api/v1/apps/{appId}/connections/default/lifecycle/deactivate | Deactivate the default Provisioning Connection
[**get_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#get_default_provisioning_connection_for_application) | **GET** /api/v1/apps/{appId}/connections/default | Retrieve the default Provisioning Connection
[**update_default_provisioning_connection_for_application**](ApplicationConnectionsApi.md#update_default_provisioning_connection_for_application) | **POST** /api/v1/apps/{appId}/connections/default | Update the default Provisioning Connection


# **activate_default_provisioning_connection_for_application**
> activate_default_provisioning_connection_for_application(app_id)

Activate the default Provisioning Connection

Activates the default Provisioning Connection for an app

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
    api_instance = openapi_client.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Activate the default Provisioning Connection
        api_instance.activate_default_provisioning_connection_for_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->activate_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

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

# **deactivate_default_provisioning_connection_for_application**
> deactivate_default_provisioning_connection_for_application(app_id)

Deactivate the default Provisioning Connection

Deactivates the default Provisioning Connection for an app

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
    api_instance = openapi_client.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Deactivate the default Provisioning Connection
        api_instance.deactivate_default_provisioning_connection_for_application(app_id)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->deactivate_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

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

# **get_default_provisioning_connection_for_application**
> ProvisioningConnection get_default_provisioning_connection_for_application(app_id)

Retrieve the default Provisioning Connection

Retrieves the default Provisioning Connection for an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.provisioning_connection import ProvisioningConnection
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
    api_instance = openapi_client.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application

    try:
        # Retrieve the default Provisioning Connection
        api_response = api_instance.get_default_provisioning_connection_for_application(app_id)
        print("The response of ApplicationConnectionsApi->get_default_provisioning_connection_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->get_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 

### Return type

[**ProvisioningConnection**](ProvisioningConnection.md)

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

# **update_default_provisioning_connection_for_application**
> ProvisioningConnection update_default_provisioning_connection_for_application(app_id, provisioning_connection_request, activate=activate)

Update the default Provisioning Connection

Updates the default Provisioning Connection for an app

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.provisioning_connection import ProvisioningConnection
from openapi_client.models.provisioning_connection_request import ProvisioningConnectionRequest
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
    api_instance = openapi_client.ApplicationConnectionsApi(api_client)
    app_id = '0oafxqCAJWWGELFTYASJ' # str | ID of the Application
    provisioning_connection_request = openapi_client.ProvisioningConnectionRequest() # ProvisioningConnectionRequest | 
    activate = True # bool | Activates the Provisioning Connection (optional)

    try:
        # Update the default Provisioning Connection
        api_response = api_instance.update_default_provisioning_connection_for_application(app_id, provisioning_connection_request, activate=activate)
        print("The response of ApplicationConnectionsApi->update_default_provisioning_connection_for_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationConnectionsApi->update_default_provisioning_connection_for_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the Application | 
 **provisioning_connection_request** | [**ProvisioningConnectionRequest**](ProvisioningConnectionRequest.md)|  | 
 **activate** | **bool**| Activates the Provisioning Connection | [optional] 

### Return type

[**ProvisioningConnection**](ProvisioningConnection.md)

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

