# PolicyNetworkCondition

Specifies a network selection mode and a set of network zones to be included or excluded. If the connection parameter's data type is `ZONE`, one of the `include` or `exclude` arrays is required. Specific zone IDs to include or exclude are enumerated in the respective arrays.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**PolicyNetworkConnection**](PolicyNetworkConnection.md) |  | [optional] 
**exclude** | **List[str]** | The zones to exclude. Required only if connection data type is &#x60;ZONE&#x60; | [optional] 
**include** | **List[str]** | The zones to include. Required only if connection data type is &#x60;ZONE&#x60; | [optional] 

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


