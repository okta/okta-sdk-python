# RegistrationInlineHookSSRDataAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**RegistrationInlineHookSSRDataAllOfDataContext**](RegistrationInlineHookSSRDataAllOfDataContext.md) |  | [optional] 
**action** | **str** | The default action the system will take. Will be &#x60;ALLOW&#x60;. &#x60;DENY&#x60; will never be sent to your external service. | [optional] 
**user_profile** | **Dict[str, object]** | The name-value pairs for each registration-related attribute supplied by the user in the Profile Enrollment form. | [optional] 

## Example

```python
from okta.models.registration_inline_hook_ssr_data_all_of_data import RegistrationInlineHookSSRDataAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHookSSRDataAllOfData from a JSON string
registration_inline_hook_ssr_data_all_of_data_instance = RegistrationInlineHookSSRDataAllOfData.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHookSSRDataAllOfData.to_json())

# convert the object into a dict
registration_inline_hook_ssr_data_all_of_data_dict = registration_inline_hook_ssr_data_all_of_data_instance.to_dict()
# create an instance of RegistrationInlineHookSSRDataAllOfData from a dict
registration_inline_hook_ssr_data_all_of_data_from_dict = RegistrationInlineHookSSRDataAllOfData.from_dict(registration_inline_hook_ssr_data_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


