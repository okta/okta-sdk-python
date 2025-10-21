# PolicyNetworkCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**PolicyNetworkConnection**](PolicyNetworkConnection.md) |  | [optional] 
**exclude** | **List[str]** |  | [optional] 
**include** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.policy_network_condition import PolicyNetworkCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyNetworkCondition from a JSON string
policy_network_condition_instance = PolicyNetworkCondition.from_json(json)
# print the JSON string representation of the object
print(PolicyNetworkCondition.to_json())

# convert the object into a dict
policy_network_condition_dict = policy_network_condition_instance.to_dict()
# create an instance of PolicyNetworkCondition from a dict
policy_network_condition_from_dict = PolicyNetworkCondition.from_dict(policy_network_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


