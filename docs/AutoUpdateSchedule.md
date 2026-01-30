# AutoUpdateSchedule

The schedule of auto-update configured by the admin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** | The schedule of the update in cron format. The cron settings are limited to only the day of the month or the nth-day-of-the-week configurations. For example, &#x60;0 8 ? * 6#3&#x60; indicates every third Saturday at 8:00 AM. | [optional] 
**delay** | **int** | Delay in days | [optional] 
**duration** | **int** | Duration in minutes | [optional] 
**last_updated** | **datetime** | Timestamp when the update finished (only for a successful or failed update, not for a cancelled update). Null is returned if the job hasn&#39;t finished once yet. | [optional] 
**timezone** | **str** | Timezone of where the scheduled job takes place | [optional] 

## Example

```python
from okta.models.auto_update_schedule import AutoUpdateSchedule

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


