# LinksDeactivate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deactivate** | [**LinksDeactivateDeactivate**](LinksDeactivateDeactivate.md) |  | [optional] 

## Example

```python
from okta.models.links_deactivate import LinksDeactivate

# TODO update the JSON string below
json = "{}"
# create an instance of LinksDeactivate from a JSON string
links_deactivate_instance = LinksDeactivate.from_json(json)
# print the JSON string representation of the object
print(LinksDeactivate.to_json())

# convert the object into a dict
links_deactivate_dict = links_deactivate_instance.to_dict()
# create an instance of LinksDeactivate from a dict
links_deactivate_from_dict = LinksDeactivate.from_dict(links_deactivate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


