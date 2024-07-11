# CapabilitiesObject

Defines the configurations related to an application feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**CapabilitiesCreateObject**](CapabilitiesCreateObject.md) |  | [optional] 
**update** | [**CapabilitiesUpdateObject**](CapabilitiesUpdateObject.md) |  | [optional] 

## Example

```python
from okta.models.capabilities_object import CapabilitiesObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesObject from a JSON string
capabilities_object_instance = CapabilitiesObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesObject.to_json())

# convert the object into a dict
capabilities_object_dict = capabilities_object_instance.to_dict()
# create an instance of CapabilitiesObject from a dict
capabilities_object_from_dict = CapabilitiesObject.from_dict(capabilities_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


