# UpdateUISchema

The updated request body properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ui_schema** | [**UISchemaObject**](.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_ui_schema import UpdateUISchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUISchema from a JSON string
update_ui_schema_instance = UpdateUISchema.from_json(json)
# print the JSON string representation of the object
print(UpdateUISchema.to_json())

# convert the object into a dict
update_ui_schema_dict = update_ui_schema_instance.to_dict()
# create an instance of UpdateUISchema from a dict
update_ui_schema_form_dict = update_ui_schema.from_dict(update_ui_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


