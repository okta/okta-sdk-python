# okta.NetworkZoneApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_network_zone**](NetworkZoneApi.md#activate_network_zone) | **POST** /api/v1/zones/{zoneId}/lifecycle/activate | Activate a network zone
[**create_network_zone**](NetworkZoneApi.md#create_network_zone) | **POST** /api/v1/zones | Create a network zone
[**deactivate_network_zone**](NetworkZoneApi.md#deactivate_network_zone) | **POST** /api/v1/zones/{zoneId}/lifecycle/deactivate | Deactivate a network zone
[**delete_network_zone**](NetworkZoneApi.md#delete_network_zone) | **DELETE** /api/v1/zones/{zoneId} | Delete a network zone
[**get_network_zone**](NetworkZoneApi.md#get_network_zone) | **GET** /api/v1/zones/{zoneId} | Retrieve a network zone
[**list_network_zones**](NetworkZoneApi.md#list_network_zones) | **GET** /api/v1/zones | List all network zones
[**replace_network_zone**](NetworkZoneApi.md#replace_network_zone) | **PUT** /api/v1/zones/{zoneId} | Replace a network zone


# **activate_network_zone**
> NetworkZone activate_network_zone(zone_id)

Activate a network zone

Activates a Network Zone by `zoneId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.network_zone import NetworkZone
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
    api_instance = okta.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Activate a network zone
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

Create a network zone

Creates a Network Zone * For an IP Network Zone, you must define either `gateways` or `proxies`. * For a Dynamic Network Zone, you must define at least one of the following: `asns`, `locations`, or `proxyType`. * For an Enhanced Dynamic Network Zone, you must define at least one of the following: `asns`, `locations`, or `ipServiceCategories`. > **Note:** To view all properties for an Enhanced Dynamic Network Zone, select `DYNAMIC_V2` from the `type` dropdown list.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.network_zone import NetworkZone
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
    api_instance = okta.NetworkZoneApi(api_client)
    zone = okta.NetworkZone() # NetworkZone | 

    try:
        # Create a network zone
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

Deactivate a network zone

Deactivates a Network Zone by `zoneId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.network_zone import NetworkZone
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
    api_instance = okta.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Deactivate a network zone
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

Delete a network zone

Deletes a Network Zone by `zoneId` > **Notes:** > * You can't delete a Network Zone that's used by a [Policy](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/) or [Rule](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/#tag/Policy/operation/listPolicyRules). > * For Okta Identity Engine orgs, you can't delete a Network Zone with an ACTIVE `status`. <x-lifecycle class=\"oie\"></x-lifecycle>

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
    api_instance = okta.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Delete a network zone
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

Retrieve a network zone

Retrieves a Network Zone by `zoneId`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.network_zone import NetworkZone
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
    api_instance = okta.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone

    try:
        # Retrieve a network zone
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

List all network zones

Lists all Network Zones with pagination. A subset of zones can be returned that match a supported filter expression or query.  This operation requires URL encoding. For example, `filter=(id eq \"nzoul0wf9jyb8xwZm0g3\" or id eq \"nzoul1MxmGN18NDQT0g3\")` is encoded as `filter=%28id+eq+%22nzoul0wf9jyb8xwZm0g3%22+or+id+eq+%22nzoul1MxmGN18NDQT0g3%22%29`.  Okta supports filtering on the `id`, `usage`, and `system` properties. See [Filter](https://developer.okta.com/docs/api/#filter) for more information on the expressions that are used in filtering.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.network_zone import NetworkZone
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
    api_instance = okta.NetworkZoneApi(api_client)
    after = 'BlockedIpZones' # str |  (optional)
    limit = -1 # int |  (optional) (default to -1)
    filter = 'id eq \"nzowc1U5Jh5xuAK0o0g3\"' # str |  (optional)

    try:
        # List all network zones
        api_response = api_instance.list_network_zones(after=after, limit=limit, filter=filter)
        print("The response of NetworkZoneApi->list_network_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkZoneApi->list_network_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to -1]
 **filter** | **str**|  | [optional] 

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

Replace a network zone

Replaces a Network Zone by `zoneId`. The replaced Network Zone type must be the same as the existing type. You can replace the usage (`POLICY`, `BLOCKLIST`) of a Network Zone by updating the `usage` attribute.  **IP exempt zone**<br> If you have the IP exempt zone feature enabled, you can allow traffic from specific gateway IPs irrespective of Okta ThreatInsight configurations, blocked network zones, or IP change events within Identity Threat Protection with Okta AI.<br> <br> When you enable this feature, Okta creates a zone called `DefaultExemptIpZone`. Gateway IPs that you add to this zone always have access to Okta resources. See [IP exempt zone](https://help.okta.com/okta_help.htm?type=oie&id=csh-about-ip-exempt-zone).  > **Note:** You can't add trusted proxy IPs to this zone, delete the zone, or create additional exempt IP zones.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.network_zone import NetworkZone
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
    api_instance = okta.NetworkZoneApi(api_client)
    zone_id = 'nzowc1U5Jh5xuAK0o0g3' # str | `id` of the Network Zone
    zone = okta.NetworkZone() # NetworkZone | 

    try:
        # Replace a network zone
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

