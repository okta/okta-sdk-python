# LifecycleCreateSettingObject

Determines whether to update a user in the app when a user in Okta is updated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 

## Example

```python
from okta.models.lifecycle_create_setting_object import LifecycleCreateSettingObject

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleCreateSettingObject from a JSON string
lifecycle_create_setting_object_instance = LifecycleCreateSettingObject.from_json(json)
# print the JSON string representation of the object
print(LifecycleCreateSettingObject.to_json())

# convert the object into a dict
lifecycle_create_setting_object_dict = lifecycle_create_setting_object_instance.to_dict()
# create an instance of LifecycleCreateSettingObject from a dict
lifecycle_create_setting_object_from_dict = LifecycleCreateSettingObject.from_dict(lifecycle_create_setting_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


