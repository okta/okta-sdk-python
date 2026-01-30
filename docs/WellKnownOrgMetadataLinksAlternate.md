# WellKnownOrgMetadataLinksAlternate


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
from okta.models.well_known_org_metadata_links_alternate import WellKnownOrgMetadataLinksAlternate

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownOrgMetadataLinksAlternate from a JSON string
well_known_org_metadata_links_alternate_instance = WellKnownOrgMetadataLinksAlternate.from_json(json)
# print the JSON string representation of the object
print(WellKnownOrgMetadataLinksAlternate.to_json())

# convert the object into a dict
well_known_org_metadata_links_alternate_dict = well_known_org_metadata_links_alternate_instance.to_dict()
# create an instance of WellKnownOrgMetadataLinksAlternate from a dict
well_known_org_metadata_links_alternate_from_dict = WellKnownOrgMetadataLinksAlternate.from_dict(well_known_org_metadata_links_alternate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


