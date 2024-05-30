# ApplicationGroupAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**priority** | **int** |  | [optional] 
**profile** | **Dict[str, object]** |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_group_assignment import ApplicationGroupAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationGroupAssignment from a JSON string
application_group_assignment_instance = ApplicationGroupAssignment.from_json(json)
# print the JSON string representation of the object
print(ApplicationGroupAssignment.to_json())

# convert the object into a dict
application_group_assignment_dict = application_group_assignment_instance.to_dict()
# create an instance of ApplicationGroupAssignment from a dict
application_group_assignment_form_dict = application_group_assignment.from_dict(application_group_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


