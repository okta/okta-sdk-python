# RegistrationInlineHookPPData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**RegistrationInlineHookPPDataAllOfData**](RegistrationInlineHookPPDataAllOfData.md) |  | [optional] 

## Example

```python
from okta.models.registration_inline_hook_pp_data import RegistrationInlineHookPPData

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHookPPData from a JSON string
registration_inline_hook_pp_data_instance = RegistrationInlineHookPPData.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHookPPData.to_json())

# convert the object into a dict
registration_inline_hook_pp_data_dict = registration_inline_hook_pp_data_instance.to_dict()
# create an instance of RegistrationInlineHookPPData from a dict
registration_inline_hook_pp_data_from_dict = RegistrationInlineHookPPData.from_dict(registration_inline_hook_pp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


