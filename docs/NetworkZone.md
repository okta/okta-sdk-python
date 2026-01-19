# NetworkZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**id** | **str** | Unique identifier for the Network Zone | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last modified | [optional] [readonly] 
**name** | **str** | Unique name for this Network Zone | 
**status** | [**NetworkZoneStatus**](NetworkZoneStatus.md) |  | [optional] 
**system** | **bool** | Indicates a system Network Zone: * &#x60;true&#x60; for system Network Zones * &#x60;false&#x60; for custom Network Zones  The Okta org provides the following default system Network Zones: * &#x60;LegacyIpZone&#x60; * &#x60;BlockedIpZone&#x60; * &#x60;DefaultEnhancedDynamicZone&#x60; * &#x60;DefaultExemptIpZone&#x60;  Admins can modify the name of the default system Network Zone and add up to 5000 gateway or proxy IP entries.  | [optional] [readonly] 
**type** | [**NetworkZoneType**](NetworkZoneType.md) |  | 
**usage** | [**NetworkZoneUsage**](NetworkZoneUsage.md) |  | [optional] 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.network_zone import NetworkZone

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


