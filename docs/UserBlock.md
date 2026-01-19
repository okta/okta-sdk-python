# UserBlock

Describes how the account is blocked from access. If `appliesTo` is `ANY_DEVICES`, then the account is blocked for all devices. If `appliesTo` is `UNKNOWN_DEVICES`, then the account is only blocked for unknown devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applies_to** | **str** | The devices that the block applies to | [optional] [readonly] 
**type** | **str** | Type of access block | [optional] [readonly] 

## Example

```python
from okta.models.user_block import UserBlock

# TODO update the JSON string below
json = "{}"
# create an instance of UserBlock from a JSON string
user_block_instance = UserBlock.from_json(json)
# print the JSON string representation of the object
print(UserBlock.to_json())

# convert the object into a dict
user_block_dict = user_block_instance.to_dict()
# create an instance of UserBlock from a dict
user_block_from_dict = UserBlock.from_dict(user_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


