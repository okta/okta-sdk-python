# LifecycleExpirationPolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifecycle_status** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.lifecycle_expiration_policy_rule_condition import LifecycleExpirationPolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleExpirationPolicyRuleCondition from a JSON string
lifecycle_expiration_policy_rule_condition_instance = LifecycleExpirationPolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(LifecycleExpirationPolicyRuleCondition.to_json())

# convert the object into a dict
lifecycle_expiration_policy_rule_condition_dict = lifecycle_expiration_policy_rule_condition_instance.to_dict()
# create an instance of LifecycleExpirationPolicyRuleCondition from a dict
lifecycle_expiration_policy_rule_condition_from_dict = LifecycleExpirationPolicyRuleCondition.from_dict(lifecycle_expiration_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


