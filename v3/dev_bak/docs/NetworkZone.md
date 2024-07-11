# NetworkZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asns** | **List[str]** | Dynamic network zone property. array of strings that represent an ASN numeric value | [optional] 
**created** | **datetime** | Timestamp when the network zone was created | [optional] [readonly] 
**gateways** | [**List[NetworkZoneAddress]**](NetworkZoneAddress.md) | IP network zone property: the IP addresses (range or CIDR form) of this zone. The maximum array length is 150 entries for admin-created IP zones, 1000 entries for IP blocklist zones, and 5000 entries for the default system IP Zone. | [optional] 
**id** | **str** | Unique identifier for the network zone | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the network zone was last modified | [optional] [readonly] 
**locations** | [**List[NetworkZoneLocation]**](NetworkZoneLocation.md) | Dynamic network zone property: an array of geolocations of this network zone | [optional] 
**name** | **str** | Unique name for this network zone. Maximum of 128 characters. | [optional] 
**proxies** | [**List[NetworkZoneAddress]**](NetworkZoneAddress.md) | IP network zone property: the IP addresses (range or CIDR form) that are allowed to forward a request from gateway addresses These proxies are automatically trusted by Threat Insights, and used to identify the client IP of a request. The maximum array length is 150 entries for admin-created zones and 5000 entries for the default system IP Zone. | [optional] 
**proxy_type** | **str** | Dynamic network zone property: the proxy type used | [optional] 
**status** | [**NetworkZoneStatus**](NetworkZoneStatus.md) |  | [optional] 
**system** | **bool** | Indicates if this is a system network zone. For admin-created zones, this is always &#x60;false&#x60;. The system IP Policy Network Zone (&#x60;LegacyIpZone&#x60;) is included by default in your Okta org. Notice that &#x60;system&#x3D;true&#x60; for the &#x60;LegacyIpZone&#x60; object. Admin users can modify the name of this default system Zone and can add up to 5000 gateway or proxy IP entries. | [optional] 
**type** | [**NetworkZoneType**](NetworkZoneType.md) |  | [optional] 
**usage** | [**NetworkZoneUsage**](NetworkZoneUsage.md) |  | [optional] 
**links** | [**NetworkZoneLinks**](NetworkZoneLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.network_zone import NetworkZone

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZone from a JSON string
network_zone_instance = NetworkZone.from_json(json)
# print the JSON string representation of the object
print(NetworkZone.to_json())

# convert the object into a dict
network_zone_dict = network_zone_instance.to_dict()
# create an instance of NetworkZone from a dict
network_zone_from_dict = NetworkZone.from_dict(network_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


