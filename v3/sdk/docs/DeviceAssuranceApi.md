# okta.DeviceAssuranceApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_assurance_policy**](DeviceAssuranceApi.md#create_device_assurance_policy) | **POST** /api/v1/device-assurances | Create a Device Assurance Policy
[**delete_device_assurance_policy**](DeviceAssuranceApi.md#delete_device_assurance_policy) | **DELETE** /api/v1/device-assurances/{deviceAssuranceId} | Delete a Device Assurance Policy
[**get_device_assurance_policy**](DeviceAssuranceApi.md#get_device_assurance_policy) | **GET** /api/v1/device-assurances/{deviceAssuranceId} | Retrieve a Device Assurance Policy
[**list_device_assurance_policies**](DeviceAssuranceApi.md#list_device_assurance_policies) | **GET** /api/v1/device-assurances | List all Device Assurance Policies
[**replace_device_assurance_policy**](DeviceAssuranceApi.md#replace_device_assurance_policy) | **PUT** /api/v1/device-assurances/{deviceAssuranceId} | Replace a Device Assurance Policy


# **create_device_assurance_policy**
> DeviceAssurance create_device_assurance_policy(device_assurance)

Create a Device Assurance Policy

Creates a new Device Assurance Policy

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_assurance import DeviceAssurance
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
    api_instance = okta.DeviceAssuranceApi(api_client)
    device_assurance = okta.DeviceAssurance() # DeviceAssurance | 

    try:
        # Create a Device Assurance Policy
        api_response = api_instance.create_device_assurance_policy(device_assurance)
        print("The response of DeviceAssuranceApi->create_device_assurance_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceAssuranceApi->create_device_assurance_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_assurance** | [**DeviceAssurance**](DeviceAssurance.md)|  | 

### Return type

[**DeviceAssurance**](DeviceAssurance.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_assurance_policy**
> delete_device_assurance_policy(device_assurance_id)

Delete a Device Assurance Policy

Deletes a Device Assurance Policy by `deviceAssuranceId`. If the Device Assurance Policy is currently being used in the org Authentication Policies, the delete will not be allowed.

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
    api_instance = okta.DeviceAssuranceApi(api_client)
    device_assurance_id = 'device_assurance_id_example' # str | Id of the Device Assurance Policy

    try:
        # Delete a Device Assurance Policy
        api_instance.delete_device_assurance_policy(device_assurance_id)
    except Exception as e:
        print("Exception when calling DeviceAssuranceApi->delete_device_assurance_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_assurance_id** | **str**| Id of the Device Assurance Policy | 

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
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_assurance_policy**
> DeviceAssurance get_device_assurance_policy(device_assurance_id)

Retrieve a Device Assurance Policy

Retrieves a Device Assurance Policy by `deviceAssuranceId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_assurance import DeviceAssurance
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
    api_instance = okta.DeviceAssuranceApi(api_client)
    device_assurance_id = 'device_assurance_id_example' # str | Id of the Device Assurance Policy

    try:
        # Retrieve a Device Assurance Policy
        api_response = api_instance.get_device_assurance_policy(device_assurance_id)
        print("The response of DeviceAssuranceApi->get_device_assurance_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceAssuranceApi->get_device_assurance_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_assurance_id** | **str**| Id of the Device Assurance Policy | 

### Return type

[**DeviceAssurance**](DeviceAssurance.md)

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

# **list_device_assurance_policies**
> List[DeviceAssurance] list_device_assurance_policies()

List all Device Assurance Policies

Lists all device assurance policies

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_assurance import DeviceAssurance
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
    api_instance = okta.DeviceAssuranceApi(api_client)

    try:
        # List all Device Assurance Policies
        api_response = api_instance.list_device_assurance_policies()
        print("The response of DeviceAssuranceApi->list_device_assurance_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceAssuranceApi->list_device_assurance_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DeviceAssurance]**](DeviceAssurance.md)

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

# **replace_device_assurance_policy**
> DeviceAssurance replace_device_assurance_policy(device_assurance_id, device_assurance)

Replace a Device Assurance Policy

Replaces a Device Assurance Policy by `deviceAssuranceId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_assurance import DeviceAssurance
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
    api_instance = okta.DeviceAssuranceApi(api_client)
    device_assurance_id = 'device_assurance_id_example' # str | Id of the Device Assurance Policy
    device_assurance = okta.DeviceAssurance() # DeviceAssurance | 

    try:
        # Replace a Device Assurance Policy
        api_response = api_instance.replace_device_assurance_policy(device_assurance_id, device_assurance)
        print("The response of DeviceAssuranceApi->replace_device_assurance_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceAssuranceApi->replace_device_assurance_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_assurance_id** | **str**| Id of the Device Assurance Policy | 
 **device_assurance** | [**DeviceAssurance**](DeviceAssurance.md)|  | 

### Return type

[**DeviceAssurance**](DeviceAssurance.md)

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

