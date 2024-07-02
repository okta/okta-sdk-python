# LogStreamLinksSelfAndLifecycle

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an application using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | [**LogStreamActivateLink**](LogStreamActivateLink.md) |  | [optional] 
**deactivate** | [**LogStreamDeactivateLink**](LogStreamDeactivateLink.md) |  | [optional] 
**var_self** | [**LogStreamSelfLink**](LogStreamSelfLink.md) |  | 

## Example

```python
from openapi_client.models.log_stream_links_self_and_lifecycle import LogStreamLinksSelfAndLifecycle

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamLinksSelfAndLifecycle from a JSON string
log_stream_links_self_and_lifecycle_instance = LogStreamLinksSelfAndLifecycle.from_json(json)
# print the JSON string representation of the object
print(LogStreamLinksSelfAndLifecycle.to_json())

# convert the object into a dict
log_stream_links_self_and_lifecycle_dict = log_stream_links_self_and_lifecycle_instance.to_dict()
# create an instance of LogStreamLinksSelfAndLifecycle from a dict
log_stream_links_self_and_lifecycle_from_dict = LogStreamLinksSelfAndLifecycle.from_dict(log_stream_links_self_and_lifecycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


