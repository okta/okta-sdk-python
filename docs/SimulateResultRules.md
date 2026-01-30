# SimulateResultRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[SimulateResultConditions]**](SimulateResultConditions.md) | List of all conditions involved for this rule evaluation | [optional] 
**id** | **str** | The unique ID number of the policy rule | [optional] 
**name** | **str** | The name of the policy rule | [optional] 
**status** | [**SimulateResultStatus**](SimulateResultStatus.md) |  | [optional] 

## Example

```python
from okta.models.simulate_result_rules import SimulateResultRules

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateResultRules from a JSON string
simulate_result_rules_instance = SimulateResultRules.from_json(json)
# print the JSON string representation of the object
print(SimulateResultRules.to_json())

# convert the object into a dict
simulate_result_rules_dict = simulate_result_rules_instance.to_dict()
# create an instance of SimulateResultRules from a dict
simulate_result_rules_from_dict = SimulateResultRules.from_dict(simulate_result_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


