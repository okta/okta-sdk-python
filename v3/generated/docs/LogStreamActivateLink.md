# LogStreamActivateLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of the resource | 
**method** | **str** | HTTP method allowed for the resource | [optional] 

## Example

```python
from openapi_client.models.log_stream_activate_link import LogStreamActivateLink

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamActivateLink from a JSON string
log_stream_activate_link_instance = LogStreamActivateLink.from_json(json)
# print the JSON string representation of the object
print(LogStreamActivateLink.to_json())

# convert the object into a dict
log_stream_activate_link_dict = log_stream_activate_link_instance.to_dict()
# create an instance of LogStreamActivateLink from a dict
log_stream_activate_link_form_dict = log_stream_activate_link.from_dict(log_stream_activate_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


