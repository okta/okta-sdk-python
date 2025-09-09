# ApplicationLayoutRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** |  | [optional] 
**condition** | [**ApplicationLayoutRuleCondition**](ApplicationLayoutRuleCondition.md) |  | [optional] 

## Example

```python
from okta.models.application_layout_rule import ApplicationLayoutRule

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLayoutRule from a JSON string
application_layout_rule_instance = ApplicationLayoutRule.from_json(json)
# print the JSON string representation of the object
print(ApplicationLayoutRule.to_json())

# convert the object into a dict
application_layout_rule_dict = application_layout_rule_instance.to_dict()
# create an instance of ApplicationLayoutRule from a dict
application_layout_rule_from_dict = ApplicationLayoutRule.from_dict(application_layout_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


