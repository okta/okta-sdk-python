# PlatformConditionEvaluatorPlatformOperatingSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** |  | [optional] 
**type** | [**PolicyPlatformOperatingSystemType**](PolicyPlatformOperatingSystemType.md) |  | [optional] 
**version** | [**PlatformConditionEvaluatorPlatformOperatingSystemVersion**](PlatformConditionEvaluatorPlatformOperatingSystemVersion.md) |  | [optional] 

## Example

```python
from openapi_client.models.platform_condition_evaluator_platform_operating_system import PlatformConditionEvaluatorPlatformOperatingSystem

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConditionEvaluatorPlatformOperatingSystem from a JSON string
platform_condition_evaluator_platform_operating_system_instance = PlatformConditionEvaluatorPlatformOperatingSystem.from_json(json)
# print the JSON string representation of the object
print(PlatformConditionEvaluatorPlatformOperatingSystem.to_json())

# convert the object into a dict
platform_condition_evaluator_platform_operating_system_dict = platform_condition_evaluator_platform_operating_system_instance.to_dict()
# create an instance of PlatformConditionEvaluatorPlatformOperatingSystem from a dict
platform_condition_evaluator_platform_operating_system_from_dict = PlatformConditionEvaluatorPlatformOperatingSystem.from_dict(platform_condition_evaluator_platform_operating_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


