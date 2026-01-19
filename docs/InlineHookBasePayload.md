# InlineHookBasePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 

## Example

```python
from okta.models.inline_hook_base_payload import InlineHookBasePayload

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookBasePayload from a JSON string
inline_hook_base_payload_instance = InlineHookBasePayload.from_json(json)
# print the JSON string representation of the object
print(InlineHookBasePayload.to_json())

# convert the object into a dict
inline_hook_base_payload_dict = inline_hook_base_payload_instance.to_dict()
# create an instance of InlineHookBasePayload from a dict
inline_hook_base_payload_from_dict = InlineHookBasePayload.from_dict(inline_hook_base_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


