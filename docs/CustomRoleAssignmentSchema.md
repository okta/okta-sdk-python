# CustomRoleAssignmentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_set** | **str** | Resource set ID | 
**role** | **str** | Custom role ID | 
**type** | **str** | Specify a [standard admin role](/openapi/okta-management/guides/roles/#standard-roles), an [IAM-based standard role](/openapi/okta-management/guides/roles/#iam-based-standard-roles), or &#x60;CUSTOM&#x60; for a custom role type: | 

## Example

```python
from okta.models.custom_role_assignment_schema import CustomRoleAssignmentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRoleAssignmentSchema from a JSON string
custom_role_assignment_schema_instance = CustomRoleAssignmentSchema.from_json(json)
# print the JSON string representation of the object
print(CustomRoleAssignmentSchema.to_json())

# convert the object into a dict
custom_role_assignment_schema_dict = custom_role_assignment_schema_instance.to_dict()
# create an instance of CustomRoleAssignmentSchema from a dict
custom_role_assignment_schema_from_dict = CustomRoleAssignmentSchema.from_dict(custom_role_assignment_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


