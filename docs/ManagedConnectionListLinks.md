# ManagedConnectionListLinks

Links available in managed list response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 

## Example

```python
from okta.models.managed_connection_list_links import ManagedConnectionListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedConnectionListLinks from a JSON string
managed_connection_list_links_instance = ManagedConnectionListLinks.from_json(json)
# print the JSON string representation of the object
print(ManagedConnectionListLinks.to_json())

# convert the object into a dict
managed_connection_list_links_dict = managed_connection_list_links_instance.to_dict()
# create an instance of ManagedConnectionListLinks from a dict
managed_connection_list_links_from_dict = ManagedConnectionListLinks.from_dict(managed_connection_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


