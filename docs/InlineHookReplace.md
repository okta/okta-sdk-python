# InlineHookReplace

An inline hook object that specifies the details of the inline hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**InlineHookChannelCreate**](InlineHookChannelCreate.md) |  | [optional] 
**name** | **str** | The display name of the inline hook | [optional] 
**version** | **str** | Version of the inline hook type. The currently supported version is &#x60;1.0.0&#x60;. | [optional] 

## Example

```python
from okta.models.inline_hook_replace import InlineHookReplace

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookReplace from a JSON string
inline_hook_replace_instance = InlineHookReplace.from_json(json)
# print the JSON string representation of the object
print(InlineHookReplace.to_json())

# convert the object into a dict
inline_hook_replace_dict = inline_hook_replace_instance.to_dict()
# create an instance of InlineHookReplace from a dict
inline_hook_replace_from_dict = InlineHookReplace.from_dict(inline_hook_replace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


