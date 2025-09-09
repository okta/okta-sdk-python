# GroupPolicyRuleCondition

Specifies a set of Groups whose Users are to be included or excluded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Groups to be excluded | [optional] 
**include** | **List[str]** | Groups to be included | [optional] 

## Example

```python
from okta.models.group_policy_rule_condition import GroupPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPolicyRuleCondition from a JSON string
group_policy_rule_condition_instance = GroupPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(GroupPolicyRuleCondition.to_json())

# convert the object into a dict
group_policy_rule_condition_dict = group_policy_rule_condition_instance.to_dict()
# create an instance of GroupPolicyRuleCondition from a dict
group_policy_rule_condition_from_dict = GroupPolicyRuleCondition.from_dict(group_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


