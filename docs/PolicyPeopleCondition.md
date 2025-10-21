# PolicyPeopleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**GroupCondition**](GroupCondition.md) |  | [optional] 
**users** | [**UserCondition**](UserCondition.md) |  | [optional] 

## Example

```python
from okta.models.policy_people_condition import PolicyPeopleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyPeopleCondition from a JSON string
policy_people_condition_instance = PolicyPeopleCondition.from_json(json)
# print the JSON string representation of the object
print(PolicyPeopleCondition.to_json())

# convert the object into a dict
policy_people_condition_dict = policy_people_condition_instance.to_dict()
# create an instance of PolicyPeopleCondition from a dict
policy_people_condition_from_dict = PolicyPeopleCondition.from_dict(policy_people_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


