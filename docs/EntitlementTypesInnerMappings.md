# EntitlementTypesInnerMappings

The property mapping between an Okta entitlement and an app entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The field that maps to the entitlement ID | 
**display_name** | **str** | The field that maps to the entitlement display name | 
**description** | **str** | The field that maps to entitlement description | [optional] 

## Example

```python
from okta.models.entitlement_types_inner_mappings import EntitlementTypesInnerMappings

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementTypesInnerMappings from a JSON string
entitlement_types_inner_mappings_instance = EntitlementTypesInnerMappings.from_json(json)
# print the JSON string representation of the object
print(EntitlementTypesInnerMappings.to_json())

# convert the object into a dict
entitlement_types_inner_mappings_dict = entitlement_types_inner_mappings_instance.to_dict()
# create an instance of EntitlementTypesInnerMappings from a dict
entitlement_types_inner_mappings_from_dict = EntitlementTypesInnerMappings.from_dict(entitlement_types_inner_mappings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


