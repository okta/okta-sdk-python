# EntitlementTypesInnerAttributes

Attributes for the entitlement type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** | A boolean value to indicate if this entitlement type is required for the user | [optional] [default to False]
**multivalued** | **bool** | A boolean value to indicate if a user can have multiple entitlements of this type | [optional] [default to False]

## Example

```python
from okta.models.entitlement_types_inner_attributes import EntitlementTypesInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementTypesInnerAttributes from a JSON string
entitlement_types_inner_attributes_instance = EntitlementTypesInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(EntitlementTypesInnerAttributes.to_json())

# convert the object into a dict
entitlement_types_inner_attributes_dict = entitlement_types_inner_attributes_instance.to_dict()
# create an instance of EntitlementTypesInnerAttributes from a dict
entitlement_types_inner_attributes_from_dict = EntitlementTypesInnerAttributes.from_dict(entitlement_types_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


