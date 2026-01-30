# PolicyContextZones

The zone ID under the network rule condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.policy_context_zones import PolicyContextZones

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyContextZones from a JSON string
policy_context_zones_instance = PolicyContextZones.from_json(json)
# print the JSON string representation of the object
print(PolicyContextZones.to_json())

# convert the object into a dict
policy_context_zones_dict = policy_context_zones_instance.to_dict()
# create an instance of PolicyContextZones from a dict
policy_context_zones_from_dict = PolicyContextZones.from_dict(policy_context_zones_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


