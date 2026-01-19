# ImportScheduleObject

Import schedule configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_import** | [**ImportScheduleObjectFullImport**](ImportScheduleObjectFullImport.md) |  | [optional] 
**incremental_import** | [**ImportScheduleObjectIncrementalImport**](ImportScheduleObjectIncrementalImport.md) |  | [optional] 
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 

## Example

```python
from okta.models.import_schedule_object import ImportScheduleObject

# TODO update the JSON string below
json = "{}"
# create an instance of ImportScheduleObject from a JSON string
import_schedule_object_instance = ImportScheduleObject.from_json(json)
# print the JSON string representation of the object
print(ImportScheduleObject.to_json())

# convert the object into a dict
import_schedule_object_dict = import_schedule_object_instance.to_dict()
# create an instance of ImportScheduleObject from a dict
import_schedule_object_from_dict = ImportScheduleObject.from_dict(import_schedule_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


