# BehaviorRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Timestamp when the Behavior Detection Rule was created | [optional] [readonly] 
**id** | **str** | ID of the Behavior Detection Rule | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the Behavior Detection Rule was last modified | [optional] [readonly] 
**name** | **str** | Name of the Behavior Detection Rule | 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**BehaviorRuleType**](BehaviorRuleType.md) |  | 
**link** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.behavior_rule import BehaviorRule

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRule from a JSON string
behavior_rule_instance = BehaviorRule.from_json(json)
# print the JSON string representation of the object
print(BehaviorRule.to_json())

# convert the object into a dict
behavior_rule_dict = behavior_rule_instance.to_dict()
# create an instance of BehaviorRule from a dict
behavior_rule_from_dict = BehaviorRule.from_dict(behavior_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


