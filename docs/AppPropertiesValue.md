# AppPropertiesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the property | [optional] 
**value** | **str** | Value of the property | [optional] 

## Example

```python
from okta.models.app_properties_value import AppPropertiesValue

# TODO update the JSON string below
json = "{}"
# create an instance of AppPropertiesValue from a JSON string
app_properties_value_instance = AppPropertiesValue.from_json(json)
# print the JSON string representation of the object
print(AppPropertiesValue.to_json())

# convert the object into a dict
app_properties_value_dict = app_properties_value_instance.to_dict()
# create an instance of AppPropertiesValue from a dict
app_properties_value_from_dict = AppPropertiesValue.from_dict(app_properties_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


