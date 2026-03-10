# LogUserBehavior

The result of the user behavior detection models associated with the event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the user behavior detection model [configured by admins](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Behavior/) | [optional] [readonly] 
**id** | **str** | The unique identifier of the user behavior detection model | [optional] [readonly] 
**result** | **str** | The result of the user behavior analysis | [optional] [readonly] 

## Example

```python
from okta.models.log_user_behavior import LogUserBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of LogUserBehavior from a JSON string
log_user_behavior_instance = LogUserBehavior.from_json(json)
# print the JSON string representation of the object
print(LogUserBehavior.to_json())

# convert the object into a dict
log_user_behavior_dict = log_user_behavior_instance.to_dict()
# create an instance of LogUserBehavior from a dict
log_user_behavior_from_dict = LogUserBehavior.from_dict(log_user_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


