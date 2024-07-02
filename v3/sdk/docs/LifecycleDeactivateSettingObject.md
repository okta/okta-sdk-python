# LifecycleDeactivateSettingObject

Determines whether deprovisioning occurs when the app is unassigned

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.lifecycle_deactivate_setting_object import LifecycleDeactivateSettingObject

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleDeactivateSettingObject from a JSON string
lifecycle_deactivate_setting_object_instance = LifecycleDeactivateSettingObject.from_json(json)
# print the JSON string representation of the object
print(LifecycleDeactivateSettingObject.to_json())

# convert the object into a dict
lifecycle_deactivate_setting_object_dict = lifecycle_deactivate_setting_object_instance.to_dict()
# create an instance of LifecycleDeactivateSettingObject from a dict
lifecycle_deactivate_setting_object_from_dict = LifecycleDeactivateSettingObject.from_dict(lifecycle_deactivate_setting_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


