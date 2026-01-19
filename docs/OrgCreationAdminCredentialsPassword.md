# OrgCreationAdminCredentialsPassword

Specifies a password for a user > **Note:** For information on defaults and configuring your password policies, see [Configure the password authenticator](https://help.okta.com/okta_help.htm?type=oie&id=ext-configure-password) in the help documentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Password value (which is validated by the password policy) | [optional] 

## Example

```python
from okta.models.org_creation_admin_credentials_password import OrgCreationAdminCredentialsPassword

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCreationAdminCredentialsPassword from a JSON string
org_creation_admin_credentials_password_instance = OrgCreationAdminCredentialsPassword.from_json(json)
# print the JSON string representation of the object
print(OrgCreationAdminCredentialsPassword.to_json())

# convert the object into a dict
org_creation_admin_credentials_password_dict = org_creation_admin_credentials_password_instance.to_dict()
# create an instance of OrgCreationAdminCredentialsPassword from a dict
org_creation_admin_credentials_password_from_dict = OrgCreationAdminCredentialsPassword.from_dict(org_creation_admin_credentials_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


