# AuthenticatorKeyTac


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**AuthenticatorKeyTacAllOfProvider**](AuthenticatorKeyTacAllOfProvider.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_tac import AuthenticatorKeyTac

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyTac from a JSON string
authenticator_key_tac_instance = AuthenticatorKeyTac.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyTac.to_json())

# convert the object into a dict
authenticator_key_tac_dict = authenticator_key_tac_instance.to_dict()
# create an instance of AuthenticatorKeyTac from a dict
authenticator_key_tac_from_dict = AuthenticatorKeyTac.from_dict(authenticator_key_tac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


