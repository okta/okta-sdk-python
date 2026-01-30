# AuthenticatorKeyDuo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**AuthenticatorKeyDuoAllOfProvider**](AuthenticatorKeyDuoAllOfProvider.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_duo import AuthenticatorKeyDuo

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyDuo from a JSON string
authenticator_key_duo_instance = AuthenticatorKeyDuo.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyDuo.to_json())

# convert the object into a dict
authenticator_key_duo_dict = authenticator_key_duo_instance.to_dict()
# create an instance of AuthenticatorKeyDuo from a dict
authenticator_key_duo_from_dict = AuthenticatorKeyDuo.from_dict(authenticator_key_duo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


