# RegistrationInlineHookRequest

Registration inline hook request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of inline hook. The registration inline hook type is &#x60;com.okta.user.pre-registration&#x60;. | [optional] 
**request_type** | [**RegistrationInlineHookRequestType**](RegistrationInlineHookRequestType.md) |  | [optional] 
**source** | **str** | The ID of the registration inline hook | [optional] 

## Example

```python
from okta.models.registration_inline_hook_request import RegistrationInlineHookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHookRequest from a JSON string
registration_inline_hook_request_instance = RegistrationInlineHookRequest.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHookRequest.to_json())

# convert the object into a dict
registration_inline_hook_request_dict = registration_inline_hook_request_instance.to_dict()
# create an instance of RegistrationInlineHookRequest from a dict
registration_inline_hook_request_from_dict = RegistrationInlineHookRequest.from_dict(registration_inline_hook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


