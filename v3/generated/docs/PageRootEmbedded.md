# PageRootEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**CustomizablePage**](CustomizablePage.md) |  | [optional] 
**customized** | [**CustomizablePage**](CustomizablePage.md) |  | [optional] 
**customized_url** | **str** |  | [optional] 
**preview** | [**CustomizablePage**](CustomizablePage.md) |  | [optional] 
**preview_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.page_root_embedded import PageRootEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of PageRootEmbedded from a JSON string
page_root_embedded_instance = PageRootEmbedded.from_json(json)
# print the JSON string representation of the object
print(PageRootEmbedded.to_json())

# convert the object into a dict
page_root_embedded_dict = page_root_embedded_instance.to_dict()
# create an instance of PageRootEmbedded from a dict
page_root_embedded_form_dict = page_root_embedded.from_dict(page_root_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


