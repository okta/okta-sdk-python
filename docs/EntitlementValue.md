# EntitlementValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entitlement value ID | [optional] 
**name** | **str** | The entitlement value resource name | [optional] 
**value** | **str** | The entitlement value resource [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) | [optional] 
**links** | [**EntitlementValueLinks**](EntitlementValueLinks.md) |  | [optional] 

## Example

```python
from okta.models.entitlement_value import EntitlementValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementValue from a JSON string
entitlement_value_instance = EntitlementValue.from_json(json)
# print the JSON string representation of the object
print(EntitlementValue.to_json())

# convert the object into a dict
entitlement_value_dict = entitlement_value_instance.to_dict()
# create an instance of EntitlementValue from a dict
entitlement_value_from_dict = EntitlementValue.from_dict(entitlement_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


