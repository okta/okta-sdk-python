# LogTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternate_id** | **str** | The alternate ID of the target | [optional] [readonly] 
**change_details** | [**LogTargetChangeDetails**](LogTargetChangeDetails.md) |  | [optional] 
**detail_entry** | **Dict[str, object]** | Further details on the target | [optional] [readonly] 
**display_name** | **str** | The display name of the target | [optional] [readonly] 
**id** | **str** | The ID of the target | [optional] [readonly] 
**type** | **str** | The type of target | [optional] [readonly] 

## Example

```python
from okta.models.log_target import LogTarget

# TODO update the JSON string below
json = "{}"
# create an instance of LogTarget from a JSON string
log_target_instance = LogTarget.from_json(json)
# print the JSON string representation of the object
print(LogTarget.to_json())

# convert the object into a dict
log_target_dict = log_target_instance.to_dict()
# create an instance of LogTarget from a dict
log_target_from_dict = LogTarget.from_dict(log_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


