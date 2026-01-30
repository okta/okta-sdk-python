# PasswordCredential

Specifies a password for a user.  When a user has a valid password, imported hashed password, or password hook, and a response object contains a password credential, then the password object is a bare object without the value property defined (for example, `password: {}`). This indicates that a password value exists. You can modify password policy requirements in the Admin Console by editing the Password authenticator:  **Security** > **Authenticators** > **Password** (or for Okta Classic orgs, use **Security** > **Authentication** > **Password**).  For information on defaults and configuring your password policies, see [Configure the password authenticator](https://help.okta.com/okta_help.htm?type=oie&id=ext-configure-password) in the help documentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | [**PasswordCredentialHash**](PasswordCredentialHash.md) |  | [optional] 
**hook** | [**PasswordCredentialHook**](PasswordCredentialHook.md) |  | [optional] 
**value** | **str** | Specifies the password for a user. The password policy validates this password. | [optional] 

## Example

```python
from okta.models.password_credential import PasswordCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordCredential from a JSON string
password_credential_instance = PasswordCredential.from_json(json)
# print the JSON string representation of the object
print(PasswordCredential.to_json())

# convert the object into a dict
password_credential_dict = password_credential_instance.to_dict()
# create an instance of PasswordCredential from a dict
password_credential_from_dict = PasswordCredential.from_dict(password_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


