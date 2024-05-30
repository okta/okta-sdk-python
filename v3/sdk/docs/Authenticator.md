# Authenticator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**key** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**provider** | [**AuthenticatorProvider**](AuthenticatorProvider.md) |  | [optional] 
**settings** | [**AuthenticatorSettings**](AuthenticatorSettings.md) |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**AuthenticatorType**](AuthenticatorType.md) |  | [optional] 
**links** | [**AuthenticatorLinks**](AuthenticatorLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator import Authenticator

# TODO update the JSON string below
json = "{}"
# create an instance of Authenticator from a JSON string
authenticator_instance = Authenticator.from_json(json)
# print the JSON string representation of the object
print(Authenticator.to_json())

# convert the object into a dict
authenticator_dict = authenticator_instance.to_dict()
# create an instance of Authenticator from a dict
authenticator_form_dict = authenticator.from_dict(authenticator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


