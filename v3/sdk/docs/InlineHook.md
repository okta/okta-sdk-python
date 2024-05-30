# InlineHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**InlineHookChannel**](InlineHookChannel.md) |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**status** | [**InlineHookStatus**](InlineHookStatus.md) |  | [optional] 
**type** | [**InlineHookType**](InlineHookType.md) |  | [optional] 
**version** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.inline_hook import InlineHook

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHook from a JSON string
inline_hook_instance = InlineHook.from_json(json)
# print the JSON string representation of the object
print(InlineHook.to_json())

# convert the object into a dict
inline_hook_dict = inline_hook_instance.to_dict()
# create an instance of InlineHook from a dict
inline_hook_form_dict = inline_hook.from_dict(inline_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


