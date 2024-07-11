# LogStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the Log Stream object was created | [readonly] 
**id** | **str** | Unique identifier for the Log Stream | [readonly] 
**last_updated** | **datetime** | Timestamp when the Log Stream object was last updated | [readonly] 
**name** | **str** | Unique name for the Log Stream object | 
**status** | **str** | Lifecycle status of the Log Stream object | [readonly] 
**type** | [**LogStreamType**](LogStreamType.md) |  | 
**links** | [**LogStreamLinksSelfAndLifecycle**](LogStreamLinksSelfAndLifecycle.md) |  | 

## Example

```python
from openapi_client.models.log_stream import LogStream

# TODO update the JSON string below
json = "{}"
# create an instance of LogStream from a JSON string
log_stream_instance = LogStream.from_json(json)
# print the JSON string representation of the object
print(LogStream.to_json())

# convert the object into a dict
log_stream_dict = log_stream_instance.to_dict()
# create an instance of LogStream from a dict
log_stream_from_dict = LogStream.from_dict(log_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


