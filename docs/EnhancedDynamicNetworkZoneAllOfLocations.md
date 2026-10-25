# EnhancedDynamicNetworkZoneAllOfLocations

The list of geolocations to include or exclude for an Enhanced Dynamic Network Zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**List[NetworkZoneLocation]**](NetworkZoneLocation.md) | An array of geolocations to include for an Enhanced Dynamic Network Zone | [optional] 
**exclude** | [**List[NetworkZoneLocation]**](NetworkZoneLocation.md) | An array of geolocations to exclude for an Enhanced Dynamic Network Zone | [optional] 

## Example

```python
from okta.models.enhanced_dynamic_network_zone_all_of_locations import EnhancedDynamicNetworkZoneAllOfLocations

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedDynamicNetworkZoneAllOfLocations from a JSON string
enhanced_dynamic_network_zone_all_of_locations_instance = EnhancedDynamicNetworkZoneAllOfLocations.from_json(json)
# print the JSON string representation of the object
print(EnhancedDynamicNetworkZoneAllOfLocations.to_json())

# convert the object into a dict
enhanced_dynamic_network_zone_all_of_locations_dict = enhanced_dynamic_network_zone_all_of_locations_instance.to_dict()
# create an instance of EnhancedDynamicNetworkZoneAllOfLocations from a dict
enhanced_dynamic_network_zone_all_of_locations_from_dict = EnhancedDynamicNetworkZoneAllOfLocations.from_dict(enhanced_dynamic_network_zone_all_of_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


