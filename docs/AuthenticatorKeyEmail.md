# AuthenticatorKeyEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorKeyEmailAllOfSettings**](AuthenticatorKeyEmailAllOfSettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_email import AuthenticatorKeyEmail

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyEmail from a JSON string
authenticator_key_email_instance = AuthenticatorKeyEmail.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyEmail.to_json())

# convert the object into a dict
authenticator_key_email_dict = authenticator_key_email_instance.to_dict()
# create an instance of AuthenticatorKeyEmail from a dict
authenticator_key_email_from_dict = AuthenticatorKeyEmail.from_dict(authenticator_key_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


