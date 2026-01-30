# BehaviorRuleASN


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**BehaviorRuleSettingsAnomalousASN**](BehaviorRuleSettingsAnomalousASN.md) |  | [optional] 

## Example

```python
from okta.models.behavior_rule_asn import BehaviorRuleASN

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorRuleASN from a JSON string
behavior_rule_asn_instance = BehaviorRuleASN.from_json(json)
# print the JSON string representation of the object
print(BehaviorRuleASN.to_json())

# convert the object into a dict
behavior_rule_asn_dict = behavior_rule_asn_instance.to_dict()
# create an instance of BehaviorRuleASN from a dict
behavior_rule_asn_from_dict = BehaviorRuleASN.from_dict(behavior_rule_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


