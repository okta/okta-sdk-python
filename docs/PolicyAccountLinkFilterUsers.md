# PolicyAccountLinkFilterUsers

Filters on which users are available for account linking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Specifies the blocklist of user identifiers to exclude from account linking | [optional] 
**exclude_admins** | **bool** | Specifies whether admin users should be excluded from account linking | [optional] [default to False]

## Example

```python
from okta.models.policy_account_link_filter_users import PolicyAccountLinkFilterUsers

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAccountLinkFilterUsers from a JSON string
policy_account_link_filter_users_instance = PolicyAccountLinkFilterUsers.from_json(json)
# print the JSON string representation of the object
print(PolicyAccountLinkFilterUsers.to_json())

# convert the object into a dict
policy_account_link_filter_users_dict = policy_account_link_filter_users_instance.to_dict()
# create an instance of PolicyAccountLinkFilterUsers from a dict
policy_account_link_filter_users_from_dict = PolicyAccountLinkFilterUsers.from_dict(policy_account_link_filter_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


