# InlineHookCreate

An inline hook object that specifies the details of the inline hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**InlineHookChannelCreate**](InlineHookChannelCreate.md) |  | [optional] 
**name** | **str** | The display name of the inline hook | [optional] 
**type** | [**InlineHookType**](InlineHookType.md) |  | [optional] 
**version** | **str** | Version of the inline hook type. The currently supported version is &#x60;1.0.0&#x60;. | [optional] 

## Example

```python
from okta.models.inline_hook_create import InlineHookCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookCreate from a JSON string
inline_hook_create_instance = InlineHookCreate.from_json(json)
# print the JSON string representation of the object
print(InlineHookCreate.to_json())

# convert the object into a dict
inline_hook_create_dict = inline_hook_create_instance.to_dict()
# create an instance of InlineHookCreate from a dict
inline_hook_create_from_dict = InlineHookCreate.from_dict(inline_hook_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


