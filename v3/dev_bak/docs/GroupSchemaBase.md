# GroupSchemaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**properties** | [**GroupSchemaBaseProperties**](GroupSchemaBaseProperties.md) |  | [optional] 
**required** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.group_schema_base import GroupSchemaBase

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaBase from a JSON string
group_schema_base_instance = GroupSchemaBase.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaBase.to_json())

# convert the object into a dict
group_schema_base_dict = group_schema_base_instance.to_dict()
# create an instance of GroupSchemaBase from a dict
group_schema_base_from_dict = GroupSchemaBase.from_dict(group_schema_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


