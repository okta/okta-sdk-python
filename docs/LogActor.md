# LogActor

Describes the user, app, client, or other entity (actor) who performs an action on a target. The actor is dependent on the action that is performed. All events have actors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_id** | **str** | Alternative ID of the actor | [optional] [readonly] 
**detail_entry** | **Dict[str, object]** | Further details about the actor | [optional] [readonly] 
**display_name** | **str** | Display name of the actor | [optional] [readonly] 
**id** | **str** | ID of the actor | [optional] [readonly] 
**type** | **str** | Type of actor | [optional] [readonly] 

## Example

```python
from okta.models.log_actor import LogActor

# TODO update the JSON string below
json = "{}"
# create an instance of LogActor from a JSON string
log_actor_instance = LogActor.from_json(json)
# print the JSON string representation of the object
print(LogActor.to_json())

# convert the object into a dict
log_actor_dict = log_actor_instance.to_dict()
# create an instance of LogActor from a dict
log_actor_from_dict = LogActor.from_dict(log_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


