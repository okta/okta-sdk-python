# AutoUpdateSchedule

The schedule of auto-update configured by admin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** |  | [optional] 
**delay** | **int** | delay in days | [optional] 
**duration** | **int** | duration in minutes | [optional] 
**last_updated** | **datetime** | last time when the updated finished (success or failed, exclude cancelled), null if job haven&#39;t finished once yet. | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auto_update_schedule import AutoUpdateSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of AutoUpdateSchedule from a JSON string
auto_update_schedule_instance = AutoUpdateSchedule.from_json(json)
# print the JSON string representation of the object
print(AutoUpdateSchedule.to_json())

# convert the object into a dict
auto_update_schedule_dict = auto_update_schedule_instance.to_dict()
# create an instance of AutoUpdateSchedule from a dict
auto_update_schedule_from_dict = AutoUpdateSchedule.from_dict(auto_update_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


