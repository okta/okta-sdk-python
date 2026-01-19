# EnhancedDynamicNetworkZoneAllOfIpServiceCategories

IP services, such as a proxy or VPN, to include or exclude for an Enhanced Dynamic Network Zone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**List[IPServiceCategory]**](IPServiceCategory.md) | IP services to include for an Enhanced Dynamic Network Zone | [optional] 
**exclude** | [**List[IPServiceCategory]**](IPServiceCategory.md) | IP services to exclude for an Enhanced Dynamic Network Zone | [optional] 

## Example

```python
from okta.models.enhanced_dynamic_network_zone_all_of_ip_service_categories import EnhancedDynamicNetworkZoneAllOfIpServiceCategories

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedDynamicNetworkZoneAllOfIpServiceCategories from a JSON string
enhanced_dynamic_network_zone_all_of_ip_service_categories_instance = EnhancedDynamicNetworkZoneAllOfIpServiceCategories.from_json(json)
# print the JSON string representation of the object
print(EnhancedDynamicNetworkZoneAllOfIpServiceCategories.to_json())

# convert the object into a dict
enhanced_dynamic_network_zone_all_of_ip_service_categories_dict = enhanced_dynamic_network_zone_all_of_ip_service_categories_instance.to_dict()
# create an instance of EnhancedDynamicNetworkZoneAllOfIpServiceCategories from a dict
enhanced_dynamic_network_zone_all_of_ip_service_categories_from_dict = EnhancedDynamicNetworkZoneAllOfIpServiceCategories.from_dict(enhanced_dynamic_network_zone_all_of_ip_service_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


