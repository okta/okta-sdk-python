# CapabilitiesUpdateObject

Determines whether updates to a user's profile are pushed to the app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifecycle_deactivate** | [**LifecycleDeactivateSettingObject**](LifecycleDeactivateSettingObject.md) |  | [optional] 
**password** | [**PasswordSettingObject**](PasswordSettingObject.md) |  | [optional] 
**profile** | [**ProfileSettingObject**](ProfileSettingObject.md) |  | [optional] 

## Example

```python
from okta.models.capabilities_update_object import CapabilitiesUpdateObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesUpdateObject from a JSON string
capabilities_update_object_instance = CapabilitiesUpdateObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesUpdateObject.to_json())

# convert the object into a dict
capabilities_update_object_dict = capabilities_update_object_instance.to_dict()
# create an instance of CapabilitiesUpdateObject from a dict
capabilities_update_object_from_dict = CapabilitiesUpdateObject.from_dict(capabilities_update_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


