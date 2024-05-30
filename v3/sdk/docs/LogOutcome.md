# LogOutcome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] [readonly] 
**result** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.log_outcome import LogOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of LogOutcome from a JSON string
log_outcome_instance = LogOutcome.from_json(json)
# print the JSON string representation of the object
print(LogOutcome.to_json())

# convert the object into a dict
log_outcome_dict = log_outcome_instance.to_dict()
# create an instance of LogOutcome from a dict
log_outcome_form_dict = log_outcome.from_dict(log_outcome_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


