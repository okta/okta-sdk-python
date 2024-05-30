# UserCondition

Specifies a set of Users to be included or excluded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Users to be excluded | [optional] 
**include** | **List[str]** | Users to be included | [optional] 

## Example

```python
from openapi_client.models.user_condition import UserCondition

# TODO update the JSON string below
json = "{}"
# create an instance of UserCondition from a JSON string
user_condition_instance = UserCondition.from_json(json)
# print the JSON string representation of the object
print(UserCondition.to_json())

# convert the object into a dict
user_condition_dict = user_condition_instance.to_dict()
# create an instance of UserCondition from a dict
user_condition_form_dict = user_condition.from_dict(user_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


