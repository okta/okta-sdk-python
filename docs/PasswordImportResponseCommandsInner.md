# PasswordImportResponseCommandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | The location where you specify the command. For the password import inline hook, there&#39;s only one command, &#x60;com.okta.action.update&#x60;. | [optional] 
**value** | [**PasswordImportResponseCommandsInnerValue**](PasswordImportResponseCommandsInnerValue.md) |  | [optional] 

## Example

```python
from okta.models.password_import_response_commands_inner import PasswordImportResponseCommandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportResponseCommandsInner from a JSON string
password_import_response_commands_inner_instance = PasswordImportResponseCommandsInner.from_json(json)
# print the JSON string representation of the object
print(PasswordImportResponseCommandsInner.to_json())

# convert the object into a dict
password_import_response_commands_inner_dict = password_import_response_commands_inner_instance.to_dict()
# create an instance of PasswordImportResponseCommandsInner from a dict
password_import_response_commands_inner_from_dict = PasswordImportResponseCommandsInner.from_dict(password_import_response_commands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


