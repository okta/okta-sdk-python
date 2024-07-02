# AuthenticatorMethodConstraint

Limits the authenticators that can be used for a given method. Currently, only the `otp` method supports constraints, and Google authenticator (key : 'google_otp') is the only allowed authenticator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**allowed_authenticators** | [**List[AuthenticatorIdentity]**](AuthenticatorIdentity.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_constraint import AuthenticatorMethodConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodConstraint from a JSON string
authenticator_method_constraint_instance = AuthenticatorMethodConstraint.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodConstraint.to_json())

# convert the object into a dict
authenticator_method_constraint_dict = authenticator_method_constraint_instance.to_dict()
# create an instance of AuthenticatorMethodConstraint from a dict
authenticator_method_constraint_from_dict = AuthenticatorMethodConstraint.from_dict(authenticator_method_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


