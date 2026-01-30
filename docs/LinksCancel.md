# LinksCancel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel** | [**LinksCancelCancel**](LinksCancelCancel.md) |  | [optional] 

## Example

```python
from okta.models.links_cancel import LinksCancel

# TODO update the JSON string below
json = "{}"
# create an instance of LinksCancel from a JSON string
links_cancel_instance = LinksCancel.from_json(json)
# print the JSON string representation of the object
print(LinksCancel.to_json())

# convert the object into a dict
links_cancel_dict = links_cancel_instance.to_dict()
# create an instance of LinksCancel from a dict
links_cancel_from_dict = LinksCancel.from_dict(links_cancel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


