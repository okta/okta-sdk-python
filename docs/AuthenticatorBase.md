# AuthenticatorBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the authenticator was created | [optional] [readonly] 
**id** | **str** | A unique identifier for the authenticator | [optional] [readonly] 
**key** | [**AuthenticatorKeyEnum**](AuthenticatorKeyEnum.md) |  | [optional] 
**last_updated** | **datetime** | Timestamp when the authenticator was last modified | [optional] [readonly] 
**name** | **str** | Display name of the authenticator | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**AuthenticatorType**](AuthenticatorType.md) |  | [optional] 
**links** | [**AuthenticatorLinks**](AuthenticatorLinks.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_base import AuthenticatorBase

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorBase from a JSON string
authenticator_base_instance = AuthenticatorBase.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorBase.to_json())

# convert the object into a dict
authenticator_base_dict = authenticator_base_instance.to_dict()
# create an instance of AuthenticatorBase from a dict
authenticator_base_from_dict = AuthenticatorBase.from_dict(authenticator_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


