# okta.DevicePostureCheckApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_posture_check**](DevicePostureCheckApi.md#create_device_posture_check) | **POST** /api/v1/device-posture-checks | Create a device posture check
[**delete_device_posture_check**](DevicePostureCheckApi.md#delete_device_posture_check) | **DELETE** /api/v1/device-posture-checks/{postureCheckId} | Delete a device posture check
[**get_device_posture_check**](DevicePostureCheckApi.md#get_device_posture_check) | **GET** /api/v1/device-posture-checks/{postureCheckId} | Retrieve a device posture check
[**list_default_device_posture_checks**](DevicePostureCheckApi.md#list_default_device_posture_checks) | **GET** /api/v1/device-posture-checks/default | List all default device posture checks
[**list_device_posture_checks**](DevicePostureCheckApi.md#list_device_posture_checks) | **GET** /api/v1/device-posture-checks | List all device posture checks
[**replace_device_posture_check**](DevicePostureCheckApi.md#replace_device_posture_check) | **PUT** /api/v1/device-posture-checks/{postureCheckId} | Replace a device posture check


# **create_device_posture_check**
> DevicePostureCheck create_device_posture_check(device_posture_check)

Create a device posture check

Creates a device posture check

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_posture_check import DevicePostureCheck
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
    api_instance = okta.DevicePostureCheckApi(api_client)
    device_posture_check = okta.DevicePostureCheck() # DevicePostureCheck | 

    try:
        # Create a device posture check
        api_response = api_instance.create_device_posture_check(device_posture_check)
        print("The response of DevicePostureCheckApi->create_device_posture_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureCheckApi->create_device_posture_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_posture_check** | [**DevicePostureCheck**](DevicePostureCheck.md)|  | 

### Return type

[**DevicePostureCheck**](DevicePostureCheck.md)

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

# **delete_device_posture_check**
> delete_device_posture_check(posture_check_id)

Delete a device posture check

Deletes a device posture check by `postureCheckId`. You can't delete the device posture check if it's used in a device assurance policy.

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
    api_instance = okta.DevicePostureCheckApi(api_client)
    posture_check_id = 'posture_check_id_example' # str | ID of the device posture check

    try:
        # Delete a device posture check
        api_instance.delete_device_posture_check(posture_check_id)
    except Exception as e:
        print("Exception when calling DevicePostureCheckApi->delete_device_posture_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_check_id** | **str**| ID of the device posture check | 

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

# **get_device_posture_check**
> DevicePostureCheck get_device_posture_check(posture_check_id)

Retrieve a device posture check

Retrieves a device posture check by `postureCheckId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_posture_check import DevicePostureCheck
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
    api_instance = okta.DevicePostureCheckApi(api_client)
    posture_check_id = 'posture_check_id_example' # str | ID of the device posture check

    try:
        # Retrieve a device posture check
        api_response = api_instance.get_device_posture_check(posture_check_id)
        print("The response of DevicePostureCheckApi->get_device_posture_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureCheckApi->get_device_posture_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_check_id** | **str**| ID of the device posture check | 

### Return type

[**DevicePostureCheck**](DevicePostureCheck.md)

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

# **list_default_device_posture_checks**
> List[DevicePostureCheck] list_default_device_posture_checks()

List all default device posture checks

Lists all default device posture checks. Default device posture checks are defined by Okta. Their type will always be `BUILTIN`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_posture_check import DevicePostureCheck
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
    api_instance = okta.DevicePostureCheckApi(api_client)

    try:
        # List all default device posture checks
        api_response = api_instance.list_default_device_posture_checks()
        print("The response of DevicePostureCheckApi->list_default_device_posture_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureCheckApi->list_default_device_posture_checks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DevicePostureCheck]**](DevicePostureCheck.md)

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

# **list_device_posture_checks**
> List[DevicePostureCheck] list_device_posture_checks()

List all device posture checks

Lists all device posture checks

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_posture_check import DevicePostureCheck
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
    api_instance = okta.DevicePostureCheckApi(api_client)

    try:
        # List all device posture checks
        api_response = api_instance.list_device_posture_checks()
        print("The response of DevicePostureCheckApi->list_device_posture_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureCheckApi->list_device_posture_checks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DevicePostureCheck]**](DevicePostureCheck.md)

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

# **replace_device_posture_check**
> DevicePostureCheck replace_device_posture_check(posture_check_id, device_posture_check)

Replace a device posture check

Replaces a device posture check by `postureCheckId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_posture_check import DevicePostureCheck
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
    api_instance = okta.DevicePostureCheckApi(api_client)
    posture_check_id = 'posture_check_id_example' # str | ID of the device posture check
    device_posture_check = okta.DevicePostureCheck() # DevicePostureCheck | 

    try:
        # Replace a device posture check
        api_response = api_instance.replace_device_posture_check(posture_check_id, device_posture_check)
        print("The response of DevicePostureCheckApi->replace_device_posture_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureCheckApi->replace_device_posture_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_check_id** | **str**| ID of the device posture check | 
 **device_posture_check** | [**DevicePostureCheck**](DevicePostureCheck.md)|  | 

### Return type

[**DevicePostureCheck**](DevicePostureCheck.md)

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

