# UserLifecycleAttributePolicyRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** |  | [optional] 
**matching_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_lifecycle_attribute_policy_rule_condition import UserLifecycleAttributePolicyRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of UserLifecycleAttributePolicyRuleCondition from a JSON string
user_lifecycle_attribute_policy_rule_condition_instance = UserLifecycleAttributePolicyRuleCondition.from_json(json)
# print the JSON string representation of the object
print(UserLifecycleAttributePolicyRuleCondition.to_json())

# convert the object into a dict
user_lifecycle_attribute_policy_rule_condition_dict = user_lifecycle_attribute_policy_rule_condition_instance.to_dict()
# create an instance of UserLifecycleAttributePolicyRuleCondition from a dict
user_lifecycle_attribute_policy_rule_condition_form_dict = user_lifecycle_attribute_policy_rule_condition.from_dict(user_lifecycle_attribute_policy_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


