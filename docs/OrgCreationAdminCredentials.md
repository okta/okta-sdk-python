# OrgCreationAdminCredentials

Specifies primary authentication and recovery credentials for a user. Credential types and requirements vary depending on the provider and security policy of the org.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**OrgCreationAdminCredentialsPassword**](OrgCreationAdminCredentialsPassword.md) |  | [optional] 
**recovery_question** | [**RecoveryQuestionCredential**](RecoveryQuestionCredential.md) |  | [optional] 

## Example

```python
from okta.models.org_creation_admin_credentials import OrgCreationAdminCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCreationAdminCredentials from a JSON string
org_creation_admin_credentials_instance = OrgCreationAdminCredentials.from_json(json)
# print the JSON string representation of the object
print(OrgCreationAdminCredentials.to_json())

# convert the object into a dict
org_creation_admin_credentials_dict = org_creation_admin_credentials_instance.to_dict()
# create an instance of OrgCreationAdminCredentials from a dict
org_creation_admin_credentials_from_dict = OrgCreationAdminCredentials.from_dict(org_creation_admin_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


