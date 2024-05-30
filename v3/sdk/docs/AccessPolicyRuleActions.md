# AccessPolicyRuleActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_sign_on** | [**AccessPolicyRuleApplicationSignOn**](AccessPolicyRuleApplicationSignOn.md) |  | [optional] 

## Example

```python
from openapi_client.models.access_policy_rule_actions import AccessPolicyRuleActions

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyRuleActions from a JSON string
access_policy_rule_actions_instance = AccessPolicyRuleActions.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyRuleActions.to_json())

# convert the object into a dict
access_policy_rule_actions_dict = access_policy_rule_actions_instance.to_dict()
# create an instance of AccessPolicyRuleActions from a dict
access_policy_rule_actions_form_dict = access_policy_rule_actions.from_dict(access_policy_rule_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


