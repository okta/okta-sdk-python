# RegistrationInlineHookResponse

Registration inline hook response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.registration_inline_hook_response import RegistrationInlineHookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHookResponse from a JSON string
registration_inline_hook_response_instance = RegistrationInlineHookResponse.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHookResponse.to_json())

# convert the object into a dict
registration_inline_hook_response_dict = registration_inline_hook_response_instance.to_dict()
# create an instance of RegistrationInlineHookResponse from a dict
registration_inline_hook_response_from_dict = RegistrationInlineHookResponse.from_dict(registration_inline_hook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


