# AppAndInstanceConditionEvaluatorAppOrInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the app | [optional] 
**name** | **str** | Name of the app type | [optional] 
**type** | [**AppAndInstanceType**](AppAndInstanceType.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_and_instance_condition_evaluator_app_or_instance import AppAndInstanceConditionEvaluatorAppOrInstance

# TODO update the JSON string below
json = "{}"
# create an instance of AppAndInstanceConditionEvaluatorAppOrInstance from a JSON string
app_and_instance_condition_evaluator_app_or_instance_instance = AppAndInstanceConditionEvaluatorAppOrInstance.from_json(json)
# print the JSON string representation of the object
print(AppAndInstanceConditionEvaluatorAppOrInstance.to_json())

# convert the object into a dict
app_and_instance_condition_evaluator_app_or_instance_dict = app_and_instance_condition_evaluator_app_or_instance_instance.to_dict()
# create an instance of AppAndInstanceConditionEvaluatorAppOrInstance from a dict
app_and_instance_condition_evaluator_app_or_instance_from_dict = AppAndInstanceConditionEvaluatorAppOrInstance.from_dict(app_and_instance_condition_evaluator_app_or_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


