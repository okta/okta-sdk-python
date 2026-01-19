# PermissionConditions

Conditions for further restricting a permission. See [Permission conditions](https://help.okta.com/okta_help.htm?type=oie&id=ext-permission-conditions).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **Dict[str, object]** | Exclude attributes with specific values for the permission | [optional] 
**include** | **Dict[str, object]** | Include attributes with specific values for the permission | [optional] 

## Example

```python
from okta.models.permission_conditions import PermissionConditions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionConditions from a JSON string
permission_conditions_instance = PermissionConditions.from_json(json)
# print the JSON string representation of the object
print(PermissionConditions.to_json())

# convert the object into a dict
permission_conditions_dict = permission_conditions_instance.to_dict()
# create an instance of PermissionConditions from a dict
permission_conditions_from_dict = PermissionConditions.from_dict(permission_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


