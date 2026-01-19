# GroupEmbeddedStats

Statistics about the group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_count** | **int** | Number of users in the group | [optional] 
**apps_count** | **int** | Number of apps associated with the group | [optional] 
**group_push_mappings_count** | **int** | Number of group push mappings associated with the group | [optional] 
**has_admin_privlege** | **bool** | Indicates if the group has admin privileges via a group-level role assignment | [optional] 

## Example

```python
from okta.models.group_embedded_stats import GroupEmbeddedStats

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEmbeddedStats from a JSON string
group_embedded_stats_instance = GroupEmbeddedStats.from_json(json)
# print the JSON string representation of the object
print(GroupEmbeddedStats.to_json())

# convert the object into a dict
group_embedded_stats_dict = group_embedded_stats_instance.to_dict()
# create an instance of GroupEmbeddedStats from a dict
group_embedded_stats_from_dict = GroupEmbeddedStats.from_dict(group_embedded_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


