# PotentialConnectionListLinks

Links available for the potential connection list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 

## Example

```python
from okta.models.potential_connection_list_links import PotentialConnectionListLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PotentialConnectionListLinks from a JSON string
potential_connection_list_links_instance = PotentialConnectionListLinks.from_json(json)
# print the JSON string representation of the object
print(PotentialConnectionListLinks.to_json())

# convert the object into a dict
potential_connection_list_links_dict = potential_connection_list_links_instance.to_dict()
# create an instance of PotentialConnectionListLinks from a dict
potential_connection_list_links_from_dict = PotentialConnectionListLinks.from_dict(potential_connection_list_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


