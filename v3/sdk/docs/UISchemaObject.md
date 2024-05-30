# UISchemaObject

Properties of the UI schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_label** | **str** | Specifies the button label for the &#x60;Submit&#x60; button at the bottom of the enrollment form. | [optional] [default to 'Submit']
**elements** | **object** |  | [optional] 
**label** | **str** | Specifies the label at the top of the enrollment form under the logo. | [optional] [default to 'Sign in']
**type** | **str** | Specifies the type of layout | [optional] 

## Example

```python
from openapi_client.models.ui_schema_object import UISchemaObject

# TODO update the JSON string below
json = "{}"
# create an instance of UISchemaObject from a JSON string
ui_schema_object_instance = UISchemaObject.from_json(json)
# print the JSON string representation of the object
print(UISchemaObject.to_json())

# convert the object into a dict
ui_schema_object_dict = ui_schema_object_instance.to_dict()
# create an instance of UISchemaObject from a dict
ui_schema_object_form_dict = ui_schema_object.from_dict(ui_schema_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


