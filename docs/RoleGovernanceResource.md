# RoleGovernanceResource

The resource of a grant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The resource name | [optional] 
**resource** | **str** | The resources id | [optional] 

## Example

```python
from okta.models.role_governance_resource import RoleGovernanceResource

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGovernanceResource from a JSON string
role_governance_resource_instance = RoleGovernanceResource.from_json(json)
# print the JSON string representation of the object
print(RoleGovernanceResource.to_json())

# convert the object into a dict
role_governance_resource_dict = role_governance_resource_instance.to_dict()
# create an instance of RoleGovernanceResource from a dict
role_governance_resource_from_dict = RoleGovernanceResource.from_dict(role_governance_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


