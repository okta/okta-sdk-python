# BeforeScheduledActionPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**Duration**](Duration.md) |  | [optional] 
**lifecycle_action** | [**ScheduledUserLifecycleAction**](ScheduledUserLifecycleAction.md) |  | [optional] 

## Example

```python
from okta.models.before_scheduled_action_policy_rule_condition import BeforeScheduledActionPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of BeforeScheduledActionPolicyRuleCondition from a JSON string
before_scheduled_action_policy_rule_condition_instance = BeforeScheduledActionPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(BeforeScheduledActionPolicyRuleCondition.to_json())

# convert the object into a dict
before_scheduled_action_policy_rule_condition_dict = before_scheduled_action_policy_rule_condition_instance.to_dict()
# create an instance of BeforeScheduledActionPolicyRuleCondition from a dict
before_scheduled_action_policy_rule_condition_from_dict = BeforeScheduledActionPolicyRuleCondition.from_dict(before_scheduled_action_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


