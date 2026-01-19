# SimulateResultConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SimulateResultStatus**](SimulateResultStatus.md) |  | [optional] 
**type** | **str** | The type of condition | [optional] 

## Example

```python
from okta.models.simulate_result_conditions import SimulateResultConditions

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateResultConditions from a JSON string
simulate_result_conditions_instance = SimulateResultConditions.from_json(json)
# print the JSON string representation of the object
print(SimulateResultConditions.to_json())

# convert the object into a dict
simulate_result_conditions_dict = simulate_result_conditions_instance.to_dict()
# create an instance of SimulateResultConditions from a dict
simulate_result_conditions_from_dict = SimulateResultConditions.from_dict(simulate_result_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


