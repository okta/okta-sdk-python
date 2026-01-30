# ImportScheduleSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | The import schedule in UNIX cron format | 
**timezone** | **str** | The import schedule time zone in Internet Assigned Numbers Authority (IANA) time zone name format | [optional] 

## Example

```python
from okta.models.import_schedule_settings import ImportScheduleSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ImportScheduleSettings from a JSON string
import_schedule_settings_instance = ImportScheduleSettings.from_json(json)
# print the JSON string representation of the object
print(ImportScheduleSettings.to_json())

# convert the object into a dict
import_schedule_settings_dict = import_schedule_settings_instance.to_dict()
# create an instance of ImportScheduleSettings from a dict
import_schedule_settings_from_dict = ImportScheduleSettings.from_dict(import_schedule_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


