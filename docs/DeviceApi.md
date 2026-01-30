# okta.DeviceApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_device**](DeviceApi.md#activate_device) | **POST** /api/v1/devices/{deviceId}/lifecycle/activate | Activate a device
[**deactivate_device**](DeviceApi.md#deactivate_device) | **POST** /api/v1/devices/{deviceId}/lifecycle/deactivate | Deactivate a device
[**delete_device**](DeviceApi.md#delete_device) | **DELETE** /api/v1/devices/{deviceId} | Delete a device
[**get_device**](DeviceApi.md#get_device) | **GET** /api/v1/devices/{deviceId} | Retrieve a device
[**list_device_users**](DeviceApi.md#list_device_users) | **GET** /api/v1/devices/{deviceId}/users | List all users for a device
[**list_devices**](DeviceApi.md#list_devices) | **GET** /api/v1/devices | List all devices
[**suspend_device**](DeviceApi.md#suspend_device) | **POST** /api/v1/devices/{deviceId}/lifecycle/suspend | Suspend a Device
[**unsuspend_device**](DeviceApi.md#unsuspend_device) | **POST** /api/v1/devices/{deviceId}/lifecycle/unsuspend | Unsuspend a Device


# **activate_device**
> activate_device(device_id)

Activate a device

Activates a device by setting its status to `ACTIVE` by `deviceId`. Activated devices are used to create and delete device user links.

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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # Activate a device
        api_instance.activate_device(device_id)
    except Exception as e:
        print("Exception when calling DeviceApi->activate_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

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

# **deactivate_device**
> deactivate_device(device_id)

Deactivate a device

Deactivates a device by setting its status to `DEACTIVATED` by `deviceId`. Deactivation causes a device to lose all device user links. Set the device status to `DEACTIVATED` before deleting it. > **Note:** When deactivating a Device, keep in mind the following:   - Device deactivation is a destructive operation for device factors and client certificates. Device reenrollment using Okta Verify allows end users to set up new factors on the device.   - Device deletion removes the device record from Okta. Reenrollment creates a new device record.

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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # Deactivate a device
        api_instance.deactivate_device(device_id)
    except Exception as e:
        print("Exception when calling DeviceApi->deactivate_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

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

# **delete_device**
> delete_device(device_id)

Delete a device

Deletes (permanently) a device by `deviceId` if it has a status of `DEACTIVATED`. You can transition the device to `DEACTIVATED` status using the [Deactivate a Device](/openapi/okta-management/management/tag/Device/#tag/Device/operation/deactivateDevice) endpoint. This request is destructive and deletes all of the profile data related to the device. Once deleted, device data can't be recovered. However, reenrollment creates a new device record. > **Note:** Attempts to delete a device that isn't in a `DEACTIVATED` state raise an error.

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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # Delete a device
        api_instance.delete_device(device_id)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

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

# **get_device**
> Device get_device(device_id)

Retrieve a device

Retrieves a device by `deviceId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device import Device
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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # Retrieve a device
        api_response = api_instance.get_device(device_id)
        print("The response of DeviceApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

### Return type

[**Device**](Device.md)

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

# **list_device_users**
> List[DeviceUser] list_device_users(device_id)

List all users for a device

Lists all Users for a device by `deviceId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_user import DeviceUser
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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # List all users for a device
        api_response = api_instance.list_device_users(device_id)
        print("The response of DeviceApi->list_device_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_device_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

### Return type

[**List[DeviceUser]**](DeviceUser.md)

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

# **list_devices**
> List[DeviceList] list_devices(after=after, limit=limit, search=search, expand=expand)

List all devices

Lists all devices with pagination support.  >**Note:** To list all devices enrolled by a user, use the [List all devices endpoint in the User Resources API](/openapi/okta-management/management/tag/UserResources/#tag/UserResources/operation/listUserDevices).  You can return a subset of devices that match a supported search criteria using the `search` query parameter. Searches for devices based on the properties specified in the `search` parameter conforming SCIM filter specifications (case-insensitive). This data is eventually consistent. The API returns different results depending on specified queries in the request. Empty list is returned if no objects match `search` request.  > **Note:** The `search` parameter results are sourced from an eventually consistent datasource and may not reflect the latest information.  Don't use search results directly for record updates, as the data might be stale and therefore overwrite newer data, resulting in data loss.  Use an `id` lookup for records that you update to ensure your results contain the latest data.  This operation requires [URL encoding](https://www.w3.org/TR/html4/interact/forms.html#h-17.13.4.1). For example, `search=profile.displayName eq \"Bob\"` is encoded as `search=profile.displayName%20eq%20%22Bob%22`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.device_list import DeviceList
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
    api_instance = okta.DeviceApi(api_client)
    after = '200u3des4afA47rYJu1d7' # str |  (optional)
    limit = 200 # int | A limit on the number of objects to return (recommend `20`) (optional) (default to 200)
    search = 'status%20eq%20%22ACTIVE%22' # str | A SCIM filter expression that filters the results. Searches include all device `profile` properties and the device `id`, `status`, and `lastUpdated` properties.  Searches for devices can be filtered by the contains (`co`) operator. You can only use `co` with these select device profile attributes: `profile.displayName`, `profile.serialNumber`, `profile.imei`, `profile.meid`, `profile.udid`, and `profile.sid`. See [Operators](https://developer.okta.com/docs/api/#operators). (optional)
    expand = 'user' # str | Includes associated user details and management status for the device in the `_embedded` attribute (optional)

    try:
        # List all devices
        api_response = api_instance.list_devices(after=after, limit=limit, search=search, expand=expand)
        print("The response of DeviceApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**| A limit on the number of objects to return (recommend &#x60;20&#x60;) | [optional] [default to 200]
 **search** | **str**| A SCIM filter expression that filters the results. Searches include all device &#x60;profile&#x60; properties and the device &#x60;id&#x60;, &#x60;status&#x60;, and &#x60;lastUpdated&#x60; properties.  Searches for devices can be filtered by the contains (&#x60;co&#x60;) operator. You can only use &#x60;co&#x60; with these select device profile attributes: &#x60;profile.displayName&#x60;, &#x60;profile.serialNumber&#x60;, &#x60;profile.imei&#x60;, &#x60;profile.meid&#x60;, &#x60;profile.udid&#x60;, and &#x60;profile.sid&#x60;. See [Operators](https://developer.okta.com/docs/api/#operators). | [optional] 
 **expand** | **str**| Includes associated user details and management status for the device in the &#x60;_embedded&#x60; attribute | [optional] 

### Return type

[**List[DeviceList]**](DeviceList.md)

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

# **suspend_device**
> suspend_device(device_id)

Suspend a Device

Suspends a device by setting its status to `SUSPENDED`. Use suspended devices to create and delete device user links. You can only unsuspend or deactivate suspended devices. > **Note:** `SUSPENDED` status is meant to be temporary, so it isn't destructive.

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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # Suspend a Device
        api_instance.suspend_device(device_id)
    except Exception as e:
        print("Exception when calling DeviceApi->suspend_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

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

# **unsuspend_device**
> unsuspend_device(device_id)

Unsuspend a Device

Unsuspends a device by returning its `status` to `ACTIVE`. >**Note:** Only devices with a `SUSPENDED` status can be unsuspended.

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
    api_instance = okta.DeviceApi(api_client)
    device_id = 'guo4a5u7JHHhjXrMK0g4' # str | `id` of the device

    try:
        # Unsuspend a Device
        api_instance.unsuspend_device(device_id)
    except Exception as e:
        print("Exception when calling DeviceApi->unsuspend_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| &#x60;id&#x60; of the device | 

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

