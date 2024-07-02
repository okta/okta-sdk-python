# PolicyAccountLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**PolicyAccountLinkAction**](PolicyAccountLinkAction.md) |  | [optional] 
**filter** | [**PolicyAccountLinkFilter**](PolicyAccountLinkFilter.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_account_link import PolicyAccountLink

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAccountLink from a JSON string
policy_account_link_instance = PolicyAccountLink.from_json(json)
# print the JSON string representation of the object
print(PolicyAccountLink.to_json())

# convert the object into a dict
policy_account_link_dict = policy_account_link_instance.to_dict()
# create an instance of PolicyAccountLink from a dict
policy_account_link_from_dict = PolicyAccountLink.from_dict(policy_account_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


