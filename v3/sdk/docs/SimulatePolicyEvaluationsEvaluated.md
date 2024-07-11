# SimulatePolicyEvaluationsEvaluated

A list of evaluated but not matched policies and rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[SimulateResultPoliciesItems]**](SimulateResultPoliciesItems.md) |  | [optional] 

## Example

```python
from okta.models.simulate_policy_evaluations_evaluated import SimulatePolicyEvaluationsEvaluated

# TODO update the JSON string below
json = "{}"
# create an instance of SimulatePolicyEvaluationsEvaluated from a JSON string
simulate_policy_evaluations_evaluated_instance = SimulatePolicyEvaluationsEvaluated.from_json(json)
# print the JSON string representation of the object
print(SimulatePolicyEvaluationsEvaluated.to_json())

# convert the object into a dict
simulate_policy_evaluations_evaluated_dict = simulate_policy_evaluations_evaluated_instance.to_dict()
# create an instance of SimulatePolicyEvaluationsEvaluated from a dict
simulate_policy_evaluations_evaluated_from_dict = SimulatePolicyEvaluationsEvaluated.from_dict(simulate_policy_evaluations_evaluated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


