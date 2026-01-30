# EnhancedDynamicNetworkZoneAllOfAsns

The list of ASNs associated with an Enhanced Dynamic Network Zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**EnhancedDynamicNetworkZoneAllOfAsnsInclude**](EnhancedDynamicNetworkZoneAllOfAsnsInclude.md) |  | [optional] 
**exclude** | [**EnhancedDynamicNetworkZoneAllOfAsnsExclude**](EnhancedDynamicNetworkZoneAllOfAsnsExclude.md) |  | [optional] 

## Example

```python
from okta.models.enhanced_dynamic_network_zone_all_of_asns import EnhancedDynamicNetworkZoneAllOfAsns

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedDynamicNetworkZoneAllOfAsns from a JSON string
enhanced_dynamic_network_zone_all_of_asns_instance = EnhancedDynamicNetworkZoneAllOfAsns.from_json(json)
# print the JSON string representation of the object
print(EnhancedDynamicNetworkZoneAllOfAsns.to_json())

# convert the object into a dict
enhanced_dynamic_network_zone_all_of_asns_dict = enhanced_dynamic_network_zone_all_of_asns_instance.to_dict()
# create an instance of EnhancedDynamicNetworkZoneAllOfAsns from a dict
enhanced_dynamic_network_zone_all_of_asns_from_dict = EnhancedDynamicNetworkZoneAllOfAsns.from_dict(enhanced_dynamic_network_zone_all_of_asns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


