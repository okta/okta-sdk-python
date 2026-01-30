# RoleGovernanceResources

The resources of a grant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[RoleGovernanceResource]**](RoleGovernanceResource.md) |  | [optional] 
**links** | [**AIAgentOperationListResponseLinks**](AIAgentOperationListResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.role_governance_resources import RoleGovernanceResources

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGovernanceResources from a JSON string
role_governance_resources_instance = RoleGovernanceResources.from_json(json)
# print the JSON string representation of the object
print(RoleGovernanceResources.to_json())

# convert the object into a dict
role_governance_resources_dict = role_governance_resources_instance.to_dict()
# create an instance of RoleGovernanceResources from a dict
role_governance_resources_from_dict = RoleGovernanceResources.from_dict(role_governance_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


