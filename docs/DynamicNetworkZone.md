# DynamicNetworkZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asns** | [**DynamicNetworkZoneAllOfAsns**](DynamicNetworkZoneAllOfAsns.md) |  | [optional] 
**proxy_type** | **str** | The proxy type used for a Dynamic Network Zone | [optional] 
**locations** | [**DynamicNetworkZoneAllOfLocations**](DynamicNetworkZoneAllOfLocations.md) |  | [optional] 

## Example

```python
from okta.models.dynamic_network_zone import DynamicNetworkZone

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicNetworkZone from a JSON string
dynamic_network_zone_instance = DynamicNetworkZone.from_json(json)
# print the JSON string representation of the object
print(DynamicNetworkZone.to_json())

# convert the object into a dict
dynamic_network_zone_dict = dynamic_network_zone_instance.to_dict()
# create an instance of DynamicNetworkZone from a dict
dynamic_network_zone_from_dict = DynamicNetworkZone.from_dict(dynamic_network_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


