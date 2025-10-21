# GroupProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from okta.models.group_profile import GroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GroupProfile from a JSON string
group_profile_instance = GroupProfile.from_json(json)
# print the JSON string representation of the object
print(GroupProfile.to_json())

# convert the object into a dict
group_profile_dict = group_profile_instance.to_dict()
# create an instance of GroupProfile from a dict
group_profile_from_dict = GroupProfile.from_dict(group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


