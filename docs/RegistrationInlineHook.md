# RegistrationInlineHook


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
**links** | [**InlineHookLinks**](InlineHookLinks.md) |  | [optional] 

## Example

```python
from okta.models.registration_inline_hook import RegistrationInlineHook

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHook from a JSON string
registration_inline_hook_instance = RegistrationInlineHook.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHook.to_json())

# convert the object into a dict
registration_inline_hook_dict = registration_inline_hook_instance.to_dict()
# create an instance of RegistrationInlineHook from a dict
registration_inline_hook_from_dict = RegistrationInlineHook.from_dict(registration_inline_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


