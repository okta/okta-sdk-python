# InlineHookCreateResponse

An inline hook object that specifies the details of the inline hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**InlineHookChannel**](InlineHookChannel.md) |  | [optional] 
**created** | **datetime** | Date of the inline hook creation | [optional] [readonly] 
**id** | **str** | The unique identifier for the inline hook | [optional] [readonly] 
**last_updated** | **datetime** | Date of the last inline hook update | [optional] [readonly] 
**name** | **str** | The display name of the inline hook | [optional] 
**status** | [**InlineHookStatus**](InlineHookStatus.md) |  | [optional] 
**type** | [**InlineHookType**](InlineHookType.md) |  | [optional] 
**version** | **str** | Version of the inline hook type. The currently supported version is &#x60;1.0.0&#x60;. | [optional] [readonly] 
**links** | [**InlineHookLinksCreate**](InlineHookLinksCreate.md) |  | [optional] 

## Example

```python
from okta.models.inline_hook_create_response import InlineHookCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookCreateResponse from a JSON string
inline_hook_create_response_instance = InlineHookCreateResponse.from_json(json)
# print the JSON string representation of the object
print(InlineHookCreateResponse.to_json())

# convert the object into a dict
inline_hook_create_response_dict = inline_hook_create_response_instance.to_dict()
# create an instance of InlineHookCreateResponse from a dict
inline_hook_create_response_from_dict = InlineHookCreateResponse.from_dict(inline_hook_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


