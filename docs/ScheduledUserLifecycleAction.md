# ScheduledUserLifecycleAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PolicyUserStatus**](PolicyUserStatus.md) |  | [optional] 

## Example

```python
from okta.models.scheduled_user_lifecycle_action import ScheduledUserLifecycleAction

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledUserLifecycleAction from a JSON string
scheduled_user_lifecycle_action_instance = ScheduledUserLifecycleAction.from_json(json)
# print the JSON string representation of the object
print(ScheduledUserLifecycleAction.to_json())

# convert the object into a dict
scheduled_user_lifecycle_action_dict = scheduled_user_lifecycle_action_instance.to_dict()
# create an instance of ScheduledUserLifecycleAction from a dict
scheduled_user_lifecycle_action_from_dict = ScheduledUserLifecycleAction.from_dict(scheduled_user_lifecycle_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


