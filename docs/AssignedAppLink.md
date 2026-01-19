# AssignedAppLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_assignment_id** | **str** |  | [optional] [readonly] 
**app_instance_id** | **str** |  | [optional] [readonly] 
**app_name** | **str** |  | [optional] [readonly] 
**credentials_setup** | **bool** |  | [optional] [readonly] 
**hidden** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**label** | **str** |  | [optional] [readonly] 
**link_url** | **str** |  | [optional] [readonly] 
**logo_url** | **str** |  | [optional] [readonly] 
**sort_order** | **int** |  | [optional] [readonly] 

## Example

```python
from okta.models.assigned_app_link import AssignedAppLink

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedAppLink from a JSON string
assigned_app_link_instance = AssignedAppLink.from_json(json)
# print the JSON string representation of the object
print(AssignedAppLink.to_json())

# convert the object into a dict
assigned_app_link_dict = assigned_app_link_instance.to_dict()
# create an instance of AssignedAppLink from a dict
assigned_app_link_from_dict = AssignedAppLink.from_dict(assigned_app_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


