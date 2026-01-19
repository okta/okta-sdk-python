# AuthorizationServerResourceHrefObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 
**title** | **str** | Link name | [optional] 

## Example

```python
from okta.models.authorization_server_resource_href_object import AuthorizationServerResourceHrefObject

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerResourceHrefObject from a JSON string
authorization_server_resource_href_object_instance = AuthorizationServerResourceHrefObject.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerResourceHrefObject.to_json())

# convert the object into a dict
authorization_server_resource_href_object_dict = authorization_server_resource_href_object_instance.to_dict()
# create an instance of AuthorizationServerResourceHrefObject from a dict
authorization_server_resource_href_object_from_dict = AuthorizationServerResourceHrefObject.from_dict(authorization_server_resource_href_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


