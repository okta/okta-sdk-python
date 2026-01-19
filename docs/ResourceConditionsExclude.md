# ResourceConditionsExclude

Specific resources to exclude

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**okta_orn** | **List[str]** | List of specific resources to exclude in ORN format | [optional] 

## Example

```python
from okta.models.resource_conditions_exclude import ResourceConditionsExclude

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceConditionsExclude from a JSON string
resource_conditions_exclude_instance = ResourceConditionsExclude.from_json(json)
# print the JSON string representation of the object
print(ResourceConditionsExclude.to_json())

# convert the object into a dict
resource_conditions_exclude_dict = resource_conditions_exclude_instance.to_dict()
# create an instance of ResourceConditionsExclude from a dict
resource_conditions_exclude_from_dict = ResourceConditionsExclude.from_dict(resource_conditions_exclude_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


