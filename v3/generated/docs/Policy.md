# Policy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the Policy was created | [optional] [readonly] 
**description** | **str** | Policy description | [optional] 
**id** | **str** | Policy ID | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the Policy was last updated | [optional] [readonly] 
**name** | **str** | Policy name | [optional] 
**priority** | **int** | Specifies the order in which this Policy is evaluated in relation to the other policies | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**system** | **bool** | Specifies whether Okta created the Policy | [optional] 
**type** | [**PolicyType**](PolicyType.md) |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**PolicyLinks**](PolicyLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy import Policy

# TODO update the JSON string below
json = "{}"
# create an instance of Policy from a JSON string
policy_instance = Policy.from_json(json)
# print the JSON string representation of the object
print(Policy.to_json())

# convert the object into a dict
policy_dict = policy_instance.to_dict()
# create an instance of Policy from a dict
policy_form_dict = policy.from_dict(policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


