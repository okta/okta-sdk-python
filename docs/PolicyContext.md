# PolicyContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**PolicyContextDevice**](PolicyContextDevice.md) |  | [optional] 
**groups** | [**PolicyContextGroups**](PolicyContextGroups.md) |  | 
**ip** | **str** | The network rule condition, zone, or IP address | [optional] 
**risk** | [**PolicyContextRisk**](PolicyContextRisk.md) |  | [optional] 
**user** | [**PolicyContextUser**](PolicyContextUser.md) |  | 
**zones** | [**PolicyContextZones**](PolicyContextZones.md) |  | [optional] 

## Example

```python
from okta.models.policy_context import PolicyContext

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyContext from a JSON string
policy_context_instance = PolicyContext.from_json(json)
# print the JSON string representation of the object
print(PolicyContext.to_json())

# convert the object into a dict
policy_context_dict = policy_context_instance.to_dict()
# create an instance of PolicyContext from a dict
policy_context_from_dict = PolicyContext.from_dict(policy_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


