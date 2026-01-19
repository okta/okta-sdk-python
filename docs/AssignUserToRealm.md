# AssignUserToRealm

Action that assigns a user to a realm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm_id** | **str** | ID of the realm | [optional] 

## Example

```python
from okta.models.assign_user_to_realm import AssignUserToRealm

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUserToRealm from a JSON string
assign_user_to_realm_instance = AssignUserToRealm.from_json(json)
# print the JSON string representation of the object
print(AssignUserToRealm.to_json())

# convert the object into a dict
assign_user_to_realm_dict = assign_user_to_realm_instance.to_dict()
# create an instance of AssignUserToRealm from a dict
assign_user_to_realm_from_dict = AssignUserToRealm.from_dict(assign_user_to_realm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


