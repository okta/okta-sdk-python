# GroupSchemaCustom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**properties** | [**Dict[str, GroupSchemaAttribute]**](GroupSchemaAttribute.md) |  | [optional] 
**required** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.group_schema_custom import GroupSchemaCustom

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaCustom from a JSON string
group_schema_custom_instance = GroupSchemaCustom.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaCustom.to_json())

# convert the object into a dict
group_schema_custom_dict = group_schema_custom_instance.to_dict()
# create an instance of GroupSchemaCustom from a dict
group_schema_custom_form_dict = group_schema_custom.from_dict(group_schema_custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


