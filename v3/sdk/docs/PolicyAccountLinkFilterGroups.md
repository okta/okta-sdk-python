# PolicyAccountLinkFilterGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.policy_account_link_filter_groups import PolicyAccountLinkFilterGroups

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAccountLinkFilterGroups from a JSON string
policy_account_link_filter_groups_instance = PolicyAccountLinkFilterGroups.from_json(json)
# print the JSON string representation of the object
print(PolicyAccountLinkFilterGroups.to_json())

# convert the object into a dict
policy_account_link_filter_groups_dict = policy_account_link_filter_groups_instance.to_dict()
# create an instance of PolicyAccountLinkFilterGroups from a dict
policy_account_link_filter_groups_from_dict = PolicyAccountLinkFilterGroups.from_dict(policy_account_link_filter_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


