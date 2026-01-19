# AuthenticatorKeySecurityQuestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorKeyPhoneAllOfSettings**](AuthenticatorKeyPhoneAllOfSettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_security_question import AuthenticatorKeySecurityQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeySecurityQuestion from a JSON string
authenticator_key_security_question_instance = AuthenticatorKeySecurityQuestion.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeySecurityQuestion.to_json())

# convert the object into a dict
authenticator_key_security_question_dict = authenticator_key_security_question_instance.to_dict()
# create an instance of AuthenticatorKeySecurityQuestion from a dict
authenticator_key_security_question_from_dict = AuthenticatorKeySecurityQuestion.from_dict(authenticator_key_security_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


