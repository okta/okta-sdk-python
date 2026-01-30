# OfflineAccessScopeResourceHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 
**title** | **str** | Link name | [optional] 

## Example

```python
from okta.models.offline_access_scope_resource_href_object import OfflineAccessScopeResourceHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of OfflineAccessScopeResourceHrefObject from a JSON string
offline_access_scope_resource_href_object_instance = OfflineAccessScopeResourceHrefObject.from_json(json)
# print the JSON string representation of the object
print(OfflineAccessScopeResourceHrefObject.to_json())

# convert the object into a dict
offline_access_scope_resource_href_object_dict = offline_access_scope_resource_href_object_instance.to_dict()
# create an instance of OfflineAccessScopeResourceHrefObject from a dict
offline_access_scope_resource_href_object_from_dict = OfflineAccessScopeResourceHrefObject.from_dict(offline_access_scope_resource_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


