# UserCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**PasswordCredential**](PasswordCredential.md) |  | [optional] 
**provider** | [**AuthenticationProvider**](AuthenticationProvider.md) |  | [optional] 
**recovery_question** | [**RecoveryQuestionCredential**](RecoveryQuestionCredential.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_credentials import UserCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of UserCredentials from a JSON string
user_credentials_instance = UserCredentials.from_json(json)
# print the JSON string representation of the object
print(UserCredentials.to_json())

# convert the object into a dict
user_credentials_dict = user_credentials_instance.to_dict()
# create an instance of UserCredentials from a dict
user_credentials_from_dict = UserCredentials.from_dict(user_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


