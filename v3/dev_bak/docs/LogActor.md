# LogActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_id** | **str** |  | [optional] [readonly] 
**detail_entry** | **Dict[str, object]** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.log_actor import LogActor

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


