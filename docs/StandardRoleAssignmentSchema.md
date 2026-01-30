# StandardRoleAssignmentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specify a [standard admin role](/openapi/okta-management/guides/roles/#standard-roles), an [IAM-based standard role](/openapi/okta-management/guides/roles/#iam-based-standard-roles), or &#x60;CUSTOM&#x60; for a custom role type: | 

## Example

```python
from okta.models.standard_role_assignment_schema import StandardRoleAssignmentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StandardRoleAssignmentSchema from a JSON string
standard_role_assignment_schema_instance = StandardRoleAssignmentSchema.from_json(json)
# print the JSON string representation of the object
print(StandardRoleAssignmentSchema.to_json())

# convert the object into a dict
standard_role_assignment_schema_dict = standard_role_assignment_schema_instance.to_dict()
# create an instance of StandardRoleAssignmentSchema from a dict
standard_role_assignment_schema_from_dict = StandardRoleAssignmentSchema.from_dict(standard_role_assignment_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


