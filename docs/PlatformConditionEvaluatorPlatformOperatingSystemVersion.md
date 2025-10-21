# PlatformConditionEvaluatorPlatformOperatingSystemVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | [**PlatformConditionOperatingSystemVersionMatchType**](PlatformConditionOperatingSystemVersionMatchType.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from okta.models.platform_condition_evaluator_platform_operating_system_version import PlatformConditionEvaluatorPlatformOperatingSystemVersion

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConditionEvaluatorPlatformOperatingSystemVersion from a JSON string
platform_condition_evaluator_platform_operating_system_version_instance = PlatformConditionEvaluatorPlatformOperatingSystemVersion.from_json(json)
# print the JSON string representation of the object
print(PlatformConditionEvaluatorPlatformOperatingSystemVersion.to_json())

# convert the object into a dict
platform_condition_evaluator_platform_operating_system_version_dict = platform_condition_evaluator_platform_operating_system_version_instance.to_dict()
# create an instance of PlatformConditionEvaluatorPlatformOperatingSystemVersion from a dict
platform_condition_evaluator_platform_operating_system_version_from_dict = PlatformConditionEvaluatorPlatformOperatingSystemVersion.from_dict(platform_condition_evaluator_platform_operating_system_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


