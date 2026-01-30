# GroupLinks

[Discoverable resources](/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroups!c=200&path=_links&t=response) related to the group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**apps** | [**HrefObject**](HrefObject.md) |  | [optional] 
**logo** | [**List[HrefObject]**](HrefObject.md) |  | [optional] 
**source** | [**HrefObject**](HrefObject.md) |  | [optional] 
**users** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.group_links import GroupLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GroupLinks from a JSON string
group_links_instance = GroupLinks.from_json(json)
# print the JSON string representation of the object
print(GroupLinks.to_json())

# convert the object into a dict
group_links_dict = group_links_instance.to_dict()
# create an instance of GroupLinks from a dict
group_links_from_dict = GroupLinks.from_dict(group_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


