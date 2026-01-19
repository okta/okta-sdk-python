# RegistrationInlineHookPPDataAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**RegistrationInlineHookPPDataAllOfDataContext**](RegistrationInlineHookPPDataAllOfDataContext.md) |  | [optional] 
**action** | **str** | The default action the system takes. Set to &#x60;ALLOW&#x60;. &#x60;DENY&#x60; is never sent to your external service | [optional] 
**user_profile_update** | **Dict[str, object]** | Name-value pairs for each new attribute supplied by the user in the Progressive Profile form | [optional] 

## Example

```python
from okta.models.registration_inline_hook_pp_data_all_of_data import RegistrationInlineHookPPDataAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHookPPDataAllOfData from a JSON string
registration_inline_hook_pp_data_all_of_data_instance = RegistrationInlineHookPPDataAllOfData.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHookPPDataAllOfData.to_json())

# convert the object into a dict
registration_inline_hook_pp_data_all_of_data_dict = registration_inline_hook_pp_data_all_of_data_instance.to_dict()
# create an instance of RegistrationInlineHookPPDataAllOfData from a dict
registration_inline_hook_pp_data_all_of_data_from_dict = RegistrationInlineHookPPDataAllOfData.from_dict(registration_inline_hook_pp_data_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


