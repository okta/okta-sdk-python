# RegistrationInlineHookPPDataAllOfDataContextUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_changed** | **datetime** | The last time the user&#39;s password was updated | [optional] 
**links** | [**BaseContextUserLinks**](BaseContextUserLinks.md) |  | [optional] 
**profile** | **Dict[str, object]** | The user to update&#39;s current attributes | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from okta.models.registration_inline_hook_pp_data_all_of_data_context_user import RegistrationInlineHookPPDataAllOfDataContextUser

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInlineHookPPDataAllOfDataContextUser from a JSON string
registration_inline_hook_pp_data_all_of_data_context_user_instance = RegistrationInlineHookPPDataAllOfDataContextUser.from_json(json)
# print the JSON string representation of the object
print(RegistrationInlineHookPPDataAllOfDataContextUser.to_json())

# convert the object into a dict
registration_inline_hook_pp_data_all_of_data_context_user_dict = registration_inline_hook_pp_data_all_of_data_context_user_instance.to_dict()
# create an instance of RegistrationInlineHookPPDataAllOfDataContextUser from a dict
registration_inline_hook_pp_data_all_of_data_context_user_from_dict = RegistrationInlineHookPPDataAllOfDataContextUser.from_dict(registration_inline_hook_pp_data_all_of_data_context_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


