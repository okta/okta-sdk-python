# StandardRoleEmbedded

Optional embedded resources for the role assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**StandardRoleEmbeddedTargets**](StandardRoleEmbeddedTargets.md) |  | [optional] 

## Example

```python
from okta.models.standard_role_embedded import StandardRoleEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of StandardRoleEmbedded from a JSON string
standard_role_embedded_instance = StandardRoleEmbedded.from_json(json)
# print the JSON string representation of the object
print(StandardRoleEmbedded.to_json())

# convert the object into a dict
standard_role_embedded_dict = standard_role_embedded_instance.to_dict()
# create an instance of StandardRoleEmbedded from a dict
standard_role_embedded_from_dict = StandardRoleEmbedded.from_dict(standard_role_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


