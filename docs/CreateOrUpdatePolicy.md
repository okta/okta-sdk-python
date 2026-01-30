# CreateOrUpdatePolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the policy was created | [optional] [readonly] 
**description** | **str** | Description of the policy | [optional] 
**id** | **str** | Identifier of the policy | [optional] [readonly] [default to 'Assigned']
**last_updated** | **datetime** | Timestamp when the policy was last modified | [optional] [readonly] 
**name** | **str** | Name of the policy | 
**priority** | **int** | Specifies the order in which this policy is evaluated in relation to the other policies | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**system** | **bool** | Specifies whether Okta created the policy | [optional] [default to False]
**type** | [**PolicyType**](PolicyType.md) |  | 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**PolicyLinks**](PolicyLinks.md) |  | [optional] 

## Example

```python
from okta.models.create_or_update_policy import CreateOrUpdatePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdatePolicy from a JSON string
create_or_update_policy_instance = CreateOrUpdatePolicy.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdatePolicy.to_json())

# convert the object into a dict
create_or_update_policy_dict = create_or_update_policy_instance.to_dict()
# create an instance of CreateOrUpdatePolicy from a dict
create_or_update_policy_from_dict = CreateOrUpdatePolicy.from_dict(create_or_update_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


