# openapi_client.NetworkZoneApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_network_zone**](NetworkZoneApi.md#activate_network_zone) | **POST** /api/v1/zones/{zoneId}/lifecycle/activate | Activate a Network Zone
[**create_network_zone**](NetworkZoneApi.md#create_network_zone) | **POST** /api/v1/zones | Create a Network Zone
[**deactivate_network_zone**](NetworkZoneApi.md#deactivate_network_zone) | **POST** /api/v1/zones/{zoneId}/lifecycle/deactivate | Deactivate a Network Zone
[**delete_network_zone**](NetworkZoneApi.md#delete_network_zone) | **DELETE** /api/v1/zones/{zoneId} | Delete a Network Zone
[**get_network_zone**](NetworkZoneApi.md#get_network_zone) | **GET** /api/v1/zones/{zoneId} | Retrieve a Network Zone
[**list_network_zones**](NetworkZoneApi.md#list_network_zones) | **GET** /api/v1/zones | List all Network Zones
[**replace_network_zone**](NetworkZoneApi.md#replace_network_zone) | **PUT** /api/v1/zones/{zoneId} | Replace a Network Zone


# **activate_network_zone**
> NetworkZone activate_network_zone(zone_id)

Activate a Network Zone

Activates a network zone by `zoneId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.network_zone import NetworkZone
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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Activate a Network Zone
        api_response = api_instance.activate_network_zone(zone_id)
        print("The response of NetworkZoneApi->activate_network_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->activate_network_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| &#x60;id&#x60; of the Network Zone | 

### Return type

[**NetworkZone**](NetworkZone.md)

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

# **create_network_zone**
> NetworkZone create_network_zone(zone)

Create a Network Zone

Creates a new network zone. * At least one of either the `gateways` attribute or `proxies` attribute must be defined when creating a Network Zone. * At least one of the following attributes must be defined: `proxyType`, `locations`, or `asns`.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.network_zone import NetworkZone
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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    zone = openapi_client.NetworkZone() # NetworkZone | 

    try:
        # Create a Network Zone
        api_response = api_instance.create_network_zone(zone)
        print("The response of NetworkZoneApi->create_network_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->create_network_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**NetworkZone**](NetworkZone.md)|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_network_zone**
> NetworkZone deactivate_network_zone(zone_id)

Deactivate a Network Zone

Deactivates a network zone by `zoneId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.network_zone import NetworkZone
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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Deactivate a Network Zone
        api_response = api_instance.deactivate_network_zone(zone_id)
        print("The response of NetworkZoneApi->deactivate_network_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->deactivate_network_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| &#x60;id&#x60; of the Network Zone | 

### Return type

[**NetworkZone**](NetworkZone.md)

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

# **delete_network_zone**
> delete_network_zone(zone_id)

Delete a Network Zone

Deletes network zone by `zoneId`

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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Delete a Network Zone
        api_instance.delete_network_zone(zone_id)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->delete_network_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| &#x60;id&#x60; of the Network Zone | 

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

# **get_network_zone**
> NetworkZone get_network_zone(zone_id)

Retrieve a Network Zone

Retrieves a network zone by `zoneId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.network_zone import NetworkZone
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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Retrieve a Network Zone
        api_response = api_instance.get_network_zone(zone_id)
        print("The response of NetworkZoneApi->get_network_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->get_network_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| &#x60;id&#x60; of the Network Zone | 

### Return type

[**NetworkZone**](NetworkZone.md)

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

# **list_network_zones**
> List[NetworkZone] list_network_zones(after=after, limit=limit, filter=filter)

List all Network Zones

Lists all network zones with pagination. A subset of zones can be returned that match a supported filter expression or query.  This operation requires URL encoding. For example, `filter=(id eq \"nzoul0wf9jyb8xwZm0g3\" or id eq \"nzoul1MxmGN18NDQT0g3\")` is encoded as `filter=%28id+eq+%22nzoul0wf9jyb8xwZm0g3%22+or+id+eq+%22nzoul1MxmGN18NDQT0g3%22%29`.  Okta supports filtering on the `id` and `usage` properties. See [Filtering](https://developer.okta.com/docs/reference/core-okta-api/#filter) for more information on the expressions that are used in filtering.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.network_zone import NetworkZone
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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    after = '200u7yq5goxNFTiMjW1d7' # str | Specifies the pagination cursor for the next page of network zones (optional)
    limit = -1 # int | Specifies the number of results for a page (optional) (default to -1)
    filter = 'filter=%28id+eq+%22nzowc1U5Jh5xuAK0o0g3%22%29' # str | Filters zones by usage or ID expression (optional)

    try:
        # List all Network Zones
        api_response = api_instance.list_network_zones(after=after, limit=limit, filter=filter)
        print("The response of NetworkZoneApi->list_network_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->list_network_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Specifies the pagination cursor for the next page of network zones | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to -1]
 **filter** | **str**| Filters zones by usage or ID expression | [optional] 

### Return type

[**List[NetworkZone]**](NetworkZone.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_network_zone**
> NetworkZone replace_network_zone(zone_id, zone)

Replace a Network Zone

Replaces a network zone by `zoneId`. The replaced network zone type must be the same as the existing type. You may replace the usage (`POLICY`, `BLOCKLIST`) of a network zone by updating the `usage` attribute.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import openapi_client
from openapi_client.models.network_zone import NetworkZone
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
    api_instance = openapi_client.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone
    zone = openapi_client.NetworkZone() # NetworkZone | 

    try:
        # Replace a Network Zone
        api_response = api_instance.replace_network_zone(zone_id, zone)
        print("The response of NetworkZoneApi->replace_network_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->replace_network_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| &#x60;id&#x60; of the Network Zone | 
 **zone** | [**NetworkZone**](NetworkZone.md)|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

