# swagger_client.NetworkZoneApi

All URIs are relative to *https://your-subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_network_zone**](NetworkZoneApi.md#activate_network_zone) | **POST** /api/v1/zones/{zoneId}/lifecycle/activate | Activate Network Zone
[**create_network_zone**](NetworkZoneApi.md#create_network_zone) | **POST** /api/v1/zones | Add Network Zone
[**deactivate_network_zone**](NetworkZoneApi.md#deactivate_network_zone) | **POST** /api/v1/zones/{zoneId}/lifecycle/deactivate | Deactivate Network Zone
[**delete_network_zone**](NetworkZoneApi.md#delete_network_zone) | **DELETE** /api/v1/zones/{zoneId} | Delete Network Zone
[**get_network_zone**](NetworkZoneApi.md#get_network_zone) | **GET** /api/v1/zones/{zoneId} | Get Network Zone
[**list_network_zones**](NetworkZoneApi.md#list_network_zones) | **GET** /api/v1/zones | List Network Zones
[**update_network_zone**](NetworkZoneApi.md#update_network_zone) | **PUT** /api/v1/zones/{zoneId} | Update Network Zone

# **activate_network_zone**
> NetworkZone activate_network_zone(zone_id)

Activate Network Zone

Activate Network Zone

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Activate Network Zone
    api_response = api_instance.activate_network_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->activate_network_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_zone**
> NetworkZone create_network_zone(body)

Add Network Zone

Adds a new network zone to your Okta organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
body = swagger_client.NetworkZone() # NetworkZone | 

try:
    # Add Network Zone
    api_response = api_instance.create_network_zone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->create_network_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkZone**](NetworkZone.md)|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_network_zone**
> NetworkZone deactivate_network_zone(zone_id)

Deactivate Network Zone

Deactivates a network zone.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Deactivate Network Zone
    api_response = api_instance.deactivate_network_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->deactivate_network_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_zone**
> delete_network_zone(zone_id)

Delete Network Zone

Removes network zone.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Delete Network Zone
    api_instance.delete_network_zone(zone_id)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->delete_network_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_zone**
> NetworkZone get_network_zone(zone_id)

Get Network Zone

Fetches a network zone from your Okta organization by `id`.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Get Network Zone
    api_response = api_instance.get_network_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->get_network_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_zones**
> list[NetworkZone] list_network_zones(after=after, limit=limit, filter=filter)

List Network Zones

Enumerates network zones added to your organization with pagination. A subset of zones can be returned that match a supported filter expression or query.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
after = 'after_example' # str | Specifies the pagination cursor for the next page of network zones (optional)
limit = -1 # int | Specifies the number of results for a page (optional) (default to -1)
filter = 'filter_example' # str | Filters zones by usage or id expression (optional)

try:
    # List Network Zones
    api_response = api_instance.list_network_zones(after=after, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->list_network_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Specifies the pagination cursor for the next page of network zones | [optional] 
 **limit** | **int**| Specifies the number of results for a page | [optional] [default to -1]
 **filter** | **str**| Filters zones by usage or id expression | [optional] 

### Return type

[**list[NetworkZone]**](NetworkZone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_zone**
> NetworkZone update_network_zone(body, zone_id)

Update Network Zone

Updates a network zone in your organization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NetworkZoneApi(swagger_client.ApiClient(configuration))
body = swagger_client.NetworkZone() # NetworkZone | 
zone_id = 'zone_id_example' # str | 

try:
    # Update Network Zone
    api_response = api_instance.update_network_zone(body, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkZoneApi->update_network_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkZone**](NetworkZone.md)|  | 
 **zone_id** | **str**|  | 

### Return type

[**NetworkZone**](NetworkZone.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

