# SimulatePolicyResult

The result of the policy evaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[SimulateResultPoliciesItems]**](SimulateResultPoliciesItems.md) |  | [optional] 

## Example

```python
from openapi_client.models.simulate_policy_result import SimulatePolicyResult

# TODO update the JSON string below
json = "{}"
# create an instance of SimulatePolicyResult from a JSON string
simulate_policy_result_instance = SimulatePolicyResult.from_json(json)
# print the JSON string representation of the object
print(SimulatePolicyResult.to_json())

# convert the object into a dict
simulate_policy_result_dict = simulate_policy_result_instance.to_dict()
# create an instance of SimulatePolicyResult from a dict
simulate_policy_result_from_dict = SimulatePolicyResult.from_dict(simulate_policy_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


