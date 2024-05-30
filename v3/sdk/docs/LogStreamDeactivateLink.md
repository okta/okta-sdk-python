# LogStreamDeactivateLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of the resource | 
**method** | **str** | HTTP method allowed for the resource | [optional] 

## Example

```python
from openapi_client.models.log_stream_deactivate_link import LogStreamDeactivateLink

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamDeactivateLink from a JSON string
log_stream_deactivate_link_instance = LogStreamDeactivateLink.from_json(json)
# print the JSON string representation of the object
print(LogStreamDeactivateLink.to_json())

# convert the object into a dict
log_stream_deactivate_link_dict = log_stream_deactivate_link_instance.to_dict()
# create an instance of LogStreamDeactivateLink from a dict
log_stream_deactivate_link_form_dict = log_stream_deactivate_link.from_dict(log_stream_deactivate_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


