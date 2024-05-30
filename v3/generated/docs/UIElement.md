# UIElement

Specifies the configuration of an input field on an enrollment form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label name for the UI element | [optional] 
**options** | [**UIElementOptions**](UIElementOptions.md) |  | [optional] 
**scope** | **str** | Specifies the property bound to the input field. It must follow the format &#x60;#/properties/PROPERTY_NAME&#x60; where &#x60;PROPERTY_NAME&#x60; is a variable name for an attribute in &#x60;profile editor&#x60;. | [optional] 
**type** | **str** | Specifies the relationship between this input element and &#x60;scope&#x60;. The &#x60;Control&#x60; value specifies that this input controls the value represented by &#x60;scope&#x60;. | [optional] 

## Example

```python
from openapi_client.models.ui_element import UIElement

# TODO update the JSON string below
json = "{}"
# create an instance of UIElement from a JSON string
ui_element_instance = UIElement.from_json(json)
# print the JSON string representation of the object
print(UIElement.to_json())

# convert the object into a dict
ui_element_dict = ui_element_instance.to_dict()
# create an instance of UIElement from a dict
ui_element_form_dict = ui_element.from_dict(ui_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


