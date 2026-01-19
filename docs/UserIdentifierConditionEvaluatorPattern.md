# UserIdentifierConditionEvaluatorPattern

Specifies the details of the patterns to match against

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | [**UserIdentifierMatchType**](UserIdentifierMatchType.md) |  | 
**value** | **str** | The regular expression or simple match string | 

## Example

```python
from okta.models.user_identifier_condition_evaluator_pattern import UserIdentifierConditionEvaluatorPattern

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentifierConditionEvaluatorPattern from a JSON string
user_identifier_condition_evaluator_pattern_instance = UserIdentifierConditionEvaluatorPattern.from_json(json)
# print the JSON string representation of the object
print(UserIdentifierConditionEvaluatorPattern.to_json())

# convert the object into a dict
user_identifier_condition_evaluator_pattern_dict = user_identifier_condition_evaluator_pattern_instance.to_dict()
# create an instance of UserIdentifierConditionEvaluatorPattern from a dict
user_identifier_condition_evaluator_pattern_from_dict = UserIdentifierConditionEvaluatorPattern.from_dict(user_identifier_condition_evaluator_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


