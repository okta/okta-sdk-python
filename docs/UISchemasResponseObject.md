# UISchemasResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the UI Schema was created (ISO 86001) | [readonly] 
**id** | **str** | Unique identifier for the UI Schema | [readonly] 
**last_updated** | **datetime** | Timestamp when the UI Schema was last modified (ISO 86001) | [readonly] 
**ui_schema** | [**UISchemaObject**](UISchemaObject.md) |  | 
**links** | [**LinksSelf**](LinksSelf.md) |  | 

## Example

```python
from okta.models.ui_schemas_response_object import UISchemasResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of UISchemasResponseObject from a JSON string
ui_schemas_response_object_instance = UISchemasResponseObject.from_json(json)
# print the JSON string representation of the object
print(UISchemasResponseObject.to_json())

# convert the object into a dict
ui_schemas_response_object_dict = ui_schemas_response_object_instance.to_dict()
# create an instance of UISchemasResponseObject from a dict
ui_schemas_response_object_from_dict = UISchemasResponseObject.from_dict(ui_schemas_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


