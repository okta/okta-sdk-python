# AuthenticatorMethodBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**AuthenticatorMethodType**](AuthenticatorMethodType.md) |  | [optional] 
**links** | [**LinksSelfAndLifecycle**](LinksSelfAndLifecycle.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_base import AuthenticatorMethodBase

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodBase from a JSON string
authenticator_method_base_instance = AuthenticatorMethodBase.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodBase.to_json())

# convert the object into a dict
authenticator_method_base_dict = authenticator_method_base_instance.to_dict()
# create an instance of AuthenticatorMethodBase from a dict
authenticator_method_base_form_dict = authenticator_method_base.from_dict(authenticator_method_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


