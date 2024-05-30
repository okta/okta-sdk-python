# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_membership_updated** | **datetime** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**object_class** | **List[str]** |  | [optional] [readonly] 
**profile** | [**GroupProfile**](GroupProfile.md) |  | [optional] 
**type** | [**GroupType**](GroupType.md) |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**GroupLinks**](GroupLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_form_dict = group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


