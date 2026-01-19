# AuthenticatorMethodTac


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**AuthenticatorMethodType**](AuthenticatorMethodType.md) |  | [optional] 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_method_tac import AuthenticatorMethodTac

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodTac from a JSON string
authenticator_method_tac_instance = AuthenticatorMethodTac.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodTac.to_json())

# convert the object into a dict
authenticator_method_tac_dict = authenticator_method_tac_instance.to_dict()
# create an instance of AuthenticatorMethodTac from a dict
authenticator_method_tac_from_dict = AuthenticatorMethodTac.from_dict(authenticator_method_tac_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


