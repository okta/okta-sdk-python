# AvailableAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action identifier | 
**provider** | [**WorkflowAvailableActionProvider**](WorkflowAvailableActionProvider.md) |  | 

## Example

```python
from okta.models.available_action import AvailableAction

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableAction from a JSON string
available_action_instance = AvailableAction.from_json(json)
# print the JSON string representation of the object
print(AvailableAction.to_json())

# convert the object into a dict
available_action_dict = available_action_instance.to_dict()
# create an instance of AvailableAction from a dict
available_action_from_dict = AvailableAction.from_dict(available_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


