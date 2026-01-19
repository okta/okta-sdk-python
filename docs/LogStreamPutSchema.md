# LogStreamPutSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name for the log stream object | 
**type** | [**LogStreamType**](LogStreamType.md) |  | 

## Example

```python
from okta.models.log_stream_put_schema import LogStreamPutSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamPutSchema from a JSON string
log_stream_put_schema_instance = LogStreamPutSchema.from_json(json)
# print the JSON string representation of the object
print(LogStreamPutSchema.to_json())

# convert the object into a dict
log_stream_put_schema_dict = log_stream_put_schema_instance.to_dict()
# create an instance of LogStreamPutSchema from a dict
log_stream_put_schema_from_dict = LogStreamPutSchema.from_dict(log_stream_put_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


