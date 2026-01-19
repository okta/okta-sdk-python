# IPNetworkZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_as_exempt_list** | **bool** | You can **only** use this parameter when making a request to the Replace the network zone endpoint (&#x60;/api/v1/zones/{zoneId}&#x60;). Set this parameter to &#x60;true&#x60; in your request when you update the &#x60;DefaultExemptIpZone&#x60; to allow IPs through the blocklist. | [optional] 
**gateways** | [**List[NetworkZoneAddress]**](NetworkZoneAddress.md) | The IP addresses (range or CIDR form) for an IP Network Zone. The maximum array length is 150 entries for admin-created IP zones, 1000 entries for IP blocklist zones, and 5000 entries for the default system IP Zone. | [optional] 
**proxies** | [**List[NetworkZoneAddress]**](NetworkZoneAddress.md) | The IP addresses (range or CIDR form) that are allowed to forward a request from gateway addresses for an IP Network Zone. These proxies are automatically trusted by Threat Insights and used to identify the client IP of a request. The maximum array length is 150 entries for admin-created zones and 5000 entries for the default system IP Zone. | [optional] 

## Example

```python
from okta.models.ip_network_zone import IPNetworkZone

# TODO update the JSON string below
json = "{}"
# create an instance of IPNetworkZone from a JSON string
ip_network_zone_instance = IPNetworkZone.from_json(json)
# print the JSON string representation of the object
print(IPNetworkZone.to_json())

# convert the object into a dict
ip_network_zone_dict = ip_network_zone_instance.to_dict()
# create an instance of IPNetworkZone from a dict
ip_network_zone_from_dict = IPNetworkZone.from_dict(ip_network_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


