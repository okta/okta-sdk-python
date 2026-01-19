# PolicyCommon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the policy was created | [optional] [readonly] 
**description** | **str** | Description of the Policy | [optional] 
**id** | **str** | Identifier of the Policy | [optional] [readonly] [default to 'Assigned']
**last_updated** | **datetime** | Timestamp when the policy was last modified | [optional] [readonly] 
**name** | **str** | Name of the policy | 
**priority** | **int** | Specifies the order in which this policy is evaluated in relation to the other policies | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**system** | **bool** | Specifies whether Okta created the Policy | [optional] [default to False]
**type** | [**PolicyType**](PolicyType.md) |  | 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**PolicyLinks**](PolicyLinks.md) |  | [optional] 

## Example

```python
from okta.models.policy_common import PolicyCommon

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCommon from a JSON string
policy_common_instance = PolicyCommon.from_json(json)
# print the JSON string representation of the object
print(PolicyCommon.to_json())

# convert the object into a dict
policy_common_dict = policy_common_instance.to_dict()
# create an instance of PolicyCommon from a dict
policy_common_from_dict = PolicyCommon.from_dict(policy_common_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


