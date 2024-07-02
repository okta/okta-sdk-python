# PageRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**PageRootEmbedded**](PageRootEmbedded.md) |  | [optional] 
**links** | [**PageRootLinks**](PageRootLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.page_root import PageRoot

# TODO update the JSON string below
json = "{}"
# create an instance of PageRoot from a JSON string
page_root_instance = PageRoot.from_json(json)
# print the JSON string representation of the object
print(PageRoot.to_json())

# convert the object into a dict
page_root_dict = page_root_instance.to_dict()
# create an instance of PageRoot from a dict
page_root_from_dict = PageRoot.from_dict(page_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


