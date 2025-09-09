# AuthenticatorIdentity

Represents a particular authenticator serving as a constraint on a method

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 

## Example

```python
from okta.models.authenticator_identity import AuthenticatorIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorIdentity from a JSON string
authenticator_identity_instance = AuthenticatorIdentity.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorIdentity.to_json())

# convert the object into a dict
authenticator_identity_dict = authenticator_identity_instance.to_dict()
# create an instance of AuthenticatorIdentity from a dict
authenticator_identity_from_dict = AuthenticatorIdentity.from_dict(authenticator_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


