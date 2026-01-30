# AuthenticatorKeyOktaVerify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorKeyOktaVerifyAllOfSettings**](AuthenticatorKeyOktaVerifyAllOfSettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_okta_verify import AuthenticatorKeyOktaVerify

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyOktaVerify from a JSON string
authenticator_key_okta_verify_instance = AuthenticatorKeyOktaVerify.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyOktaVerify.to_json())

# convert the object into a dict
authenticator_key_okta_verify_dict = authenticator_key_okta_verify_instance.to_dict()
# create an instance of AuthenticatorKeyOktaVerify from a dict
authenticator_key_okta_verify_from_dict = AuthenticatorKeyOktaVerify.from_dict(authenticator_key_okta_verify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


