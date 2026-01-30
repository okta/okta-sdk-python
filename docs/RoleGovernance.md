# RoleGovernance

List of all user role governance sources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grants** | [**List[RoleGovernanceSource]**](RoleGovernanceSource.md) |  | [optional] 
**links** | [**LinksGovernanceSources**](LinksGovernanceSources.md) |  | [optional] 

## Example

```python
from okta.models.role_governance import RoleGovernance

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGovernance from a JSON string
role_governance_instance = RoleGovernance.from_json(json)
# print the JSON string representation of the object
print(RoleGovernance.to_json())

# convert the object into a dict
role_governance_dict = role_governance_instance.to_dict()
# create an instance of RoleGovernance from a dict
role_governance_from_dict = RoleGovernance.from_dict(role_governance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


