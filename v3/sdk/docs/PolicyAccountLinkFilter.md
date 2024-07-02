# PolicyAccountLinkFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**PolicyAccountLinkFilterGroups**](PolicyAccountLinkFilterGroups.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_account_link_filter import PolicyAccountLinkFilter

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAccountLinkFilter from a JSON string
policy_account_link_filter_instance = PolicyAccountLinkFilter.from_json(json)
# print the JSON string representation of the object
print(PolicyAccountLinkFilter.to_json())

# convert the object into a dict
policy_account_link_filter_dict = policy_account_link_filter_instance.to_dict()
# create an instance of PolicyAccountLinkFilter from a dict
policy_account_link_filter_from_dict = PolicyAccountLinkFilter.from_dict(policy_account_link_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


