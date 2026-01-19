# AvailableActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[AvailableAction]**](AvailableAction.md) |  | [optional] 

## Example

```python
from okta.models.available_actions import AvailableActions

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableActions from a JSON string
available_actions_instance = AvailableActions.from_json(json)
# print the JSON string representation of the object
print(AvailableActions.to_json())

# convert the object into a dict
available_actions_dict = available_actions_instance.to_dict()
# create an instance of AvailableActions from a dict
available_actions_from_dict = AvailableActions.from_dict(available_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


