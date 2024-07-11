# PageRootLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**default** | [**HrefObject**](HrefObject.md) |  | [optional] 
**customized** | [**HrefObject**](HrefObject.md) |  | [optional] 
**preview** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.page_root_links import PageRootLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PageRootLinks from a JSON string
page_root_links_instance = PageRootLinks.from_json(json)
# print the JSON string representation of the object
print(PageRootLinks.to_json())

# convert the object into a dict
page_root_links_dict = page_root_links_instance.to_dict()
# create an instance of PageRootLinks from a dict
page_root_links_from_dict = PageRootLinks.from_dict(page_root_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


