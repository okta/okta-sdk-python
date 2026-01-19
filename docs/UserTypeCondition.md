# UserTypeCondition

<x-lifecycle class=\"oie\"></x-lifecycle> Specifies which user types to include and/or exclude

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | The user types to exclude | 
**include** | **List[str]** | The user types to include | 

## Example

```python
from okta.models.user_type_condition import UserTypeCondition

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypeCondition from a JSON string
user_type_condition_instance = UserTypeCondition.from_json(json)
# print the JSON string representation of the object
print(UserTypeCondition.to_json())

# convert the object into a dict
user_type_condition_dict = user_type_condition_instance.to_dict()
# create an instance of UserTypeCondition from a dict
user_type_condition_from_dict = UserTypeCondition.from_dict(user_type_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


