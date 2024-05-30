# PolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the rule was created | [optional] [readonly] 
**id** | **str** | Identifier for the rule | [optional] 
**last_updated** | **datetime** | Timestamp when the rule was last modified | [optional] [readonly] 
**name** | **str** | Name of the rule | [optional] 
**priority** | **int** | Priority of the rule | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**system** | **bool** | Specifies whether Okta created the Policy Rule (&#x60;system&#x3D;true&#x60;). You can&#39;t delete Policy Rules that have &#x60;system&#x60; set to &#x60;true&#x60;. | [optional] [default to False]
**type** | [**PolicyRuleType**](PolicyRuleType.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_rule import PolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRule from a JSON string
policy_rule_instance = PolicyRule.from_json(json)
# print the JSON string representation of the object
print(PolicyRule.to_json())

# convert the object into a dict
policy_rule_dict = policy_rule_instance.to_dict()
# create an instance of PolicyRule from a dict
policy_rule_form_dict = policy_rule.from_dict(policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


