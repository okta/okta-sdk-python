# EnhancedDynamicNetworkZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asns** | [**EnhancedDynamicNetworkZoneAllOfAsns**](EnhancedDynamicNetworkZoneAllOfAsns.md) |  | [optional] 
**locations** | [**EnhancedDynamicNetworkZoneAllOfLocations**](EnhancedDynamicNetworkZoneAllOfLocations.md) |  | [optional] 
**ip_service_categories** | [**EnhancedDynamicNetworkZoneAllOfIpServiceCategories**](EnhancedDynamicNetworkZoneAllOfIpServiceCategories.md) |  | [optional] 

## Example

```python
from okta.models.enhanced_dynamic_network_zone import EnhancedDynamicNetworkZone

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedDynamicNetworkZone from a JSON string
enhanced_dynamic_network_zone_instance = EnhancedDynamicNetworkZone.from_json(json)
# print the JSON string representation of the object
print(EnhancedDynamicNetworkZone.to_json())

# convert the object into a dict
enhanced_dynamic_network_zone_dict = enhanced_dynamic_network_zone_instance.to_dict()
# create an instance of EnhancedDynamicNetworkZone from a dict
enhanced_dynamic_network_zone_from_dict = EnhancedDynamicNetworkZone.from_dict(enhanced_dynamic_network_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


