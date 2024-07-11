# InlineHookResponseCommands


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**value** | [**List[InlineHookResponseCommandValue]**](InlineHookResponseCommandValue.md) |  | [optional] 

## Example

```python
from okta.models.inline_hook_response_commands import InlineHookResponseCommands

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookResponseCommands from a JSON string
inline_hook_response_commands_instance = InlineHookResponseCommands.from_json(json)
# print the JSON string representation of the object
print(InlineHookResponseCommands.to_json())

# convert the object into a dict
inline_hook_response_commands_dict = inline_hook_response_commands_instance.to_dict()
# create an instance of InlineHookResponseCommands from a dict
inline_hook_response_commands_from_dict = InlineHookResponseCommands.from_dict(inline_hook_response_commands_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


