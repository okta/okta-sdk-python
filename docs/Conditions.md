# Conditions

Conditions of applying realm assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**Expression**](Expression.md) |  | [optional] 
**profile_source_id** | **str** | ID of the profile source | [optional] 

## Example

```python
from okta.models.conditions import Conditions

# TODO update the JSON string below
json = "{}"
# create an instance of Conditions from a JSON string
conditions_instance = Conditions.from_json(json)
# print the JSON string representation of the object
print(Conditions.to_json())

# convert the object into a dict
conditions_dict = conditions_instance.to_dict()
# create an instance of Conditions from a dict
conditions_from_dict = Conditions.from_dict(conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


