# AppUserPasswordCredential

The user's password. This is a write-only property. An empty `password` object is returned to indicate that a password value exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Password value | [optional] 

## Example

```python
from okta.models.app_user_password_credential import AppUserPasswordCredential

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserPasswordCredential from a JSON string
app_user_password_credential_instance = AppUserPasswordCredential.from_json(json)
# print the JSON string representation of the object
print(AppUserPasswordCredential.to_json())

# convert the object into a dict
app_user_password_credential_dict = app_user_password_credential_instance.to_dict()
# create an instance of AppUserPasswordCredential from a dict
app_user_password_credential_from_dict = AppUserPasswordCredential.from_dict(app_user_password_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


