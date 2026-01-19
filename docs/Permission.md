# Permission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**PermissionConditions**](PermissionConditions.md) |  | [optional] 
**created** | **datetime** | Timestamp when the permission was assigned | [optional] [readonly] 
**label** | **str** | The assigned Okta [permission](/openapi/okta-management/guides/permissions) | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the permission was last updated | [optional] [readonly] 
**links** | [**PermissionLinks**](PermissionLinks.md) |  | [optional] 

## Example

```python
from okta.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print(Permission.to_json())

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_from_dict = Permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


