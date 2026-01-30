# PasswordCredentialHook

Specify a [password import inline hook](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/createPasswordImportInlineHook) to trigger verification of the user's password the first time the user signs in. This allows an existing password to be imported into Okta directly from some other store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of password inline hook. Currently, must be set to default. | [optional] 

## Example

```python
from okta.models.password_credential_hook import PasswordCredentialHook

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordCredentialHook from a JSON string
password_credential_hook_instance = PasswordCredentialHook.from_json(json)
# print the JSON string representation of the object
print(PasswordCredentialHook.to_json())

# convert the object into a dict
password_credential_hook_dict = password_credential_hook_instance.to_dict()
# create an instance of PasswordCredentialHook from a dict
password_credential_hook_from_dict = PasswordCredentialHook.from_dict(password_credential_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


