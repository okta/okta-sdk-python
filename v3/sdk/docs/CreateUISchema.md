# CreateUISchema

The request body properties for the new UI Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ui_schema** | [**UISchemaObject**](.md) |  | [optional] 

## Example

```python
from okta.models.create_ui_schema import CreateUISchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUISchema from a JSON string
create_ui_schema_instance = CreateUISchema.from_json(json)
# print the JSON string representation of the object
print(CreateUISchema.to_json())

# convert the object into a dict
create_ui_schema_dict = create_ui_schema_instance.to_dict()
# create an instance of CreateUISchema from a dict
create_ui_schema_from_dict = CreateUISchema.from_dict(create_ui_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


