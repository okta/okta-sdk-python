# InlineHookResponseCommandValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.inline_hook_response_command_value import InlineHookResponseCommandValue

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookResponseCommandValue from a JSON string
inline_hook_response_command_value_instance = InlineHookResponseCommandValue.from_json(json)
# print the JSON string representation of the object
print(InlineHookResponseCommandValue.to_json())

# convert the object into a dict
inline_hook_response_command_value_dict = inline_hook_response_command_value_instance.to_dict()
# create an instance of InlineHookResponseCommandValue from a dict
inline_hook_response_command_value_form_dict = inline_hook_response_command_value.from_dict(inline_hook_response_command_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


