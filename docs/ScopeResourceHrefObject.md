# ScopeResourceHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 
**title** | **str** | Link name | [optional] 

## Example

```python
from okta.models.scope_resource_href_object import ScopeResourceHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeResourceHrefObject from a JSON string
scope_resource_href_object_instance = ScopeResourceHrefObject.from_json(json)
# print the JSON string representation of the object
print(ScopeResourceHrefObject.to_json())

# convert the object into a dict
scope_resource_href_object_dict = scope_resource_href_object_instance.to_dict()
# create an instance of ScopeResourceHrefObject from a dict
scope_resource_href_object_from_dict = ScopeResourceHrefObject.from_dict(scope_resource_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


