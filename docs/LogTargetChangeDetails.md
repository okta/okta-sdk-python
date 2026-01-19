# LogTargetChangeDetails

Details on the target's changes. Not all event types support the `changeDetails` property, and not all `target` objects contain the `changeDetails` property.  > **Note:** You can't run queries on `changeDetails` or the object's `to` or `from` properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **Dict[str, object]** | The original properties of the target | [optional] 
**to** | **Dict[str, object]** | The updated properties of the target | [optional] 

## Example

```python
from okta.models.log_target_change_details import LogTargetChangeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LogTargetChangeDetails from a JSON string
log_target_change_details_instance = LogTargetChangeDetails.from_json(json)
# print the JSON string representation of the object
print(LogTargetChangeDetails.to_json())

# convert the object into a dict
log_target_change_details_dict = log_target_change_details_instance.to_dict()
# create an instance of LogTargetChangeDetails from a dict
log_target_change_details_from_dict = LogTargetChangeDetails.from_dict(log_target_change_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


