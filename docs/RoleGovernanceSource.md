# RoleGovernanceSource

User role governance source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle_id** | **str** | &#x60;id&#x60; of the entitlement bundle | [optional] [readonly] 
**expiration_date** | **datetime** | The expiration date of the entitlement bundle | [optional] [readonly] 
**grant_id** | **str** | &#x60;id&#x60; of the grant | [readonly] 
**type** | [**GovernanceSourceType**](GovernanceSourceType.md) |  | 
**links** | [**RoleGovernanceSourceLinks**](RoleGovernanceSourceLinks.md) |  | [optional] 

## Example

```python
from okta.models.role_governance_source import RoleGovernanceSource

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGovernanceSource from a JSON string
role_governance_source_instance = RoleGovernanceSource.from_json(json)
# print the JSON string representation of the object
print(RoleGovernanceSource.to_json())

# convert the object into a dict
role_governance_source_dict = role_governance_source_instance.to_dict()
# create an instance of RoleGovernanceSource from a dict
role_governance_source_from_dict = RoleGovernanceSource.from_dict(role_governance_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


