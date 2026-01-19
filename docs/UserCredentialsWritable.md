# UserCredentialsWritable

Specifies primary authentication and recovery credentials for a user. Credential types and requirements vary depending on the provider and security policy of the org.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**PasswordCredential**](PasswordCredential.md) |  | [optional] 
**provider** | [**AuthenticationProviderWritable**](AuthenticationProviderWritable.md) |  | [optional] 
**recovery_question** | [**RecoveryQuestionCredential**](RecoveryQuestionCredential.md) |  | [optional] 

## Example

```python
from okta.models.user_credentials_writable import UserCredentialsWritable

# TODO update the JSON string below
json = "{}"
# create an instance of UserCredentialsWritable from a JSON string
user_credentials_writable_instance = UserCredentialsWritable.from_json(json)
# print the JSON string representation of the object
print(UserCredentialsWritable.to_json())

# convert the object into a dict
user_credentials_writable_dict = user_credentials_writable_instance.to_dict()
# create an instance of UserCredentialsWritable from a dict
user_credentials_writable_from_dict = UserCredentialsWritable.from_dict(user_credentials_writable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


