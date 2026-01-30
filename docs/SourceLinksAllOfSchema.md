# SourceLinksAllOfSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.source_links_all_of_schema import SourceLinksAllOfSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SourceLinksAllOfSchema from a JSON string
source_links_all_of_schema_instance = SourceLinksAllOfSchema.from_json(json)
# print the JSON string representation of the object
print(SourceLinksAllOfSchema.to_json())

# convert the object into a dict
source_links_all_of_schema_dict = source_links_all_of_schema_instance.to_dict()
# create an instance of SourceLinksAllOfSchema from a dict
source_links_all_of_schema_from_dict = SourceLinksAllOfSchema.from_dict(source_links_all_of_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


