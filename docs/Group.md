# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the group was created | [optional] [readonly] 
**id** | **str** | Unique ID for the group | [optional] [readonly] 
**last_membership_updated** | **datetime** | Timestamp when the groups memberships were last updated | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the group&#39;s profile was last updated | [optional] [readonly] 
**object_class** | **List[str]** | Determines the group&#39;s &#x60;profile&#x60; | [optional] [readonly] 
**profile** | [**GroupProfile**](GroupProfile.md) |  | [optional] 
**type** | [**GroupType**](GroupType.md) |  | [optional] 
**embedded** | [**GroupEmbedded**](GroupEmbedded.md) |  | [optional] 
**links** | [**GroupLinks**](GroupLinks.md) |  | [optional] 

## Example

```python
from okta.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


