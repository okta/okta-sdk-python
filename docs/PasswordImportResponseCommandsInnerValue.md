# PasswordImportResponseCommandsInnerValue

The parameter value of the command. * To indicate that the supplied credentials are valid, supply a type property set to `com.okta.action.update` together with a value property set to `{\"credential\": \"VERIFIED\"}`. * To indicate that the supplied credentials are invalid, supply a type property set to `com.okta.action.update` together with a value property set to `{\"credential\": \"UNVERIFIED\"}`. Alternatively, you can send an empty response (`204`). By default, the `data.action.credential` is always set to `UNVERIFIED`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | **str** |  | [optional] 

## Example

```python
from okta.models.password_import_response_commands_inner_value import PasswordImportResponseCommandsInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportResponseCommandsInnerValue from a JSON string
password_import_response_commands_inner_value_instance = PasswordImportResponseCommandsInnerValue.from_json(json)
# print the JSON string representation of the object
print(PasswordImportResponseCommandsInnerValue.to_json())

# convert the object into a dict
password_import_response_commands_inner_value_dict = password_import_response_commands_inner_value_instance.to_dict()
# create an instance of PasswordImportResponseCommandsInnerValue from a dict
password_import_response_commands_inner_value_from_dict = PasswordImportResponseCommandsInnerValue.from_dict(password_import_response_commands_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


