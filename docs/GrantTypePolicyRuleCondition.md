# GrantTypePolicyRuleCondition

Array of grant types that this condition includes. Determines the mechanism that Okta uses to authorize the creation of the tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Array of grant types thagt this condition includes. | [optional] 

## Example

```python
from okta.models.grant_type_policy_rule_condition import GrantTypePolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of GrantTypePolicyRuleCondition from a JSON string
grant_type_policy_rule_condition_instance = GrantTypePolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(GrantTypePolicyRuleCondition.to_json())

# convert the object into a dict
grant_type_policy_rule_condition_dict = grant_type_policy_rule_condition_instance.to_dict()
# create an instance of GrantTypePolicyRuleCondition from a dict
grant_type_policy_rule_condition_from_dict = GrantTypePolicyRuleCondition.from_dict(grant_type_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


