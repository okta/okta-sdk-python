# UIElementOptions

UI Schema element options object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Specifies how the input appears | [optional] 

## Example

```python
from okta.models.ui_element_options import UIElementOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UIElementOptions from a JSON string
ui_element_options_instance = UIElementOptions.from_json(json)
# print the JSON string representation of the object
print(UIElementOptions.to_json())

# convert the object into a dict
ui_element_options_dict = ui_element_options_instance.to_dict()
# create an instance of UIElementOptions from a dict
ui_element_options_from_dict = UIElementOptions.from_dict(ui_element_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


