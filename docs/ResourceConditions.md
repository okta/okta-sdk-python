# ResourceConditions

Conditions for further restricting a resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | [**ResourceConditionsExclude**](ResourceConditionsExclude.md) |  | [optional] 

## Example

```python
from okta.models.resource_conditions import ResourceConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConditions from a JSON string
resource_conditions_instance = ResourceConditions.from_json(json)
# print the JSON string representation of the object
print(ResourceConditions.to_json())

# convert the object into a dict
resource_conditions_dict = resource_conditions_instance.to_dict()
# create an instance of ResourceConditions from a dict
resource_conditions_from_dict = ResourceConditions.from_dict(resource_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


