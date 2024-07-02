# SelfServicePasswordResetAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**PolicyAccess**](PolicyAccess.md) |  | [optional] 
**type** | **str** | The type of rule action | [optional] [readonly] 
**requirement** | [**SsprRequirement**](SsprRequirement.md) |  | [optional] 

## Example

```python
from openapi_client.models.self_service_password_reset_action import SelfServicePasswordResetAction

# TODO update the JSON string below
json = "{}"
# create an instance of SelfServicePasswordResetAction from a JSON string
self_service_password_reset_action_instance = SelfServicePasswordResetAction.from_json(json)
# print the JSON string representation of the object
print(SelfServicePasswordResetAction.to_json())

# convert the object into a dict
self_service_password_reset_action_dict = self_service_password_reset_action_instance.to_dict()
# create an instance of SelfServicePasswordResetAction from a dict
self_service_password_reset_action_from_dict = SelfServicePasswordResetAction.from_dict(self_service_password_reset_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


