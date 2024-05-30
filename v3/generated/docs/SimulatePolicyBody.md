# SimulatePolicyBody

The request body required for a simulate policy operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_types** | [**List[PolicyType]**](PolicyType.md) | Supported policy types for a simulate operation. The default value, &#x60;null&#x60;, returns all types. | [optional] 
**app_instance** | **str** | The application instance ID for a simulate operation | 
**policy_context** | [**PolicyContext**](PolicyContext.md) |  | [optional] 

## Example

```python
from openapi_client.models.simulate_policy_body import SimulatePolicyBody

# TODO update the JSON string below
json = "{}"
# create an instance of SimulatePolicyBody from a JSON string
simulate_policy_body_instance = SimulatePolicyBody.from_json(json)
# print the JSON string representation of the object
print(SimulatePolicyBody.to_json())

# convert the object into a dict
simulate_policy_body_dict = simulate_policy_body_instance.to_dict()
# create an instance of SimulatePolicyBody from a dict
simulate_policy_body_form_dict = simulate_policy_body.from_dict(simulate_policy_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


