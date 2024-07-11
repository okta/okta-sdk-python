# CapabilitiesCreateObject

Determines whether Okta assigns a new application account to each user managed by Okta.  Okta doesn't create a new account if it detects that the username specified in Okta already exists in the application. The user's Okta username is assigned by default. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifecycle_create** | [**LifecycleCreateSettingObject**](LifecycleCreateSettingObject.md) |  | [optional] 

## Example

```python
from okta.models.capabilities_create_object import CapabilitiesCreateObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesCreateObject from a JSON string
capabilities_create_object_instance = CapabilitiesCreateObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesCreateObject.to_json())

# convert the object into a dict
capabilities_create_object_dict = capabilities_create_object_instance.to_dict()
# create an instance of CapabilitiesCreateObject from a dict
capabilities_create_object_from_dict = CapabilitiesCreateObject.from_dict(capabilities_create_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


