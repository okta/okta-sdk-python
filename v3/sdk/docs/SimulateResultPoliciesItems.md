# SimulateResultPoliciesItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**conditions** | [**SimulateResultConditions**](SimulateResultConditions.md) |  | [optional] 
**rules** | [**SimulateResultRules**](SimulateResultRules.md) |  | [optional] 

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


