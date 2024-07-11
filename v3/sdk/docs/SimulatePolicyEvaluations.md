# SimulatePolicyEvaluations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The result of this entity evaluation | [optional] 
**policy_type** | [**List[PolicyType]**](PolicyType.md) | The policy type of the simulate operation | [optional] 
**result** | [**SimulatePolicyResult**](SimulatePolicyResult.md) |  | [optional] 
**undefined** | [**SimulatePolicyEvaluationsUndefined**](SimulatePolicyEvaluationsUndefined.md) |  | [optional] 
**evaluated** | [**SimulatePolicyEvaluationsEvaluated**](SimulatePolicyEvaluationsEvaluated.md) |  | [optional] 

## Example

```python
from okta.models.simulate_policy_evaluations import SimulatePolicyEvaluations

# TODO update the JSON string below
json = "{}"
# create an instance of SimulatePolicyEvaluations from a JSON string
simulate_policy_evaluations_instance = SimulatePolicyEvaluations.from_json(json)
# print the JSON string representation of the object
print(SimulatePolicyEvaluations.to_json())

# convert the object into a dict
simulate_policy_evaluations_dict = simulate_policy_evaluations_instance.to_dict()
# create an instance of SimulatePolicyEvaluations from a dict
simulate_policy_evaluations_from_dict = SimulatePolicyEvaluations.from_dict(simulate_policy_evaluations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


