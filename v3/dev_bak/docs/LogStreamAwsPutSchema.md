# LogStreamAwsPutSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**LogStreamSettingsAws**](LogStreamSettingsAws.md) |  | 

## Example

```python
from openapi_client.models.log_stream_aws_put_schema import LogStreamAwsPutSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamAwsPutSchema from a JSON string
log_stream_aws_put_schema_instance = LogStreamAwsPutSchema.from_json(json)
# print the JSON string representation of the object
print(LogStreamAwsPutSchema.to_json())

# convert the object into a dict
log_stream_aws_put_schema_dict = log_stream_aws_put_schema_instance.to_dict()
# create an instance of LogStreamAwsPutSchema from a dict
log_stream_aws_put_schema_from_dict = LogStreamAwsPutSchema.from_dict(log_stream_aws_put_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


