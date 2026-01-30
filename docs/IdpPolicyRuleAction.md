# IdpPolicyRuleAction

Specifies where to route users when they are attempting to sign in to your org, if the rule conditions are satisfied. You can add up to 10 providers to a single `idp` policy action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp** | [**IdpPolicyRuleActionIdp**](IdpPolicyRuleActionIdp.md) |  | [optional] 

## Example

```python
from okta.models.idp_policy_rule_action import IdpPolicyRuleAction

# TODO update the JSON string below
json = "{}"
# create an instance of IdpPolicyRuleAction from a JSON string
idp_policy_rule_action_instance = IdpPolicyRuleAction.from_json(json)
# print the JSON string representation of the object
print(IdpPolicyRuleAction.to_json())

# convert the object into a dict
idp_policy_rule_action_dict = idp_policy_rule_action_instance.to_dict()
# create an instance of IdpPolicyRuleAction from a dict
idp_policy_rule_action_from_dict = IdpPolicyRuleAction.from_dict(idp_policy_rule_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


