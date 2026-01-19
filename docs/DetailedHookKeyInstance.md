# DetailedHookKeyInstance

A key object with public key details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the key was created | [optional] [readonly] 
**id** | **str** | The unique Okta ID of this key record | [optional] [readonly] 
**is_used** | **bool** | Whether this key is currently in use by other applications | [optional] [readonly] 
**key_id** | **str** | The alias of the public key | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the key was updated | [optional] [readonly] 
**name** | **str** | Display name of the key | [optional] 
**embedded** | [**Embedded**](Embedded.md) |  | [optional] 

## Example

```python
from okta.models.detailed_hook_key_instance import DetailedHookKeyInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedHookKeyInstance from a JSON string
detailed_hook_key_instance_instance = DetailedHookKeyInstance.from_json(json)
# print the JSON string representation of the object
print(DetailedHookKeyInstance.to_json())

# convert the object into a dict
detailed_hook_key_instance_dict = detailed_hook_key_instance_instance.to_dict()
# create an instance of DetailedHookKeyInstance from a dict
detailed_hook_key_instance_from_dict = DetailedHookKeyInstance.from_dict(detailed_hook_key_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


