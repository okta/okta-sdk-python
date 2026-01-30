# UserResourceHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 
**title** | **str** | Link name | [optional] 

## Example

```python
from okta.models.user_resource_href_object import UserResourceHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserResourceHrefObject from a JSON string
user_resource_href_object_instance = UserResourceHrefObject.from_json(json)
# print the JSON string representation of the object
print(UserResourceHrefObject.to_json())

# convert the object into a dict
user_resource_href_object_dict = user_resource_href_object_instance.to_dict()
# create an instance of UserResourceHrefObject from a dict
user_resource_href_object_from_dict = UserResourceHrefObject.from_dict(user_resource_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


