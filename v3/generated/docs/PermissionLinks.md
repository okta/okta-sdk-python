# PermissionLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**role** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.permission_links import PermissionLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionLinks from a JSON string
permission_links_instance = PermissionLinks.from_json(json)
# print the JSON string representation of the object
print(PermissionLinks.to_json())

# convert the object into a dict
permission_links_dict = permission_links_instance.to_dict()
# create an instance of PermissionLinks from a dict
permission_links_form_dict = permission_links.from_dict(permission_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


