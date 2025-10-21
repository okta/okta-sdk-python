# InlineHookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[InlineHookResponseCommands]**](InlineHookResponseCommands.md) |  | [optional] 

## Example

```python
from okta.models.inline_hook_response import InlineHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InlineHookResponse from a JSON string
inline_hook_response_instance = InlineHookResponse.from_json(json)
# print the JSON string representation of the object
print(InlineHookResponse.to_json())

# convert the object into a dict
inline_hook_response_dict = inline_hook_response_instance.to_dict()
# create an instance of InlineHookResponse from a dict
inline_hook_response_from_dict = InlineHookResponse.from_dict(inline_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


