# SimulateResultPoliciesItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[SimulateResultConditions]**](SimulateResultConditions.md) | List of all conditions involved for this policy evaluation | [optional] 
**id** | **str** | ID of the specified policy type | [optional] 
**name** | **str** | Policy name | [optional] 
**rules** | [**List[SimulateResultRules]**](SimulateResultRules.md) |  | [optional] 
**status** | [**SimulateResultStatus**](SimulateResultStatus.md) |  | [optional] 

## Example

```python
from okta.models.simulate_result_policies_items import SimulateResultPoliciesItems

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateResultPoliciesItems from a JSON string
simulate_result_policies_items_instance = SimulateResultPoliciesItems.from_json(json)
# print the JSON string representation of the object
print(SimulateResultPoliciesItems.to_json())

# convert the object into a dict
simulate_result_policies_items_dict = simulate_result_policies_items_instance.to_dict()
# create an instance of SimulateResultPoliciesItems from a dict
simulate_result_policies_items_from_dict = SimulateResultPoliciesItems.from_dict(simulate_result_policies_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


