# UserIdentifierConditionEvaluatorPattern

Used in the User Identifier Condition object. Specifies the details of the patterns to match against.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | [**UserIdentifierMatchType**](UserIdentifierMatchType.md) |  | [optional] 
**value** | **str** | The regex expression of a simple match string | [optional] 

## Example

```python
from openapi_client.models.user_identifier_condition_evaluator_pattern import UserIdentifierConditionEvaluatorPattern

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentifierConditionEvaluatorPattern from a JSON string
user_identifier_condition_evaluator_pattern_instance = UserIdentifierConditionEvaluatorPattern.from_json(json)
# print the JSON string representation of the object
print(UserIdentifierConditionEvaluatorPattern.to_json())

# convert the object into a dict
user_identifier_condition_evaluator_pattern_dict = user_identifier_condition_evaluator_pattern_instance.to_dict()
# create an instance of UserIdentifierConditionEvaluatorPattern from a dict
user_identifier_condition_evaluator_pattern_form_dict = user_identifier_condition_evaluator_pattern.from_dict(user_identifier_condition_evaluator_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


