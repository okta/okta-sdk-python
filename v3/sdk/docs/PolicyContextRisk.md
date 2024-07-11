# PolicyContextRisk

The risk rule condition level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** |  | [optional] 

## Example

```python
from okta.models.policy_context_risk import PolicyContextRisk

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyContextRisk from a JSON string
policy_context_risk_instance = PolicyContextRisk.from_json(json)
# print the JSON string representation of the object
print(PolicyContextRisk.to_json())

# convert the object into a dict
policy_context_risk_dict = policy_context_risk_instance.to_dict()
# create an instance of PolicyContextRisk from a dict
policy_context_risk_from_dict = PolicyContextRisk.from_dict(policy_context_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


