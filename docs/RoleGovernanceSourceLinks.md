# RoleGovernanceSourceLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**HrefObjectGovernanceResourcesLink**](HrefObjectGovernanceResourcesLink.md) |  | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.role_governance_source_links import RoleGovernanceSourceLinks

# TODO update the JSON string below
json = "{}"
# create an instance of RoleGovernanceSourceLinks from a JSON string
role_governance_source_links_instance = RoleGovernanceSourceLinks.from_json(json)
# print the JSON string representation of the object
print(RoleGovernanceSourceLinks.to_json())

# convert the object into a dict
role_governance_source_links_dict = role_governance_source_links_instance.to_dict()
# create an instance of RoleGovernanceSourceLinks from a dict
role_governance_source_links_from_dict = RoleGovernanceSourceLinks.from_dict(role_governance_source_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


