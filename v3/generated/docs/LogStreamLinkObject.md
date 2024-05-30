# LogStreamLinkObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of the resource | 
**method** | **str** | HTTP method allowed for the resource | [optional] 

## Example

```python
from openapi_client.models.log_stream_link_object import LogStreamLinkObject

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamLinkObject from a JSON string
log_stream_link_object_instance = LogStreamLinkObject.from_json(json)
# print the JSON string representation of the object
print(LogStreamLinkObject.to_json())

# convert the object into a dict
log_stream_link_object_dict = log_stream_link_object_instance.to_dict()
# create an instance of LogStreamLinkObject from a dict
log_stream_link_object_form_dict = log_stream_link_object.from_dict(log_stream_link_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


