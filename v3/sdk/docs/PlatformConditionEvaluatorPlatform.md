# PlatformConditionEvaluatorPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os** | [**PlatformConditionEvaluatorPlatformOperatingSystem**](PlatformConditionEvaluatorPlatformOperatingSystem.md) |  | [optional] 
**type** | [**PolicyPlatformType**](PolicyPlatformType.md) |  | [optional] 

## Example

```python
from openapi_client.models.platform_condition_evaluator_platform import PlatformConditionEvaluatorPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConditionEvaluatorPlatform from a JSON string
platform_condition_evaluator_platform_instance = PlatformConditionEvaluatorPlatform.from_json(json)
# print the JSON string representation of the object
print(PlatformConditionEvaluatorPlatform.to_json())

# convert the object into a dict
platform_condition_evaluator_platform_dict = platform_condition_evaluator_platform_instance.to_dict()
# create an instance of PlatformConditionEvaluatorPlatform from a dict
platform_condition_evaluator_platform_form_dict = platform_condition_evaluator_platform.from_dict(platform_condition_evaluator_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


