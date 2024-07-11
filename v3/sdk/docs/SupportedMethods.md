# SupportedMethods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SupportedMethodsSettings**](SupportedMethodsSettings.md) |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from okta.models.supported_methods import SupportedMethods

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedMethods from a JSON string
supported_methods_instance = SupportedMethods.from_json(json)
# print the JSON string representation of the object
print(SupportedMethods.to_json())

# convert the object into a dict
supported_methods_dict = supported_methods_instance.to_dict()
# create an instance of SupportedMethods from a dict
supported_methods_from_dict = SupportedMethods.from_dict(supported_methods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


