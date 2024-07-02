# LogStreamSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**error_message** | **object** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**properties** | **object** |  | [optional] 
**required** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.log_stream_schema import LogStreamSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamSchema from a JSON string
log_stream_schema_instance = LogStreamSchema.from_json(json)
# print the JSON string representation of the object
print(LogStreamSchema.to_json())

# convert the object into a dict
log_stream_schema_dict = log_stream_schema_instance.to_dict()
# create an instance of LogStreamSchema from a dict
log_stream_schema_from_dict = LogStreamSchema.from_dict(log_stream_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


