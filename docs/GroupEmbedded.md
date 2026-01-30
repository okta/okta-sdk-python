# GroupEmbedded

Embedded resources related to the group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**GroupEmbeddedStats**](GroupEmbeddedStats.md) |  | [optional] 
**app** | [**GroupEmbeddedApp**](GroupEmbeddedApp.md) |  | [optional] 

## Example

```python
from okta.models.group_embedded import GroupEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEmbedded from a JSON string
group_embedded_instance = GroupEmbedded.from_json(json)
# print the JSON string representation of the object
print(GroupEmbedded.to_json())

# convert the object into a dict
group_embedded_dict = group_embedded_instance.to_dict()
# create an instance of GroupEmbedded from a dict
group_embedded_from_dict = GroupEmbedded.from_dict(group_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


