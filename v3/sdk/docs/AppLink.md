# AppLink


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
from openapi_client.models.app_link import AppLink

# TODO update the JSON string below
json = "{}"
# create an instance of AppLink from a JSON string
app_link_instance = AppLink.from_json(json)
# print the JSON string representation of the object
print(AppLink.to_json())

# convert the object into a dict
app_link_dict = app_link_instance.to_dict()
# create an instance of AppLink from a dict
app_link_from_dict = AppLink.from_dict(app_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


