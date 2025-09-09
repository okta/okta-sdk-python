# HookKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the key was created. | [optional] [readonly] 
**id** | **str** | The unique identifier for the key. | [optional] [readonly] 
**is_used** | **bool** | Whether this key is currently in use by other hooks. | [optional] 
**key_id** | **str** | The alias of the public key. | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the key was updated. | [optional] [readonly] 
**name** | **str** | Display name of the key. | [optional] 
**embedded** | [**JsonWebKey**](JsonWebKey.md) |  | [optional] 

## Example

```python
from okta.models.hook_key import HookKey

# TODO update the JSON string below
json = "{}"
# create an instance of HookKey from a JSON string
hook_key_instance = HookKey.from_json(json)
# print the JSON string representation of the object
print(HookKey.to_json())

# convert the object into a dict
hook_key_dict = hook_key_instance.to_dict()
# create an instance of HookKey from a dict
hook_key_from_dict = HookKey.from_dict(hook_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


