# LogStreamSplunkPutSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**LogStreamSettingsSplunkPut**](LogStreamSettingsSplunkPut.md) |  | 

## Example

```python
from okta.models.log_stream_splunk_put_schema import LogStreamSplunkPutSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamSplunkPutSchema from a JSON string
log_stream_splunk_put_schema_instance = LogStreamSplunkPutSchema.from_json(json)
# print the JSON string representation of the object
print(LogStreamSplunkPutSchema.to_json())

# convert the object into a dict
log_stream_splunk_put_schema_dict = log_stream_splunk_put_schema_instance.to_dict()
# create an instance of LogStreamSplunkPutSchema from a dict
log_stream_splunk_put_schema_from_dict = LogStreamSplunkPutSchema.from_dict(log_stream_splunk_put_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


