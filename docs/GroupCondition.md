# GroupCondition

Specifies a set of groups whose users are to be included or excluded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Groups to be excluded | [optional] 
**include** | **List[str]** | Groups to be included | [optional] 

## Example

```python
from okta.models.group_condition import GroupCondition

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCondition from a JSON string
group_condition_instance = GroupCondition.from_json(json)
# print the JSON string representation of the object
print(GroupCondition.to_json())

# convert the object into a dict
group_condition_dict = group_condition_instance.to_dict()
# create an instance of GroupCondition from a dict
group_condition_from_dict = GroupCondition.from_dict(group_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


