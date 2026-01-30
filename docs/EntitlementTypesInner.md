# EntitlementTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The entitlement type name | 
**description** | **str** | Description of the entitlement type | [optional] 
**endpoint** | **str** | URL of the entitlement type endpoint | 
**attributes** | [**EntitlementTypesInnerAttributes**](EntitlementTypesInnerAttributes.md) |  | 
**mappings** | [**EntitlementTypesInnerMappings**](EntitlementTypesInnerMappings.md) |  | 

## Example

```python
from okta.models.entitlement_types_inner import EntitlementTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementTypesInner from a JSON string
entitlement_types_inner_instance = EntitlementTypesInner.from_json(json)
# print the JSON string representation of the object
print(EntitlementTypesInner.to_json())

# convert the object into a dict
entitlement_types_inner_dict = entitlement_types_inner_instance.to_dict()
# create an instance of EntitlementTypesInner from a dict
entitlement_types_inner_from_dict = EntitlementTypesInner.from_dict(entitlement_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


